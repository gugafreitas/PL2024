import json
import re

def carregar_stock():
    with open('stock.json', 'r') as file:
        return json.load(file)

def salvar_stock(stock):
    with open('stock.json', 'w') as file:
        json.dump(stock, file, indent=2)

def listar_stock(stock):
    print("cod | nome | quantidade | preço")
    print("--------------------------------")
    for produto in stock:
        print(f"{produto['cod']} {produto['nome']} {produto['quant']} {produto['preco']}")

def atualizar_saldo(saldo_atual, entrada_moedas):
    padrao_moeda = re.compile(r'(\d+)\s*(e|c)')
    moedas = padrao_moeda.findall(entrada_moedas)
    for valor, tipo_moeda in moedas:
        if tipo_moeda == 'e':
            saldo_atual += int(valor) * 100
        elif tipo_moeda == 'c':
            saldo_atual += int(valor)
    return saldo_atual

def processar_comando(comando, stock, saldo):
    if comando == "LISTAR":
        listar_stock(stock)
    elif comando.startswith("MOEDA"):
        # Implementar lógica para atualizar o saldo com base nas moedas inseridas
        entrada_moedas = comando.split()[1]  # Extrai a parte da entrada contendo as moedas
        saldo = atualizar_saldo(saldo, entrada_moedas)
        print(f"Saldo atualizado: {saldo} centavos")
        pass
    elif comando.startswith("SELECIONAR"):
        # Implementar lógica para selecionar um produto
        pass
    elif comando == "SAIR":
        # Implementar lógica para retornar o troco e encerrar a interação
        pass
    else:
        print("Comando inválido")

def main():
    stock = carregar_stock()
    saldo = 0
    print("maq: 2024-03-08, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    while True:
        comando = input(">> ").strip().upper()
        if comando:
            processar_comando(comando, stock, saldo)
        else:
            print("Comando vazio. Por favor, insira um comando.")

if __name__ == "__main__":
    main()
