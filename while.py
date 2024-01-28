notas = []

contador = 1

while contador <= 3:
    nome = input("nome:")
    nota = float(input("nota:"))
    resultado = [nome, nota]
    notas.append(resultado)

    # alterando contador:
    contador = contador + 1
    # ou contador += 1

print("Quantidade de notas", len(notas))

for n in notas:
    nome = n[0]
    nota = n[1]
    print("O aluno ", nome, "tirou nota ", nota)