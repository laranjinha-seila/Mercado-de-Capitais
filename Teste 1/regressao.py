"""Ajuste polinomial global por mínimos quadrados."""
from __future__ import annotations

from typing import Iterable, List, Tuple

import numpy as np


def ajustar_polinomio(
    xs: Iterable[float],
    ys: Iterable[float],
    grau: int,
) -> np.ndarray:
    """Ajusta um polinômio de grau informado aos pontos (mínimos quadrados)."""
    x_vals = np.array(list(xs), dtype=float)
    y_vals = np.array(list(ys), dtype=float)
    if x_vals.size != y_vals.size:
        raise ValueError("xs e ys devem ter o mesmo tamanho")
    if x_vals.size == 0:
        raise ValueError("xs e ys não podem estar vazios")
    if grau < 1:
        raise ValueError("grau deve ser >= 1")
    if grau >= x_vals.size:
        raise ValueError("grau deve ser menor que o número de pontos")

    return np.polyfit(x_vals, y_vals, grau)


def avaliar_polinomio(coeficientes: np.ndarray, xs: Iterable[float]) -> List[float]:
    """Avalia o polinômio ajustado nos pontos informados."""
    x_vals = np.array(list(xs), dtype=float)
    return np.polyval(coeficientes, x_vals).tolist()


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


def ajustar_curva_global(
    xs: Iterable[float],
    ys: Iterable[float],
    grau: int,
    num_pontos: int = 200,
) -> Tuple[List[float], List[float]]:
    """Ajusta uma curva polinomial global usando todos os pontos."""
    malha = gerar_malha(xs, num_pontos=num_pontos)
    coeficientes = ajustar_polinomio(xs, ys, grau)
    valores = avaliar_polinomio(coeficientes, malha)
    return malha, valores
