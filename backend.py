menu = ''
cate = ''
sacola = []
item_sacola = []
remov = ''
finalizar = ''
efetuar_compra =[]
nome = ''
cadastro = ''
app = ''
bandeira = '4000.1234.5678.'
cartao = ''
verificador = ''
forma_pag = ''
key = ''
endereco = ''
cad_end = ''
rua = ''
num_casa = ''
cep = ''
referencia = ''
complemento = ''
           
app = input('Iniciar App? S/n: ')
if app == 'S' or app == 's':
    cadastro = input('Deseja fazer o login com sua conta Google? S/n: ')
    if cadastro == 'S' or cadastro == 's':
        nome = input('Digite o seu nome? ')
        print('Login efetuado com sucesso!') 
        print('-'*50) 
        
        


while True:
    
        
    
            print('==== Bem vindo ao Restaurante do Mineiro ====')
            
            print(f'===== Menu ====== User:{nome}')
            print('1-cardápio')
            print('2-Sacola')
            print('3-Entrar em contato')
            print('4-Perfil - Em construção')
            
            menu = input('Escola a opção desejada: ')
            
            print('-'*50)
            
            while True:
                if menu == '1':
                    print('Aqui você pode visualizar as nossas opções')
                
                    print('1-Lanches')
                    print('2-Doces')
                    print('3-Salgados')
                    print('4-Bebidas')
                    print('5-Menu')
                    
                    cate = input('Escolha a categoria que deseja acessar: ')
                
                    if cate == '1':
                        print('===== Opções de lanches =====')
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
                            break
                        continue
                        
                            
                        
                    elif cate == '2':
                        print('===== Opções de Doces =====')
                        print('1-ENROLADINHO DE KIT KAT COM BRIGADEIRO APROX. 90G (PAGUE 1 LEVE 2)')
                        print('Delicioso Enroladinho De Kit Kat de chocolate ao leite com brigadeiro Gourmet')
                        print('A partir de R$ 24,90')
                        lanche_01 = ('ENROLADINHO DE KIT KAT COM BRIGADEIRO APROX. 90G (PAGUE 1 LEVE 2)')
                        
                        print('-'*50)
                        
                        print('2- TORTA DE FRANGO COM CATUPIRY APROX 185G')
                        print('Torta caseira quentinha, recheada com frango e Catupiry Original e milho de 185g Massa caseira e fofinha.')
                        lanche_02 = ('TORTA DE FRANGO COM CATUPIRY APROX 185G')
                        print('R$ 20,00')
                        
                        print('-'*50)
                        
                        print('3- BROWNIE RECHEADO COM BRIGADEIRO DE NINHO COM NUTELLA APROX. 90G')
                        lanche_03 = ('BROWNIE RECHEADO COM BRIGADEIRO DE NINHO COM NUTELLA APROX. 90G')
                        print('Delicioso brownie de brigadeiro de Ninho com Nutella'
                                '\nmacio e molhado recheio cremoso.'
                                '\ntamanho de 7x7 aproximadamente 90g cada')
                        print('R$ 16,90')
                        
                        print('-'*50)
                        
                        print('4- BOLO NO POTE NINHO COM NUTELLA 185G')
                        lanche_04 = ('BOLO NO POTE NINHO COM NUTELLA 185G')
                        print('Delicioso bolo chiffon de massa branca recheado com muito Ninho e ganache de Nutella.')
                        print('Serve 1 pessoa (185g)')
                        print('R$ 25,90')
                        
                        print('-'*50)
                        
                        
                        print('5- BOLO GELADO APROX. 100G')
                        lanche_05 = ('BOLO GELADO APROX. 100G')
                        print('Delicioso bolo gelado escolha o seu sabor preferido')
                        print('Serve 1 pessoa (100g)')
                        print('R$ 17,90')
                        
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
                            break
                        continue
                    
                    elif cate == '3':
                        print('===== Opções de Salgados =====')
                        print('1-30 MINI SALGADOS SORTIDOS')
                        print('Aqui você monta seu Kit com sua porção mista.'
                            '\ntemos 5 tipos de Sabores: Coxinha, Queijo, Risole, Carne e Calabresa. Produzidos Diariamente!')
                        print('A partir de R$ 63,90')
                        lanche_01 = ('30 MINI SALGADOS SORTIDOS')
                        print('Serve 2 pessoas')
                        
                        print('-'*50)
                        
                        print('2- TORTA DE FRANGO COM CATUPIRY APROX 185G')
                        print('Torta caseira quentinha, recheada com frango e Catupiry Original e milho de 185g Massa caseira e fofinha.')
                        lanche_02 = ('TORTA DE FRANGO COM CATUPIRY APROX 185G')
                        print('R$ 20,00')
                        
                        print('-'*50)
                        
                        print('3-100 - SALGADOS (MONTE DO SEU JEITO) + 30 - MINI CHURROS + 1 COCA-COLA 2 LT')
                        lanche_03 = ('100 - SALGADOS (MONTE DO SEU JEITO) + 30 - MINI CHURROS + 1 COCA-COLA 2 LT')
                        print('R$  139,90')
                        print('Serve 4 pessoas (2Kg)')
                        
                        print('-'*50)
                        
                        print('4- 4 EMPADAS SALGADAS E GANHE 10 MINI CHURROS (10G)')
                        lanche_04 = ('4 EMPADAS SALGADAS E GANHE 10 MINI CHURROS (10G)')
                        print('Serve 2 pessoas (90g)')
                        print('R$ 44,90')
                        
                        print('-'*50)
                        
                        
                        print('5- EMPADA CALABRESA')
                        lanche_05 = ('EMPADA CALABRESA')
                        print('Calabresa picada, com cebola, tomate e salsinha triturados.')
                        print('Serve 1 pessoa (90g)')
                        print('R$ 9,90')
                        
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
                            break
                        continue
                    
                    elif cate == '4':
                        print('===== Opções de Bebidas =====')
                        print('1-CERVEJA HEINEKEN PACK COM 06 UNIDADES 330ML CADA')
                        print('Produto para maiores de 18 anos')
                        lanche_01 = ('CERVEJA HEINEKEN PACK COM 06 UNIDADES 330ML CADA')
                        print('A partir de R$ 58,99')
                        
                        print('-'*50)
                        
                        print('2- GIN BOMBAY SAPHIRE 750ML')
                        print('Produto para maiores de 18 anos')
                        lanche_02 = ('GIN BOMBAY SAPHIRE 750ML')
                        print('R$  160,20')
                        
                        print('-'*50)
                        
                        print('3-ENERGÉTICO MONSTER 473ML')
                        lanche_03 = ('ENERGÉTICO MONSTER 473ML')
                        print('R$ 13,99')
                        
                        print('-'*50)
                        
                        print('4- GATORADE MARACUJA 500ML')
                        lanche_04 = ('GATORADE MARACUJA 500ML')
                        print('R$ 8,48')
                        
                        print('-'*50)
                        
                        
                        print('5- REFRIGERANTE DE LARANJA FANTA 350ML')
                        lanche_05 = ('REFRIGERANTE DE LARANJA FANTA 350ML')
                        print('R$ 4,99')
                        
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
                            break
                        continue
                    
                    
                        
                    elif cate == '5':
                        print('Retornando ao Menu')
                        break
                    continue
                    
                
                    
                    
                
                
                elif menu == '2':
                    if len(sacola) >= 0:
                        print('Itens da sua sacola')
                        print('-'*50)
                        item_sacola.append(sacola)
                        for indice, item_sacola in enumerate(item_sacola):
                            print(indice, item_sacola)
                            
                            remov = input('Deseja remover algum item da sacola? S/n: ')
                            
                            if remov == 'S' or remov == 's':
                                apagar = int(input('Qual item deseja remover? '))
                                print(len(item_sacola))
                                if apagar >= 0 and apagar < len(item_sacola):
                                    del item_sacola[apagar]
                                print('Item removido da sacola')
                                print('-'*50)
                                
                            elif remov == 'N' or remov == 'n':
                                finalizar = input('Deseja finalizar a sua compra? S/n ')
                                
                                print('-'*50)
                                
                                if finalizar == 'S' or finalizar == 's':
                                    cartao = input('Digite somente os último 4 digitos do seu cartão: ')
                                    verificador = input('Digite o código de verificação do seu cartão: ')
                                    forma_pag = input('Deseja realizar a sua compra no [D]ébito ou [C]rédito? ')
                                    
                                    if forma_pag == 'D' or forma_pag == 'd':
                                        key = input('Digite a sua senha de 4 digitos: ')
                                        
                                        print('-'*50)
                                        
                                        print(f'Compra no débito sendo finalizada no cartão {bandeira}{cartao}')
                                
                                    
                                        print('Compra finalizada')
                                        print('pedidos em andamento...')
                                        item_sacola.clear()
                                    
                                    elif forma_pag == 'C' or forma_pag == 'c':
                                        key = input('Digite a sua senha de 4 digitos: ')
                                        
                                        print('-'*50)
                                        
                                        print(f'Compra no crédito sendo finalizada no cartão {bandeira}{cartao}')
                                        
                                        print('Compra finalizada')
                                        print('pedidos em andamento...')
                                        item_sacola.clear()
                        break        
                             
                                
                
                    elif len(sacola) <= 0:
                        print('A sua sacola está vazia!')
                    
                
                elif menu == '3':
                    print('Os nossos contatos disponiveis são:'
                            '\n telefone: (11) 95147-3297'
                            '\n E-mail: Restaurantemineiro@gmail.com')
                    
                elif menu == '4':
                    print(f'Usuário: {nome}')

                    if len(endereco) == 0:
                        cad_end = input('Você ainda não possui um endereço, deseja inserir? S/n: ')

                        if cad_end == 's':
                            rua = input('Digite a rua: ')
                            num_casa = input('informe o número da casa: ')
                            cep = input('Informe o CEP: ')
                            referencia = input('O endereço possui um complemento? S/n: ')

                            if referencia == 's':
                                complemento = input('informe o completo: ')
                            elif referencia == 'n':
                                print('Retornando ao menu...')
                break
            continue


        
            



