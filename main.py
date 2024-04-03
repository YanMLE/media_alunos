TotalAlunos = int(input("Quantos alunos há na sala? "))
d = {}
for i in range(TotalAlunos):
    nome = input("Qual o nome do aluno? ")
    z = nome.split()
    nota = float(input("Qual a nota do aluno? "))
    for i in z:
        if i not in d:
            d[i] = nota
    print(d)
MaisNerd = max(d, key=d.get)
MaiorNota = d[MaisNerd]
print(f"a maior nota foi de {MaisNerd} com nota {MaiorNota}")
MaisBurro= min(d, key=d.get)
MenorNota = d[MaisBurro]
print(f"a menor nota foi de {MaisBurro} com nota {MenorNota}")
TodasNotas = sum(d.values())
média = TodasNotas / TotalAlunos
print(f"a média das notas é {média}")