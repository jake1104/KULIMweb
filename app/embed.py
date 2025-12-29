from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()

@router.get("/embed", response_class=HTMLResponse)
def kulim_embed():
    html = Path("static/embed.html").read_text(encoding="utf-8")
    return html
