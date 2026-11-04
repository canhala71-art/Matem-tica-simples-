"""Auxiliares para gerar aulas ricas. Todas as respostas são calculadas (Fraction), nunca escritas à mão."""
import json, os
from fractions import Fraction as F

ROOT = os.path.join(os.path.dirname(__file__), '..', '..', 'content')

def T(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def num(d, comp, st, val, expl, steps, accepted=None):
    return {"type": "numeric", "difficulty": d, "competency": comp, "statement": st, "options": None,
            "answer": {"value": T(val) if not isinstance(val, str) else val, "accepted": accepted or []},
            "tolerance": 0, "explanation": expl, "steps": steps}

def mc(d, comp, st, labels, correct, expl, steps):
    assert len(set(labels)) == 4 and 0 <= correct < 4
    return {"type": "multiple_choice", "difficulty": d, "competency": comp, "statement": st,
            "options": [{"id": "abcd"[i], "label": l} for i, l in enumerate(labels)],
            "answer": {"choice": "abcd"[correct]}, "tolerance": 0, "explanation": expl, "steps": steps}

def tf(d, comp, st, truth, expl, steps):
    return {"type": "true_false", "difficulty": d, "competency": comp, "statement": st, "options": None,
            "answer": {"boolean": truth}, "tolerance": 0, "explanation": expl, "steps": steps}

def write(level, idx, doc):
    assert len(doc["exercises"]) >= 8, doc["lesson_slug"]
    for k in ["introduction","intuition","definition","formulas","worked_example","guided_exercise",
              "independent_exercise","challenge","assessment"]:
        assert len(doc["blocks"][k]) > 60, (doc["lesson_slug"], k)
    d = os.path.join(ROOT, f"nivel-{level}")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"{idx:02d}-{doc['lesson_slug']}.json"), "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)

INDEP = ("Chegou a tua vez. Resolve os exercícios sem pressa e usa **Verificar** para confirmar. Se errares, não faz mal: lê a resolução passo a passo, "
         "percebe onde o raciocínio escorregou e tenta outra vez. É assim que se aprende de verdade.")
