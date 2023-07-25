menu = ''
cate = ''
sacola = []
item_sacola = []
remov = ''
finalizar = ''
efetuar_compra =[]

while True:
    print('==== Bem vindo ao Restaurante do Mineiro ====')
    
    print('===== Menu ======')
    print('1-cardápio')
    print('2-Sacola')
    print('3-Entrar em contato')
    print('4-Sair do App')
    
    menu = input('Escola a opção desejada: ')
    
    print('-'*50)
    
    while True:
        if menu == '1':
            print('Aqui você pode visualizar as nossas opções')
        
            print('1-Lanches')
            print('2-Doces - Em construção')
            print('3-Salgados - Em construção')
            print('4-Bebidas - Em construção')
            print('5-Menu')
            cate = input('Escolha a categoria que deseja acessar: ')
        
            if cate == '1':
                print('===== Opações de lanches =====')
                print('1- 1 Veggie Cheese + 1 Entrada + 1 Bebida')
                print('Pão, 115g do blend feito de plantas do incrível Futuro Burger, queijo cheddar, queijo muçarela, alface picado, cebola no shoyu, alho frito e molho à sua escolha.')
                print('A partir de R$ 55,00')
                lanche_01 = ('1 Veggie Cheese + 1 Entrada + 1 Bebida')
                
                print('-'*50)
                
                print('2- QUESADILLA DE FRANGO')
                print('Um pedacinho do méxico por aqui! Tortilha de trigo recheada com frango desfiado, mix de queijo muçarela com cheddar, bacon em cubos e pico de gallo. Arriba!')
                lanche_02 = ('QUESADILLA DE FRANGO')
                print('R$ 29,00')
                
                print('-'*50)
                
                print('3- FRANGO CREAM CHEESE')
                lanche_03 = ('FRANGO CREAM CHEESE')
                print('Frango empanado, muçarela derretida, cream cheese, alho crocante, cebola roxa, tomate e alface.')
                print('R$ 33,00')
                
                print('-'*50)
                
                print('4- COMPLETÃO')
                lanche_04 = ('COMPLETÃO')
                print('2 salsicha perdigão, purê, milho, ervilha, maionese, batata palha, Catupiry, cheddar, muçarela, bacon e calabresa.')
                print('Serve 1 pessoa')
                print('R$ 33,99')
                
                print('-'*50)
                
                
                print('5- CHEESE SALADA VEGETARIANO + COCA-COLA 350ML + FRITAS')
                lanche_05 = ('CHEESE SALADA VEGETARIANO + COCA-COLA 350ML + FRITAS')
                print('Pão Hambúrguer, Hambúrguer Vegetariano, Queijo, Alface, Tomate e Maionese - Coca-Cola lata 350ml + Fritas Individual 200')
                print('Serve 1 pessoa')
                print('#Combo Hamburguer Week')
                print('R$ 41,90')
                
                print('-'*50)
                
                pedi = input('Selecione o lanche desejado: ')
                
                if pedi == '1':
                    sacola.append(lanche_01)
                if pedi == '2':    
                    sacola.append(lanche_02)
                if pedi == '3':    
                    sacola.append(lanche_03)
                if pedi == '4':    
                    sacola.append(lanche_04)
                if pedi == '5':    
                    sacola.append(lanche_05)
                    
                    print('Pedido adcionado a Sacola')
                    print('-'*50)
                    continue
            if cate == '5':
                print('Retornando ao Menu')
                break
            continue
        elif menu == '2':
            if len(sacola) >= 0:
                print('Itens da sua sacola')
                item_sacola.append(sacola)
                for indice, item_sacola in enumerate(item_sacola):
                    print(indice, item_sacola)
                    
                    remov = input('Deseja remover algum item da sacola? sim ou não: ')
                    
                    if remov == 'sim':
                        apagar = int(input('Qual item deseja remover? '))
                        print(len(item_sacola))
                        if apagar >= 0 and apagar < len(item_sacola):
                            del item_sacola[apagar]
                        print('Item removido da sacola')
                        
                    elif remov == 'não':
                        finalizar = input('Deseja finalizar a sua compra? sim ou não ')
                        
                        if finalizar == 'sim':
                            efetuar_compra.append(item_sacola)
                            efetuar_compra.clear()
                            print('Compra finalizada')
                            print('pedidos em andamento...')
                            
            elif len(sacola) <= 0:
                print('A sua sacola está vazia!')
            break
        continue
      
    
    

