from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco
#Funçoes

#Funções abrir paginas
#Abrir pagina Aluno
def abirAluno():
    exec(open("aluno.py").read())

#Abrir pagina NOTA do aluno
def abrirNotaAluno():
    exec(open("notas.py").read())



#Função Dublo Clic da lista
def duplo_clique(event):
    #global cnome_professor  
    id_professor.delete(0, END)
    nome_professor.delete(0, END)
    cpf_professor.delete(0, END)
    lista_professor.selection()
    for i in lista_professor.selection():
        cid_professor,cnome_professor,ccpf_professor = lista_professor.item(i,'values')
    id_professor.insert(END,cid_professor)
    nome_professor.insert(END,cnome_professor)
    cpf_professor.insert(END,ccpf_professor)

#Funções para os BOTÕES

def gravarDados():
    #Pegando as informações

    v_id_professor=id_professor.get()
    v_nome_professor=nome_professor.get()
    v_cpf_professor= cpf_professor.get()
    #Criando uma condição de erro 
    if v_id_professor == '' or v_nome_professor == '' or v_cpf_professor == '':
        messagebox.showerror("Erro","Vc esqueceu de adcionar um campo")
        return
    vquery = "INSERT INTO alunos(id_professor,nome_professor,cpf_professor,turma_id) VALUES ("+v_id_professor+",'"+v_nome_professor+"','"+v_cpf_professor+"')"
    print(vquery)
    banco.dml(vquery)
    messagebox.showinfo("Cadastro aluno", f"Informação do aluno {nome_professor.get()} salvado com sucesso")
    visualiza()
    
        
   

def limpa():#limpar os dados
    lista_professor.delete(*lista_professor.get_children())
    id_professor.delete(0, END)
    nome_professor.delete(0, END)
    cpf_professor.delete(0, END)



def seleciona():
    vquery = "SELECT professor.id_professor, professor.nome_professor, professor.cpf_professor, disciplina.nome_disciplina From professor, disciplina, prof_disc where professor.id_professor=prof_disc.id_professor and disciplina.id_disciplina = prof_disc.id_disciplina"

    return banco.dql(vquery)

def visualiza():
    lista_professor.delete(*lista_professor.get_children())
    linhas = seleciona()
    for dados in linhas:
        lista_professor.insert("", END, values= dados)



def excluir():
    try:
        vquery = "DELETE FROM alunos WHERE id_professor = " + id_professor.get()
        print(vquery)
        banco.dml(vquery)
        messagebox.showinfo("Cadastro de alunos", f"Registro do aluno {nome_professor.get()} excluido com sucesso")
        visualiza()
    except:
        messagebox.showerror("ERRO Campo vazio", "Selecione os campos para excluir")


def atualizar():
    v_nome_professor=nome_professor.get()
    v_cpf_professor=cpf_professor.get()
    v_id_professor=id_professor.get()
    vquery = "UPDATE professor SET nome_professor = '"+v_nome_professor+"',cpf_professor = '"+v_cpf_professor+"' WHERE id_professor = "+v_id_professor
    print(vquery) 
    banco.dml(vquery)
    messagebox.showinfo("Cadatro de alunos", f"Cadatro atualizado do aluno {nome_professor.get()}")
    visualiza()
    


def vusualizar_pesquisa():
    v_nome_professor=nome_professor.get()
    v_cpf_professor=cpf_professor.get()
    v_id_professor=id_professor.get()

    # antes vquery = "SELECT * FROM alunos WHERE nome_professor = '"+nome_professor.get()+"' OR id_professor = "+id_professor.get()+" OR cpf_professor = '"+cpf_professor.get()+"' OR turma_id = "+disciplina_professor.get()+""
    if v_id_professor == "":
        print("Nada")
    else:
        vquery = "SELECT * FROM professor WHERE id_professor = "+v_id_professor+""
        print(vquery)
        return banco.dql(vquery)

    if v_nome_professor == "":
        print("Campo vazio")
    else:
        vquery = "SELECT * FROM professor WHERE nome_professor = '"+v_nome_professor+"'"
        print(vquery)
        return banco.dql(vquery)

    if v_cpf_professor == "":
        print("Campo vazio")
    else:
        vquery = "SELECT * FROM professor WHERE cpf_professor = '"+v_cpf_professor+"'"
        print(vquery)
        return banco.dql(vquery)


def pesquisar():
    lista_professor.delete(*lista_professor.get_children())
    linhas = vusualizar_pesquisa()
    for dados in linhas:
        lista_professor.insert("", END, values= dados)

#Criação do inicio app
app = Tk()
app.title("Professor")
app.geometry("635x1200")

#Barra de menu 
barraDeMenu = Menu(app)
menuAluno = Menu(barraDeMenu, tearoff=0)
menuProfessor = Menu(barraDeMenu, tearoff=0)

menuAluno.add_command(label="Editar", command=abirAluno)
menuAluno.add_cascade(label= "Notas", command=abrirNotaAluno)
barraDeMenu.add_cascade(label="Aluno", menu= menuAluno)
barraDeMenu.add_cascade(label="Professores", menu=menuProfessor)
app.config(menu = barraDeMenu)

#Cria width 
frame_professor = Frame(app,bg='#DFE3EE', highlightbackground='#63031F',highlightthickness=4)
frame_professor.place(relx= 0.02, rely=0.01, relwidth=0.96, relheight=0.55)

frame_professor_lista = Frame(app, bg='#DFE3EE', highlightbackground='#63031F',highlightthickness=4)
frame_professor_lista.place(relx=0.02, rely=0.58, relwidth=0.96, relheight=0.40)

#Criar LABEL
Label(frame_professor, text="Id do professor",background="#DFE3EE", foreground="#63031F").place(x=10,y=20,width=84,height=20)
id_professor = Entry(frame_professor)
id_professor.place(x=10, y=40,width=200,height=20)

Label(frame_professor, text="Nome do Professor",background="#DFE3EE", foreground="#63031F").place(x=10,y=80,width=101,height=20)
nome_professor = Entry(frame_professor)
nome_professor.place(x=10, y=100,width=200,height=20)

Label(frame_professor, text="CPF do professor",background="#DFE3EE", foreground="#63031F").place(x=10,y=140,width=90,height=20)
cpf_professor = Entry(frame_professor)
cpf_professor.place(x=10, y=160,width=200,height=20)

#Adcionar Botões
adcionar = Button(frame_professor,text = 'Adcionar',command=gravarDados)
adcionar.place(x=500,y=20,width=80,height=40)

bPesquisa = Button(frame_professor,text = 'Pesquisa', command=pesquisar)
bPesquisa.place(x=500,y=70,width=80,height=40)

bAtual = Button(frame_professor,text = 'Atualiza', command=atualizar)
bAtual.place(x=500,y=120,width=80,height=40)

bExclui = Button(frame_professor,text = 'Exclui',command=excluir)
bExclui.place(x=500,y=170,width=80,height=40)

bLimpa = Button(frame_professor,text = 'Limpa', command=limpa)
bLimpa.place(x=500,y=220,width=80,height=40)

bFecha = Button(frame_professor,text = 'Fecha', command=app.destroy)
bFecha.place(x=500,y=270,width=80,height=40)

bTodos = Button(frame_professor,text = 'Todos', command=visualiza)
bTodos.place(x=500,y=320,width=80,height=40)

#Criar ComBox
"""cb_produto = ttk.Combobox(frame_professor,
    values=lista_professor, textvariable=t_produto,
    state="readonly") 

def carrega_produtos():
    vquery = 'SELECT cod_produto, descricao_produto FROM produto WHERE descricao_produto <> ""'
    banco.dql(vquery)
    lst_prd = []

    for i in banco:
        dic_produto[i[1]] = i[0]
        lst_prd.append(i[1])
    #print('oi',dic_produto)
    conn.commit()
    conn.close()
    return lst_prd

def selecionado(event):
    sSQL = 'SELECT cod_produto FROM produto WHERE descricao_produto = "{0}"'.format(cb_produto.get())
    conn = sqlite3.connect("controle_estoque.db")
    cur = conn.cursor()
    cur.execute(sSQL)
    idproduto = cur.fetchone()
    t_idproduto.set(idproduto)
    t_idproduto.set(dic_produto[cb_produto.get()])
"""

#Criar lista
#lista_professor = ttk.Treeview(frm_lista_escola, he)
# AQUI DEFINIMOS LISTAS E GRIDS
#Cria a lista e a posicina dentro do frame
# AQUI DEFINIMOS LISTAS E GRIDS
#Cria a lista e a posicina dentro do frame
colunas = ('col0','col1','col2','col3','col4')
cabecalho = ('', 'Id', 'Nome', 'CPF', 'Disciplina','')
largura = (5,20,90,80,80)
#Define a ação a ser realizada na lista (evento - Duplo Clique)
#lista_professor = ttk.Treeview(frm_lista_professor, height=3, column = ('col0','col1','col2','col3','col4','col5'))
lista_professor = ttk.Treeview(frame_professor_lista, height=3, column=colunas)
lista_professor.bind("<Double-1>",duplo_clique)
conta = 0
for i in colunas:
   coluna = "#" +  str(conta)
   #print(cabecalho[conta])
   lista_professor.heading(coluna,text=cabecalho[conta])
   lista_professor.column(coluna,width=largura[conta])
   conta  += 1

# Posiciona a lista
lista_professor.place(relx= 0.01, rely=0.1, relwidth=0.95, relheight=0.85)
scr_lstcliente = Scrollbar(frame_professor_lista,orient='vertical')

#Faz a ligação entre a barra de rolagem e o GRID.
lista_professor.configure(yscroll=scr_lstcliente.set)
scr_lstcliente.place(relx= 0.96, rely=0.1,relwidth=0.02,relheight=0.85)


#Criar loop para rodar
app.mainloop()