from app.services.math_solver import solve_math_problem
from app.services.llm_explainer import explain_math
from fastapi import APIRouter

router = APIRouter()

@router.post("/solve")
async def solve_problem(payload: dict):
    problem = payload.get("problem", "")
    if not problem:
        return {"error": "Aucun problème fourni."}

    result = solve_math_problem(problem)
    explanation = explain_math(problem, result.get("answer"))

    return {
        "problem": problem,
        "result": result,
        "explanation": explanation,
    }
