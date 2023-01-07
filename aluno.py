from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import banco


#Funções para o Label
"""def format_cpf(event = None):
    
    text = cpf_aluno.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return
    
    for index in range(len(text)):
        
        if not text[index] in "0123456789": continue
        if index in [2, 5]: new_text += text[index] + "."
        elif index == 8: new_text += text[index] + "-"
        else: new_text += text[index]

    cpf_aluno.delete(0, "end")
    cpf_aluno.insert(0, new_text)"""



#Função para o botões com o DB

def gravarDados():
    #Pegando as informações

    v_id_aluno=id_aluno.get()
    v_nome_aluno=nome_aluno.get()
    v_cpf_aluno= cpf_aluno.get()
    print(v_cpf_aluno)
    v_turma_aluno=turma_aluno.get()
    #Criando uma condição de erro 
    if v_id_aluno == '' or v_nome_aluno == '' or v_cpf_aluno == '' or v_turma_aluno == '':
        messagebox.showerror("Erro","Vc esqueceu de adcionar um campo")
        return
    vquery = "INSERT INTO alunos(id_aluno,nome_aluno,cpf_aluno,turma_id) VALUES ("+v_id_aluno+",'"+v_nome_aluno+"','"+v_cpf_aluno+"',"+v_turma_aluno+")"
    print(vquery)
    banco.dml(vquery)
    messagebox.showinfo("Cadastro aluno", f"Informação do aluno {nome_aluno.get()} salvado com sucesso")
    visualiza()
    
        
   

def limpa():#limpar os dados
    lista_aluno.delete(*lista_aluno.get_children())
    id_aluno.delete(0, END)
    turma_aluno.delete(0, END)
    nome_aluno.delete(0, END)
    cpf_aluno.delete(0, END)



def seleciona():
    vquery = "SELECT * FROM alunos"

    return banco.dql(vquery)

def visualiza():
    lista_aluno.delete(*lista_aluno.get_children())
    linhas = seleciona()
    for dados in linhas:
        lista_aluno.insert("", END, values= dados)



def excluir():
    try:
        vquery = "DELETE FROM alunos WHERE id_aluno = " + id_aluno.get()
        print(vquery)
        banco.dml(vquery)
        messagebox.showinfo("Cadastro de alunos", f"Registro do aluno {nome_aluno.get()} excluido com sucesso")
        visualiza()
    except:
        messagebox.showerror("ERRO Campo vazio", "Selecione os campos para excluir")


def atualizar():
    v_nome_aluno=nome_aluno.get()
    v_cpf_aluno=cpf_aluno.get()
    v_turma_aluno=turma_aluno.get()
    v_id_aluno=id_aluno.get()
    vquery = "UPDATE alunos SET nome_aluno = '"+v_nome_aluno+"',cpf_aluno = '"+v_cpf_aluno+"', turma_id = "+v_turma_aluno+" WHERE id_aluno = "+v_id_aluno
    print(vquery) 
    banco.dml(vquery)
    messagebox.showinfo("Cadatro de alunos", f"Cadatro atualizado do aluno {nome_aluno.get()}")
    visualiza()
    


def vusualizar_pesquisa():
    v_nome_aluno=nome_aluno.get()
    v_cpf_aluno=cpf_aluno.get()
    v_turma_aluno=turma_aluno.get()
    v_id_aluno=id_aluno.get()
    
    """vquery = "SELECT * FROM alunos WHERE nome_aluno = '"+nome_aluno.get()+"' OR id_aluno = "+id_aluno.get()+" OR cpf_aluno = '"+cpf_aluno.get()+"' OR turma_id = "+turma_aluno.get()+""
    print(vquery)
    return banco.dql(vquery)"""
    if v_id_aluno == "":
        print("Nada")
    else:
        vquery = "SELECT * FROM alunos WHERE id_aluno = "+v_id_aluno+""
        print(vquery)
        return banco.dql(vquery)

    if v_nome_aluno == "":
        print("Campo vazio")
    else:
        vquery = "SELECT * FROM alunos WHERE nome_aluno = '"+v_nome_aluno+"'"
        print(vquery)
        return banco.dql(vquery)

    if v_cpf_aluno == "":
        print("Campo vazio")
    else:
        vquery = "SELECT * FROM alunos WHERE cpf_aluno = '"+v_cpf_aluno+"'"
        print(vquery)
        return banco.dql(vquery)

    if v_turma_aluno == "":
        print("Campo vazio")
    else:
        vquery = "SELECT * FROM alunos WHERE turma_id ="+v_turma_aluno+""
        print(vquery)
        return banco.dql(vquery)
        

def pesquisar():
    lista_aluno.delete(*lista_aluno.get_children())
    linhas = vusualizar_pesquisa()
    for dados in linhas:
        lista_aluno.insert("", END, values= dados)


#Abrir novas janelas
def abrirProfessor():
    print("Abrir")

    exec(open("professor.py").read())

#Abrir pagina NOTA do aluno
def abrirNotaAluno():
    exec(open("notas.py").read())

app = Tk()

app.title("Informações do aluno")
app.geometry("635x1200")
#app.configure( background= "ffff")

#Barra de menu
barraDeMenus = Menu(app)
menuAlunos = Menu(barraDeMenus, tearoff=0)
menuProfessores = Menu(barraDeMenus,tearoff=0)

barraDeMenus.add_cascade(label="Alunos", menu=menuAlunos )
barraDeMenus.add_cascade(label="Professores", menu=menuProfessores)
menuProfessores.add_command(label='Editar', command=abrirProfessor)
menuAlunos.add_cascade(label="Nota", command=abrirNotaAluno)
app.config(menu= barraDeMenus)


#Criando Width
frame_escola = Frame(app,bg='#DFE3EE', highlightbackground='#63031F',highlightthickness=4)
frame_escola.place(relx= 0.02, rely=0.01, relwidth=0.96, relheight=0.55)

frm_lista_escola = Frame(app,bg='#DFE3EE', highlightbackground='#63031F', highlightthickness=4)
frm_lista_escola.place(relx=0.02, rely=0.58, relwidth=0.96, relheight=0.40)

#Criando os Label
Label(frame_escola,text="id_aluno",background="#DFE3EE", foreground="#63031F").place(x=10,y=10,width=100,height=20)
id_aluno= Entry(frame_escola)
id_aluno.place(x=10,y=40,width=200,height=20)

Label(frame_escola,text="nome do aluno",background="#DFE3EE", foreground="#63031F").place(x=10,y=70,width=100,height=20)
nome_aluno= Entry(frame_escola)
nome_aluno.place(x=10,y=100,width=200,height=20)

Label(frame_escola,text="CPF do aluno",background="#DFE3EE", foreground="#63031F").place(x=10,y=130,width=100,height=20)
cpf_aluno= Entry(frame_escola)
cpf_aluno.place(x=10,y=160,width=200,height=20)

Label(frame_escola,text="Turma do aluno",background="#DFE3EE", foreground="#63031F").place(x=10,y=200,width=100,height=20)
turma_aluno= Entry(frame_escola)
turma_aluno.place(x=10,y=220,width=200,height=20)


#Botões
adcionar = Button(frame_escola,text = 'Adcionar',command=gravarDados)
adcionar.place(x=500,y=20,width=80,height=40)

bPesquisa = Button(frame_escola,text = 'Pesquisa', command=pesquisar)
bPesquisa.place(x=500,y=70,width=80,height=40)

bAtual = Button(frame_escola,text = 'Atualiza', command=atualizar)
bAtual.place(x=500,y=120,width=80,height=40)

bExclui = Button(frame_escola,text = 'Exclui',command=excluir)
bExclui.place(x=500,y=170,width=80,height=40)

bLimpa = Button(frame_escola,text = 'Limpa', command=limpa)
bLimpa.place(x=500,y=220,width=80,height=40)

bFecha = Button(frame_escola,text = 'Fecha', command=app.destroy)
bFecha.place(x=500,y=270,width=80,height=40)

bTodos = Button(frame_escola,text = 'Todos', command=visualiza)
bTodos.place(x=500,y=320,width=80,height=40)

#Deixar responsivel (relx= 0.8, rely=0.20, relwidth=0.08, relheight=0.1)

#Duplo clic da lista
def duplo_clique(event):
    #global cnome_aluno  
    id_aluno.delete(0, END)
    turma_aluno.delete(0, END)
    nome_aluno.delete(0, END)
    cpf_aluno.delete(0, END)
    lista_aluno.selection()
    for i in lista_aluno.selection():
        cid_aluno,cnome_aluno,ccpf_aluno,cturma_aluno = lista_aluno.item(i,'values')
    id_aluno.insert(END,cid_aluno)
    turma_aluno.insert(END,cturma_aluno)
    nome_aluno.insert(END,cnome_aluno)
    cpf_aluno.insert(END,ccpf_aluno)



#Criar lista
#lista_aluno = ttk.Treeview(frm_lista_escola, he)
# AQUI DEFINIMOS LISTAS E GRIDS
#Cria a lista e a posicina dentro do frame
# AQUI DEFINIMOS LISTAS E GRIDS
#Cria a lista e a posicina dentro do frame
colunas = ('col0','col1','col2','col3','col4')
cabecalho = ('', 'Id', 'Nome', 'CPF', 'Turma','')
largura = (5,30,90,90,50)
#Define a ação a ser realizada na lista (evento - Duplo Clique)
#lista_aluno = ttk.Treeview(frm_lista_aluno, height=3, column = ('col0','col1','col2','col3','col4','col5'))
lista_aluno = ttk.Treeview(frm_lista_escola, height=3, column=colunas)
lista_aluno.bind("<Double-1>",duplo_clique)
conta = 0
for i in colunas:
   coluna = "#" +  str(conta)
   #print(cabecalho[conta])
   lista_aluno.heading(coluna,text=cabecalho[conta])
   lista_aluno.column(coluna,width=largura[conta])
   conta  += 1

# Posiciona a lista
lista_aluno.place(relx= 0.01, rely=0.1, relwidth=0.95, relheight=0.85)
scr_lstcliente = Scrollbar(frm_lista_escola,orient='vertical')

#Faz a ligação entre a barra de rolagem e o GRID.
lista_aluno.configure(yscroll=scr_lstcliente.set)
scr_lstcliente.place(relx= 0.96, rely=0.1,relwidth=0.02,relheight=0.85)


"""vtxt="Módulo Tkinter"
vbg= "#ff0"
vfg="#000"
txt2= Label(app,text=vtxt,bg=vbg,fg=vfg)
txt2.pack(ipadx=20,ipady=20,padx=5,pady=5,side="top",fill=Y,expand=True)"""
app.mainloop()

