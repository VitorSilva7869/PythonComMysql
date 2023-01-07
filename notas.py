from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco

#Criando funções
#Abrir pagina Aluno
def abirAluno():
    exec(open("aluno.py").read())

#Abrir pagina professor
def abrirProfessor():
    exec(open("professor.py").read())

#Função duplo clic
def duplo_clique(event):
    id_nota_aluno.delete(0,END)
    lista_nota.selection()
    for i in lista_nota.selection():
        cid_nota_aluno = lista_nota.item(i,'values')
    id_nota_aluno.insert(END,cid_nota_aluno)    
#Funções para os botões

#Função Todos
def seleciona():
    vquery = "SELECT * FROM avaliação"

    return banco.dql(vquery)

def visualiza():
    lista_nota.delete(*lista_nota.get_children())
    linhas = seleciona()
    for dados in linhas:
        lista_nota.insert("", END, values= dados)

#Função pesquisar 
def vusualizar_pesquisa():
    v_id_aluno = id_nota_aluno.get()
    print(v_id_aluno)
    if id_nota_aluno == "":
        print("Nada")
    else:
        vquery = "SELECT * FROM avaliação WHERE id_aluno = "+id_nota_aluno.get()+""
        print(vquery)
        return banco.dql(vquery)
def pesquisar():
    lista_nota.delete(*lista_nota.get_children())
    linhas = vusualizar_pesquisa()
    for dados in linhas:
        lista_nota.insert("", END, values= dados)


#Inicio do Sistema
app = Tk()
app.title("Nota do Aluno")
app.geometry("635x600")

#Barra de menu
barraDeMenu = Menu(app)
menuAluno = Menu(barraDeMenu, tearoff=0)
menuProfessor = Menu(barraDeMenu, tearoff=0)

menuAluno.add_command(label="Editar", command=abirAluno)
barraDeMenu.add_cascade(label="Aluno", menu= menuAluno)
barraDeMenu.add_cascade(label="Professores", menu=menuProfessor)
menuProfessor.add_cascade(label="Editar", command= abrirProfessor)
app.config(menu = barraDeMenu)

#Criando Width
freme_nota_aluno = Frame(app,bg='#DFE3EE', highlightbackground='#63031F',highlightthickness=4)
freme_nota_aluno.place(relx= 0.02, rely=0.01, relwidth=0.96, relheight=0.40)

frame_nota_lista = Frame(app, bg='#DFE3EE', highlightbackground='#63031F',highlightthickness=4)
frame_nota_lista.place(relx=0.02, rely=0.43, relwidth=0.96, relheight=0.55)

#Label
Label(freme_nota_aluno, text="Id do luno" ,background="#DFE3EE", foreground="#63031F").place(x=10,y=20,width=84,height=20)
id_nota_aluno = Entry(freme_nota_aluno)
id_nota_aluno.place(x=20, y=40,width=200,height=20)

#Criando Botões
bTodos = Button(freme_nota_aluno,text = 'Todos', command=visualiza).place(relx= 0.7, rely=0.25, relwidth=0.15, relheight=0.2)

bPesquisar = Button(freme_nota_aluno,text = 'Pesquisar', command=pesquisar ).place(relx= 0.7, rely=0.50, relwidth=0.15, relheight=0.2)

#Criando Listas
colunas = ('col0','col1','col2','col3','col4','col5','col6')
cabecalho = ('', 'ID aluno', 'ID professor', 'ID disciplina', 'Nt test','Nt trabalho', 'Nt prova')
largura = (5,60,80,80,50,80,60)
#Define a ação a ser realizada na lista (evento - Duplo Clique)
#lista_nota = ttk.Treeview(frm_lista_nota, height=3, column = ('col0','col1','col2','col3','col4','col5'))
lista_nota = ttk.Treeview(frame_nota_lista, height=3, column=colunas)
lista_nota.bind("<Double-1>",duplo_clique)
conta = 0
for i in colunas:
   coluna = "#" +  str(conta)
   #print(cabecalho[conta])
   lista_nota.heading(coluna,text=cabecalho[conta])
   lista_nota.column(coluna,width=largura[conta])
   conta  += 1

# Posiciona a lista
lista_nota.place(relx= 0.01, rely=0.1, relwidth=0.95, relheight=0.85)
scr_lstcliente = Scrollbar(frame_nota_lista,orient='vertical')

#Faz a ligação entre a barra de rolagem e o GRID.
lista_nota.configure(yscroll=scr_lstcliente.set)
scr_lstcliente.place(relx= 0.96, rely=0.1,relwidth=0.02,relheight=0.85)



#Criar loop
app.mainloop()