
import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Controle Acadêmico")
window.geometry("600x600")

barraDeMenus = Menu(window)
menuAlunos = Menu(barraDeMenus, tearoff=0)
menuAlunos.add_command(label='Incluir')
menuAlunos.add_command(label='Atualizar')
menuAlunos.add_command(label='Pesquisar')
menuAlunos.add_separator()
menuAlunos.add_command(label='sair',command=window.quit)

menuProfessores = Menu(barraDeMenus,tearoff=0)
menuProfessores.add_command(label='Incluir')
menuProfessores.add_command(label='Atualizar')
menuProfessores.add_command(label='Pesquisar')
menuProfessores.add_separator()
menuProfessores.add_command(label='sair',command=window.quit)

barraDeMenus.add_cascade(label="Alunos", menu=menuAlunos)
barraDeMenus.add_cascade(label="Professores", menu=menuProfessores)


#Criando od dois widthe

frame_escola = Frame(window,bg='#DFE3EE', highlightbackground='#3EB21E',highlightthickness=4)
frame_escola.place(relx= 0.02, rely=0.01, relwidth=0.96, relheight=0.55)

frm_lista_escola = Frame(window,bg='#DFE3EE', highlightbackground='#3EB21E', highlightthickness=4)
frm_lista_escola.place(relx=0.02, rely=0.58, relwidth=0.96, relheight=0.40)

#Cores
cor_txt_lbl = '#2F528F'
lbl_relhight = 0.06
lbl_relwidth = 0.07
lbl_relx=0.009

#Label

l_id_curso = Label(frame_escola, text= 'id_curso:', justify=LEFT,font='Arial 10 bold', fg=cor_txt_lbl, anchor=W)
l_id_curso.place(relx=lbl_relx, rely=0.01, relwidth=lbl_relwidth, relheight=lbl_relhight)

lNome = Label(frame_escola, text='nome_curso:', justify=LEFT,  font='Arial 10 bold', fg=cor_txt_lbl, anchor=W)
lNome.place(relx=lbl_relx, rely=0.10, relwidth=lbl_relwidth, relheight=lbl_relhight)

t_id_curso = StringVar()

#Cria um ojbeto para a entrada de dados na interface e associa esse objeto ao objeto texto criado.
e_id_curso = Entry(frame_escola, textvariable=t_id_curso)

# Posiciona o objeto de entrada de dados no grid
e_id_curso.place(relx= 0.07, rely=0.01, width=70, relheight=lbl_relhight)

t_nome = StringVar()
e_nome = Entry(frame_escola, textvariable=t_nome)
e_nome.place(relx= 0.07, rely=0.10, width=200, relheight=lbl_relhight)

#06 - AQUI FICAM TODOS OS BOTÕES

bTodos = Button(frame_escola,text = 'Todos')
bTodos.place(relx= 0.8, rely=0.10, relwidth=0.05, relheight=0.1)

bPesquisa = Button(frame_escola,text = 'Pesquisa')
bPesquisa.place(relx= 0.8, rely=0.20, relwidth=0.05, relheight=0.1)

bAdd = Button(frame_escola,text = 'Inclui')
bAdd.place(relx= 0.8, rely=0.30, relwidth=0.05, relheight=0.1)

bAtual = Button(frame_escola,text = 'Atualiza')
bAtual.place(relx= 0.8, rely=0.40, relwidth=0.05, relheight=0.1)

bExclui = Button(frame_escola,text = 'Exclui')
bExclui.place(relx= 0.8, rely=0.50, relwidth=0.05, relheight=0.1)

bLimpa = Button(frame_escola,text = 'Limpa')
bLimpa.place(relx= 0.8, rely=0.60, relwidth=0.05, relheight=0.1)

bFecha = Button(frame_escola,text = 'Fecha')
bFecha.place(relx= 0.8, rely=0.70, relwidth=0.05, relheight=0.1)

window.config(menu=barraDeMenus)

window.mainloop()
