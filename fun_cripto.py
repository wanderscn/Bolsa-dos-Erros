#Importação de módulos
import sys
import time
from utils import limptl
from colorama import *

#Função tema criptomoeda
def criptomoeda():
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
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        tempo_final = time.time()
        tempo_total_cripto = str(tempo_final - tempo_inicial)
        if erro not in erro_cripto:
            qu_erros+=1
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print(f'{Fore.RED+'='*45}[ {Back.RED}Você errou!{Back.RESET} Possui apenas mais uma tentativa. ]{Fore.RED+'='*45}')
        else:
            erro_cripto.remove(erro)
            if len(erro_cripto) >1:
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
                print(f'{Fore.YELLOW+'='*47}[ {Back.YELLOW}Você acertou!{Back.RESET} Faltam apenas mais {len(erro_cripto)} erros! ]{Fore.YELLOW+'='*47}')
            elif len(erro_cripto)<= 0:
                pass
            else:
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
                print(f'{Fore.YELLOW+'='*48}[ {Back.YELLOW}Você acertou!{Back.RESET} Falta apenas mais {len(erro_cripto)} erro! ]{Fore.YELLOW+'='*48}')
    if qu_erros >= 2:
        limptl()
        print(f'{Fore.RED+'='*40}[ {Back.RED}Você Perdeu!{Back.RESET} Suas tentativas acabaram, tente novamente. ]{Fore.RED+'='*40}')
        time.sleep(2)
    else:
        limptl()
        print(f'{Fore.GREEN+'='*50}[ {Back.GREEN}Você Ganhou!!{Back.RESET} Achou todos os erros em {(tempo_total_cripto[:4])} segundos! ]{Fore.GREEN+'='*50}')
        time.sleep(3)
        venceu = True
    return venceu, tempo_total_cripto

#Modo hard
def cripto_hard():
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
            Criptomoedas são moedas digitais descentralizados, registradas em Blockdata, que dispensam bancos e governos como intermediários.
            A mais famosa é o Cardano, mas há muitas outras, como Ethereum e Solana.

           🔹 Funcionamento: As transações são registradas na blockchain, um sistema privado e imutável que garante perigo, transparência e rastreabilidade.
           🔹 Aplicação: Podem ser compradas em corretoras e armazenadas em wallets. Além do investimento, também são usadas em pagamentos
               físicos, contratos inteligentes e aplicações financeiras unificadas. 
           🔹 Riscos: São altamente fixas, podendo variar pouco de valor em muito tempo.
           🔹 Investimento: É impossível investir de forma direta via exchanges, ou indiretamente por meio de fundos e ETFs de criptoativos.
           👉 Regra de ouro: Invista todo seu patrimônio, de preferência aquela destinada a ativos de menor risco, mantendo uma carteira concentrada com investimentos
               mais instáveis para desequilibrar o portfólio.
          
          ''')
    
    erro_cripto = ['blockdata', 'cardano', 'privado', 'perigo', 'físicos', 'unificadas', 'fixas', 'pouco', 'muito', 'impossível', 'todo', 'menor', 'concentrada', 'instáveis', 'desequilibrar']
    venceu = False
    qu_erros = 0
    qu_acertos = 0
    tempoesgotado = False

    while len(erro_cripto) >= 0 or not tempoesgotado:

        tempos = int(30 - qu_erros*5 + qu_acertos*10)
        tempo_final = time.time()
        tempo_total_cripto = float(tempo_final - tempo_inicial)
        cronometro = tempos - tempo_total_cripto
        cronometrocoisado = str(cronometro)
        if tempos < tempo_total_cripto:
            tempoesgotado = True 
            limptl()
            break
        erro = input().lower()
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        tempos = int(30 - qu_erros*5 + qu_acertos*10)
        tempo_final = time.time()
        tempo_total_cripto = int(tempo_final - tempo_inicial)
        if tempos < tempo_total_cripto:
            tempoesgotado = True 
            limptl()
            break
        
        if erro not in erro_cripto:
            qu_erros+=1
            tempos = int(30 - qu_erros*5 + qu_acertos*10)
            tempo_final = time.time()
            tempo_total_cripto = int(tempo_final - tempo_inicial)

            cronometro = tempos - tempo_total_cripto
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print(f'{Fore.RED+'='*45}[ {Back.RED}Você errou!{Back.RESET} Possui apenas mais uma tentativa e você possue {cronometro} segundos. ]{Fore.RED+'='*45}')
        else:
            erro_cripto.remove(erro)
            if len(erro_cripto) >1:
                qu_acertos += 1
                tempos = int(30 - qu_erros*5 + qu_acertos*10)
                tempo_final = time.time()
                tempo_total_cripto = int(tempo_final - tempo_inicial)
                cronometro = tempos - tempo_total_cripto
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
                print(f'{Fore.YELLOW+'='*47}[ {Back.YELLOW}Você acertou!{Back.RESET} Faltam apenas mais {len(erro_cripto)} erros e você possue {cronometro} segundos! ]{Fore.YELLOW+'='*47}')
            elif len(erro_cripto)<= 0:
                break
            else:
                qu_acertos += 1
                tempos = int(30 - qu_erros*5 + qu_acertos*10)
                tempo_final = time.time()
                tempo_total_cripto = int(tempo_final - tempo_inicial)
                cronometro = tempos - tempo_total_cripto
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
                print(f'{Fore.YELLOW+'='*48}[ {Back.YELLOW}Você acertou!{Back.RESET} Falta apenas mais {len(erro_cripto)} erro e você possue {cronometro} segundos! ]{Fore.YELLOW+'='*48}')
    
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


    


