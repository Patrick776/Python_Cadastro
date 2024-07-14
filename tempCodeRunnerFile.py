import datetime

cadastros = []

def cadastrar ():
    print("\n===== Cadastro de Usuário =====")
    nome_completo = input("Nome completo: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
    nome_mae = input("Nome da mãe: ")
    nome_pai = input("Nome do pai: ")
    estado_civil = input("Estado civil: ")
    endereco = input("Endereço: ")
    numero_residencia = input("Número da residência: ")
    bairro = input("Bairro: ")
    cep = input("CEP: ")
    formacao = input("Formação de estudo com nível faculdade: ")
    ultimo_emprego = input("Último emprego ou atual empregado: ")
    idioma = input("Idioma que saiba escrever e ler: ")

cadastro [
    "nome_completo": nome_completo,
    "cpf": cpf,
    "rg": rg,
    "data_nascimento": data_nascimento,
    "nome_mae": nome_mae,
    "nome_pai": nome_pai,
    "estado_civil": estado_civil,
    "endereco": endereco,
    "numero_residencia": numero_residencia,
    "bairro": bairro,
    "cep": cep,
    "formacao": formacao,
    "ultimo_emprego": ultimo_emprego,
    "idioma": idioma
    ]

    cadastros.append(cadastro)
    print("Usuário cadastrado com sucesso!")
    
def consultar():
    cpf = input("\nDigite o CPF do usuário para consulta: ")
    for cadastro in cadastros:
        if cadastro["cpf"] == cpf:
            print("\n===== Dados do Usuário =====")
            for key, value in cadastro.items():
                print(f"{key.replace('.'. '-').capitalize()}: {value}")
            return
    print("Usuário não encontrado.")

def alterar():
    cpf = input("\nDigite o CPF do usuário para alteração: ")
    for cadastro in cadastros:
        if cadastro["cpf"] == cpf:
            print("\n===== Alterar Dados do Usuário =====")
            for key, value in cadastro.items():
                novo_valor = input(f"{key.replace('.', '-').capitalize()} ({value}): ")
                if novo_valor:
                    cadastro[key] = novo_valor
            print("Dados alterados com sucesso!")
            return
        print("Usuário não encontrado.")

def remover():
    cpf = input("\nDigite o CPF do usuário para remoção: ")
    for cadastro in cadastros:
        if cadastro["cpf"] == cpf:
        cadastros.remove(cadastro)
        print("Usuário removido com sucesso!")
        return
    print("Usuário não encontrado.")

def menu():
    while true:
        print("\n===== Menu =====")
        print("1 - Cadastrar")
        print("2 - Consultar")
        print("3 - Alterar ou atualizar dados")
        print("4 - Remover dados cadastrados")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            consultar()
        elif opcao == '3':
            alterar()
        elif opcao == '4':
            remover()
        elif opcao == '5':
            print("Saindo do progreama...Obrigado")
            break
        else:
            print("Opção inválida, por favor escolha novamente.")

if __name__== "__main__":
    menu()