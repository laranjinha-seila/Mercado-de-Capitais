#Exercícios Unidade 1

# 1
print("Hello, World!")

# 2
a = 2 
b = 3
print(a + b)

# 3
x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))
Soma = x + y
print("Soma:", Soma)

# 4
nome = input("Digite seu nome: ")
print("Oi,", nome)

# 5
horas = float(input("Horas trabalhadas: "))
salario_bruto = horas * 40
desconto = salario_bruto * 0.3
salario_liquido = salario_bruto - desconto
print(salario_bruto, salario_liquido, desconto)

# 6 (PA)
a1 = float(input("Primeiro termo: "))
r = float(input("Razão: "))
n = int(input("Quantos termos: "))
an = a1 + (n - 1) * r
soma = n * (a1 + an) / 2
print(an, soma)

# 7 (PG)
a1 = float(input("Primeiro termo: "))
r = float(input("Razão: "))
n = int(input("Quantos termos: "))
an = a1 * (r ** (n - 1))
soma = a1 * (r**n - 1) / (r - 1) if r != 1 else a1 * n
print(an, soma)

# 8 (ax = b)
a = float(input("a: "))
b = float(input("b: "))
if a != 0:
    print("x =", b / a)

# 9 (2º grau)
import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
delta = b**2 - 4*a*c
if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(x1, x2)

# 10 (juros compostos)
C = float(input("Capital: "))
t = float(input("Tempo: "))
i = float(input("Taxa: "))
M = C * (1 + i) ** t
print(M)

# 11
nums = [float(input(f"Escolha o {i+1}º número: ")) for i in range(4)]
print(sum(nums)/4)

# 12 (círculo)
r = float(input("Raio: "))
area = 3.14 * r**2
circ = 2 * 3.14 * r
print(area, "e", circ)

# 13
renda = float(input("Qual sua renda?: "))
preco = float(input("Qual o preço do bem demando?: "))
q = renda / preco
print("A quantidade é", q)

# 14 (distância)
x1, y1 = float(input("x1 é igual a: ")), float(input("y1 é igual a: "))
x2, y2 = float(input("x2 é igual a: ")), float(input("y2 é igual a: "))
dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(dist)

# 15
numeros = [float(input(f"Digite o {i+1}º valor: ")) for i in range(3)]
numeros.sort()
print(f"\nValores em ordem crescente: {numeros}")

# 16 (CAPM)
Rf = float(input("Qual o retorno do ativo sem risco?: "))
Rm = float(input("Qual o retorno da carteira de mercado?: "))
beta = float(input("Qual o coeficiente de sensibilidade?: "))
ER = Rf + beta * (Rm - Rf)
print(ER)
