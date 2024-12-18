from pinecone.grpc import PineconeGRPC as Pinecone
from dotenv import load_dotenv
import os
import json

def getData():
    file_path = os.path.join(os.path.dirname(__file__), '../data/tax_filing_faq.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

load_dotenv()

pinecone_api_key = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone with your API key
pc = Pinecone(api_key=pinecone_api_key)

data = getData()

embeddings = pc.inference.embed(
    model="multilingual-e5-large",
    inputs=[d['question'] for d in data],
    parameters={"input_type": "passage", "truncate": "END"}
)

print(embeddings)