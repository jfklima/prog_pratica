# Lista de Exercícios da Python Brasil
# Tópico: Estrutura de decisaõ
# Exercício 05

# Faça um programa para a leitura de duas notas parciais de
# um aluno. O programa deve calcular a média alcançada por
# aluno e apresentar.
#   * A mensagem "Aprovado", se a média alcançada for maior
#   * ou igual a sete;
#   * A mensagem "Reprovado", se a média alcançada for
#   * menor do que sete;
#   * A mensagem "Aprovado com Distinção", se a média for
#   * igual a dez;

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) / 2

print(f"Média: {media}")
if media == 10:
    print("Aprovado com Disitinção")
elif media >= 7:
    print("Aprovado")
elif media <= 7:
    print("Reprovado")
