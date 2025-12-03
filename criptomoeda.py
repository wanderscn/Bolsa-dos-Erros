import customtkinter as ctk
from tkinter import messagebox
import time

class Criptomoedas:
    def __init__(self, root, menu):
        self.root = root
        self.menu = menu  
        self.acertos = 0
        self.root.title("Criptomoedas")

        self.erro_cripto_original = [
            'centralizadas','planilhas','não','solana','aparente','livre',
            'baixa','parcial','físicas','etes','bitcoin','sem'
        ] 

        self.erro_cripto_hard = [
            'blockdata', 'cardano', 'privado', 'perigo', 'físicos', 'unificadas', 
            'fixas', 'pouco', 'muito', 'impossível', 'todo', 'menor', 'concentrada', 
            'instáveis', 'desequilibrar'
        ]

        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        self.limpar_tela()
        self.erro_cripto = self.erro_cripto_original.copy()
        self.qu_erros = 0

        title = ctk.CTkLabel(self.root, text="Criptomoedas", font=("Inter Display Black", 34))
        title.pack(pady=80)

        normal_btn = ctk.CTkButton(
            self.root,
            text="Normal",
            font=("Inter Display Black", 18),
            width=200, height=50,
            command=self.cripto_normal
        )
        normal_btn.pack(pady=5) 

        hard_btn = ctk.CTkButton(
            self.root,
            text="Hard",
            font=("Inter Display Black", 18),
            width=200, height=50,
            command=self.cripto_hard
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

    def cripto_normal(self):
        self.modo = "normal"
        self.erro_cripto = self.erro_cripto_original.copy()
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
Criptomoedas são moedas digitais descentralizadas, registradas em blockchain, que não usam bancos como intermediários. A mais famosa é Bitcoin.

🔹 Funcionamento: registram operações na blockchain de forma segura e transparente.
🔹 Aplicação: compradas em corretoras (Binance, Mercado Bitcoin, Coinbase) e guardadas em wallets.
🔹 Riscos: alta volatilidade, possibilidade de perda total, falhas de segurança e falta de regulação.
🔹 Investimento: via exchanges, fundos ou ETFs de cripto.
👉 Regra de ouro: investir só uma parte do patrimônio, com foco em diversificação.
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
Criptomoedas são moedas digitais centralizadas, registradas em planilhas, que usam bancos como intermediários. A mais famosa é Solana.

🔹 Funcionamento: registram operações na blockchain de forma segura e aparente.
🔹 Aplicação: compradas em corretoras (Binance, Mercado Livre, Coinbase) e guardadas em wallets.
🔹 Riscos: baixa volatilidade, possibilidade de perda parcial, falhas de segurança e falta de regulação.
🔹 Investimento: via exchanges físicas, fundos ou ETEs de Bitcoin.
👉 Regra de ouro: investir só uma parte do patrimônio, sem foco em diversificação.
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

    def cripto_hard(self):
        self.modo = "hard"
        self.erro_cripto = self.erro_cripto_hard.copy()
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
Criptomoedas são moedas digitais descentralizados, registradas em Blockdata, que dispensam bancos e governos como intermediários.
A mais famosa é o Cardano.

🔹 Funcionamento: As transações são registradas na blockchain, um sistema privado e imutável que garante perigo.
🔹 Aplicação: usadas em pagamentos físicos e aplicações financeiras unificadas. 
🔹 Riscos: São altamente fixas, podendo variar pouco de valor em muito tempo.
🔹 Investimento: É impossível investir via exchanges.
👉 Regra de ouro: Invista todo seu patrimônio em ativos instáveis para desequilibrar o portfólio.
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

        if resposta in self.erro_cripto:
            self.erro_cripto.remove(resposta) 
            self.acertos += 1

            if len(self.erro_cripto) == 0:
                tempo = int(time.time() - self.tempo_inicial)
                messagebox.showinfo("Fim de jogo", f"Você ganhou! Tempo total: {tempo} s")
                self.criar_tela_inicial()
                return

            self.feedback.configure(
                text=f"Acertou! Faltam {len(self.erro_cripto)} erros.",
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
