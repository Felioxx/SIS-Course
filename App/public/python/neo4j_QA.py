import sys
from langchain_openai import ChatOpenAI
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain.prompts import PromptTemplate
import getpass
import os
import asyncio
import json
import re

from langchain.prompts.prompt import PromptTemplate

#Always return the IDs of all used entities in the context in two separate arrays named 'questionIDs' and 'answerIDs'.

CYPHER_GENERATION_TEMPLATE = """
Task:Generate Cypher statement to query a graph database and include the IDs of all the nodes which are used in the question and the answer as well as the asked properties from the user.
Instructions:
Never use the ID attribute in the answer sentence.
Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.
Use the unit km insteat of meters in your answer.
All questions are in utf-8 encoded.
Always return the whole graph (RETURN p) in the Cypher statement.
Use the following examples for few shot learning.

Schema:
{schema}

Cypher examples:
# Which cities lie left of Münster?
MATCH p=(C:City WHERE C.Name = "Münster") -[T:touches WHERE T.`Rel_Position`in ["western","southwestern","northwestern"]]->(:City) RETURN p

# Which districts lie right of Münster?
MATCH p=(D:District WHERE C.Name = "Münster") 
        -[T:touches WHERE T.`Rel_Position`in ["eastern","southeastern","northeastern"]]->(:City) RETURN p

# Which cities lie above of Selm?
MATCH p=(C:City WHERE C.Name = "Selm") 
        -[T:touches WHERE T.`Rel_Position`in ["southern","southwestern","southeastern"]]->(:City) RETURN p

# Which districts lie eastern of the Hochsauerlandkreis?
MATCH p=(D:District WHERE D.Name = "Hochsauerlandkreis")
        -[T:touches WHERE T.`Rel_Position`in ["eastern","southeastern","northeastern"]]->(:District) RETURN p

# Which districts lie southern of the Hochsauerlandkreis?
MATCH p=(D:District WHERE D.Name = "Hochsauerlandkreis")
        -[T:touches WHERE T.`Rel_Position`in ["southern","southeastern","southwestern"]]->(:District) RETURN p
        
# Which administrative Districts lie beneath Arnsberg?
MATCH p=(A:AdministrativeDistrict WHERE A.Name = "Arnsberg")
        -[T:touches WHERE T.`Rel_Position`in ["nothern","northeastern","northwestern"]]->(:AdministrativeDistrict) RETURN p

# Which districts lie next to Köln?
MATCH p=(D:District WHERE D.Name = "Köln")
        -[T:touches]->(:District) RETURN p

# In which administrative District lies Siegburg?
MATCH p=(C:City WHERE C.Name = "Siegburg")-[:within]->(D:District) -[:within]->(A:AdministrativeDistrict) RETURN P

# How large is Köln?
MATCH p=(C:City WHERE C.Name = "Köln") RETURN p

# How large is the district Köln?
MATCH p=(D:District WHERE D.Name = "Köln") RETURN p

# How large is the administrative district Köln?
MATCH p=(A:AdministrativeDistrict WHERE A.Name = "Köln") RETURN p

# What lies within the district Borken?
MATCH p=(D:District WHERE D.Name = "Borken")<-[:within]-(C:City) RETURN p

# Where lie Münster and Soest?
MATCH p=(C:City WHERE C.Name = "Münster" OR C.Name = "Soest") RETURN p

# Show me every city that lies eastern of Bocholt?
MATCH p=(c1:City WHERE c1.Name = "Bocholt") - [r:relates WHERE r.Rel_Position IN ["eastern","northeastern","southeastern"]] -> (:City) RETURN p

# What is the distance between Bocholt and Telgte?
MATCH p=(C1:City WHERE C1.Name = "Bocholt") -[R:relates]->(C2:City WHERE C2.Name = "Telgte") RETURN p,R.Distance_Between

# Which Cities lie in the administrative Disctrict Münster?
MATCH p=(C:City)-[:within]->(D:District)-[:within]->(A:AdministrativeDistrict WHERE A.Name = "Münster") RETURN p

# How does Münster relate to Selm?
MATCH p=(C1:City WHERE C1.Name = "Münster") -[R:relates]->(C2:City WHERE C2.Name = "Selm") RETURN p

# What's the relative position of Münster an Selm?
MATCH p=(C1:City WHERE C1.Name = "Münster") -[R:relates]->(C2:City WHERE C2.Name = "Selm") RETURN p

Note: Do not include any explanations or apologies in your responses.
Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
Do not include any text except the generated Cypher statement.

The question is:
{question}"""
CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], template=CYPHER_GENERATION_TEMPLATE
)

url = "neo4j+ssc://f02e0524.databases.neo4j.io:7687"
username = "neo4j"
password = "w60PF-SK2gGIlDII6zZMw8XMo67mqIFSrPU54_E3AU4"

graph = Neo4jGraph(
    url=url,
    username=username,
    password=password
)

from neo4j import GraphDatabase

openAiKey = sys.argv[2]
os.environ["OPENAI_API_KEY"] = openAiKey

chain = GraphCypherQAChain.from_llm(
    graph=graph,
    cypher_llm=ChatOpenAI(temperature=0, model="gpt-4o-mini"), # gpt-4o-mini	gpt-3.5-turbo
    qa_llm=ChatOpenAI(temperature=0, model="gpt-4o-mini"),
    verbose=False,
    allow_dangerous_requests=True,
    cypher_prompt=CYPHER_GENERATION_PROMPT,
    return_intermediate_steps=True,
    top_k=9999
)

# Async function in Python - waits for the neo4j request before printing the answer
async def handle_request(input_data):
    try:
        result = await chain.ainvoke(input_data)
        # Process result
        return result
    except:
        return {"result": "An error occurred while processing the request. Maybe the given API key is not valid." }

question = sys.argv[1]
response = asyncio.run(handle_request(question))

# Entferne ANSI-Codes und andere Debug-Ausgaben
#response_str = str(response)
#cleaned_response = re.sub(r'\x1b\[.*?m', '', response_str)  # Entfernt ANSI-Codes
#cleaned_response = cleaned_response.split("\n")[-1]  # Nimm nur die letzte relevante Zeile (JSON)

json_response = json.dumps(response, indent=2)  # Convert to JSON format with indentation
print(json_response)
#result = response.get("answer")
#print("Ergebnis aus der Neo4j-Datenbank:", len(result))
