import time
from fun_limpartela import limptl
from colorama import *

#Função tema Fundo Imobiliário 
def fundos():
    print('Vai começar!')
    for B in range(3,0,-1):
        lista_cor = [Back.RESET,Back.YELLOW,Back.RED,Back.RED]
        print(f'{lista_cor[B]}{B}'+'...')
        time.sleep(1)
    print(f'{Back.GREEN}Já!{Back.RESET}')
    time.sleep(1)
    limptl()

    print(Fore.GREEN+'='*50+'[', end='')
    print(Fore.WHITE+Back.GREEN+' Texto Verdadeiro ', end='')
    print(Fore.GREEN+']'+'='*50)
    print ('''
            As cotas são compradas na bolsa; cada cota representa parte do fundo. A gestão é profissional e os lucros são distribuídos mensalmente, muitas vezes sem IR para pessoa física.

            🔹 Funcionamento: As cotas são compradas na bolsa; cada cota representa parte do fundo. A gestão é profissional e os lucros são distribuídos mensalmente, muitas vezes sem IR para pessoa física.
            🔹 Aplicação: Abrir conta em corretora, usar o home broker e comprar cotas. É essencial analisar o tipo de fundo, qualidade dos imóveis e gestão.
            🔹 Riscos: Imóveis vazios, inadimplência, desvalorização, juros altos e má administração.
            🔹 Investimento: Corretoras, fundos imobiliários e ETFs de FIIs na bolsa.
            👉 Regra de ouro: Diversificar entre diferentes fundos e focar em renda passiva de longo prazo.
            ''')
    print(Fore.RED+'='*52+'[', end='')
    print(Fore.WHITE+Back.RED+' Texto  Falso ', end='')      
    print(Fore.RED+']'+'='*52)
    print('''
            Fundos de investimentos imobiliários(FIIs) são investimentos que reúnem dinheiro de poucos investidores para aplicar em imóveis como shoppings, galpões e escritórios. O investidor perde rendimentos dos aluguéis ou vendas.

            🔹 Funcionamento: As cotas são compradas na lotérica; cada cota representa parte do fundo. A gestão é profissional e os lucros são distribuídos anualmente.
            🔹 Aplicação: Fechar conta em corretora, usar o home broker e comprar cotas. É essencial ignorar o tipo de fundo, qualidade dos imóveis e gestão.
            🔹 Riscos: Imóveis vazios, inadimplência, valorização, juros baixos e boa administração.
            🔹 Investimento: Corretoras, fundos públicos e ETFs de FIIs na bolsa. 
            👉 Regra de ouro: Diversificar entre diferentes fundos e focar em renda ativa de curto prazo.
          ''')
    erro_fundo = ['poucos', 'curto', 'ativa', 'públicos', 'baixos', 'boa', 'ignorar', 'fechar', 'anualmente', 'lotérica', 'perde', 'valorização']
    venceu = False
    qu_erros = 0
    while qu_erros < 2 and len(erro_fundo) > 0:
        erro = input().lower()
        if erro not in erro_fundo:
            qu_erros+=1
            print(f'{Fore.RED+'='*45}[ {Back.RED}Você errou!{Back.RESET} Possui apenas mais uma tentativa. ]{Fore.RED+'='*45}')
        else:
            erro_fundo.remove(erro)
            if len(erro_fundo) >1:
                print(f'{Fore.YELLOW+'='*47}[ {Back.YELLOW}Você acertou!{Back.RESET} Faltam apenas mais {len(erro_fundo)} erros! ]{Fore.YELLOW+'='*47}')
            elif len(erro_fundo)<= 0:
                pass
            else:
                print(f'{Fore.YELLOW+'='*48}[ {Back.YELLOW}Você acertou!{Back.RESET} Falta apenas mais {len(erro_fundo)} erro! ]{Fore.YELLOW+'='*48}')
    if qu_erros >= 2:
        print(f'{Fore.RED+'='*40}[ {Back.RED}Você Perdeu!{Back.RESET} Suas tentativas acabaram, tente novamente. ]{Fore.RED+'='*40}')
        time.sleep(2)
    else:
        print(f'{Fore.GREEN+'='*50}[ {Back.GREEN}Você Ganhou!!{Back.RESET} Achou todos os erros! ]{Fore.GREEN+'='*50}')
        time.sleep(3)
        venceu = True
    return venceu
