"""Programa principal para leitura e plot da curva de juros."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from es import ler_curva_csv
from interpol import interpolar_curva


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    caminho_csv = base_dir / "CurvaZero_04052026.csv"

    vertices, taxas = ler_curva_csv(caminho_csv)
    xs_interp, ys_interp = interpolar_curva(vertices, taxas, num_pontos=300)

    plt.figure(figsize=(10, 6))
    plt.plot(vertices, taxas, "o", label="ETTJ Pré (dados)")
    plt.plot(xs_interp, ys_interp, "-", label="Interpolação polinomial")
    plt.title("Curva de Juros - ETTJ Pré ANBIMA")
    plt.xlabel("Vértices (dias)")
    plt.ylabel("Taxa (% a.a.)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
