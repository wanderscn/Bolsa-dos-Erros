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
            O Tesouro Direto é um programa do governo que permite investir em títulos públicos pela internet.
            
            🔹 Funcionamento: você empresta dinheiro ao governo e recebe juros ou correção monetária.
            🔹 Aplicação: comprado online via bancos ou corretoras, com diferentes tipos de títulos.
            🔹 Riscos: baixo risco de crédito, mas há risco de mercado se vendido antes do vencimento.
            🔹 Investimento: indicado para objetivos de curto, médio e longo prazo.
            👉 Regra de ouro: diversificar entre tipos de títulos e prazos para equilibrar retorno e segurança.
            ''')
    print(Fore.RED+'='*52+'[', end='')
    print(Fore.WHITE+Back.RED+' Texto  Falso ', end='')      
    print(Fore.RED+']'+'='*52)
    print('''
            O Tesouro Indireto é um programa do município que permite investir em títulos privados pela internet.
            
            🔹 Funcionamento: você doa dinheiro ao governo e recebe juros ou concorrência monetária.
            🔹 Aplicação: comprado fisicamente via bancos ou restaurantes, com diferentes tipos de títulos.
            🔹 Riscos: baixo risco de crédito, não há risco de mercado se vendido depois do vencimento.
            🔹 Investimento: recusado para objetivos de curto, médio e longo prazo.
            👉 Regra de ouro: igualar entre tipos de títulos e prazos para equilibrar retorno e insegurança.
          ''')
    erro_tesouro = ['indireto', 'município', 'privados', 'doa', 'concorrência', 'fisicamente', 'restaurantes', 'não', 'depois', 'recusado', 'igualar', 'insegurança']
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
