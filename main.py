def adicionar_produto(estoque, produto, quantidade):
    if produto in estoque:
        estoque[produto] += quantidade
    else:
        estoque[produto] = quantidade


def listar_produtos(estoque):
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade}")


def remover_produto(estoque, produto, quantidade):
    if produto in estoque:
        if estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
            if estoque[produto] == 0:
                del estoque[produto]
        else:
            print("Quantidade insuficiente no estoque.")
    else:
        print("Produto não encontrado no estoque.")


def buscar_produto(estoque, produto):
    return estoque.get(produto, "Produto não encontrado no estoque.")


estoque = {}

while True:
    print("Sistema de Estoque")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print('3. Remover Produto')
    print("4. Buscar Produto")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        adicionar_produto(estoque, produto, quantidade)

    elif opcao == "2":
        listar_produtos(estoque)

    elif opcao == "3":
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade a remover: "))
        remover_produto(estoque, produto, quantidade)
    elif opcao == "4":
        produto = input("Digite o nome do produto: ")
        resultado = buscar_produto(estoque, produto)
        print(f"{produto}: {resultado}")
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
