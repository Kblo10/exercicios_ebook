idade = int(input("Qual a sua idade: "))
experiencia = input("Tem experiência? (S/N): ")

if idade >= 18 and experiencia == "S":
    print("Candidato apto.")
else:
    print("Candidato não apto.")