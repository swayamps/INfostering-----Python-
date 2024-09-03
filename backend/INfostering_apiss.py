from fastapi import FastAPI, HTTPException
from INfostering import INfoster
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware
import aicontent



app = FastAPI()
handler = Mangum(app)
MAX_INPUT_LENGTH = 32

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    validate_input_length(prompt)
    snippet = INfoster.generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []}


@app.get("/generate_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    keywords = INfoster.generate_keywords(prompt)
    return {"snippet": None, "keywords": keywords}


@app.get("/generate_snippet_and_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    snippet = INfoster.generate_branding_snippet(prompt)
    keywords = INfoster.generate_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}

@app.get("/generate_snippet_and_tagline")
async def generate_snippet_tagline_api(prompt: str):
    validate_input_length(prompt)
    snippet = INfoster.generate_branding_snippet(prompt)
    tagline = aicontent.taglineGenerator(prompt)
    return {"snippet": snippet, "tagline": []}

@app.get("/product-description")
async def product_desc_api(prompt: str):
    validate_input_length(prompt)
    snippet = aicontent.productDescription(prompt)
    return {snippet}

def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} characters.",
        )

# uvicorn INfostering_api:app --reload
