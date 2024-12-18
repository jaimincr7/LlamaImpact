from pinecone.grpc import PineconeGRPC as Pinecone
from dotenv import load_dotenv
import os
import json

def upsert_embeddings(data, embeddings):
    # Target the index where you'll store the vector embeddings
    index = pc.Index("us-tax-faq-index")

    # Prepare the records for upsert
    # Each contains an 'id', the embedding 'values', and the original text as 'metadata'
    records = []
    for d, e in zip(data, embeddings):
        records.append({
            "id": d['id'],
            "values": e['values'],
            "metadata": {'text': d['text']}
        })

    # Upsert the records into the index
    index.upsert(
        vectors=records,
        namespace="us-tax-faq-namespace"
    )


def getData():
    file_path = os.path.join(os.path.dirname(__file__), '../data/tax_filing_faq.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    #Index data with 'id'
    for idx, obj in enumerate(data, start=1):  # start=1 gives IDs starting from 1
        obj['id'] = idx

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

upsert_embeddings(data, embeddings)