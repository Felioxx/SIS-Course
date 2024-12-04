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


CYPHER_GENERATION_TEMPLATE = """
Task:Generate Cypher statement to query a graph database.
Instructions:
Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.
Schema:
{schema}
Cypher examples:
# Which cities lie left of Münster?
MATCH p=(C:City WHERE C.Name = "Münster") -[T:touches WHERE T.`Rel_Position`in ["western","southwestern","northwestern"]]->(:City) RETURN p

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

os.environ["OPENAI_API_KEY"] = "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"

chain = GraphCypherQAChain.from_llm(
    graph=graph,
    cypher_llm=ChatOpenAI(temperature=0, model="gpt-4o-mini"), # gpt-4o-mini	gpt-3.5-turbo
    qa_llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k"),
    verbose=False,
    allow_dangerous_requests=True,
    cypher_prompt=CYPHER_GENERATION_PROMPT
)

# Async function in Python - waits for the neo4j request before printing the answer
async def handle_request(input_data):
    result = await chain.ainvoke(input_data)
    # Process result
    return result

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
