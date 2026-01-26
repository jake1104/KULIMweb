from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel
from grammar import MorphAnalyzer, SyntaxAnalyzer
from pronunciation import pronounce
from romanization import romanize, romanize_standard

morph_analyzer = MorphAnalyzer(use_rust=True, use_neural=True, use_gpu=True)
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


@router.post("/pronunciation")
def pronunciation_api(req: TextRequest):
    return pronounce(req.text)


@router.post("/romanization")
def romanization_api(req: TextRequest):
    return romanize(req.text)


@router.post("/romanization_standard")
def romanization_standard_api(req: TextRequest):
    return romanize_standard(req.text)


