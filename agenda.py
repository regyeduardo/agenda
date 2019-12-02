# -*- coding: utf-8 -*-
import csv
def salvar_contato(nome, tel, email, ende):
    with open('contatos.csv', 'a') as file:
            file.write(f"{nome},{tel},{email},{ende}\n")



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

def apagar_contato():
    contato = input("Qual contato quer apagar? ")
    contatos = []
    aux = []
    with open('contatos.csv','r') as file:
        for lines in file:
            contatos.append(lines.strip().split(','))
    
    ver = False
    for n in contatos:
        if contato in n[0]:
            ver = True
        else:
            aux.append(n)
    
    if not ver:
        print("Contato não encontrado")
    else:
        with open('contatos.csv', 'w') as file:
            file.write("") # Precisa do \n para pular uma linha
        print("Apagado com sucesso")
    
        for cont in aux:
            nome = cont[0]
            tel = cont[1]
            email = cont[2]
            endereco = cont[3]
            salvar_contato(nome, tel, email,endereco)
        
        

while True:
    print("\nOpção 1 - Inserir Contato")
    print("Opção 3 - Apagar Contato")
    print("Opção 5 - Mostrar Contatos")
    print("Opção 0 - Sair")
    opcao = input("Digite uma opção: ")
    if opcao == "1":
        try:
            inserir_contato()
        except:
            print(f"\nContato inserido...")
    elif opcao == "3":
        apagar_contato()
    elif opcao == "5":
        mostrar_contatos()
    elif opcao == "0":
        break
    else:
        print("Opção Inválida")