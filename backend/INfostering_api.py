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

@app.get("/product-description")
async def product_desc_api(prompt: str):
    validate_input_length(prompt)
    snippet = aicontent.productDescription(prompt)
    return {snippet}

@app.get("/cold-emails")
async def cold_email_api(prompt: str):
    validate_input_length(prompt)
    snippet = aicontent.coldEmails(prompt)
    return {snippet}

@app.get("/tweet-ideas")
async def tweet_ideas_api(prompt: str):
    validate_input_length(prompt)
    snippet = aicontent.tweetIdeas(prompt)
    return {snippet}

@app.get("/business-pitch")
async def business_pitch_api(prompt: str):
    validate_input_length(prompt)
    snippet = aicontent.businessPitch(prompt)
    return {snippet}

@app.get("/video-ideas")
async def video_ideas_api(prompt: str):
    validate_input_length(prompt)
    snippet = aicontent.videoIdeas(prompt)
    return {snippet}

@app.get("/social-media")
async def social_media_api(prompt: str):
    validate_input_length(prompt)
    snippet = aicontent.socialMedia(prompt)
    return {snippet}

@app.get("/keyword_generator")
async def keyword_generator_api(prompt: str):
    validate_input_length(prompt)
    snippet = aicontent.keywordGenerator(prompt)
    return {snippet}


@app.get("/tagline-generator")
async def tagline_generator_api(prompt: str):
    validate_input_length(prompt)
    snippet = aicontent.taglineGenerator(prompt)
    return {snippet}

# @app.get("/generate_keywords")
# async def generate_keywords_api(prompt: str):
#     validate_input_length(prompt)
#     keywords = generate_keywords(prompt)
#     return {"snippet": None, "keywords": keywords}


@app.get("/generate_snippet_and_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    snippet = INfoster.generate_branding_snippet(prompt)
    keywords = INfoster.generate_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}


def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} characters.",
        )

