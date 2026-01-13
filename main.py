import tkinter as tk
import json
import os

janela = tk.Tk()
janela.title("Sistema de Estoque")
janela.geometry("600x500")
tk.Label(janela, text="Bem-vindo ao Sistema de Estoque").pack()
tk.Label(janela, text="SISTEMA DE ESTOQUE", bg="#f0f0f0", font=("Helvetica", 16, "bold"), fg="#333").pack(pady=10)

cor_fundo = "#d1d1d1"
largura_botoes = 25


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


Arquivo_estoque = "estoque_dados.json"


def salvar_dados():
    with open(Arquivo_estoque, 'w') as f:
        json.dump(estoque, f, indent=4)


def carregar_dados():
    global estoque
    if os.path.exists(Arquivo_estoque):
        with open(Arquivo_estoque, 'r') as f:
            estoque = json.load(f)
    else:
        estoque = {}


def clicar_adicionar():
    nome = entra_nome.get()
    qtd = int(entra_quantidade.get())

    adicionar_produto(estoque, nome, qtd)
    salvar_dados()
    print(f"Produto {nome} adicionado com quantidade {qtd}.")


def clicar_listar():
    if not estoque:
        label_lista.config(text="Estoque vazio.")
        return

    texto_acumulado = "Lista de Produtos no Estoque:\n"
    for produto, quantidade in estoque.items():
        texto_acumulado += f"{produto}: {quantidade}\n"

    label_lista.config(text=texto_acumulado)


def excluir_produto():
    nome = entra_nome.get()
    qtd = int(entra_quantidade.get())

    remover_produto(estoque, nome, qtd)
    salvar_dados()
    print(f"Produto {nome} removido com quantidade {qtd}.")


def buscar_produto_gui():
    if not estoque:
        label_lista.config(text="Estoque vazio.")
        return
    texto = entra_nome.get()
    resultado = buscar_produto(estoque, texto)
    label_lista.config(text=f"Produto: {texto}, Quantidade: {resultado}")


estoque = {}
carregar_dados()

tk.Label(janela, text="Nome do Produto:", bg=cor_fundo, font=("Arial", 10, "bold")).pack(pady=(10, 0))
entra_nome = tk.Entry(janela, font=("Arial", 11), width=35)
entra_nome.pack(pady=5)

tk.Label(janela, text="Quantidade:", bg=cor_fundo, font=("Arial", 10, "bold")).pack(pady=(10, 0))
entra_quantidade = tk.Entry(janela, font=("Arial", 11), width=35)
entra_quantidade.pack(pady=5)

botao_add = tk.Button(janela, text="Adicionar ao Estoque", command=clicar_adicionar,
                      bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=largura_botoes)
botao_add.pack(pady=5)

botao_listar = tk.Button(janela, text="Listar Produtos", command=clicar_listar, width=largura_botoes)
botao_listar.pack(pady=2)

botao_remover = tk.Button(janela, text="Remover do Estoque", command=excluir_produto, width=largura_botoes)
botao_remover.pack(pady=2)

botao_buscar = tk.Button(janela, text="Buscar Produto", command=buscar_produto_gui, width=largura_botoes)
botao_buscar.pack(pady=2)

label_lista = tk.Label(janela, text="",
                       bg="white", font=("Consolas", 10),
                       width=50, height=8, relief="sunken", anchor="nw", justify="left", padx=10, pady=10)
label_lista.pack()

janela.mainloop()
