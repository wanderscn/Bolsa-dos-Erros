import customtkinter as ctk

class Sobre:
    def __init__(self, root, menu):
        self.root = root
        self.menu = menu
        self.root.title("Sobre")

        self.info_sobre()


    def info_sobre(self):
        self.limpar_tela()
        title = ctk.CTkLabel(
            self.root,
            text="Sobre",
            font=("Inter Display Black", 34)
        )
        title.pack(pady=20)

        frame = ctk.CTkFrame(self.root, fg_color="transparent")
        frame.pack(pady=10, padx=20)

        texto_sobre = ctk.CTkLabel(
            frame,
            text='''
Este é um GAME inspirado no jogo dos 7 erros, focado em ensinar de forma lúdica o básico dos mais famosos métodos de investimento.

São 2 textos: o primeiro com informações verídicas sobre um investimento; o segundo é praticamente idêntico, mas contém erros que alteram o sentido.

Seu dever é encontrar, digitar e confirmar todas as diferenças entre os dois textos e aprender os principais fatos sobre o mundo dos investimentos.
''',
            font=("Inter Display Black", 16),
            justify="left",
            wraplength=600
        )
        texto_sobre.pack(pady=5)

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
        command=self.menu.menu_inicial
        )
        btn_voltar_pequeno.place(relx=0.12, rely=0.95, anchor="sw")


    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()
