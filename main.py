import tkinter as tk
from tkcalendar import Calendar, DateEntry
from cgitb import text
from tkinter import font, Button

# Definir cores
c0 = "#f0f3f5"  # Preto
c1 = "#feffff"  # branco
c2 = "#4fa882"  # verde
c3 = "#38576b"  # valor
c4 = "#403d3d"  # letra
c5 = "#e06636"  # - profit
c6 = "#038cfc"  # azul
c7 = "#ef5350"  # vermelha
c8 = "#263238"  # + verde
c9 = "#e9edf5"  # sky blue

# Criar a janela
janela = tk.Tk()
janela.title("SADP")
janela.geometry('1200x720')
janela.configure(background=c9)
janela.resizable(width=False, height=False)

# Criar os frames
frame_superior = tk.Frame(janela, width=480, height=50, background=c2, relief='flat')
frame_superior.grid(row=0, column=0)

frame_inferior = tk.Frame(janela, width=480, height=720, background=c1, relief='flat')
frame_inferior.grid(row=1, column=0, sticky=tk.NSEW, padx=0, pady=1)

frame_direita = tk.Frame(janela, width=800, height=710, background=c1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=5, pady=0, sticky=tk.NSEW)

##=========== Label Superior ===============##
app_nome = tk.Label(frame_superior, text='SADP - Sistema de Administração de Despesas Pessoais', anchor='nw', font=('Ivy', 13, 'bold'), bg=c2, fg=c1, relief='flat')
app_nome.place(x=10, y=20)

##=========== Label inferior ===============##
#Campo Nome#
lbl_nome = tk.Label(frame_inferior, text='Nome *', anchor='nw', font=('Ivy', 11, 'bold'), bg=c1, fg=c4, relief='flat')
lbl_nome.place(x=10, y=10)
etr_nome = tk.Entry(frame_inferior, width=50, justify='left', relief='solid')
etr_nome.place(x=70, y=10)

#Campo Valor#
lbl_valor = tk.Label(frame_inferior, text='Valor *', anchor='nw', font=('Ivy', 11, 'bold'), bg=c1, fg=c4, relief='flat')
lbl_valor.place(x=10, y=70)
etr_valor = tk.Entry(frame_inferior, width=50, justify='left', relief='solid')
etr_valor.place(x=70, y=70)

#Campo Método de Pagamento#
lbl_pagamento = tk.Label(frame_inferior, text='Método de pagamento *', anchor='nw', font=('Ivy', 11, 'bold'), bg=c1, fg=c4, relief='flat')
lbl_pagamento.place(x=10, y=130)
etr_pagamento = tk.Entry(frame_inferior, width=40, justify='left', relief='solid')
etr_pagamento.place(x=195, y=130)

#Campo Descrição#
lbl_descricao = tk.Label(frame_inferior, text='Descrição *', anchor='nw', font=('Ivy', 11, 'bold'), bg=c1, fg=c4, relief='flat')
lbl_descricao.place(x=10, y=190)
etr_descricao = tk.Entry(frame_inferior, width=50,justify='left', relief='solid')
etr_descricao.place(x=105, y=190)

#Campo Data#
lbl_data = tk.Label(frame_inferior, text='Data da despesa *', anchor='nw', font=('Ivy', 11, 'bold'), bg=c1, fg=c4, relief='flat')
lbl_data.place(x=9, y=250)
etr_data = DateEntry(frame_inferior, width=12, background='darkblue', foreground='white', borderwidth=2)
etr_data.place(x=10, y=280)

#Campo Status da Despesa#
lbl_despesa = tk.Label(frame_inferior, text='Status da Despesa *', anchor='nw', font=('Ivy', 11, 'bold'), bg=c1, fg=c4, relief='flat')
lbl_despesa.place(x=270, y=250)
etr_despesa = tk.Entry(frame_inferior, width=25, justify='left', relief='solid')
etr_despesa.place(x=270, y=280)

#Botão Adicionar
btn_adicionar = Button()


















janela.mainloop()
