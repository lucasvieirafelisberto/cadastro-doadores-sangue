#Bibliotecas
from datetime import datetime

#Cadastro da ficha do doador
print('=' * 50)
print("Bem-vindo ao Cadastro de doadores de sangue")
nome = str(input("Por favor informe o seu nome completo: "))
peso = float(input("Por favor informe o seu peso: "))
altura = int(input("Por favor informe sua altura em cm: "))
ano_nascimento = int(input("Por favor informe seu ano de nascimento: "))

erro = False

if peso <= 0:
    print("Peso inválido")
    erro = True

if altura <= 0:
    print("Altura inválida")
    erro = True

if erro:
    exit()

#Regras
idade = datetime.now().year - ano_nascimento 
pode_doar = peso >= 50 and 16 <= idade <= 69

#Saída dos valores informados:
print(f"NOME: {nome}")
print(f"PESO: {peso}kg")
print(f"ALTURA: {altura}cm")
print(f"IDADE: {idade} anos")
print(f"Pode doar sangue: {'Sim' if pode_doar else 'Não'}")
print('=' * 50)