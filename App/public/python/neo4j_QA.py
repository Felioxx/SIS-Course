import sys
from langchain_openai import ChatOpenAI
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
import getpass
import os
import asyncio

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
    verbose=True,
    allow_dangerous_requests=True
)

# Async function in Python - waits for the neo4j request before printing the answer
async def handle_request(input_data):
    result = await chain.ainvoke(input_data)
    # Process result
    return result

question = sys.argv[1]
response = asyncio.run(handle_request(question))
print("test")
print(response)
#result = response.get("answer")
#print("Ergebnis aus der Neo4j-Datenbank:", len(result))
