#Importação de módulos
import time
from fun_limpartela import limptl
from colorama import *

#Função tema criptomoeda
def criptomoeda():
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
            Criptomoedas são moedas digitais descentralizadas, registradas em blockchain,
            que não usam bancos como intermediários. A mais famosa é Bitcoin.

            🔹 Funcionamento: registram operações na blockchain de forma segura e transparente.
            🔹 Aplicação: compradas em corretoras (Binance, Mercado Bitcoin, Coinbase) e guardadas em wallets.
            🔹 Riscos: alta volatilidade, possibilidade de perda total, falhas de segurança e falta de regulação.
            🔹 Investimento: via exchanges, fundos ou ETFs de cripto.
            👉 Regra de ouro: investir só uma parte do patrimônio, com foco em diversificação.
            ''')
    print(Fore.RED+'='*52+'[', end='')
    print(Fore.WHITE+Back.RED+' Texto  Falso ', end='')      
    print(Fore.RED+']'+'='*52)
    print('''
            Criptomoedas são moedas digitais centralizadas, registradas em planilhas, que usam bancos como intermediários.
            A mais famosa é Solana.

            🔹 Funcionamento: registram operações na blockchain de forma segura e aparente.
            🔹 Aplicação: compradas em corretoras (Binance, Mercado Livre, Coinbase) e guardadas em wallets.
            🔹 Riscos: baixa volatilidade, possibilidade de perda parcial, falhas de segurança e falta de regulação.
            🔹 Investimento: via exchanges físicas, fundos ou ETEs de Bitcoin.
            👉 Regra de ouro: investir só uma parte do patrimônio, sem foco em diversificação.
          ''')
    erro_cripto = ['centralizadas','planilhas','não','solana','aparente','livre','baixa','parcial','físicas','etes','bitcoin','sem']
    venceu = False
    qu_erros = 0
    while qu_erros < 2 and len(erro_cripto) > 0:
        erro = input().lower()
        if erro not in erro_cripto:
            qu_erros+=1
            print(f'{Fore.RED+'='*45}[ {Back.RED}Você errou!{Back.RESET} Possui apenas mais uma tentativa. ]{Fore.RED+'='*45}')
        else:
            erro_cripto.remove(erro)
            if len(erro_cripto) >1:
                print(f'{Fore.YELLOW+'='*47}[ {Back.YELLOW}Você acertou!{Back.RESET} Faltam apenas mais {len(erro_cripto)} erros! ]{Fore.YELLOW+'='*47}')
            elif len(erro_cripto)<= 0:
                pass
            else:
                print(f'{Fore.YELLOW+'='*48}[ {Back.YELLOW}Você acertou!{Back.RESET} Falta apenas mais {len(erro_cripto)} erro! ]{Fore.YELLOW+'='*48}')
    if qu_erros >= 2:
        print(f'{Fore.RED+'='*40}[ {Back.RED}Você Perdeu!{Back.RESET} Suas tentativas acabaram, tente novamente. ]{Fore.RED+'='*40}')
        time.sleep(2)
    else:
        print(f'{Fore.GREEN+'='*50}[ {Back.GREEN}Você Ganhou!!{Back.RESET} Achou todos os erros! ]{Fore.GREEN+'='*50}')
        time.sleep(3)
        venceu = True
    return venceu
#a



    

    