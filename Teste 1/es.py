"""Leitura de dados da ETTJ pré da ANBIMA."""
from __future__ import annotations

import csv
from pathlib import Path
from typing import List, Tuple


def _parse_decimal(value: str) -> float:
    return float(value.replace(".", "").replace(",", "."))


def ler_curva_csv(caminho_csv: str | Path) -> Tuple[List[float], List[float]]:
    """Lê arquivo CSV da ETTJ pré e retorna vértices (dias) e taxas (% a.a.)."""
    vertices: List[float] = []
    taxas: List[float] = []
    with open(caminho_csv, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo, delimiter=";")
        next(leitor, None)
        for linha in leitor:
            if not linha or len(linha) < 2:
                continue
            vertice_raw = linha[0].strip()
            taxa_raw = linha[1].strip()
            if not vertice_raw or not taxa_raw:
                continue
            vertices.append(_parse_decimal(vertice_raw))
            taxas.append(_parse_decimal(taxa_raw))
    return vertices, taxas
