import os  

mensagens = []

nome = input("Nome: ")

while True:

    #limpa terminal

    os.system('clear')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("--------------------------------")

    #Pegando o texto
    texto = input("Mensagem: ")
    if texto == "fim":
        break

    mensagens.append({
        "nome": nome,
        "texto": texto
    })