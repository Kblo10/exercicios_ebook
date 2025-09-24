nota = float(input("Digite sua nota final: "))

if nota >= 7:
    print("Parabéns, você passou!")
elif nota >= 5:
    print("Você está de recuperação")
else:
    print("Reprovado.")