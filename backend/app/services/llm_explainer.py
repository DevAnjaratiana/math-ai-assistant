import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def explain_math(problem: str, result):
    result_text = "Aucun résultat calculé" if result is None else str(result)

    if not os.getenv("OPENAI_API_KEY"):
        return (
            "Le calcul a été effectué par le moteur mathématique. "
            f"Pour le problème '{problem}', le résultat est : {result_text}. "
            "Ajoute OPENAI_API_KEY pour obtenir une explication plus détaillée."
        )

    prompt = f"""
Tu es un professeur de mathématiques très clair.
Explique, en français, comment résoudre ce problème de manière pédagogique.
Reste simple, précis et accessible.

Problème:
{problem}

Résultat:
{result_text}

Donne une explication courte mais utile, avec des étapes.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content
