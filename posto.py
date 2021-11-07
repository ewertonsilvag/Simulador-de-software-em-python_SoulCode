# import libraries
import time
import csv


def is_empty(text):
    return not bool(text)


class color():
    '''
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    Bright Black: \u001b[30;1m
    Bright Red: \u001b[31;1m
    Bright Green: \u001b[32;1m
    Bright Yellow: \u001b[33;1m
    Bright Blue: \u001b[34;1m
    Bright Magenta: \u001b[35;1m
    Bright Cyan: \u001b[36;1m
    Bright White: \u001b[37;1m
    Reset: \u001b[0m

    Background Black: \u001b[40m
    Background Red: \u001b[41m
    Background Green: \u001b[42m
    Background Yellow: \u001b[43m
    Background Blue: \u001b[44m
    Background Magenta: \u001b[45m
    Background Cyan: \u001b[46m
    Background White: \u001b[47m
    '''
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    Bright_Black = '\u001b[30;1m'
    Bright_Red = '\u001b[31;1m'
    Bright_Green = '\u001b[32;1m'
    Bright_Yellow = '\u001b[33;1m'
    Bright_Blue = '\u001b[34;1m'
    Bright_Magenta = '\u001b[35;1m'
    Bright_Cyan = '\u001b[36;1m'
    Bright_White = '\u001b[37;1m'
    Reset = '\u001b[0m'

    Background_Black = '\u001b[40m'
    Background_Red = '\u001b[41m'
    Background_Green = '\u001b[42m'
    Background_Yellow = '\u001b[43m'
    Background_Blue = '\u001b[44m'
    Background_Magenta = '\u001b[45m'
    Background_Cyan = '\u001b[46m'
    Background_White = '\u001b[47m'

    Background_Bright_Black = '\u001b[40;1m'
    Background_Bright_Red = '\u001b[41;1m'
    Background_Bright_Green = '\u001b[42;1m'
    Background_Bright_Yellow = '\u001b[43;1m'
    Background_Bright_Blue = '\u001b[44;1m'
    Background_Bright_Magenta = '\u001b[45;1m'
    Background_Bright_Cyan = '\u001b[46;1m'
    Background_Bright_White = '\u001b[47;1m'


# MENSAGEMS DO SISTEMA
access_message = '''
{}Bem vindo ao Posto ⛽️ e conveniência 🏪 SoulCoders!{}\n
     Para acessar os nossos produtos digite:
     (A) para acessar
     (F) para finalizar
'''.format(color.BOLD, color.END)
access_message_error = '''
     Atenção!
     Para acessar os nossos produtos digite:
     (A) para acessar
     (F) para finalizar
'''
options_message = '''
        {}Escolha uma das opções:{}

        1 - Abastecimento
        2 - Loja de conveniência
        3 - Ir para o caixa
        4 - Desistir da compra
        5 - Sair do menu de compras
'''.format(color.UNDERLINE, color.END)
options_message_error = '''

        Opção inválida!

        Para acessar os nossos produtos digite:
        (A) para acessar
        (F) para finalizar
        '''

error_message = '''
        Digite uma opção válida!
'''


class products():
    '''
    This python class lists the produsts in the
    gas station catalogue and prints a list with
    the items.
    '''
    list_shop = (['(1) Água', 3.00],
                 ['(2) Café', 4.00],
                 ['(3) Cerveja', 6.00],
                 ['(4) Chocolate', 5.00],
                 ['(5) Lanche', 12.00],
                 ['(6) Refrigerante', 4.00])

    list_fuel = (['(1) ALCOOL', 3.00],
                 ['(2) DIESEL', 4.00],
                 ['(3) GAS', 2.00],
                 ['(4) GASOLINA', 4.00])

    def menu_shop():
        '''
        Print the list of products in the gas
        station catalogue
        '''
        print('=' * 40)
        print(f'{"🏪 CONVENIÊNCIA":^40}')
        print('=' * 40)
        print(f'{"#ID":<}', end='')
        print(f'{"PREÇOS":>36}')
        print('=' * 40)

        # Print da lista de produtos
        for item in range(0, len(products.list_shop)):
            print(f'{products.list_shop[item][0]:.<30}', end='')
            print(f'R${products.list_shop[item][1]:>6.2f}')
        print('=' * 40)

    def menu_fuel():
        '''
        Print the list of products in the gas
        station catalogue
        '''
        print('=' * 40)
        print(f'{"⛽️ COMBUSTIVEL":^40}')
        print('=' * 40)
        print(f'{"#ID":<}', end='')
        print(f'{"PREÇOS":>36}')
        print('=' * 40)

        # Print da lista de produtos
        for fuel in range(0, len(products.list_fuel)):
            print(f'{products.list_fuel[fuel][0]:.<30}', end='')
            print(f'R${products.list_fuel[fuel][1]:>6.2f}')
        print('=' * 40)

    def basket(all_products):
        '''
        Print the list of products purchased
        in the gas
        '''
        print(color.YELLOW)
        print('=' * 40)
        print(f'{"CARRINHO DE COMPRAS":^40}')
        print('=' * 40)
        print(f'{"#ID":<10}', end='')
        print(f'{"NOME":15}', end='')
        print(f'{"UNIT":10}', end='')
        print(f'{"PREÇO":>}')
        print('=' * 40)

        if not all_products:
            print(f'{"SEU VARRINHO ESTÁ VAZIO":^40}')
        else:
            # Print da lista de produtos
            for item in all_products:
                print(f'{item[0][:3]:.<10}', end='')
                print(f'{item[0][4:]:.<15}', end='')
                print(f'{item[1]:^}', end='')
                print(f'{item[2]:.>11}')
            print('=' * 40)
            price_total = sum(x[2] for x in all_products)
            print(f'{color.BOLD}{"TOTAL":<}', end='')
            print(f" (R$){price_total:>30.2f}{color.END}")
            print(color.YELLOW + '=' * 40 + color.END)
            print(color.END)


class payment():

    def payment():

        def confirmation():
            print(color.GREEN + "Pagamento realizado com sucesso" + color.END)

        def row():
            print('=' * 40)

        def change(all_products):

            # Calculo de despesas totais
            price_total = sum(x[2] for x in all_products)

            # Validações
            while True:
                try:
                    money_received = float(input('Qual o valor em dinheiro? '))
                    break
                except:
                    print('Valor digitado inválido. Tente novamente.')

            # Troco
            cifrao = 'R$'
            change = money_received - price_total
            print('=' * 40)
            print(f'Valor recebido: {cifrao:.>16} {money_received:.2f}')
            print(f'Valor a pagar: {cifrao:.>17} {price_total:.2f}')
            print(f'Troco: {cifrao:.>25} {change:.2f}')
            print('=' * 40)
            ballots = 50
            total = change
            amount_cedulas = 0

            # Teste de cédulas
            while True:

                if total >= ballots:
                    total = total - ballots
                    amount_cedulas = amount_cedulas + 1
                else:
                    if amount_cedulas > 0:
                        print(
                            f'Troco:{amount_cedulas:.>12.0f} cédula(s) de R$ {ballots:.2f}. ')
                    if ballots == 50:
                        ballots = 20
                    elif ballots == 20:
                        ballots = 10
                    elif ballots == 10:
                        ballots = 5
                    elif ballots == 5:
                        ballots = 2
                    elif ballots == 2:
                        ballots = 1
                    amount_cedulas = 0
                    if total < 1:
                        break

            # Print payment confirmation message
            confirmation()

        payment = (1, 2, 3)
        # VALIDAÇÃO
        row()
        print('''
    {}Escolha a forma de pagamento:{}

        [1] Dinheiro
        [2] Cartão de débito
        [3] Cartão de crédito'''.format(color.YELLOW, color.END))

        while True:
            try:
                payment_option = int(
                    input('\nDigite 1, 2 ou 3: '))
                row()
                while payment_option not in payment:
                    print('Valor digitado inválido. Tente novamente.')
                    row()
                    payment_option = int(
                        input('\nDigite 1, 2 ou 3: '))
                break
            except:
                print('Valor digitado inválido. Tente novamente.')

        # DINHEIRO CHAMANDO FUNÇÃO TROCO
        price_total = sum(x[2] for x in all_products)

        if payment_option == 1:
            products.basket(all_products)
            change(all_products)

        # CARTÃO DE DÉBITO
        elif payment_option == 2:
            products.basket(all_products)
            print("FORMA DE PAGAMENTO: ")
            print('''Débito selecionado.''')
            cifrao = 'R$'
            print('=' * 40)
            print(f'Valor a pagar: {cifrao:.>18} {price_total:.2f}')
            # Print payment confirmation message
            confirmation()

        # CARTÃO DE CRÉDITO
        elif payment_option == 3:
            # OPÇÕES
            products.basket(all_products)
            print("FORMA DE PAGAMENTO: ")
            print('''Crédito selecionado.''')
            print()
            print('''Escolha em quantas vezes deseja pagar:
        [1] Á vista sem juros
        [2] 2 x sem juros
        [3] 3 x sem juros''')
            while True:
                try:
                    payment_option = int(
                        input('\nQual a opção desejada? \nDigite 1, 2 ou 3: '))
                    while payment_option not in payment:
                        print('Valor digitado inválido. Tente novamente.')
                        payment_option = int(
                            input('\nQual a opção desejada?\nDigite 1, 2 ou 3: '))
                    break
                except:
                    print('Valor digitado inválido. Tente novamente.')
            row()
            cifrao = 'R$'
            print('=' * 40)
            print(f'Valor a pagar: {cifrao:.>18} {price_total:.2f}.')
            payment_parcela = price_total / payment_option
            if payment_option == 1:
                print(
                    f'Pagamento à vista no crédito: {cifrao} {price_total:.2f}.')
            elif payment_option == 2:
                print(
                    f'Pagamento parcelado 2 x: {cifrao:.>8} {payment_parcela:.2f}.')
            elif payment_option == 3:
                print(
                    f'Pagamento parcelado 3 x: {cifrao:.>8} {payment_parcela:.2f}.')
            # Print payment confirmation message
            confirmation()


def logic(service):
    '''
    This function calls the product class
    to print the items on the screen and
    handles tehe logic of purchase
    '''
    buy = 'n'
    count_shop = 0
    count_fuel = 0

    while buy not in ['S', 's']:

        # Printa o menu de opções apenas na primeira compra do cliente

        if service == 1 and count_fuel == 0:
            products.menu_fuel()
            count_fuel += 1
            validation = products.list_fuel
            range_products = range(1, 5)

        elif service == 2 and count_shop == 0:
            products.menu_shop()
            count_shop += 1
            validation = products.list_shop
            range_products = range(1, 7)

        # Input do usuário para escolha do produto

        while True:
            try:
                item = int(input("\nDigite o ID do produto: "))
                break
            except:
                print('Valor inválido! Tente novamente')

        # Validação do input do usuário
        # VALIDATION variable is assigned in the if statement to get the correct lenght

        while item not in range_products:
            item = int(input("\nValor inválido! Tente novamente"))

        # Input da quantidade desejada
        while True:
            try:
                item_amount = int(input(f"\nDigite a quantidade de {validation[item - 1][0][4:]}(s) desejada: "))
                break
            except:
                print('Valor inválido! Tente novamente')
        # Validação do input
        while item_amount <= 0:
            item_amount = int(
                input("\nQuantidade inválida! Tente novamente: "))

        purchase = validation[item - 1][0], \
                   validation[item - 1][1], \
                   validation[item - 1][1] * item_amount

        all_products.append(purchase)

        # Faz o print do recibo
        products.basket(all_products)

        buy = input("\nDeseja finalizar a compra?\n\
        (S) Sim\n\
        Pressione qualquer outra tecla para continuar comprando")

        if buy in ["S", "s"]:
            break


def user_score():
    score = []

    print(color.GREEN + "\nSua avaliação é importante para nós!" + color.END)
    user_stars = int(
        input("\nDe 1 a 5 estrelas, quão satisfeito vocé está com nosso atendimento? "))

    while user_stars not in range(1, 6):
        user_stars = int(input("\nPor favor, digite um número de 1 a 5! "))

    user_stars = int(user_stars) * '*'

    user_name = input("\nDigite o seu nome: ")
    while user_name == '' or user_name == ' ':
        user_name = input("\nPor favor. Digite o seu nome: ")
    user_sugestion = input(
        "\nNos dê uma sugestão de como melhorar sua experiência! ")
    score = [user_stars, user_name, user_sugestion]

    print(color.BOLD + f"\nAgradecemos a sua avaliação, {user_name}!" + color.END)

    print(color.YELLOW + f"{user_stars}" + color.END)

    print(color.Bright_White + f"\n{user_sugestion}\n" + color.Reset)

    return score


# CONTROLE DE ACESSO AO SISTEMA DO POSTO
access_control = 'a'
# CONTROLE DE COMPRAS
all_products = []
option = '0'
# if access_control in 'Aa':
while access_control in ['A', 'a']:
    print(access_message)
    access_control = input()
    if access_control in ['F', 'f']:
        break
    while access_control not in ['A', 'a', 'f', 'F']:
        print(access_message_error)
        access_control = input()

    # Permissão de acesso
    if access_control in ['F', 'f']:
        break
    if access_control in ['A', 'a']:
        print(options_message)
        option = input()

        # Validação do input do usuário
        while option not in ['1', '2', '3', '4', '5']:
            print(error_message)
            option = input()

        while option in ['1', '2', '3', '4', '5']:
            if option in ['1', '2']:
                # Atribuição da primeria compra do usuario
                purchased = logic(int(option))
                # Append das compras seguintes do usuário
            elif option == '3':
                if all_products:
                    payment.payment()
                    all_products = []
                else:
                    print(color.YELLOW + '''
        Realize uma compra para ir ao caixa''' + color.END)
            elif option == '4' and not is_empty(option):
                if all_products:
                    print(color.YELLOW + "ATENÇÃO! Você quer desistir dos seguintes\nitems?" + color.END)
                    products.basket(all_products)

                    quit = input('''
        (S) Sim, eu quero desistir da compra
        (N) Não. quero continuar comprando''')
                    while quit not in ['S', 's', 'N', 'n']:
                        quit = input('''
        {}ATENÇÃO! Digite um valor válido.{}
        
        (S) Sim, eu quero desistir da compra
        (N) Não. quero continuar comprando'''.format(color.RED, color.END))
                    if quit in 'Ss':
                        all_products = []
                        access_control = 'a'
                    elif quit in 'Nn':
                        access_control = 'f'

                else:
                    print(color.YELLOW + '''
        Você ainda não realizou uma compra''' + color.END)
            elif option == '5' and not is_empty(option):
                if all_products:
                    print(color.YELLOW + "ATENÇÃO! Pague suas compras antes de sair! " + color.END)
                    products.basket(all_products)
                else:
                    access_control = 'a'
                    break

            print(options_message)
            option = input()
            while option not in ['1', '2', '3', '4', '5']:
                option = input('Digite uma opção válida: ')

# FINALIZAR SISTEMA
while access_control not in ['A', 'a', 'F', 'f']:
    access_control = input("Por favor, digite uma opção válida: ")
if access_control in ['F', 'f']:  # or option == '4':
    print("\nEncerrando acesso", end='')
    for i in range(24):
        time.sleep(0.2)
        print('.', end='')
if option == '4':
    print("\nEncerrando acesso", end='')
    for i in range(24):
        time.sleep(0.2)
        print('.', end='')
print()
print(color.GREEN + "\nAcesso encerrado. Agradecemos a sua visita.\n" + color.END)

# AVALIAÇÂO E SUGESTÂO
user_service_evaluation = user_score()
receipt_to_write = all_products + user_service_evaluation
with open("vendas.csv", 'w') as sales:
    writer = csv.writer(sales)
    writer.writerow(receipt_to_write)
