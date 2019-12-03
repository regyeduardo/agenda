# -*- coding: utf-8 -*-
import csv
def salvar_contato(nome, tel, email, ende):
    with open('contatos.csv', 'a') as file:
            nome = nome.replace(","," ")
            tel = tel.replace(","," ")
            email = email.replace(","," ")
            ende = ende.replace(","," ")
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

def apagar_contato(contato):
    contatos = retorna_lista_contatos()
    aux = []
    
    for n in contatos:
        if contato.lower() == n[0].lower():
            pass
        else:
            aux.append(n)
    
    if verifica_existencia_contato(contato):
        with open('contatos.csv', 'w') as file:
            file.write("")

        for cont in aux:
            nome = cont[0]
            tel = cont[1]
            email = cont[2]
            endereco = cont[3]
            salvar_contato(nome, tel, email,endereco)
        return aux
    else:
        print("Contato não encontrado")
    
    
def verifica_existencia_contato(contato):
    contatos = []
    with open('contatos.csv','r') as file:
        for lines in file:
            contatos.append(lines.strip().split(','))
    
    ver = False
    for n in contatos:
        if contato.lower() == n[0].lower():
            ver = True
    
    if ver:
        return True
    else:
        return False

def retorna_lista_contatos():
    contatos = []
    with open('contatos.csv','r') as file:
        for lines in file:
            contatos.append(lines.strip().split(','))
    
    return contatos

    
def buscar_contato(contato):
    
    contatos = retorna_lista_contatos()

    if verifica_existencia_contato(contato):
        for n in contatos:
            if contato.lower() == n[0].lower():
                print(f"\nNome: {n[0]}")
                print(f"Telefone: {n[1]}")
                print(f"Email: {n[2]}")
                print(f"Endereço: {n[3]}")
    else:
        print("Contato não encontrada")



def editar_contato(contato):
    if verifica_existencia_contato(contato):
        apagar_contato(contato)
        tel = input(f"Insira o novo tefone: ") 
        email = input("Insira o novo email: ") 
        ende = input("Insira o novo endereço: ")
        salvar_contato(f"{contato[0].upper()+contato[1:]}", tel, email, ende)
    else:
        print("Contato não existe")


def exportar_contatos():
    filename = input("Digite o nome do arquivo para exportar: ")
    contatos = retorna_lista_contatos()
    with open(f'{filename}.csv', 'w') as file:
        file.write("")
    for cont in contatos:
        with open(f'{filename}.csv', 'a') as file:
            nome = cont[0].replace(","," ")
            tel = cont[1].replace(","," ")
            email = cont[2].replace(","," ")
            ende = cont[3].replace(","," ")
            file.write(f"{nome},{tel},{email},{ende}\n")
    

while True:
    print("\nOpção 1 - Inserir Contato")
    print("Opção 2 - Editar Contato")
    print("Opção 3 - Apagar Contato")
    print("opção 4 - Buscar Contato")
    print("Opção 5 - Mostrar Contatos")
    print("Opção 6 - Exportar Contatos")
    print("Opção 0 - Sair")
    opcao = input("Digite uma opção: ")
    if opcao == "1":
        try:
            inserir_contato()
        except:
            print(f"\nContato inserido...")
    elif opcao == "2":
        contato = input("Qual contato quer editar? ")
        editar_contato(contato)
    elif opcao == "3":
        contato = input("Qual contato quer apagar? ")
        apagar_contato(contato)
    elif opcao == "4":
        contato = input("Qual contato quer buscar? ")
        buscar_contato(contato)
    elif opcao == "5":
        mostrar_contatos()
    elif opcao == "6":
        exportar_contatos()
    elif opcao == "0":
        break
    else:
        print("Opção Inválida")