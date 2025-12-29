from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel
from grammar import MorphAnalyzer, SyntaxAnalyzer

morph_analyzer = MorphAnalyzer()
syntax_analyzer = SyntaxAnalyzer()

router = APIRouter(prefix="/api")

class TextRequest(BaseModel):
    text: str


@router.post("/morph")
def morph_api(req: TextRequest):
    return morph_analyzer.analyze(req.text)


@router.post("/syntax")
def syntax_api(req: TextRequest):
    return syntax_analyzer.analyze(text=req.text, morph_analyzer=morph_analyzer)
