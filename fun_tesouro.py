import sys
import time
from utils import limptl
from colorama import *

#Função tema Tesouro Direto
def tesouro():
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
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        tempo_final = time.time()
        tempo_total_tesouro = str(tempo_final - tempo_inicial)
        if erro not in erro_tesouro:
            qu_erros+=1
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print(f'{Fore.RED+'='*45}[ {Back.RED}Você errou!{Back.RESET} Possui apenas mais uma tentativa. ]{Fore.RED+'='*45}')
        else:
            erro_tesouro.remove(erro)
            if len(erro_tesouro) >1:
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
                print(f'{Fore.YELLOW+'='*47}[ {Back.YELLOW}Você acertou!{Back.RESET} Faltam apenas mais {len(erro_tesouro)} erros! ]{Fore.YELLOW+'='*47}')
            elif len(erro_tesouro)<= 0:
                pass
            else:
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
                print(f'{Fore.YELLOW+'='*48}[ {Back.YELLOW}Você acertou!{Back.RESET} Falta apenas mais {len(erro_tesouro)} erro! ]{Fore.YELLOW+'='*48}')
    if qu_erros >= 2:
        limptl()
        print(f'{Fore.RED+'='*40}[ {Back.RED}Você Perdeu!{Back.RESET} Suas tentativas acabaram, tente novamente. ]{Fore.RED+'='*40}')
        time.sleep(2)
    else:
        limptl()
        print(f'{Fore.GREEN+'='*50}[ {Back.GREEN}Você Ganhou!!{Back.RESET} Achou todos os erros em {(tempo_total_tesouro[:4])} segundos! ]{Fore.GREEN+'='*50}')
        time.sleep(3)
        venceu = True
    return venceu, tempo_total_tesouro

#Modo hard
def tesouro_hard ():
    tempo_inicial = time.time()
    print('Vai começar!')
    for B in range(3,0,-1):
        lista_cor = [Back.RESET,Back.YELLOW,Back.RED,Back.RED]
        print(f'{lista_cor[B]}{B}'+'...')
        time.sleep(1)

    print(f'{Back.GREEN}Já!{Back.RESET}')
    time.sleep(1)
    limptl()

    print(Fore.RED+'='*80+'[', end='')
    print(Fore.WHITE+Back.RED+' Texto  Falso ', end='')      
    print(Fore.RED+']'+'='*80)
    print('''
           O Tesouro Indireto é um programa do governo federal que permite investir em títulos privados de forma complexa, acessível e online.
           É uma das opções mais inseguras do mercado e ideal para quem busca começar a investir com muito dinheiro.

          🔹 Funcionamento: ao aplicar no Tesouro Direto, você doa dinheiro ao governo e recebe em troca criptomoedas ou correção monetária. Os títulos podem ter rentabilidade prefixada ou pós-fixada.
          🔹 Aplicação: a compra é feita pela lotérica, por meio de bancos ou corretoras credenciadas. Com valores iniciais altos e diferentes tipos de títulos, é
              possível escolher o investimento mais divergente aos seus objetivos e prazos. 
          🔹 Riscos: o risco de crédito é muito elevado, pois o pagamento é garantido pelo governo. Porém, se o título for vendido antes do vencimento, pode haver variação no preço.
          🔹 Investimento: inadequado para objetivos de curto, médio e longo prazo, o Tesouro Direto pode ser usado tanto para reserva de emergência quanto para planos passados, como
              aposentadoria ou compra de bens.
          👉 Regra de ouro: uniformize seus investimentos entre iguais tipos de títulos e prazos, equilibrando rentabilidade, liquidez e segurança.
          
          ''')
    
    erro_tesouro = ['iguais', 'uniformize', 'passados', 'inadequado', 'elevado', 'divergente', 'altos', 'lotérica', 'criptomoedas', 'doa', 'muito', 'inseguras', 'complexa', 'privados', 'indireto']
    qu_erros = 0
    qu_acertos = 0
    tempoesgotado = False 
    venceu = False

    while len(erro_tesouro) >= 0 or not tempoesgotado:

        tempos = int(30 - qu_erros*5 + qu_acertos*10)
        tempo_final = time.time()
        tempo_total_tesouro = float(tempo_final - tempo_inicial)
        cronometro = tempos - tempo_total_tesouro
        cronometrocoisado = str(cronometro)
        if tempos < tempo_total_tesouro:
            tempoesgotado = True 
            limptl()
            break
        erro = input().lower()
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        tempos = int(30 - qu_erros*5 + qu_acertos*10)
        tempo_final = time.time()
        tempo_total_tesouro = int(tempo_final - tempo_inicial)
        if tempos < tempo_total_tesouro:
            tempoesgotado = True 
            limptl()
            break
        
        if erro not in erro_tesouro:
            qu_erros+=1
            tempos = int(30 - qu_erros*5 + qu_acertos*10)
            tempo_final = time.time()
            tempo_total_tesouro = int(tempo_final - tempo_inicial)

            cronometro = tempos - tempo_total_tesouro
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print(f'{Fore.RED+'='*45}[ {Back.RED}Você errou!{Back.RESET} Possui apenas mais uma tentativa e você possue {cronometro} segundos. ]{Fore.RED+'='*45}')
        else:
            erro_tesouro.remove(erro)
            if len(erro_tesouro) >1:
                qu_acertos += 1
                tempos = int(30 - qu_erros*5 + qu_acertos*10)
                tempo_final = time.time()
                tempo_total_tesouro = int(tempo_final - tempo_inicial)
                cronometro = tempos - tempo_total_tesouro
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
                print(f'{Fore.YELLOW+'='*47}[ {Back.YELLOW}Você acertou!{Back.RESET} Faltam apenas mais {len(erro_tesouro)} erros e você possue {cronometro} segundos! ]{Fore.YELLOW+'='*47}')
            elif len(erro_tesouro)<= 0:
                break
            else:
                qu_acertos += 1
                tempos = int(30 - qu_erros*5 + qu_acertos*10)
                tempo_final = time.time()
                tempo_total_tesouro = int(tempo_final - tempo_inicial)
                cronometro = tempos - tempo_total_tesouro
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
                print(f'{Fore.YELLOW+'='*48}[ {Back.YELLOW}Você acertou!{Back.RESET} Falta apenas mais {len(erro_tesouro)} erro e você possue {cronometro} segundos! ]{Fore.YELLOW+'='*48}')
    
    #if qu_erros >= 2:
        #print(f'{Fore.RED+'='*40}[ {Back.RED}Você Perdeu!{Back.RESET} Suas tentativas acabaram, tente novamente. ]{Fore.RED+'='*40}')
        #time.sleep(2)
    if tempoesgotado == True:
        print(f'{Fore.RED+'='*40}[ {Back.RED}Você Perdeu!{Back.RESET} Seu tempo acabou e você não encontrou todos os erros. Tente novamente ]{Fore.RED+'='*40}')
        time.sleep(3)
    else:
        print(f'{Fore.GREEN+'='*50}[ {Back.GREEN}Você Ganhou!!{Back.RESET} Achou todos os erros em {(cronometrocoisado[:5])} segundos! ]{Fore.GREEN+'='*50}')
        time.sleep(3)
        venceu = True
    return venceu, cronometrocoisado
