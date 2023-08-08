menu = ''
cate = ''
sacola = []
nome = ''
endereco = {}
bandeira = '9874.****.****.'
complemento = ''


app = input('Iniciar App? S/n: ')
if app.lower() == 's':
    cadastro = input('Deseja fazer o login com sua conta Google? S/n: ')
    if cadastro.lower() == 's':
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
            
    menu = input('Escolha a opção desejada: ')
    print('-'*50)
            
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
            print('A partir de R$ 55,00')
            lanche_01 = ('1 Veggie Cheese + 1 Entrada + 1 Bebida', 55.00)
                        
            print('-'*50)
                        
            print('2- QUESADILLA DE FRANGO')
            lanche_02 = ('QUESADILLA DE FRANGO', 29.00)
            print('R$ 29,00')
                        
            print('-'*50)
                        
            print('3- FRANGO CREAM CHEESE')
            lanche_03 = ('FRANGO CREAM CHEESE', 33.00)
            print('R$ 33,00')
                        
            print('-'*50)
                        
            print('4- COMPLETÃO')
            lanche_04 = ('COMPLETÃO')
            print('Serve 1 pessoa', 33.99)
            print('R$ 33,99')
                        
            print('-'*50)
                        
                        
            print('5- CHEESE SALADA VEGETARIANO + COCA-COLA 350ML + FRITAS')
            lanche_05 = ('CHEESE SALADA VEGETARIANO + COCA-COLA 350ML + FRITAS', 41.90)
            print('Serve 1 pessoa')
            print('#Combo Hamburguer Week')
            print('R$ 41,90')
                        
            print('-'*50)
                        
            pedi = input('Selecione o lanche desejado: ')
            if pedi == '1':
                sacola.append(lanche_01)
            elif pedi == '2':
                sacola.append(lanche_02)
            elif pedi == '3':
                sacola.append(lanche_03)
            elif pedi == '4':
                sacola.append(lanche_04)
            elif pedi == '5':
                sacola.append(lanche_05)
                            
            print('Pedido adicionado à Sacola')
            print('-'*50)
                
        elif cate == '2':
            print('===== Opções de Doces =====')
            print('1-ENROLADINHO DE KIT KAT COM BRIGADEIRO APROX. 90G (PAGUE 1 LEVE 2)')
            print('A partir de R$ 24,90')
            lanche_01 = ('ENROLADINHO DE KIT KAT COM BRIGADEIRO APROX. 90G (PAGUE 1 LEVE 2)', 24.90)
            
            print('-'*50)
            
            print('2- TORTA DE FRANGO COM CATUPIRY APROX 185G')
            print('R$ 20,00')
            lanche_02 = ('TORTA DE FRANGO COM CATUPIRY APROX 185G', 20.00)
            
            print('-'*50)
            
            print('3- BROWNIE RECHEADO COM BRIGADEIRO DE NINHO COM NUTELLA APROX. 90G')
            print('R$ 16,90')
            lanche_03 = ('BROWNIE RECHEADO COM BRIGADEIRO DE NINHO COM NUTELLA APROX. 90G', 16.90)
            
            print('-'*50)
            
            print('4- BOLO NO POTE NINHO COM NUTELLA 185G')
            print('R$ 25,90')
            lanche_04 = ('BOLO NO POTE NINHO COM NUTELLA 185G', 25.90)
            
            
            print('-'*50)
            
            print('5- BOLO GELADO APROX. 100G')
            print('R$ 17,90') 
            lanche_05 = ('BOLO GELADO APROX. 100G', 17.90) 
            
            
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
                        
                        
            
            
        elif cate == '3':
            
            print('===== Opções de Salgados =====')
            print('1-30 MINI SALGADOS SORTIDOS')
            print('A partir de R$ 63,90')
            lanche_01 = ('30 MINI SALGADOS SORTIDOS', 63.90)

                        
            print('-'*50)
                        
            print('2- TORTA DE FRANGO COM CATUPIRY APROX 185G')
            print('R$ 20,00')
            lanche_02 = ('TORTA DE FRANGO COM CATUPIRY APROX 185G', 20.00)
                        
                        
            print('-'*50)
            print('3-100 - SALGADOS (MONTE DO SEU JEITO) + 30 - MINI CHURROS + 1 COCA-COLA 2 LT')
            print('R$  139,90')
            lanche_03 = ('100 - SALGADOS (MONTE DO SEU JEITO) + 30 - MINI CHURROS + 1 COCA-COLA 2 LT', 139.90)
                        
                        
                        
            print('-'*50)
                        
            print('4- 4 EMPADAS SALGADAS E GANHE 10 MINI CHURROS (10G)')
            print('R$ 44,90')
            lanche_04 = ('4 EMPADAS SALGADAS E GANHE 10 MINI CHURROS (10G)', 44.90)
                        
                        
                        
            print('-'*50)
                        
                        
            print('5- EMPADA CALABRESA')
            print('R$ 9,90')
            lanche_05 = ('EMPADA CALABRESA', 9.90)
                        
                        
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
            

            
        elif cate == '4':
            print('===== Opções de Bebidas =====')
            print('1-CERVEJA HEINEKEN PACK COM 06 UNIDADES 330ML CADA')
            print('Produto para maiores de 18 anos')
            print('A partir de R$ 58,99')
            lanche_01 = ('CERVEJA HEINEKEN PACK COM 06 UNIDADES 330ML CADA', 58.99)
            
                        
            print('-'*50)
                        
            print('2- GIN BOMBAY SAPHIRE 750ML')
            print('Produto para maiores de 18 anos')
            print('R$  160,20')
            lanche_02 = ('GIN BOMBAY SAPHIRE 750ML', 160.20)
            
                        
            print('-'*50)
                        
            print('3-ENERGÉTICO MONSTER 473ML')
            print('R$ 13,99')
            lanche_03 = ('ENERGÉTICO MONSTER 473ML', 13.99)
            
                        
            print('-'*50)
                        
            print('4- GATORADE MARACUJA 500ML')
            print('R$ 8,48')
            lanche_04 = ('GATORADE MARACUJA 500ML', 8.48)
            
                        
            print('-'*50)
                        
                        
            print('5- REFRIGERANTE DE LARANJA FANTA 350ML')
            print('R$ 4,99')
            lanche_05 = ('REFRIGERANTE DE LARANJA FANTA 350ML', 4.99)
            
                        
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
            
            pass
        elif cate == '5':
            print('Retornando ao Menu')
        else:
            print('Opção inválida! Escolha uma categoria válida.')

    elif menu == '2':
        if len(sacola) > 0:
            print('Itens da sua sacola')
            print('-'*50)
            total = 0
            for indice, item in enumerate(sacola):
                print(indice, item[0], item[1])
                total += item[1]
            
            print('O valor total é:', total)
            
            remov = input('Deseja remover algum item da sacola? S/n: ')
            if remov.lower() == 's':
                apagar = int(input('Qual item deseja remover? '))
                if 0 <= apagar < len(sacola):
                    del sacola[apagar]
                    print('Item removido da sacola')
                else:
                    print('Opção inválida! Escolha um número de item válido.')
            elif remov.lower() == 'n':
                finalizar = input('Deseja finalizar a sua compra? S/n ')
                if finalizar.lower() == 's':
                    cartao = input('Digite somente os últimos 4 dígitos do seu cartão: ')
                    verificador = input('Digite o código de verificação do seu cartão: ')
                    forma_pag = input('Deseja realizar a sua compra no [D]ébito ou [C]rédito? ')
                    
                    if forma_pag.lower() == 'd':
                        key = input('Digite a sua senha de 4 dígitos: ')
                        print('-'*50)
                        print(f'Compra no débito sendo finalizada no cartão {bandeira}{cartao}')
                        print('Compra finalizada')
                        print('pedidos em andamento...')
                        sacola.clear()
                    elif forma_pag.lower() == 'c':
                        key = input('Digite a sua senha de 4 dígitos: ')
                        print('-'*50)
                        print(f'Compra no crédito sendo finalizada no cartão {bandeira}{cartao}')
                        print('Compra finalizada')
                        print('pedidos em andamento...')
                        sacola.clear()
                else:
                    print('Compra não finalizada. Retornando ao Menu')
            else:
                print('Opção inválida! Escolha S (sim) ou N (não).')
        else:
            print('A sua sacola está vazia!')
            
    elif menu == '3':
        print('Os nossos contatos disponíveis são:')
        print('Telefone: (11) 95147-3297')
        print('E-mail: Restaurantemineiro@gmail.com')
        
    elif menu == '4':
        print(f'Usuário: {nome}')

        print('1- Nome.')
        print('2- Endereço.')

        perfil = input('Escolha uma opção: ')

        if perfil == '1':
            alterar_nome = input(f'O seu nome de usuário atual é {nome},deseja alterar? S/n: ')

            if alterar_nome.lower() == 's':
                nome = input('Insira o seu nome correto: ')

                print('Alteração cadastral realizada com sucesso!')

        if perfil == '2':
            if len(endereco) >= 0:
                cad_end = input('Você ainda não possui um endereço, deseja inserir? S/n: ')
                if cad_end.lower() == 's':
                    rua = input('Digite a rua: ')
                    num_casa = input('Informe o número da casa: ')
                    cep = input('Informe o CEP: ')
                    referencia = input('O endereço possui um complemento? S/n: ')
                    if referencia.lower() == 's':
                        complemento = input('Informe o complemento: ')
                    elif referencia.lower() == 'n':
                        print('Endereço cadastrado com sucesso!')
                    endereco = {
                        'rua': rua,
                        'numero': num_casa,
                        'cep': cep,
                        'complemento': complemento
                    }
            else:
                print('Endereço já cadastrado:', endereco)
    else:
        print('Opção inválida! Escolha uma opção válida.')

    print('-'*50)

