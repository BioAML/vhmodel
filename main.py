from fastapi import FastAPI
from pydantic import BaseModel
from gradio_client import Client
from fastapi.middleware.cors import CORSMiddleware

client = Client("https://rajaatif786-vhbert.hf.space")


app = FastAPI(title="Proxy API for VirTransformer")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development/testing. Use exact domain in prod.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class DNAInput(BaseModel):
    seq: str

@app.post("/predict")
def predict(input: DNAInput):
    try:
        result = client.predict(
            input.seq,
            api_name="//predict_dna"  # this must match your Hugging Face `api_name`
        )
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
