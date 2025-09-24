import json
import os

ARQUIVO_JSON = "cadastros.json"
cadastros = []

# Função para salvar no JSON
def salvar_json():
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(cadastros, f, ensure_ascii=False, indent=4)

# Função para carregar do JSON
def carregar_json():
    global cadastros
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            cadastros = json.load(f)

# Função para cadastrar um pet
def cadastrar_pet():
    print("\n--- Cadastro de Pet ---")
    nome_dono = input("Nome do dono: ")
    nome_pet = input("Nome do Pet: ")
    raca = input("Raça do pet: ")
    print("Tipos de serviço: banho, tosa, vacina, etc")
    servico = input("Tipo de serviço: ")

    pet = {
        "dono": nome_dono,
        "pet": nome_pet,
        "raça": raca,
        "servico": servico
    }

    cadastros.append(pet)
    salvar_json()
    print("✅ Cadastro realizado com sucesso!\n")

# Função para listar os cadastros
def listar_cadastro():
    print("\n--- Lista de Cadastros ---")
    if not cadastros:
        print("ℹ️ Nenhum Pet cadastrado ainda.")
    else:
        for i, pet in enumerate(cadastros, 1):
            print(f"{i}. Dono: {pet.get('dono')}, Pet: {pet.get('pet')}, Serviço: {pet.get('servico')}")

# Função para editar um cadastro
def editar_cadastro():
    listar_cadastro()
    if not cadastros:
        return
    
    try:
        indice = int(input("Digite o número do pet que deseja editar: ")) - 1
        if 0 <= indice < len(cadastros):
            cadastros[indice]['dono'] = input("Novo nome do dono: ")
            cadastros[indice]['pet'] = input("Novo nome do pet: ")
            cadastros[indice]['raça'] = input("Nova raça: ")
            cadastros[indice]['servico'] = input("Novo serviço: ")
            salvar_json()
            print("✅ Cadastro atualizado com sucesso!\n")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida.")

# Função para excluir um cadastro 

def excluir_cadastro():
    listar_cadastro()
    if cadastros:
        try:
            indice = int(input("Digite o número do pet que deseja excluir: ")) - 1
            if 0 <= indice < len(cadastros):
                cadastros.pop(indice)
                salvar_json()
                print("🗑️ Cadastro excluído com sucesso!\n")
            else:
                print("❌ Número inválido.")
        except ValueError:
            print("❌ Entrada inválida.")

# Menu Principal
def menu():
    carregar_json()  # 🔹 Carrega os dados salvos antes de iniciar
    while True:
        print("\n🐾 Bem-vindo ao Pet Shop AuMigo 🐾")
        print("1 - Cadastrar Pet")
        print("2 - Listar Cadastros")
        print("3 - Editar Cadastro")
        print("4 - Excluir Cadastro")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pet()
        elif opcao == "2":
            listar_cadastro()
        elif opcao == "3":
            editar_cadastro()
        elif opcao == "4":
            excluir_cadastro()
        elif opcao == "5":
            print("\nSaindo... Até a próxima!\n")
            break
        else:
            print("❌ Opção inválida!")

# Executar o programa
menu()