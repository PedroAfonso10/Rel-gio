from datetime import datetime
import tkinter as tk

# ------------ CONFIGURAÇÃO DA JANELA -----------
janela = tk.Tk()
janela.title("Relógio")
janela.geometry("400x300")
janela.resizable(True, True)
janela.configure(bg="black")

label = tk.Label(
    janela, 
    font=("Arial", 40, "bold"), 
    bg="black", 
    fg="white"
)

label.pack(expand=True)
label.config(anchor="center")

def atualizar_hora(): 
    # ---------- ATUALIZA A CADA 1000 MILISEGUNDOS COM O HORÁRIO ATUAL ----------
    atual = datetime.now().strftime("%H:%M:%S:%p\n %d: %m: %y")
    label.config(text=atual) # ATUALIZA O TEXTO
    janela.after(1000, atualizar_hora)


def fechar_janela(event=None):
    janela.destroy()

# -------- FECHA A JANELA NESSES DOIS EVENTOS ----------    
janela.protocol("WM_DELETE_WINDOW", fechar_janela) #FECHA AO CLICAR NO X
janela.bind("<Escape>", fechar_janela) # FECHA AO CLICAR NO ESC

atualizar_hora()
janela.mainloop()
