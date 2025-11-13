import time
from fun_limpartela import limptl
from colorama import *

#Função tema cdi
def cdi():
    tempo_inicial = time.time()
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
            CDI é uma taxa de juros usada como referência em investimentos de renda fixa no Brasil,
            especialmente em produtos como CDB, LCI, LCA e fundos.

            🔹 Funcionamento: acompanha a Selic e representa o custo dos empréstimos entre bancos.
            🔹 Aplicação: produtos como CDB, LCI, LCA e fundos rendem um percentual do CDI.
            🔹 Riscos: baixo risco, mas podem ter prazo de resgate e rendimento menor com juros baixos.
            🔹 Investimento: disponível em bancos e corretoras de investimento.
            👉 Regra de ouro: indicado para perfil conservador e reserva de emergência, comparando o percentual do CDI oferecido.
            ''')
    print(Fore.RED+'='*52+'[', end='')
    print(Fore.WHITE+Back.RED+' Texto  Falso ', end='') 
    print(Fore.RED+']'+'='*52)
    print('''
            CDI é uma taxa de juros usada como referência em investimentos de renda variável no exterior,
            especialmente em produtos como CDB, LCI, LCA e fundos.

           🔹 Funcionamento: acompanha a Serasa e representa o custo dos empréstimos entre bancadas.
           🔹 Aplicação: produtos como CDB, LCI, LCA e fundos regridem um percentual do CDI.
           🔹 Riscos: alto risco, mas podem ter prazo de resgate e rendimento maior com juros médios.
           🔹 Investimento: disponível em lojas e correios de investimento.
           👉 Regra de ouro: indicado para perfil arriscado e reserva de emergência, comparando o percentual do COI oferecido.
           ''')
    erro_cdi = ['variável','exterior','serasa','bancadas','alto','médios','lojas','correios','arriscado','regridem','maior','coi']
    venceu = False
    qu_erros = 0
    while qu_erros < 2 and len(erro_cdi) > 0:
        erro = input().lower()
        tempo_final = time.time()
        tempo_total_cdi = str(tempo_final - tempo_inicial)
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
        print(f'{Fore.GREEN+'='*50}[ {Back.GREEN}Você Ganhou!!{Back.RESET} Achou todos os erros em {(tempo_total_cdi[:4])} segundos! ]{Fore.GREEN+'='*50}')
        time.sleep(3)
        venceu = True
    return venceu, tempo_total_cdi

#Modo hard
def cdi_hard ():
    tempo_inicial = time.time()
    print('Vai começar!')
    for B in range(3,0,-1):
        lista_cor = [Back.RESET,Back.YELLOW,Back.RED,Back.RED]
        print(f'{lista_cor[B]}{B}'+'...')
        time.sleep(1)

    print(f'{Back.GREEN}Já!{Back.RESET}')
    time.sleep(1)
    limptl()

    print(Fore.RED+'='*52+'[', end='')
    print(Fore.WHITE+Back.RED+' Texto  Falso ', end='')      
    print(Fore.RED+']'+'='*52)
    print('''
            CDI (Certificado de Depósito Intermediário) é uma taxa de juros utilizada como referência em poucos investimentos de renda variável no Chile, especialmente em produtos como CDB, LCI, LCA e fundos de investimento.
           🔹 Funcionamento: o bitcoin acompanha de perto a taxa Selic e representa o custo dos empréstimos realizados entre países.
           🔹 Aplicação: serve como base para o rendimento de investimentos como CDBs, LCIs, LCAs e fundos, que costumam oferecer uma rentabilidade diferente em um percentual do CDI.
           🔹 Riscos: é considerado um investimento de alto risco, mas pode apresentar restrições de liquidez (prazo máximo para resgate) e rendimentos menores em períodos de juros elevados.
           🔹 Investimento: disponível em bancos e correios, é uma opção insegura e inacessível para investidores iniciantes ou arriscados.
           👉 Regra de ouro: ideal para quem busca segurança e liquidez, como em uma reserva de emergência. Nunca compare o percentual do CDI oferecido para desconsiderar o potencial de rentabilidade do investimento.
          ''')
    erro_cdi = ['intermediário', 'poucos', 'variável', 'chile', 'países', 'diferente', 'alto', 'máximo', 'elevados', 'correios', 'insegura', 'inacessível', 'arriscados', 'nunca', 'desconsiderar', 'bitcoin']
    qu_erros = 0
    qu_acertos = 0
    tempoesgotado = False 
    venceu = False

    while qu_erros < 2 and len(erro_cdi) > 0:

        erro = input().lower()
        tempo_final = time.time()
        tempo = (tempo_final - tempo_inicial)

        if (30 - qu_erros*5 + qu_acertos*10) < tempo:
            tempoesgotado = True 
            break
        if erro not in erro_cdi:
            qu_erros+=1
            print(f'{Fore.RED+'='*45}[ {Back.RED}Você errou!{Back.RESET} Possui apenas mais uma tentativa. ]{Fore.RED+'='*45}')
        else:
            erro_cdi.remove(erro)
            if len(erro_cdi) >1:
                print(f'{Fore.YELLOW+'='*47}[ {Back.YELLOW}Você acertou!{Back.RESET} Faltam apenas mais {len(erro_cdi)} erros! ]{Fore.YELLOW+'='*47}')
                qu_acertos += 1
            elif len(erro_cdi)<= 0:
                pass
            else:
                print(f'{Fore.YELLOW+'='*48}[ {Back.YELLOW}Você acertou!{Back.RESET} Falta apenas mais {len(erro_cdi)} erro! ]{Fore.YELLOW+'='*48}')
                qu_acertos += 1 
    
    if qu_erros >= 2:
        print(f'{Fore.RED+'='*40}[ {Back.RED}Você Perdeu!{Back.RESET} Suas tentativas acabaram, tente novamente. ]{Fore.RED+'='*40}')
        time.sleep(2)
    elif tempoesgotado == True:
        print(f'{Fore.RED+'='*40}[ {Back.RED}Você Perdeu!{Back.RESET} Seu tempo acabou e você não encontrou todos os erros. Tente novamente ]{Fore.RED+'='*40}')
        time.sleep(3)
    else:
        print(f'{Fore.GREEN+'='*50}[ {Back.GREEN}Você Ganhou! Achou todas as palavras incorretas no tempo. ]{Fore.GREEN+'='*50}')
        time.sleep(3)
        venceu = True
    return venceu 
