from html.entities import name2codepoint
import os
# Adicionar itens
# Remover itens
# Exibir itens e valor a pagar

produtos = (
    {'id': 1, 'nome': 'Filme1', 'precoCompra': 8.00, 'precoAluguel': 5.00},
    {'id': 2, 'nome': 'Filme2', 'precoCompra': 8.00, 'precoAluguel': 5.00},
    {'id': 3, 'nome': 'Filme3', 'precoCompra': 8.00, 'precoAluguel': 5.00},
    {'id': 4, 'nome': 'Filme4', 'precoCompra': 8.00, 'precoAluguel': 5.00}
)

carrinho = []


def exibirOpcoes():
    print('\n\n')
    print('1 - Adicionar Item')
    print('2 - Remover Item')
    print('3 - Exibir itens e o valor total de compra')
    print('4 - Exibir itens e o valor total de locação')
    print('5 - Limpar Carrinho')
    print('6 - Sair')


def exibirProdutos():
    for p in produtos:
        print(
            'Id: {0} - Nome: {1} - Preço de compra: {2} - Preço de aluguel: {3} \n'.format(p['id'], p['nome'], p['precoCompra'], p['precoAluguel']))


opcao = '1'

os.system('clear')
print('Meus filmes/séries \n')


def obterNomeProduto(id):
    for p in produtos:
        if p['id'] == id:
            return p['nome']


while opcao != '6':
    exibirOpcoes()
    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        exibirProdutos()
        id = int(input('Digite o número identificador do filme: '))
        quantidade = int(input('Digite quantidade de dias, em caso de aluguel (se for compra, digite 0):'))
        carrinho.append({'id': id, 'quantidade': quantidade})

    if opcao == '2':
        id = int(input('Digite o número identificador do filme que deseja excluir: '))
        temp = []
        for item in carrinho:
            if item['id'] != id:
                temp.append(item)

    if opcao == '3':
        print('\n\n')
        somatorio = 0
        for item in carrinho:
            for produto in produtos:
                if produto['id'] == item['id']:
                    somatorio = somatorio + \
                        (produto['precoCompra'])
                    break

            print(
                'Nome: {0} - Quantidade: {1}'.format(obterNomeProduto(item['id']), item['quantidade']))
        print('Preço total: {0}'.format(somatorio))

    if opcao == '4':
        print('\n\n')
        somatorio = 0
        for item in carrinho:
            for produto in produtos:
                if produto['id'] == item['id']:
                    somatorio = somatorio + \
                       (produto['precoAluguel'] * item['quantidade'])
                    break

     
            print(
                'Nome: {0} - Quantidade: {1}'.format(obterNomeProduto(item['id']), item['quantidade']))
        print('Preço total: {0}'.format(somatorio))


    if opcao == '5':
        carrinho = []