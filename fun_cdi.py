import time
from fun_limpartela import limptl
from colorama import *

#Função tema cdi
def cdi():
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
            CDI é uma taxa de juros usada como referência em investimentos de renda fixa no Brasil, especialmente em produtos como CDB, LCI, LCA e fundos. Não é um investimento em si, mas serve como base para comparar a rentabilidade.

            🔹Funcionamento: representa a taxa média de juros das operações entre bancos. Ela acompanha de perto a Selic e é usada para remunerar investimentos de renda fixa.
            🔹Aplicação: invista em produtos que rendem um percentual do CDI, como CDBs, LCIs, LCAs e fundos de renda fixa. Disponíveis em bancos e corretoras.
            🔹 Riscos: são considerados investimentos de baixo risco, mas podem ter liquidez limitada (prazo para resgate) e menor rentabilidade em momentos de juros baixos.
            🔹 Investimento: bancos tradicionais, bancos digitais e plataformas de investimento como XP, Rico, NuInvest e BTG Pactual.
            👉 Regra de ouro: ideal para o investidor conservador e para compor a reserva de emergência, sempre comparando o percentual do CDI oferecido por cada produto.
            ''')
    print(Fore.RED+'='*52+'[', end='')
    print(Fore.WHITE+Back.RED+' Texto  Falso ', end='')      
    print(Fore.RED+']'+'='*52)
    print('''
            CDI é uma taxa de juros usada como referência em investimentos de renda variável no Brasil, especialmente em produtos como ações, seguros, LCA e fundos. Não é um imposto em si, mas serve como base para comparar a rentabilidade.

            🔹Funcionamento: representa a taxa mínima de juros das operações entre bancos. Ela acompanha de perto a inflação e é usada para remunerar investimentos de renda fixa.
            🔹Aplicação: invista em produtos que rendem um percentual do CDI, como títulos, LCIs, LCAs e fundos de renda fixa. Disponíveis em bancos e correios.
            🔹Riscos: são considerados investimentos de alto risco, mas podem ter liquidez limitada (prazo para resgate) e menor rentabilidade em momentos de juros baixos.
            🔹 Investimentos: bancos tradicionais, bancos digitais e plataformas de investimento como XP, instagram, NuInvest e BTG Pactual.
            👉 Regra de ouro: ideal para o investidor arriscado e para compor a reserva de emergência, nunca comparando o percentual do CDI oferecido por cada produto.
          ''')
    erro_cdi = ['variável','ações','seguros','imposto','mínima','inflação','títulos','correios','alto','instagram','arriscado','nunca']
    venceu = False
    qu_erros = 0
    while qu_erros < 2 and len(erro_cdi) > 0:
        erro = input().lower()
        if erro not in erro_cdi:
            qu_erros+=1
            print(f'{Fore.RED+'='*45}[ {Back.RED}Você errou!{Back.RESET} Possui apenas mais uma tentativa. ]{Fore.RED+'='*45}')
        else:
            erro_cdi.remove(erro)
            if len(erro_cdi) >1:
                print(f'{Fore.YELLOW+'='*47}[ {Back.YELLOW}Você acertou!{Back.RESET} Faltam apenas mais {len(erro_cdi)} erros! ]{Fore.YELLOW+'='*47}')
            elif len(erro_cdi)<= 0:
                pass
            else:
                print(f'{Fore.YELLOW+'='*48}[ {Back.YELLOW}Você acertou!{Back.RESET} Falta apenas mais {len(erro_cdi)} erro! ]{Fore.YELLOW+'='*48}')
    if qu_erros >= 2:
        print(f'{Fore.RED+'='*40}[ {Back.RED}Você Perdeu!{Back.RESET} Suas tentativas acabaram, tente novamente. ]{Fore.RED+'='*40}')
        time.sleep(2)
    else:
        print(f'{Fore.GREEN+'='*50}[ {Back.GREEN}Você Ganhou!!{Back.RESET} Achou todos os erros! ]{Fore.GREEN+'='*50}')
        time.sleep(3)
        venceu = True
    return venceu
