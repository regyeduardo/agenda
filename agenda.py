# -*- coding: utf-8 -*-
def salvar_contato(nome, tel, email, ende):
    with open('contatos.csv', 'a') as file:
        file.write(f"{nome},{tel},{email},{ende}\n") # Precisa do \n para pular uma linha


def inserir_contato():
    nome = input("\nNome do contato: ") 
    telefone = input(f"Insira o tefone de {nome}: ") 
    email = input("Insira o email: ") 
    endereco = input("Insira o endereço: ")
    salvar_contato(nome, telefone, email, endereco)


def mostrar_contatos():
    try:
        with open('contatos.csv', 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                contatos = linha.strip().split(',')
                print(f"\nNome: {contatos[0]}")
                print(f"Telefone: {contatos[1]}")
                print(f"Email: {contatos[2]}")
                print(f"Endereço: {contatos[3]}")
    except Exception as error:
        print("Algo deu errado")
        print(error)


while True:
    print("\nOpção 1 - Inserir Contato")
    print("Opção 5 - Mostrar Contatos")
    print("Opção 0 - Sair")
    opcao = input("Digite uma opção: ")
    if opcao == "1":
        try:
            inserir_contato()
        except:
            print(f"\nContato inserido...")
    if opcao == "5":
        mostrar_contatos()
    elif opcao == "0":
        break
    else:
        print("Opção Inválida")