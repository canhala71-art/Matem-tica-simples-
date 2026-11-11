"""Auxiliar do Nível 2: monta a aula com a estrutura obrigatória e garante 3 básicos / 4 intermédios / 3 avançados."""
from common import *
import math
from collections import Counter

def std(sub, tt, ts, title, slug, summary, mins, obj, pre, intro, concept, definition, formulas, examples, guided, challenge, checks, ex):
    assert len(examples) >= 5, (slug, 'exemplos')
    c = Counter(e['difficulty'] for e in ex)
    assert c[1] >= 3 and c[2] >= 4 and c[3] >= 3, (slug, dict(c))
    assert len(ex) >= 10, slug
    return lesson(sub, tt, ts, title, slug, summary, mins,
        f"**Objetivos:** {obj} **Pré-requisitos:** {pre}\n\n{intro}", concept, definition, formulas,
        "\n\n".join(f"**Exemplo {i+1}.** {e}" for i, e in enumerate(examples)), guided, challenge,
        "Consideras a competência dominada quando consegues: " + "; ".join(f"({i+1}) {k}" for i, k in enumerate(checks)) + ".", ex)

def kz(n):
    s = f"{int(n):,}".replace(",", " ")
    return s
