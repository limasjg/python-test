notas = []

for x in range(5):
    nome = input("Nome:")
    nota = float(input("Nota:"))
    resultado = [nome, nota]
    notas.append(resultado)

print( "quantidade de notas ", len(notas) )

for n in notas:
    nome = n[0]
    nota = n[1]
    print("O aluno ", nome, "tirou nota ", nota)