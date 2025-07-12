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

@app.post("/predict_sequence")
def predict_sequence(input: DNAInput):
    try:
        result = client.predict(
            input.seq,
            api_name="//predict_dna"  # this must match your Hugging Face `api_name`
        )
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

Entrez.email = "rajaatif78600000@gmail.com"  # Required by NCBI

# Input model
class DNAInput(BaseModel):
    seq: str  # Will be an accession ID in this case

# Helper: Fetch DNA sequence from NCBI
def fetch_sequence_from_accession(accession_id):
    try:
        with Entrez.efetch(db="nucleotide", id=accession_id, rettype="fasta", retmode="text") as handle:
            record = SeqIO.read(handle, "fasta")
            return str(record.seq)
    except Exception as e:
        raise RuntimeError(f"Error fetching sequence: {e}")

# Endpoint: Accession to DNA → Prediction
@app.post("/predict_accession")
def predict_accession(input: DNAInput):
    try:
        accession_id = input.seq.strip()
        dna_sequence = fetch_sequence_from_accession(accession_id)

        # Call your Hugging Face model API
        result = client.predict(
            dna_sequence,
            api_name="/predict_dna"  # make sure your space exposes this endpoint
        )
        return {"accession": accession_id, "sequence": dna_sequence[:100] + "...", "result": result}

    except Exception as e:
        return {"error": str(e)}
