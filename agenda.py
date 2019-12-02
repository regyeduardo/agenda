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


while True:
    print("Opção 1 - Inserir Contato")
    print("Opção 0 - Sair")
    opcao = input("Digite uma opção: ")
    if opcao == "1":
        try:
            inserir_contato()
        except:
            print(f"\nContato inserido...")
    elif opcao == "0":
        break
    else:
        print("Opção Inválida")