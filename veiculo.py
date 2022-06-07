from distutils.cmd import Command
from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

##RUBENS, AS MUDANÇAS DAQUI SE APLICA IGUALMENTE AO CAIXA E AO CLIENTE

class Funcs():
    def limpa_tela(self):
        self.codVeiculo_entry.delete(0, END)
        self.marca_entry.delete(0, END)
        self.placa_entry.delete(0, END)
        self.renavam_entry.delete(0, END)
        self.chassi_entry.delete(0, END)
        self.preco_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("veiculos.bd")
        self.cursor = self.conn.cursor()
    def desconecta_bd(self):
        self.conn.close()
    def montaTabelas(self):
        self.conecta_bd(); print("Conectando ao banco de dados")
        #criação da tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS veiculos(
                codVeiculo INTEGER PRIMARY KEY,
                marca CHAR(40) NOT NULL,
                placa CHAR(7) NOT NULL,
                renavam INT(10) NOT NULL,
                chassi CHAR(30) NOT NULL,
                preco INT(8) NOT NULL
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def variaveis(self):
        self.codVeiculo = self.codVeiculo_entry.get()
        self.marca = self.marca_entry.get()
        self.placa = self.placa_entry.get()
        self.renavam = self.renavam_entry.get()
        self.chassi = self.chassi_entry.get()
        self.preco = self.preco_entry.get()
    def add_veiculo(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO veiculos (marca, placa, renavam, chassi, preco)
            VALUES (?, ?, ?, ?, ?)""", (self.marca, self.placa, self.renavam, self.chassi, self.preco))
        self.conn.commit() 
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaVei.delete(*self.listaVei.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT codVeiculo, marca, placa, renavam, chassi, preco FROM veiculos
            ORDER BY marca ASC; """)
        for i in lista:
            self.listaVei.insert("", END, values=i)
        self.desconecta_bd()
    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaVei.selection()

        for n in self.listaVei.selection():
            col1, col2, col3, col4, col5, col6 = self.listaVei.item(n, 'values')
            self.codVeiculo_entry.insert(END, col1)
            self.marca_entry.insert(END, col2)
            self.placa_entry.insert(END, col3)
            self.renavam_entry.insert(END, col4)
            self.chassi_entry.insert(END, col5) 
            self.preco_entry.insert(END, col6) 
    def deleta_veiculo(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM veiculos WHERE codVeiculo = ? """, (self.codVeiculo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()
    def altera_veiculo(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE veiculos SET marca = ?, placa = ?, renavam = ?, chassi = ?, preco = ?
            WHERE codVeiculo = ? """, (self.marca, self.placa, self.renavam, self.chassi, self.preco, self.codVeiculo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def busca_veiculo(self):
        self.conecta_bd()
        self.listaVei.delete(*self.listaVei.get_children())

        self.marca_entry.insert(END, '%')
        marca = self.marca_entry.get()
        self.cursor.execute(""" SELECT codVeiculo, marca, placa, renavam, chassi, preco FROM veiculos
            WHERE marca LIKE '%s' ORDER BY marca ASC""" % marca)
        buscanomeVei = self.cursor.fetchall()
        for i in buscanomeVei:
            self.listaVei.insert("", END, values=i)
        self.limpa_tela()
        self.desconecta_bd()

class Veiculo(Funcs):
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
    #DEIXA CENTRALIZADO E MUDA AS CORES PRA FICAR HARMONICO E BONITO DE SE VER
    #AJEITA OS BOTOES PRA Q DÊ PARA USAR COMANDOS PARA ATIVÁ-LOS
    def tela(self):
        self.root.title("Cadastro de Veiculo")
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
        self.bt_buscar = Button(self.frame_1, text = "buscar", bd = 2, command= self.busca_veiculo)
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth=0.1, relheight=0.15)
        self.bt_novo = Button(self.frame_1, text = "Novo", bd = 2, command = self.add_veiculo)
        self.bt_novo.place(relx= 0.6, rely= 0.1, relwidth=0.1, relheight=0.15)
        self.bt_alterar = Button(self.frame_1, text = "Alterar", bd = 2, command= self.altera_veiculo)
        self.bt_alterar.place(relx= 0.7, rely= 0.1, relwidth=0.1, relheight=0.15)
        self.bt_apagar = Button(self.frame_1, text = "Apagar", bd = 2, command = self.deleta_veiculo)
        self.bt_apagar.place(relx= 0.8, rely= 0.1, relwidth=0.1, relheight=0.15)

#Criação da Label e entrada do código
        self.lb_codVeiculo = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Código")
        self.lb_codVeiculo.place(relx= 0.05, rely= 0.05)

        self.codVeiculo_entry = Entry(self.frame_1)
        self.codVeiculo_entry.place(relx= 0.05, rely= 0.15, relwidth=0.08)

#Criação da Label e entrada da marca
        self.lb_marca = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Marca")
        self.lb_marca.place(relx= 0.05, rely= 0.35)

        self.marca_entry = Entry(self.frame_1)
        self.marca_entry.place(relx= 0.05, rely= 0.45, relwidth=0.8)

#Criação da Label e entrada da placa
        self.lb_placa = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Placa")
        self.lb_placa.place(relx= 0.05, rely= 0.55)

        self.placa_entry = Entry(self.frame_1)
        self.placa_entry.place(relx= 0.05, rely= 0.65, relwidth=0.15)

#Criação da Label e entrada do renavam
        self.lb_renavam = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Renavam")
        self.lb_renavam.place(relx= 0.25, rely= 0.55)

        self.renavam_entry = Entry(self.frame_1)
        self.renavam_entry.place(relx= 0.25, rely= 0.65, relwidth=0.20)

#Criação da Label e entrada do Chassi
        self.lb_chassi = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Chassi")
        self.lb_chassi.place(relx= 0.50, rely= 0.55)

        self.chassi_entry = Entry(self.frame_1)
        self.chassi_entry.place(relx= 0.50, rely= 0.65, relwidth=0.35)

#Criação da Label e entrada do Preço
        self.lb_preco = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Preço")
        self.lb_preco.place(relx= 0.05, rely= 0.75)

        self.preco_entry = Entry(self.frame_1)
        self.preco_entry.place(relx= 0.05, rely= 0.85, relwidth=0.15)

    def lista_frame2(self):
        self.listaVei = ttk.Treeview(self.frame_2, height= 3, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.listaVei.heading("#0", text="")
        self.listaVei.heading("#1", text="Código")
        self.listaVei.heading("#2", text="Marca")
        self.listaVei.heading("#3", text="Placa")
        self.listaVei.heading("#4", text="Renavam")
        self.listaVei.heading("#5", text="Chassi")
        self.listaVei.heading("#6", text="Preço")

        self.listaVei.column("#0", width=1)
        self.listaVei.column("#1", width=50)
        self.listaVei.column("#2", width=100)
        self.listaVei.column("#3", width=100)
        self.listaVei.column("#4", width=150)
        self.listaVei.column("#5", width=150)
        self.listaVei.column("#6", width=50)

        self.listaVei.place(relx=0.01, rely=0.1, relwidth=0.95,relheight=0.85)

        self.scroolLista_1 = Scrollbar(self.frame_2, orient='vertical')
        self.listaVei.configure(yscroll=self.scroolLista_1.set)
        self.scroolLista_1.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)

        self.scroolLista_2 = Scrollbar(self.frame_2, orient='horizontal')
        self.listaVei.configure(xscroll=self.scroolLista_2.set)
        self.scroolLista_2.place(relx=0.01, rely=0.91, relwidth=0.95, relheight=0.04)
        self.listaVei.bind("<Double-1>", self.OnDoubleClick)

Veiculo()
