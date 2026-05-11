"""Programa principal para leitura e plot da curva de juros."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from es import ler_curva_csv
from interpol import interpolar_curva, interpolar_curva_local


def _ler_grau(maximo: int) -> int:
    while True:
        entrada = input(
            f"Informe o grau do polinômio (1 a {maximo}): "
        ).strip()
        try:
            grau = int(entrada)
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue
        if 1 <= grau <= maximo:
            return grau
        print(f"O grau deve estar entre 1 e {maximo}.")


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    caminho_csv = base_dir / "CurvaZero_04052026.csv"

    vertices, taxas = ler_curva_csv(caminho_csv)
    grau_max = max(1, len(vertices) - 1)
    grau = _ler_grau(grau_max)

    if grau == grau_max:
        xs_interp, ys_interp = interpolar_curva(vertices, taxas, num_pontos=300)
        legenda = "Interpolação polinomial (global)"
    else:
        xs_interp, ys_interp = interpolar_curva_local(
            vertices, taxas, grau=grau, num_pontos=300
        )
        legenda = f"Interpolação polinomial (grau {grau})"

    plt.figure(figsize=(10, 6))
    plt.plot(vertices, taxas, "o", label="ETTJ Pré (dados)")
    plt.plot(xs_interp, ys_interp, "-", label=legenda)
    plt.title("Curva de Juros - ETTJ Pré ANBIMA")
    plt.xlabel("Vértices (dias)")
    plt.ylabel("Taxa (% a.a.)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
