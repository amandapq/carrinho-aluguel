from produtos import Produtos


class Cesta:
    produtos = []
    total =0


    def main():
        p1 = Produtos('Filme1',5.0)
        p2 = Produtos('Filme2', 5.0)
        p3 = Produtos('Filme3', 5.0)
        p4 = Produtos('Filme4', 5.0)
        c = Cesta()
        c.produtos.append(p1)
        c.produtos.append(p2)
        c.produtos.append(p3)
        c.produtos.append(p4)

        print("Filmes escolhidos:")
        for item in c.produtos:
                print(item.nome, item.preco)


        ### ver qual é mais fácil de fundir com o carrinho de compras 

        print("Total a pagar")
        for item in c.produtos:
            c.total+=item.preco
            print(f'R${c.total}')

            ### segunda opção:

            dias = int(input('Quantos dias de aluguel?'))
            filmes = float(input('Quantos filmes você está locando?'))
            pago = dias * 5 * filmes
            print('O total a pagar é R${:.2f}'.format(pago))

