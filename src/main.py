#Bibliotecas
from datetime import datetime
import json

def calcular_idade(ano_nascimento):
    return datetime.now().year - ano_nascimento

while True:

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
        continue

    #Regras
    idade = calcular_idade(ano_nascimento)
    pode_doar = peso >= 50 and 16 <= idade <= 69

    doador = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "pode_doar": pode_doar
    }

    with open("data/doadores.json", "a") as f:
        json.dump(doador, f)
        f.write("\n")

    #Saída dos valores informados:
    print(f"NOME: {nome}")
    print(f"PESO: {peso}kg")
    print(f"ALTURA: {altura}cm")
    print(f"IDADE: {idade} anos")
    print(f"Pode doar sangue: {'Sim' if pode_doar else 'Não'}")
    print('=' * 50)

    continuar = input("Deseja continuar? (s/n): ")

    if continuar.lower() != 's':
        break


opcao = input("1 - Cadastrar | 2 - Listar: ")

if opcao == "2":
    with open("data/doadores.json", "r") as f:
        for linha in f:
            print(linha)