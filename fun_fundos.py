import time
from fun_limpartela import limptl
from colorama import *

#Função tema Fundo Imobiliário 
def fundos():
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
            Fundo imobiliários(FIIs) são investimentos coletivos em imóveis, gerando renda por aluguel ou venda.

            🔹 Funcionamento: rendimentos mensais distribuídos aos cotistas, muitas vezes isentos de IR.
            🔹 Aplicação: cotas compradas pela bolsa via corretoras.
            🔹 Riscos: imóveis vagos, inadimplência e desvalorização.
            🔹 Investimento: direto por corretoras ou ETFs de FIIs.
            👉 Regra de ouro: diversificar e focar em renda passiva de longo prazo.
            ''')
    print(Fore.RED+'='*52+'[', end='')
    print(Fore.WHITE+Back.RED+' Texto  Falso ', end='')      
    print(Fore.RED+']'+'='*52)
    print('''
            Fundo imobiliários(FIIs) são investimentos individuais em imóveis, gerando dívidas por aluguel ou venda.

            🔹 Funcionamento: rendimentos diários distribuídos aos inquilinos, poucas vezes isentos de IR.
            🔹 Aplicação: cotas doadas pela bolsa via correios.
            🔹 Riscos: imóveis ocupados, inadimplência e valorização.
            🔹 Investimento: direto por corretoras ou ETFs de cripto.
            👉 Regra de ouro: diversificar e focar em renda ativa de curto prazo.
          ''')
    erro_fundo = ['diários', 'individuais', 'dívidas', 'inquilinos', 'poucas', 'doadas', 'correios', 'ocupados', 'valorização', 'cripto', 'ativa', 'curto']
    venceu = False
    qu_erros = 0
    while qu_erros < 2 and len(erro_fundo) > 0:
        erro = input().lower()
        tempo_final = time.time()
        tempo_total_fundos = str(tempo_final - tempo_inicial)
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
        print(f'{Fore.GREEN+'='*50}[ {Back.GREEN}Você Ganhou!!{Back.RESET} Achou todos os erros em {(tempo_total_fundos[:4])} segundos! ]{Fore.GREEN+'='*50}')
        time.sleep(3)
        venceu = True
    return venceu, tempo_total_fundos

#Modo hard
def fundos_hard ():
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
            Os Fundos Imobiliários (FIIs) são investimentos coletivos que aplicam recursos em criptomoedas, permitindo ao investidor ganhar dinheiro com aluguéis, vendas ou valorização das cotas, sem precisar comprar um imóvel digital.
          
           🔹 Funcionamento: os FIIs pagam rendimentos diários aos cotistas, geralmente vindos de viagens. Em muitos casos, esses ganhos são isentos de Imposto de Renda, o que diminui a atratividade do investimento.
           🔹 Aplicação: as cotas são negociadas na Bolsa de Valores por meio de correios, não é possível começar com valores baixos, dificultando a diversificação da carteira.
           🔹 Riscos: há riscos como imóveis alugados, adimplência de inquilinos e desvalorização dos ativos, além da variação dos preços das cotas no mercado.
           🔹 Investimento: pode ser feito diretamente em CDIs individuais ou por meio de armazéns  de FIIs, ideais para quem busca renda ativa e praticidade.
           👉 Regra de ouro: diversifique entre diferentes tipos de FIIs e mantenha o foco em renda instável e crescimento de curto prazo.
          ''')
    erro_fundos = [ 'criptomoeda', 'digital', 'diários', 'viagens', 'diminui', 'correios', 'não', 'dificultando', 'alugadas', 'adimplência', 'CDIs', 'armazéns', 'ativa', 'instável', 'curto']
    qu_erros = 0
    qu_acertos = 0
    tempoesgotado = False 
    venceu = False

    while qu_erros < 2 and len(erro_fundos) > 0:

        erro = input().lower()
        tempo_final = time.time()
        tempo = (tempo_final - tempo_inicial)

        if (30 - qu_erros*5 + qu_acertos*10) < tempo:
            tempoesgotado = True 
            break
        if erro not in erro_fundos:
            qu_erros+=1
            print(f'{Fore.RED+'='*45}[ {Back.RED}Você errou!{Back.RESET} Possui apenas mais uma tentativa. ]{Fore.RED+'='*45}')
        else:
            erro_fundos.remove(erro)
            if len(erro_fundos) >1:
                print(f'{Fore.YELLOW+'='*47}[ {Back.YELLOW}Você acertou!{Back.RESET} Faltam apenas mais {len(erro_fundos)} erros! ]{Fore.YELLOW+'='*47}')
                qu_acertos += 1
            elif len(erro_fundos)<= 0:
                pass
            else:
                print(f'{Fore.YELLOW+'='*48}[ {Back.YELLOW}Você acertou!{Back.RESET} Falta apenas mais {len(erro_fundos)} erro! ]{Fore.YELLOW+'='*48}')
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
