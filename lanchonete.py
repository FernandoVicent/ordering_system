#---------------produtos-------------------------------------------
produto1 = {'codigo':100,'produto':"cachorro-quente",'valor':9.00}
produto2 = {'codigo':101,'produto':"cachorro-quente Duplo",'valor':11.00}
produto3 = {'codigo':102,'produto':"X-Egg",'valor':12.00}
produto4 = {'codigo':103,'produto':"X-Salada",'valor':13.00}
produto5 = {'codigo':104,'produto':"X-Bacon",'valor':14.00}
produto6 = {'codigo':105,'produto':"X-tudo",'valor':17.00}
produto7 = {'codigo':200,'produto':"refrigerante lata",'valor':5.00}
produto8 = {'codigo':201,'produto':"Chá gelado",'valor':4.00}
valor_total = {'total_a_pagar':0.00}

produtos = (f"{produto1},\n{produto2},\n{produto3},\n{produto4},\n{produto5},\n{produto6},\n{produto7},\n{produto8}")
print(f"\033[1;97mCódigo: 100   |      Cachhoro-Quente     |    Valor: R$9:00\n"
      f"Código: 101   |   Cachhoro-Quente Duplo  |    Valor: R$11:00\n"
      f"Código: 102   |         X-Egg            |    Valor: R$12:00\n"
      f"Código: 103   |        X-Salada          |    Valor: R$13:00\n"
      f"Código: 104   |        X-bacon           |    Valor: R$14:00\n"
      f"Código: 105   |        X-Tudo            |    Valor: R$17:00\n"
      f"Código: 200   |   Refrigerante Lata      |    Valor: R$5:00\n"
      f"Código: 201   |       Chá Gelado         |    Valor: R$4:00"
      f"")
def comprar():
    #--------------------Cachorro-Quente-------------------------
    escolha_de_produto = int(input(f"\033[34mdigite o Código do produto:\033[0;0m "))
    if escolha_de_produto == 100:
        print(f"Você escolheu {produto1['produto']} no valor de {produto1['valor']}")
        valor_total['total_a_pagar'] += produto1['valor']
    # --------------------Cachorro-Quente Duplo-------------------------
    elif escolha_de_produto == 101:
        print(f"Você escolheu {produto2['produto']} no valor de {produto2['valor']}")
        valor_total['total_a_pagar'] += produto2['valor']
    # --------------------x-Egg-------------------------
    elif escolha_de_produto == 102:
        print(f"Você escolheu {produto3['produto']} no valor de {produto3['valor']}")
        valor_total['total_a_pagar'] += produto3['valor']
    # --------------------X-Salada-------------------------
    elif escolha_de_produto == 103:
        print(f"Você escolheu {produto4['produto']} no valor de {produto4['valor']}")
        valor_total['total_a_pagar'] += produto4['valor']
    # --------------------X-bacon-------------------------
    elif escolha_de_produto == 104:
        print(f"Você escolheu {produto5['produto']} no valor de {produto5['valor']}")
        valor_total['total_a_pagar'] += produto5['valor']
    # --------------------X-Tudo-------------------------
    elif escolha_de_produto == 105:
        print(f"Você escolheu {produto6['produto']} no valor de {produto6['valor']}")
        valor_total['total_a_pagar'] += produto6['valor']
    # --------------------Refri lata-------------------------
    elif escolha_de_produto == 200:
        print(f"Você escolheu {produto7['produto']} no valor de {produto7['valor']}")
        valor_total['total_a_pagar'] += produto7['valor']
    # --------------------Chá gelado ----------------------------
    elif escolha_de_produto == 201:
        print(f"Você escolheu {produto8['produto']} no valor de {produto8['valor']}")
        valor_total['total_a_pagar'] += produto8['valor']

    #--------------entrada de código errada
    else:
        print(f'\033[31m este codigo não existe no nosso cardápio\033[m')

def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, Digite um opção valida.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[32mUsuario preferiu nao digitar uma opção. \033[m')
            return 0
        else:
            return n

def Menu(lista):

    c = 1
    for item in lista:
        print(f'\033[33m {c} \033[m - \033[34m{item}\033[m')
        c +=1
    opc = LeiaInt('\033[32m Sua opção : \033[m ')
    return opc

comprar()
while True:
    resposta = Menu(['continuar Comprando','Finalizar Pedido',])
    if resposta == 1:
        comprar()
    elif resposta ==2:
        print(f"\033[1;96mSeu pedido Foi finalizado, o valor total a ser pagar é\033[1;93m R$: {valor_total['total_a_pagar']}\033[0;0m")
        print("\033[1;97mObrigado pela preferencia ")
        break
    else:
        print('ops não entendemos poderia digitar novamente')
        continue
