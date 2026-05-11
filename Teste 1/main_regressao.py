"""Programa principal para ajuste polinomial global (regressão)."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from es import ler_curva_csv
from regressao import ajustar_curva_global


def _solicitar_grau(max_grau: int) -> int:
    while True:
        entrada = input(
            f"Informe o grau do polinômio (1 a {max_grau}) [default 1]: "
        ).strip()
        if not entrada:
            return 1
        try:
            grau = int(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue
        if 1 <= grau <= max_grau:
            return grau
        print(f"Grau fora do intervalo permitido (1 a {max_grau}).")


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    caminho_csv = base_dir / "CurvaZero_04052026.csv"

    vertices, taxas = ler_curva_csv(caminho_csv)
    grau = _solicitar_grau(len(vertices) - 1)
    xs_ajuste, ys_ajuste = ajustar_curva_global(
        vertices, taxas, grau=grau, num_pontos=300
    )

    plt.figure(figsize=(10, 6))
    plt.plot(vertices, taxas, "o", label="ETTJ Pré (dados)")
    plt.plot(xs_ajuste, ys_ajuste, "-", label=f"Regressão polinomial (grau {grau})")
    plt.title("Curva de Juros - ETTJ Pré ANBIMA (Ajuste Global)")
    plt.xlabel("Vértices (dias)")
    plt.ylabel("Taxa (% a.a.)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
