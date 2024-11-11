import sys
from langchain.graphs import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
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

os.environ["OPENAI_API_KEY"] = ""

llm = ChatOpenAI(temperature=0, model_name="gpt-4-turbo") # https://platform.openai.com/docs/models

llm_transformer = LLMGraphTransformer(llm=llm) # documentation, see https://python.langchain.com/docs/how_to/graph_constructing/

from langchain_core.documents import Document

documents = [Document(page_content=example_text)]
graph_documents = llm_transformer.convert_to_graph_documents(documents)
print(f"Nodes:{graph_documents[0].nodes}")
print(f"Relationships:{graph_documents[0].relationships}")
