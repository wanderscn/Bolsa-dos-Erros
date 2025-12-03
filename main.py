import customtkinter as ctk 
from criptomoeda import Criptomoedas 
from cdi import CDI
from fundos import Fundos 
from sobre import Sobre 
from fun_tesouro import Tesouro
import ctypes

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Bolsa dos Erros")
        self.root.geometry("900x650")
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("bolsa_dos_erros")
        self.root.iconbitmap('ChatGPT-Image-23-de-nov.-de-2025_-21_29_13.ico')
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("green")

        self.menu_inicial()  

    def menu_inicial(self):
        self.limpar_tela()
        title = ctk.CTkLabel(self.root, text="Bem vindo à Bolsa dos Erros",
                             font=("Inter Display Black", 34))
        title.pack(pady=80)

        btn_iniciar = ctk.CTkButton(self.root, text="Iniciar", font=("Inter Display Black", 18),
                                    width=200, height=50, command=self.tela_escolha)
        btn_iniciar.pack(pady=5)

        btn_sobre = ctk.CTkButton(self.root, text="Sobre", font=("Inter Display Black", 18),
                                  width=200, height=50, command=self.sobre)
        btn_sobre.pack(pady=5)

        btn_sair = ctk.CTkButton(self.root, text="Sair", font=("Inter Display Black", 18),
                                 width=200, height=50, command=self.sair)
        btn_sair.pack(pady=5)

    def tela_escolha(self):
        self.limpar_tela()
        title = ctk.CTkLabel(self.root, text="Escolha o Tema",
                             font=("Inter Display Black", 34))
        title.pack(pady=80)
  
        btn_cdi = ctk.CTkButton(self.root, text="CDI", font=("Inter Display Black", 18),
                                width=200, height=50, command=self.iniciar_cdi)
        btn_cdi.pack(pady=5)

        btn_cripto = ctk.CTkButton(self.root, text="Criptomoedas", font=("Inter Display Black", 18),
                                   width=200, height=50, command=self.iniciar_criptomoedas)
        btn_cripto.pack(pady=5)

        btn_fundos = ctk.CTkButton(self.root, text="Fundos Imobiliários", font=("Inter Display Black", 18),
                                   width=200, height=50, command=self.iniciar_fundos)
        btn_fundos.pack(pady=5) 

        btn_tesouro = ctk.CTkButton(self.root, text="Tesouro Direto", font=("Inter Display Black", 18),
                                    width=200, height=50, command=self.iniciar_tesouro)
        btn_tesouro.pack(pady=5)

        btn_sair_pequeno = ctk.CTkButton(
        self.root,
        text="Sair",
        width=80,
        height=30,
        font=("Inter Display Black", 14),
        command=self.sair
        )
        btn_sair_pequeno.place(relx=0.02, rely=0.95, anchor="sw")

        btn_voltar_pequeno = ctk.CTkButton(
        self.root,
        text="Voltar",
        width=80,
        height=30,
        font=("Inter Display Black", 14),
        command=self.menu_inicial
        )
        btn_voltar_pequeno.place(relx=0.12, rely=0.95, anchor="sw")

    def iniciar_cdi(self):
        CDI(self.root, self)

    def iniciar_criptomoedas(self):
        Criptomoedas(self.root, self)

    def iniciar_tesouro(self):
        Tesouro(self.root, self)

    def iniciar_fundos(self):
        Fundos(self.root, self)

    def sobre(self):
        Sobre(self.root, self)

    def sair(self):
        self.root.destroy()
        
    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = ctk.CTk()
app = Menu(root)
root.mainloop()