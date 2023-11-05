import tkinter as tk
from tkcalendar import Calendar, DateEntry

from tkinter import font, Button, ttk, messagebox
from view import *


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
# janela.resizable(width=False, height=False)

# Criar os frames
frame_superior = tk.Frame(janela, width=480, height=50, background=c2, relief='flat')
frame_superior.grid(row=0, column=0)

frame_inferior = tk.Frame(janela, width=480, height=720, background=c1, relief='flat')
frame_inferior.grid(row=1, column=0, sticky=tk.NSEW, padx=0, pady=1)

frame_direita = tk.Frame(janela, width=800, height=710, background=c1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=5, pady=0, sticky=tk.NSEW)

##======================= Tela Esquerda ==========================##

#-------------Label Superior ---------------#
app_nome = tk.Label(frame_superior, text='SADP - Sistema de Administração de Despesas Pessoais', anchor='nw', font=('Ivy', 13, 'bold'), bg=c2, fg=c1, relief='flat')
app_nome.place(x=10, y=20)

#------------- Label inferior ---------------#
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

#-------- Funções CRUD Adicionar --------#
global tree
#- Adicionar -#
def adcionar():
  nome = etr_nome.get()
  valor = etr_valor.get()
  tipo_pagamento = etr_pagamento.get()
  descricao = etr_descricao.get()
  data_compra = etr_data.get()
  status_despesa = etr_despesa.get()

  lista = [nome, valor, tipo_pagamento, descricao, data_compra, status_despesa]

  if nome=='':
      messagebox.showerror('Erro','Insira um valor no campo')
  else:
      adicionarProduto(lista)
      messagebox.showinfo('Sucesso','Informação inserida com sucesso!')

      etr_nome.delete(0,'end')
      etr_valor.delete(0,'end')
      etr_pagamento.delete(0,'end')
      etr_descricao.delete(0,'end')
      etr_data.delete(0,'end')
      etr_despesa.delete(0,'end') 

  for widget in  frame_direita.winfo_children():
      widget.destroy()

  exibir() 

#- Adicionar -#

#- Editar -#

def editar():
    try:
        treev_dados = tree.focus()
        treev_dicio = tree.item(treev_dados)
        tree_lista = treev_dicio['values']

        valor_id = tree_lista[0]

        etr_nome.delete(0,'end')
        etr_valor.delete(0,'end')
        etr_pagamento.delete(0,'end')
        etr_descricao.delete(0,'end')
        etr_data.delete(0,'end')
        etr_despesa.delete(0,'end') 


        etr_nome.insert(0,tree_lista[1])
        etr_valor.insert(0,tree_lista[2])
        etr_pagamento.insert(0,tree_lista[3])
        etr_descricao.insert(0,tree_lista[4])
        etr_data.insert(0,tree_lista[5])
        etr_despesa.insert(0,tree_lista[6]) 

        def atualizar():
            nome = etr_nome.get()
            valor = etr_valor.get()
            tipo_pagamento = etr_pagamento.get()
            descricao = etr_descricao.get()
            data_compra = etr_data.get()
            status_despesa = etr_despesa.get()

            lista = [nome, valor, tipo_pagamento, descricao, data_compra, status_despesa,valor_id]

            if nome=='':
                messagebox.showerror('Erro','Insira um valor no campo')
            else:
                atualizarProduto(lista)
                messagebox.showinfo('Sucesso','Informação atualizadas com sucesso!')

                etr_nome.delete(0,'end')
                etr_valor.delete(0,'end')
                etr_pagamento.delete(0,'end')
                etr_descricao.delete(0,'end')
                etr_data.delete(0,'end')
                etr_despesa.delete(0,'end') 

            for widget in  frame_direita.winfo_children():
                widget.destroy()

            exibir()    

        #Botão Editar
        btn_Atualizar = Button(frame_inferior,command=atualizar, text='Atualizar', width=10, font=('Ivy', 10, 'bold'), bg=c2, fg=c1, relief='raised', overrelief='ridge')
        btn_Atualizar.place(x=150,y=400)

  
      
            

        
    except IndexError:
        messagebox.showerror('Erro','Selecione a informação que deseja editar')      


        

#- Adicionar -#



#---------Botões-----------#

#Botão Adicionar
btn_adicionar = Button(frame_inferior, command=adcionar,text='Adicionar', width=10, font=('Ivy', 10, 'bold'), bg=c6, fg=c1, relief='raised', overrelief='ridge')
btn_adicionar.place(x=15,y=400)

#Botão Editar
btn_editar = Button(frame_inferior,command=editar, text='Editar', width=10, font=('Ivy', 10, 'bold'), bg=c2, fg=c1, relief='raised', overrelief='ridge')
btn_editar.place(x=150,y=400)

#Botão Deletar
btn_deletar = Button(frame_inferior, text='Deletar', width=10, font=('Ivy', 10, 'bold'), bg=c7, fg=c1, relief='raised', overrelief='ridge')
btn_deletar.place(x=280,y=400)

 




##======================= Tela Direita ===========================##
def exibir():
    global tree

    lista = exibirProduto()

    # lista para cabecario
    tabela_head = ['ID','Nome','valor','Método de pagamento', 'Descrição', 'Data da despesa','Status da Despesa']



    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","center","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor='center')
        
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

# Chamando a função Exibir
exibir()
    












janela.mainloop()
