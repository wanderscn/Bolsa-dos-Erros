import time
from fun_limpartela import limptl
from colorama import *

#Função tema Tesouro Direto
def tesouro():
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
            Tesouro Direto é um programa do governo federal que permite a qualquer pessoa investir em títulos públicos emitidos pelo Tesouro Nacional.

            🔹 Funcionamento: O investidor empresta dinheiro ao governo e recebe juros no futuro. Os títulos podem ser prefixados (taxa fixa) ou pós-fixados (atrelados à Selic ou inflação).
            🔹 Aplicação: É preciso ter conta em corretora ou banco habilitado e escolher o título na plataforma do Tesouro Direto.
            🔹 Riscos: Oscilação dos juros pode afetar o valor em resgate antecipado e inflação pode reduzir ganhos em títulos prefixados.
            🔹 Investimento: Pelo site do Tesouro Direto, corretoras ou bancos parceiros.
            👉 Regra de ouro: Escolher o título de acordo com seu objetivo e prazo, reinvestir ganhos e focar no longo prazo para aproveitar juros compostos. 
            ''')
    print(Fore.RED+'='*52+'[', end='')
    print(Fore.WHITE+Back.RED+' Texto  Falso ', end='')      
    print(Fore.RED+']'+'='*52)
    print('''
            Tesouro indireto é um programa do governo federal que permite a qualquer pessoa investir em títulos privados emitidos pelo Tesouro Internacional.

            🔹 Funcionamento: O investidor doa dinheiro ao governo e recebe juros no futuro. Os títulos podem ser prefixados (taxa fixa) ou pós-fixados (atrelados à serasa ou inflação).
            🔹 Aplicação: É preciso ter conta em cartório ou banco desabilitado e escolher o título na plataforma do Tesouro Direto.
            🔹 Riscos: Estabilização dos juros pode afetar o valor em resgate antecipado e inflação pode aumentar ganhos em títulos prefixados.
            🔹 Investimento: Pelo site do Tesouro Direto, corretoras ou bancos desconhecidos.
            👉 Regra de ouro: Escolher o título de acordo com seu objetivo e prazo, reinvestir ganhos e focar no curto prazo para aproveitar juros simples. 
          ''')
    erro_tesouro = ['indireto', 'provados', 'cartório', 'desconhecidos', 'curto', 'doa', 'serasa', 'aumentar', 'simples', 'estabilização', 'Internacional', 'desabilitado']
    venceu = False
    qu_erros = 0
    while qu_erros < 2 and len(erro_tesouro) > 0:
        erro = input().lower()
        if erro not in erro_tesouro:
            qu_erros+=1
            print(f'{Fore.RED+'='*45}[ {Back.RED}Você errou!{Back.RESET} Possui apenas mais uma tentativa. ]{Fore.RED+'='*45}')
        else:
            erro_tesouro.remove(erro)
            if len(erro_tesouro) >1:
                print(f'{Fore.YELLOW+'='*47}[ {Back.YELLOW}Você acertou!{Back.RESET} Faltam apenas mais {len(erro_tesouro)} erros! ]{Fore.YELLOW+'='*47}')
            elif len(erro_tesouro)<= 0:
                pass
            else:
                print(f'{Fore.YELLOW+'='*48}[ {Back.YELLOW}Você acertou!{Back.RESET} Falta apenas mais {len(erro_tesouro)} erro! ]{Fore.YELLOW+'='*48}')
    if qu_erros >= 2:
        print(f'{Fore.RED+'='*40}[ {Back.RED}Você Perdeu!{Back.RESET} Suas tentativas acabaram, tente novamente. ]{Fore.RED+'='*40}')
        time.sleep(2)
    else:
        print(f'{Fore.GREEN+'='*50}[ {Back.GREEN}Você Ganhou!!{Back.RESET} Achou todos os erros! ]{Fore.GREEN+'='*50}')
        time.sleep(3)
        venceu = True
    return venceu
