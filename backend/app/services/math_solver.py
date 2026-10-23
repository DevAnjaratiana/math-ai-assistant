from sympy import Eq, diff, integrate, symbols, simplify, solve, sympify
import re

x, y = symbols('x y')


def normalize_problem(problem: str) -> str:
    text = problem.strip()
    text = text.replace("×", "*").replace("÷", "/")
    text = text.replace("−", "-").replace("²", "**2").replace("³", "**3")
    text = text.replace("π", "pi").replace("√", "sqrt")
    return text


def parse_expression(expr: str):
    cleaned = normalize_problem(expr)
    cleaned = cleaned.replace("^", "**")
    return sympify(cleaned, locals={"x": x, "y": y, "pi": __import__('sympy').pi, "sqrt": __import__('sympy').sqrt}, evaluate=True)


def solve_equation_from_text(text: str):
    text = normalize_problem(text)
    if "=" in text:
        left, right = text.split("=", 1)
        left_expr = parse_expression(left)
        right_expr = parse_expression(right)
        return solve(Eq(left_expr, right_expr), x)

    expr = parse_expression(text)
    return solve(expr, x)


def solve_math_problem(problem: str):
    text = normalize_problem(problem)
    lower = text.lower()

    if "résous" in lower or "solve" in lower:
        eq_text = re.sub(r"(?i)(résous|solve)\s*", "", text)
        try:
            solution = solve_equation_from_text(eq_text)
            return {
                "kind": "solve",
                "answer": solution,
                "steps": [
                    f"Équation traitée : {eq_text}",
                    "Résolution effectuée avec SymPy.",
                ],
            }
        except Exception as exc:
            return {
                "kind": "solve",
                "answer": None,
                "error": str(exc),
                "steps": ["Je n’ai pas pu résoudre cette équation directement."],
            }

    if "dérive" in lower or "derive" in lower:
        expr_text = re.sub(r"(?i)(dérive|derive)\s*", "", text)
        try:
            expr = parse_expression(expr_text)
            result = diff(expr, x)
            return {
                "kind": "derive",
                "answer": str(result),
                "steps": [
                    f"Expression : {expr_text}",
                    f"Dérivée : {result}",
                ],
            }
        except Exception as exc:
            return {
                "kind": "derive",
                "answer": None,
                "error": str(exc),
                "steps": ["Je n’ai pas pu dériver cette expression."],
            }

    if "intègre" in lower or "integrate" in lower:
        expr_text = re.sub(r"(?i)(intègre|integrate)\s*", "", text)
        try:
            expr = parse_expression(expr_text)
            result = integrate(expr, x)
            return {
                "kind": "integrate",
                "answer": str(result),
                "steps": [
                    f"Expression : {expr_text}",
                    f"Intégrale : {result}",
                ],
            }
        except Exception as exc:
            return {
                "kind": "integrate",
                "answer": None,
                "error": str(exc),
                "steps": ["Je n’ai pas pu intégrer cette expression."],
            }

    if "simplifie" in lower or "simplify" in lower:
        expr_text = re.sub(r"(?i)(simplifie|simplify)\s*", "", text)
        expr = parse_expression(expr_text)
        result = simplify(expr)
        return {
            "kind": "simplify",
            "answer": str(result),
            "steps": [
                f"Expression : {expr_text}",
                f"Forme simplifiée : {result}",
            ],
        }

    try:
        expr = parse_expression(text)
        result = simplify(expr)
        return {
            "kind": "evaluate",
            "answer": str(result),
            "steps": [
                f"Expression : {text}",
                f"Résultat : {result}",
            ],
        }
    except Exception as exc:
        return {
            "kind": "unknown",
            "answer": None,
            "error": str(exc),
            "steps": ["Je n’ai pas compris la demande ou le format du problème."],
        }
