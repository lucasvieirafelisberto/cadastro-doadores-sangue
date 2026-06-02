import json
from datetime import datetime
import os

# Garante que a pasta data existe
os.makedirs("data", exist_ok=True)


def calcular_idade(ano_nascimento):
    return datetime.now().year - ano_nascimento


def validar_dados(peso, altura):
    if peso <= 0:
        print("Peso inválido")
        return False
    if altura <= 0:
        print("Altura inválida")
        return False
    return True


def verificar_elegibilidade(peso, idade):
    return peso >= 50 and 16 <= idade <= 69


def salvar_doador(doador):
    with open("data/doadores.json", "a") as f:
        json.dump(doador, f)
        f.write("\n")


def listar_doadores():
    try:
        with open("data/doadores.json", "r") as f:
            print("\n===== DOADORES CADASTRADOS =====")
            for linha in f:
                print(linha.strip())
    except FileNotFoundError:
        print("Nenhum doador cadastrado ainda.")


def cadastrar_doador():
    print("\n===== CADASTRO =====")

    nome = input("Nome: ")
    peso = float(input("Peso: "))
    altura = int(input("Altura (cm): "))
    ano_nascimento = int(input("Ano de nascimento: "))

    if not validar_dados(peso, altura):
        return

    idade = calcular_idade(ano_nascimento)
    pode_doar = verificar_elegibilidade(peso, idade)

    doador = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "pode_doar": pode_doar
    }

    salvar_doador(doador)

    print("\n===== RESULTADO =====")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Pode doar: {'Sim' if pode_doar else 'Não'}")


# MENU PRINCIPAL
while True:
    print("\n======= MENU =======")
    print("1 - Cadastrar doador")
    print("2 - Listar doadores")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_doador()
    elif opcao == "2":
        listar_doadores()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida")