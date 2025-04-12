"""
This code implements converting any POST request into OpenAI-compatible API request, and it operates asynchronously.
You need to update all lines containing "ToChange" Tag.
"""

import json
import time
import requests
from typing import Optional, List
from pydantic import BaseModel
from starlette.responses import StreamingResponse
from fastapi import FastAPI, HTTPException
import uvicorn
import argparse
import uuid
import aiohttp

app = FastAPI(title="OpenAI-compatible API")

class Message(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    model: Optional[str] = "any_model"
    messages: List[Message]
    temperature: Optional[float] = 1.0
    top_p: Optional[float] = 1.0
    stream: Optional[bool] = False


async def _resp_async_generator(text_resp: str, request: ChatCompletionRequest):
    tokens = text_resp.split(" ")
    for i, token in enumerate(tokens):
        chunk = {
            "id": i,
            "object": "chat.completion.chunk",
            "created": time.time(),
            "model": request.model,
            "choices": [{"delta": {"content": token + " "}}],
        }
        yield f"data: {json.dumps(chunk)}\n\n"
    yield "data: [DONE]\n\n"


@app.post("/chat/completions")
async def chat_completions(request: ChatCompletionRequest):
    print(request.model)

    content = await predict(request)

    if request.stream:
        return StreamingResponse(
            _resp_async_generator(content, request), media_type="application/x-ndjson"
        )

    return {
        "id": "0",
        "object": "chat.completion",
        "created": time.time(),
        "model": request.model,
        "choices": [{"message": Message(role="assistant", content=content)}],
    }


async def predict(request: ChatCompletionRequest):
    data = request.model_dump()

    # Replace this with your actual API endpoint and authentication
    url = 'xxx'  # ToChange
    headers = {
        'Content-Type': 'application/json'  # ToChange
    }

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=600)) as session:
        async with session.post(url, json=data, headers=headers) as response:
            if response.status == 200:
                try:
                    resp_content = await response.json()
                    # Replace this with your actual response handling
                    content = resp_content['result']['choices'][0]['message']['content']  # ToChange
                    return content
                except Exception as e:
                    error_content = await response.json()
                    raise ValueError(f"Request failed with: {error_content}")
            else:
                raise HTTPException(status_code=response.status_code, detail=response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OpenAI-compatible API")
    parser.add_argument("--port", type=int, default=8001)
    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=args.port)
