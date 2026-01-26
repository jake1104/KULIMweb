from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()

@router.get("/grammar_embed", response_class=HTMLResponse)
def kulim_grammar_embed():
    html = Path("static/grammar_embed.html").read_text(encoding="utf-8")
    return html

@router.get("/pronunciation_embed", response_class=HTMLResponse)
def kulim_pronunciation_embed():
    html = Path("static/pronunciation_embed.html").read_text(encoding="utf-8")
    return html

@router.get("/romanization_embed", response_class=HTMLResponse)
def kulim_romanization_embed():
    html = Path("static/romanization_embed.html").read_text(encoding="utf-8")
    return html

@router.get("/embed", response_class=HTMLResponse)
def kulim_embed():
    html = Path("static/embed.html").read_text(encoding="utf-8")
    return html
