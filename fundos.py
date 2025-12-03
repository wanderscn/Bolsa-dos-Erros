import customtkinter as ctk
from tkinter import messagebox
import time

class Fundos:
    def __init__(self, root, menu):
        self.root = root
        self.menu = menu  
        self.acertos = 0
        self.root.title("Fundos Imobiliários")

        self.erro_fundo_normal = [
            'diários', 'individuais', 'dívidas', 'inquilinos', 'poucas', 'doadas',
            'correios', 'ocupados', 'valorização', 'cripto', 'ativa', 'curto'
        ] 

        self.erro_fundo_hard = [
            'criptomoeda', 'digital', 'diários', 'viagens', 'diminui', 'correios', 'não',
            'dificultando', 'alugadas', 'adimplência', 'cdis', 'armazéns', 'ativa', 'instável','curto'
        ]

        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        self.limpar_tela()
        self.erro_fundo = self.erro_fundo_normal.copy()
        self.qu_erros = 0

        title = ctk.CTkLabel(self.root, text="Fundos Imobiliários", font=("Inter Display Black", 34))
        title.pack(pady=80)

        normal_btn = ctk.CTkButton(
            self.root,
            text="Normal",
            font=("Inter Display Black", 18),
            width=200, height=50,
            command=self.fundo_normal
        )
        normal_btn.pack(pady=5) 

        hard_btn = ctk.CTkButton(
            self.root,
            text="Hard",
            font=("Inter Display Black", 18),
            width=200, height=50,
            command=self.fundo_hard
        )
        hard_btn.pack()

        btn_sair_pequeno = ctk.CTkButton(
            self.root,
            text="Sair",
            width=80,
            height=30,
            font=("Inter Display Black", 14),
            command=self.menu.sair
        )
        btn_sair_pequeno.place(relx=0.02, rely=0.95, anchor="sw")

        btn_voltar_pequeno = ctk.CTkButton(
            self.root,
            text="Voltar",
            width=80,
            height=30,
            font=("Inter Display Black", 14),
            command=self.menu.tela_escolha
        )
        btn_voltar_pequeno.place(relx=0.12, rely=0.95, anchor="sw")

    # ===================== MODO NORMAL ========================

    def fundo_normal(self):
        self.modo = "normal"
        self.erro_fundo = self.erro_fundo_normal.copy()
        self.qu_erros = 0

        self.limpar_tela()
        self.tempo_inicial = time.time()

        title = ctk.CTkLabel(
            self.root, 
            text="Encontre os erros no texto abaixo:", 
            font=("Arial", 20)
        )
        title.pack(pady=10)

        colunas = ctk.CTkFrame(self.root, fg_color="transparent")
        colunas.pack(pady=20, padx=20, fill="both", expand=True)

        texto_correto = ctk.CTkLabel(
            colunas,
            text="""
 Fundo imobiliários(FIIs) são investimentos coletivos em imóveis, gerando renda por aluguel ou venda.
🔹 Funcionamento: rendimentos mensais distribuídos aos cotistas, muitas vezes isentos de IR.
🔹 Aplicação: cotas compradas pela bolsa via corretoras.
🔹 Riscos: imóveis vagos, inadimplência e desvalorização.
🔹 Investimento: direto por corretoras ou ETFs de FIIs.
👉 Regra de ouro: diversificar e focar em renda passiva de longo prazo.
""",
            justify="left",
            wraplength=350,
            font=("inter Display Medium", 14),
            fg_color="#75FADD",
            corner_radius=15,
            text_color="black"
        )
        texto_correto.grid(row=0, column=0, padx=10, sticky="nw")

        texto_incorreto = ctk.CTkLabel(
            colunas,
            text="""
Fundo imobiliários(FIIs) são investimentos individuais em imóveis, gerando dívidas por aluguel ou venda.
🔹 Funcionamento: rendimentos diários distribuídos aos inquilinos, poucas vezes isentos de IR.
🔹 Aplicação: cotas doadas pela bolsa via correios.
🔹 Riscos: imóveis ocupados, inadimplência e valorização.
🔹 Investimento: direto por corretoras ou ETFs de cripto.
👉 Regra de ouro: diversificar e focar em renda ativa de curto prazo.
""",
            justify="left",
            wraplength=350,
            font=("inter Display Medium", 14),
            fg_color="#FA7575",
            corner_radius=15,
            text_color="black"
        )
        texto_incorreto.grid(row=0, column=1, padx=10, sticky="nw")

        linha = ctk.CTkFrame(self.root)
        linha.pack(pady=10)

        self.entry = ctk.CTkEntry(linha, width=250, placeholder_text="Digite um erro")
        self.entry.pack(side="left", padx=5)

        send_btn = ctk.CTkButton(linha, text="➡️", width=1, command=self.checar_resposta)
        send_btn.pack(side="left", padx=5)

        self.feedback = ctk.CTkLabel(self.root, text="", font=("Arial", 16))
        self.feedback.pack(pady=5)

        self.tempo_label = ctk.CTkLabel(self.root, text="Tempo: 0 s", font=("Arial", 16))
        self.tempo_label.pack(pady=10)

        btn_voltar = ctk.CTkButton(
            self.root,
            text="Voltar",
            width=80,
            height=30,
            font=("Inter Display Black", 14),
            command=self.criar_tela_inicial
        )
        btn_voltar.place(relx=0.12, rely=0.95, anchor="sw") 

        btn_sair_pequeno = ctk.CTkButton(
            self.root,
            text="Sair",
            width=80,
            height=30,
            font=("Inter Display Black", 14),
            command=self.menu.sair
            )
        btn_sair_pequeno.place(relx=0.02, rely=0.95, anchor="sw")
        

        self.atualizar_cronometro()

    # ===================== MODO HARD ========================

    def fundo_hard(self):
        self.modo = "hard"
        self.erro_fundo = self.erro_fundo_hard.copy()
        self.qu_erros = 0
        self.limpar_tela()
        self.tempo_inicial = time.time()

        title = ctk.CTkLabel(
            self.root, 
            text="Encontre os erros no texto abaixo:", 
            font=("Arial", 20)
        )
        title.pack(pady=10)

        texto_incorreto = ctk.CTkLabel(
            self.root,
            text="""
 Os Fundos Imobiliários (FIIs) são investimentos coletivos que aplicam recursos em criptomoedas, permitindo ao investidor ganhar dinheiro com aluguéis, vendas ou valorização das cotas, sem precisar comprar um imóvel digital.     
🔹 Funcionamento: os FIIs pagam rendimentos diários aos cotistas, geralmente vindos de viagens. Em muitos casos, esses ganhos são isentos de Imposto de Renda, o que diminui a atratividade do investimento.
🔹 Aplicação: as cotas são negociadas na Bolsa de Valores por meio de correios, não é possível começar com valores baixos, dificultando a diversificação da carteira.
🔹 Riscos: há riscos como imóveis alugados, adimplência de inquilinos e desvalorização dos ativos, além da variação dos preços das cotas no mercado.
🔹 Investimento: pode ser feito diretamente em CDIs individuais ou por meio de armazéns  de FIIs, ideais para quem busca renda ativa e praticidade.
👉 Regra de ouro: diversifique entre diferentes tipos de FIIs e mantenha o foco em renda instável e crescimento de curto prazo.
""",
            justify="left",
            wraplength=350,
            font=("inter Display Medium", 14),
            fg_color="#FA7575",
            corner_radius=15,
            text_color="black"
        )
        texto_incorreto.pack(pady=10)

        linha = ctk.CTkFrame(self.root)
        linha.pack(pady=10)

        self.entry = ctk.CTkEntry(linha, width=250, placeholder_text="Digite um erro")
        self.entry.pack(side="left", padx=5)

        send_btn = ctk.CTkButton(linha, text="➡️", width=1, command=self.checar_resposta)
        send_btn.pack(side="left", padx=5)

        self.feedback = ctk.CTkLabel(self.root, text="", font=("Arial", 16))
        self.feedback.pack(pady=5)

        self.tempo_label = ctk.CTkLabel(self.root, text="Tempo: 0 s", font=("Arial", 16))
        self.tempo_label.pack(pady=10)

        btn_voltar = ctk.CTkButton(
            self.root,
            text="Voltar",
            width=80,
            height=30,
            font=("Inter Display Black", 14),
            command=self.criar_tela_inicial
        )
        btn_voltar.place(relx=0.12, rely=0.95, anchor="sw")

        btn_sair_pequeno = ctk.CTkButton(
            self.root,
            text="Sair",
            width=80,
            height=30,
            font=("Inter Display Black", 14),
            command=self.menu.sair
            )
        btn_sair_pequeno.place(relx=0.02, rely=0.95, anchor="sw")

        self.atualizar_cronometro_hard()

    # ===================== CRONÔMETROS ========================
    
    # NORMAL 
    def atualizar_cronometro(self):
        tempo = int(time.time() - self.tempo_inicial)
        self.tempo_label.configure(text=f"Tempo: {tempo} s")
        self.root.after(1000, self.atualizar_cronometro)

    # HARD 
    def atualizar_cronometro_hard(self):
        tempo_passado = int(time.time() - self.tempo_inicial)

        tempo_restante = 30 - tempo_passado + self.acertos*10 - self.qu_erros*5 

        if tempo_restante <= 0: 
            messagebox.showinfo("Tempo Esgotado", "Você perdeu!")
            self.criar_tela_inicial()
            return

        self.tempo_label.configure(text=f"Tempo: {tempo_restante} s")
        self.root.after(1000, self.atualizar_cronometro_hard)

    # ===================== CHECAR RESPOSTA ========================

    def checar_resposta(self):
        resposta = self.entry.get().lower()
        self.entry.delete(0, "end")

        if resposta in self.erro_fundo:
            self.erro_fundo.remove(resposta) 
            self.acertos += 1

            if len(self.erro_cripto) == 0:
                tempo = int(time.time() - self.tempo_inicial)
                messagebox.showinfo("Fim de jogo", f"Você ganhou! Tempo total: {tempo} s")
                self.criar_tela_inicial()
                return

            self.feedback.configure(
                text=f"Acertou! Faltam {len(self.erro_fundo)} erros.",
                text_color="lightgreen"
            )

        else:
            self.qu_erros += 1

            if self.qu_erros >= 2:
                messagebox.showinfo("Fim de jogo", "Você perdeu! Errou duas vezes.")
                self.criar_tela_inicial()
                return

            self.feedback.configure(
                text="Errou! Você tem mais 1 tentativa.",
                text_color="red"
            )


    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()
