#importação de modulos
from colorama import *
from fun_limpartela import limptl
from fun_cripto import criptomoeda
from fun_fundos import fundos
from fun_cdi import cdi
from fun_tesouro import tesouro
import time

#função_menu_dev
def dev_():
    escolha = ''
    while escolha !='0':
         limptl()
         print (f'{Fore.RED+'='*50}[{Back.RED} DEVs {Back.RESET}]{Fore.RED+'='*50}')
         print (f'''                                        Os nossos desenvolvedores são:
                    
                                                   {Fore.YELLOW}Misael
                                                 Wanderson

                            {Fore.CYAN}Alunos de Bacharelado em Sistemas de Informação na UFRPE 25.2''')
         print(f'''{Fore.RED+'='*50}[{Back.RED}        {Back.RESET}]{Fore.RED+'='*50}''')
         print(f'''                   Escolha uma opção:
            {Back.YELLOW}[0]{Back.RESET} {Fore.YELLOW}Sair{Fore.WHITE}
                ''')
         escolha = input()
         if escolha !='0':
            print ('Esta opção não é válida.')
            time.sleep(2)
    else:
     menuinicial()

#Menu_Sobre
def sobre():
    escolha = ''
    while escolha !='0':
        limptl()
        print (f'{Fore.CYAN+'='*50}[{Back.CYAN} Sobre {Back.RESET}]{Fore.CYAN+'='*50}')
        print('''
            Este é um GAME inspirado em o jogo dos 7 erros, focado em ensinar de forma lúdica o
            básico dos mais famosos métodos de investimento.
            São 2 textos, o primeiro com informações verídicas sobre um investimento,
            o segundo, é um texto praticamente identico, mas com alguns erros que alteram o sentido da oração.
            
            Seu dever é encontrar e digitar todos os erros do segundo texto
            e aprender os principais fatos sobre o mundo dos investimentos.
              ''')
        print(f'''{Fore.CYAN+'='*50}[{Back.CYAN}        {Back.RESET}]{Fore.CYAN+'='*50}''')
        print(f'''                   Escolha uma opção:
            {Back.YELLOW}[1]{Back.RESET} {Fore.YELLOW}Devs{Fore.WHITE}
            {Back.YELLOW}[0]{Back.RESET} {Fore.YELLOW}Sair{Fore.WHITE}
                ''')
        escolha = input()
        if escolha == '1': 
            dev_()
        else:
            print('Esta opção não é válida.')
            time.sleep(2) 
    else:
     menu_bolsa()

#Menu principal
def menu_bolsa():
    menuescolha = ''
    init(autoreset=True)
    op_cripto = (f'{Back.YELLOW}[1]{Back.RESET} {Fore.YELLOW}Criptomoedas{Fore.WHITE}')
    op_fundos = (f'{Back.YELLOW}[2]{Back.RESET} {Fore.YELLOW}Fundos imobiliários{Fore.WHITE}')
    op_tesouro = (f'{Back.YELLOW}[3]{Back.RESET} {Fore.YELLOW}Tesouro direto{Fore.WHITE}')
    op_cdi = (f'{Back.YELLOW}[4]{Back.RESET} {Fore.YELLOW}CDI{Fore.WHITE}')
    jogou_cripto = 0
    jogou_fundos = 0
    jogou_tesouro = 0
    jogou_cdi = 0
    while menuescolha != '0':
        limptl()
        print(Fore.BLUE+'='*50)
        print(f'''                  Escolha o TEMA que deseja: 
              
                {op_cripto}
                {op_fundos}
                {op_tesouro}
                {op_cdi}
                {Back.YELLOW}[0]{Back.RESET} {Fore.YELLOW}Voltar para tela inicial''')
        print(Fore.BLUE+'='*50)
        print(Fore.RESET)
        menuescolha = input()
        if menuescolha == '1':
            venceu = criptomoeda()
            if venceu is True:
                (jogou_cripto)+=1
                if (jogou_cripto)>=1:
                    op_cripto = (f'{Back.YELLOW}[1]{Back.RESET} {Fore.YELLOW}Criptomoedas{Fore.WHITE} {Back.GREEN}  {Back.RESET}')
                else:
                    op_cripto = (f'{Back.YELLOW}[1]{Back.RESET} {Fore.YELLOW}Criptomoedas{Fore.WHITE} {Back.RED}  {Back.RESET}')
            else:
                if (jogou_cripto)>=1:
                    op_cripto = (f'{Back.YELLOW}[1]{Back.RESET} {Fore.YELLOW}Criptomoedas{Fore.WHITE} {Back.GREEN}  {Back.RESET}')
                else:
                     op_cripto = (f'{Back.YELLOW}[1]{Back.RESET} {Fore.YELLOW}Criptomoedas{Fore.WHITE} {Back.RED}  {Back.RESET}')
        elif menuescolha=='2':
            venceu2 = fundos()
            if venceu2 is True:
                (jogou_fundos)+=1
                if (jogou_fundos)>=1:
                    op_fundos = (f'{Back.YELLOW}[2]{Back.RESET} {Fore.YELLOW}Fundos imobiliários{Fore.WHITE} {Back.GREEN}  {Back.RESET}')
                else:
                    op_fundos = (f'{Back.YELLOW}[2]{Back.RESET} {Fore.YELLOW}Fundos imobiliários{Fore.WHITE} {Back.RED}  {Back.RESET}')
            else:
                if (jogou_fundos)>=1:
                    op_fundos = (f'{Back.YELLOW}[2]{Back.RESET} {Fore.YELLOW}Fundos imobiliários{Fore.WHITE} {Back.GREEN}  {Back.RESET}')
                else:
                    op_fundos = (f'{Back.YELLOW}[2]{Back.RESET} {Fore.YELLOW}Fundos imobiliários{Fore.WHITE} {Back.RED}  {Back.RESET}')
        elif menuescolha=='3':
            venceu3 = tesouro()
            if venceu3 is True:
                (jogou_tesouro)+=1
                if (jogou_tesouro)>=1:
                    op_tesouro = (f'{Back.YELLOW}[3]{Back.RESET} {Fore.YELLOW}Tesouro direto{Fore.WHITE} {Back.GREEN}  {Back.RESET}')
                else:
                    op_tesouro = (f'{Back.YELLOW}[3]{Back.RESET} {Fore.YELLOW}Tesouro direto{Fore.WHITE} {Back.RED}  {Back.RESET}')
            else:
                if (jogou_tesouro)>=1:
                    op_tesouro = (f'{Back.YELLOW}[3]{Back.RESET} {Fore.YELLOW}Tesouro direto{Fore.WHITE} {Back.GREEN}  {Back.RESET}')
                else:
                    op_tesouro = (f'{Back.YELLOW}[3]{Back.RESET} {Fore.YELLOW}Tesouro direto{Fore.WHITE} {Back.RED}  {Back.RESET}')
        elif menuescolha=='4':
            venceu4 = cdi()
            if venceu4 is True:
                (jogou_cdi)+=1
                if (jogou_cdi)>=1:
                    op_cdi = (f'{Back.YELLOW}[4]{Back.RESET} {Fore.YELLOW}CDI{Fore.WHITE} {Back.GREEN}  {Back.RESET}')
                else:
                    op_cdi = (f'{Back.YELLOW}[4]{Back.RESET} {Fore.YELLOW}CDI{Fore.WHITE} {Back.RED}  {Back.RESET}')
            else:
                if (jogou_cdi)>=1:
                    op_cdi = (f'{Back.YELLOW}[4]{Back.RESET} {Fore.YELLOW}CDI{Fore.WHITE} {Back.GREEN}  {Back.RESET}')
                else:
                    op_cdi = (f'{Back.YELLOW}[4]{Back.RESET} {Fore.YELLOW}CDI{Fore.WHITE} {Back.RED}  {Back.RESET}')
        elif menuescolha != '0':
            print('Esta opção não é válida.')
            time.sleep(2)
        else:
            menuinicial()
#Função menu inicial
def menuinicial():
    menuescolha = ''
    init(autoreset=True)
    while menuescolha != '0':
        limptl()
        print(Fore.BLUE+'='*50)
        print(f'''            Bem vindo ao {Fore.GREEN}{Back.GREEN}Bolsa dos erros!!{Back.RESET}{Fore.WHITE}
              
                {Back.YELLOW}[1]{Back.RESET} {Fore.YELLOW}Iniciar{Fore.WHITE}
                {Back.YELLOW}[2]{Back.RESET} {Fore.YELLOW}Sobre{Fore.WHITE}
                {Back.YELLOW}[0]{Back.RESET} {Fore.YELLOW}Sair{Fore.WHITE}
                ''')
        print(Fore.BLUE+'='*50)
        print(Fore.RESET)
        menuescolha = input()
        if menuescolha == '1':
            menu_bolsa()
        elif menuescolha=='2':
            sobre()
        elif menuescolha != '0':
            print('Esta opção não é válida.')
            time.sleep(2)
        else:
            exit
menuinicial()
#a

