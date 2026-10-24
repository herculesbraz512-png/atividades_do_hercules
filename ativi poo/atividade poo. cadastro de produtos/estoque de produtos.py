def exibir_menu():
    print ("\n====== ESTOQUE DA LOJA ======")
    print ("1 - adicionar produto")
    print ("2 - remover produto")
    print ("3 - atualizar quantidade")
    print ("4 - exibir estoque")
    print ("0 - sair")
    print ("====== ESTOQUE DA LOJA ======")

def ler_quantidade(mensagem):
    while True:
        try:
            quantidade = int(input(mensagem))
            if quantidade >= 0:
                return quantidade
            else:
                print ("a quantidae não pode ser negativa")
        except ValueError:
            print ("digite um numero: ")

def adicionar_produto(estoque, nome, quantidade):
    nome = nome.strip().title()
    if nome in estoque:
        print("ja tem o produto, use atualizar")
    else:
        estoque[nome] = quantidade
        print("produto adicionado")

def remover_produto(estoque, nome):
    nome = nome.strip().title()
    if nome in estoque:
        del estoque[nome]
        print("produto removido")
    else:
        print("produto não encontrado")

def atualizar_quantidade(estoque, nome, quantidade):
    nome = nome.strip().title()
    if nome in estoque:
        estoque[nome] = quantidade
        print("quantidade atualizada")
    else:
        print("produto não encontrado")

def exibir_estoque(estoque):
    if not estoque:
        print("estoque vazio")
    else:
        print("\n====== PRODUTOS ======")
        for nome, quantidade in estoque.items():
            print(f"{nome}:{quantidade} unidades")

def main():
    estoque = {}
    while True:
        exibir_menu()
        opcao = input("escolha uma opição: ")
        if opcao == "1":
            nome = input("nome do produto: ").strip().title()
            if nome == "":
                print("o nome não pode ficar vazio")
                continue
            quantidade = ler_quantidade("quantidade: ")
            adicionar_produto(estoque, nome, quantidade)
        elif opcao =="2":
            nome = input("nome do produto: ")
            remover_produto(estoque, nome)
        elif opcao =="3":
            nome = input("nome do produto: ")
            quantidade = ler_quantidade("nova quantidade: ")
            atualizar_quantidade(estoque, nome, quantidade)
        elif opcao == "4":
            exibir_estoque(estoque)
        elif opcao == "0":
            print("programa encerrado")
            break
        else:
            print("opção invalida")
main()                        



    