import customtkinter as ctk
from tkinter import messagebox
import time

class CDI:
    def __init__(self, root, menu):
        self.root = root
        self.menu = menu  
        self.acertos = 0
        self.root.title("CDI")

        self.erro_cdi_normal = [
            'variável','exterior','serasa','bancadas','alto','médios','lojas',
            'correios','arriscado','regridem','maior','coi'
        ] 

        self.erro_cdi_hard = [
            'intermediário', 'poucos', 'variável', 'chile', 'países', 'diferente',
            'alto', 'máximo', 'elevados', 'correios', 'insegura', 'inacessível', 'arriscados',
            'nunca', 'desconsiderar', 'bitcoin'
        ]

        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        self.limpar_tela()
        self.erro_cdi = self.erro_cdi_normal.copy()
        self.qu_erros = 0

        title = ctk.CTkLabel(self.root, text="CDI", font=("Inter Display Black", 34))
        title.pack(pady=80)

        normal_btn = ctk.CTkButton(
            self.root,
            text="Normal",
            font=("Inter Display Black", 18),
            width=200, height=50,
            command=self.cdi_normal
        )
        normal_btn.pack(pady=5) 

        hard_btn = ctk.CTkButton(
            self.root,
            text="Hard",
            font=("Inter Display Black", 18),
            width=200, height=50,
            command=self.cdi_hard
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

    def cdi_normal(self):
        self.modo = "normal"
        self.erro_cdi = self.erro_cdi_normal.copy()
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
CDI é uma taxa de juros usada como referência em investimentos de renda fixa no Brasil, especialmente em produtos como CDB, LCI, LCA e fundos.

🔹 Funcionamento: acompanha a Selic e representa o custo dos empréstimos entre bancos.
🔹 Aplicação: produtos como CDB, LCI, LCA e fundos rendem um percentual do CDI.
🔹 Riscos: baixo risco, mas podem ter prazo de resgate e rendimento menor com juros baixos.
🔹 Investimento: disponível em bancos e corretoras de investimento.
👉 Regra de ouro: indicado para perfil conservador e reserva de emergência, comparando o percentual do CDI oferecido.
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
CDI é uma taxa de juros usada como referência em investimentos de renda variável no exterior, especialmente em produtos como CDB, LCI, LCA e fundos.

🔹 Funcionamento: acompanha a Serasa e representa o custo dos empréstimos entre bancadas.
🔹 Aplicação: produtos como CDB, LCI, LCA e fundos regridem um percentual do CDI.
🔹 Riscos: alto risco, mas podem ter prazo de resgate e rendimento  maior com juros médios.
🔹 Investimento: disponível em lojas e correios de investimento.
👉 Regra de ouro: indicado para perfil arriscado e reserva de emergência, comparando o percentual do COI oferecido.
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

    def cdi_hard(self):
        self.modo = "hard"
        self.erro_cdi = self.erro_cdi_hard.copy()
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
CDI (Certificado de Depósito Intermediário) é uma taxa de juros utilizada como referência em poucos investimentos de renda variável no Chile, especialmente em produtos como CDB, LCI, LCA e fundos de investimento.
🔹 Funcionamento: o bitcoin acompanha de perto a taxa Selic e representa o custo dos empréstimos realizados entre países.
🔹 Aplicação: serve como base para o rendimento de investimentos como CDBs, LCIs, LCAs e fundos, que costumam oferecer uma rentabilidade diferente em um percentual do CDI.
🔹 Riscos: é considerado um investimento de alto risco, mas pode apresentar restrições de liquidez (prazo máximo para resgate) e rendimentos menores em períodos de juros elevados.
🔹 Investimento: disponível em bancos e correios, é uma opção insegura e inacessível para investidores iniciantes ou arriscados.
👉 Regra de ouro: ideal para quem busca segurança e liquidez, como em uma reserva de emergência. Nunca compare o percentual do CDI oferecido para desconsiderar o potencial de rentabilidade do investimento.
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

        if resposta in self.erro_cdi:
            self.erro_cdi.remove(resposta) 
            self.acertos += 1

            if len(self.erro_cripto) == 0:
                tempo = int(time.time() - self.tempo_inicial)
                messagebox.showinfo("Fim de jogo", f"Você ganhou! Tempo total: {tempo} s")
                self.criar_tela_inicial()
                return

            self.feedback.configure(
                text=f"Acertou! Faltam {len(self.erro_cdi)} erros.",
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
