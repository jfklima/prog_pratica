# numeros = []

# while len(numeros) < 5:
#   try:
#     numero = int(input("Digite número: "))
#   except ValueError:
#     print("Digite um inteiro")
#   else:
#     numeros.append(numero)

# maximo = max(numeros)

# print(f"Números: {numeros}")
# print(f"Máximo: {maximo}")

# maximo = float(input("Digite um número: "))

for _ in range(4):
    maximo = max(maximo, float(input("Digite um número: ")))
    print(f"Número máximo encontrado até agora é: {maximo}")
