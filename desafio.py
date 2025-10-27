# Escreva um programa em Python que solicita ao usuário para digitar seu nome,
# o valor do seu salário mensal e o valor do bônus que recebeu.
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e
# informando o valor do salário em comparação com o bônus recebido.

nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário mensal: "))
bonus_prc = float(input("Digite o seu bonus percentual: "))
bonus = salario * bonus_prc

print(f"Olá {nome} o seu salario é $ {salario} e o seu bonus foi de {bonus}")
