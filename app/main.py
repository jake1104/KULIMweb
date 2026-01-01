from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from pydantic import BaseModel
from grammar import MorphAnalyzer, SyntaxAnalyzer
from .embed import router as embed_router
from .api import router as api_router

morph_analyzer = MorphAnalyzer()
syntax_analyzer = SyntaxAnalyzer()

app = FastAPI(title="KULIM")


class CSPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response: Response = await call_next(request)
        response.headers["Content-Security-Policy"] = (
            "frame-ancestors *"
        )
        return response

app.add_middleware(CSPMiddleware)


app.include_router(embed_router)
app.include_router(api_router)

template = Jinja2Templates(directory="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})
