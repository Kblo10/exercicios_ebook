def calcular_media(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media

def ler_nota(numero_bimestre):
    while True:
        try:
            nota = float(input(f"Digite a {numero_bimestre}ª nota (entre 0 e 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota fora do intervalo permitido! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")

# Leitura das notas com validação
nota1 = ler_nota(1)
nota2 = ler_nota(2)
nota3 = ler_nota(3)
nota4 = ler_nota(4)

# Cálculo da média
media_final = calcular_media(nota1, nota2, nota3, nota4)

# Exibição do resultado
print(f"\nMédia final: {media_final:.2f}")

if media_final >= 7:
    print("Situação: Aprovado ✅")
else:
    print("Situação: Reprovado ❌")