import sys
from langchain_openai import ChatOpenAI
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
import getpass
import os

url = "neo4j+s://f02e0524.databases.neo4j.io"
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

question = "Give me the names of all cities, that lie next to Münster."
response = chain.invoke(question)
print(response)
#result = response.get("answer")
#print("Ergebnis aus der Neo4j-Datenbank:", len(result))
