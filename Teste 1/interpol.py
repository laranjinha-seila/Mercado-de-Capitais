"""Rotinas de interpolação polinomial (Lagrange)."""
from __future__ import annotations

from typing import Iterable, List, Tuple


def lagrange_interpolate(x: float, xs: Iterable[float], ys: Iterable[float]) -> float:
    """Avalia o polinômio interpolador de Lagrange em x."""
    x_vals = list(xs)
    y_vals = list(ys)
    if len(x_vals) != len(y_vals):
        raise ValueError("xs e ys devem ter o mesmo tamanho")
    if not x_vals:
        raise ValueError("xs e ys não podem estar vazios")

    total = 0.0
    for i, x_i in enumerate(x_vals):
        termo = y_vals[i]
        for j, x_j in enumerate(x_vals):
            if i == j:
                continue
            termo *= (x - x_j) / (x_i - x_j)
        total += termo
    return total


def gerar_malha(xs: Iterable[float], num_pontos: int = 200) -> List[float]:
    """Gera uma malha uniforme entre o menor e o maior vértice."""
    x_vals = list(xs)
    if not x_vals:
        raise ValueError("xs não pode estar vazio")
    if num_pontos < 2:
        return [float(x_vals[0])]

    x_min = min(x_vals)
    x_max = max(x_vals)
    passo = (x_max - x_min) / (num_pontos - 1)
    return [x_min + passo * i for i in range(num_pontos)]


def interpolar_curva(
    xs: Iterable[float],
    ys: Iterable[float],
    num_pontos: int = 200,
) -> Tuple[List[float], List[float]]:
    """Interpolação polinomial da curva em uma malha uniforme."""
    malha = gerar_malha(xs, num_pontos=num_pontos)
    valores = [lagrange_interpolate(x, xs, ys) for x in malha]
    return malha, valores
