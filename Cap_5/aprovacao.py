nota = float(input("Digite a nota do aluno: "))
frequencia = float(input("Digite a frequeência do aluno (%): "))

aprovado = nota >= 7 and frequencia >= 75

print("Aluno aprovado?", aprovado)