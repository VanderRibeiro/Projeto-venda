from distutils.cmd import Command
from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funcs():
    def limpa_tela(self):
        self.codCliente_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.endereco_entry.delete(0, END)
        self.CPF_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("cliente.bd")
        self.cursor = self.conn.cursor()
    def desconecta_bd(self):
        self.conn.close()
    def montaTabelas(self):
        self.conecta_bd(); print("Conectando ao banco de dados")
        #criação da tabela
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS cliente(
                codCliente INTEGER PRIMARY KEY,
                nome CHAR(40) NOT NULL,
                endereco CHAR(40),
                CPF INT(11) NOT NULL
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def variaveis(self):
        self.codCliente = self.codCliente_entry.get()
        self.nome = self.nome_entry.get()
        self.endereco = self.endereco_entry.get()
        self.CPF = self.CPF_entry.get()
    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO cliente (nome, endereco, CPF)
            VALUES (?, ?, ?)""", (self.nome, self.endereco, self.CPF))
        self.conn.commit() 
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT codCliente, nome, endereco, CPF FROM cliente
            ORDER BY nome ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codCliente_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.endereco_entry.insert(END, col3)
            self.CPF_entry.insert(END, col4)
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM cliente WHERE codCliente = ? """, (self.codCliente))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()
    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE cliente SET nome = ?, endereco = ?, CPF = ?
            WHERE codCliente = ? """, (self.nome, self.endereco, self.CPF, self.codCliente))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def busca_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute(""" SELECT codCliente, nome, endereco, CPF FROM cliente
            WHERE nome LIKE '%s' ORDER BY nome ASC""" % nome)
        buscanomeVei = self.cursor.fetchall()
        for i in buscanomeVei:
            self.listaCli.insert("", END, values=i)
        self.limpa_tela()
        self.desconecta_bd()

class cliente(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        root.mainloop()

#fundo da janela
    def tela(self):
        self.root.title("Cadastro de cliente")
        self.root.configure(background='blue')
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)

#bordas dentro da janela
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = 'gray', highlightbackground='black', highlightthickness=3)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)
        self.frame_2 = Frame(self.root, bd = 4, bg = 'gray', highlightbackground='black', highlightthickness=3)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)

#botões
    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame_1, text = "limpar", bd = 2, command=self.limpa_tela)
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth=0.1, relheight=0.15)
        self.bt_buscar = Button(self.frame_1, text = "buscar", bd = 2, command= self.busca_cliente)
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth=0.1, relheight=0.15)
        self.bt_novo = Button(self.frame_1, text = "Novo", bd = 2, command = self.add_cliente)
        self.bt_novo.place(relx= 0.6, rely= 0.1, relwidth=0.1, relheight=0.15)
        self.bt_alterar = Button(self.frame_1, text = "Alterar", bd = 2, command= self.altera_cliente)
        self.bt_alterar.place(relx= 0.7, rely= 0.1, relwidth=0.1, relheight=0.15)
        self.bt_apagar = Button(self.frame_1, text = "Apagar", bd = 2, command = self.deleta_cliente)
        self.bt_apagar.place(relx= 0.8, rely= 0.1, relwidth=0.1, relheight=0.15)

#Criação da Label e entrada do código
        self.lb_codCliente = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Código")
        self.lb_codCliente.place(relx= 0.05, rely= 0.05)

        self.codCliente_entry = Entry(self.frame_1)
        self.codCliente_entry.place(relx= 0.05, rely= 0.15, relwidth=0.08)

#Criação da Label e entrada da nome
        self.lb_nome = Label(self.frame_1, bg = 'gray', fg = 'white', text = "nome")
        self.lb_nome.place(relx= 0.05, rely= 0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.05, rely= 0.45, relwidth=0.8)

#Criação da Label e entrada da endereco
        self.lb_endereco = Label(self.frame_1, bg = 'gray', fg = 'white', text = "endereco")
        self.lb_endereco.place(relx= 0.05, rely= 0.55)

        self.endereco_entry = Entry(self.frame_1)
        self.endereco_entry.place(relx= 0.05, rely= 0.65, relwidth=0.15)

#Criação da Label e entrada do CPF
        self.lb_CPF = Label(self.frame_1, bg = 'gray', fg = 'white', text = "CPF")
        self.lb_CPF.place(relx= 0.25, rely= 0.55)

        self.CPF_entry = Entry(self.frame_1)
        self.CPF_entry.place(relx= 0.25, rely= 0.65, relwidth=0.20)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, columns=("col1", "col2", "col3", "col4", "col5"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="nome")
        self.listaCli.heading("#3", text="endereco")
        self.listaCli.heading("#4", text="CPF")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=100)
        self.listaCli.column("#3", width=100)
        self.listaCli.column("#4", width=150)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95,relheight=0.85)

        self.scroolLista_1 = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista_1.set)
        self.scroolLista_1.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)

        self.scroolLista_2 = Scrollbar(self.frame_2, orient='horizontal')
        self.listaCli.configure(xscroll=self.scroolLista_2.set)
        self.scroolLista_2.place(relx=0.01, rely=0.91, relwidth=0.95, relheight=0.04)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

cliente()


