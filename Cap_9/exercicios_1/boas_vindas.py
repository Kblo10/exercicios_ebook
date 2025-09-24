def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vindo(a) ao nosso programa."

try:
    nome_usuario = input("Digite seu nome: ")
    print(saudacao(nome_usuario))

except:
    print(f"Ocorreu um erro, tente novamente.")