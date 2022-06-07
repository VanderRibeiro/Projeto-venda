from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funcoes():
    def limpa_tela_3(self):
        self.codVeiculo_entry.delete(0, END)
        self.marca_entry.delete(0, END)
        self.codCliente_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.pagamento_entry.delete(0, END)
        self.troco_entry.delete(0, END)
    def conecta_bd(self):
        self.conn1 = sqlite3.connect("cliente.bd"); print("Conectado ao banco de dados de clientes")
        self.conn2 = sqlite3.connect("veiculos.bd"); print("Conectado ao banco de dados de veículos")
        self.cursor1 = self.conn1.cursor()
        self.cursor2 = self.conn2.cursor()
    def desconectar_bd(self):
        self.conn1.close()
        self.conn2.close()
    def add_clienteCaixa(self):
        self.nome = self.nome_entry.get()
        self.endereco = self.endereco_entry.get()
        self.conecta_bd()
        
        self.cursor1.execute("""INSERT INTO cliente (nome, endereço) VALUES (?, ?)""",
        (self.nome, self.endereco))
        self.conn1.commit()
        self.desconectar_bd()
        self.limpa_tela_3()

    def add_veiculoCaixa(self):
        self.marca = self.marca_entry.get()
        self.conecta_bd()

        self.cursor2.execute("""INSERT INTO veiculos (marca) 
            VALUES (?)""", (self.marca))
        self.conn2.commit()
        self.desconectar_bd()
        self.limpa_tela_3()
    def busca_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END, '%')
        self.cursor1.execute(""" SELECT codCliente, nome FROM cliente""")
        buscanomeCli = self.cursor2.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", END, values=i)
        self.limpa_tela_3()
        self.desconectar_bd()
    def busca_veiculo(self):
        self.conecta_bd()
        self.listaVei.delete(*self.listaVei.get_children())

        self.marca_entry.insert(END, '%')
        marca = self.marca_entry.get()
        self.cursor2.execute(""" SELECT codVeiculo, marca FROM veiculos""")
        buscanomeVei = self.cursor2.fetchall()
        for i in buscanomeVei:
            self.listaVei.insert("", END, values=i)
        self.limpa_tela_3()
        self.desconectar_bd()


class Caixa(Funcoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.limpa_tela_3()
        self.conecta_bd()
        self.desconectar_bd()
        self.add_clienteCaixa()
        self.add_veiculoCaixa() 
        self.busca_veiculo()
        root.mainloop()
    def tela(self):
        self.root.title("Caixa")
        self.root.configure(background='blue')
        self.root.geometry("500x300")
        self.root.resizable(False, False)

#bordas dentro da janela
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = 'gray', highlightbackground='black', highlightthickness=3)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.96)

#botões
    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame_1, text = "Consultar Cliente", bd = 2, command=self.busca_cliente)
        self.bt_limpar.place(relx= 0, rely= 0.4, relwidth=0.3, relheight=0.10)
        self.bt_limpar = Button(self.frame_1, text = "Consultar Veículo", bd = 2, command=self.busca_veiculo)
        self.bt_limpar.place(relx= 0.35, rely= 0.4, relwidth=0.3, relheight=0.10)

        self.bt_limpar = Button(self.frame_1, text = "Limpar", bd = 2, command=self.limpa_tela_3)
        self.bt_limpar.place(relx= 0, rely= 0.74, relwidth=0.3, relheight=0.10)
        self.bt_buscar = Button(self.frame_1, text = "Comprar", bd = 2)
        self.bt_buscar.place(relx= 0, rely= 0.88, relwidth=0.3, relheight=0.10)


#Criação da Label e entrada da nome
        self.lb_codVeiculo = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Código do Veiculo")
        self.lb_codVeiculo.place(relx= 0, rely= 0)

        self.codVeiculo_entry = Entry(self.frame_1)
        self.codVeiculo_entry.place(relx= 0, rely= 0.09, relwidth=0.22)

        self.lb_marca = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Marca")
        self.lb_marca.place(relx= 0.25, rely= 0)

        self.marca_entry = Entry(self.frame_1)
        self.marca_entry.place(relx= 0.25, rely= 0.09, relwidth=0.75)


#Criação da Label e entrada da endereco
        self.lb_codCliente = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Código do Cliente")
        self.lb_codCliente.place(relx= 0, rely= 0.2)

        self.codCliente_entry = Entry(self.frame_1)
        self.codCliente_entry.place(relx= 0, rely= 0.3, relwidth=0.22)

        self.lb_nome = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Nome")
        self.lb_nome.place(relx= 0.25, rely= 0.2)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.25, rely= 0.3, relwidth=0.75)

#pagamento/troco
        self.lb_valor = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Valor")
        self.lb_valor.place(relx= 0.75, rely= 0.4)

        self.valor_entry = Entry(self.frame_1)
        self.valor_entry.place(relx= 0.75, rely= 0.5, relwidth=0.22)

        self.lb_pagamento = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Pagamento")
        self.lb_pagamento.place(relx= 0.75, rely= 0.6)

        self.pagamento_entry = Entry(self.frame_1)
        self.pagamento_entry.place(relx= 0.75, rely= 0.7, relwidth=0.22)

        self.lb_troco = Label(self.frame_1, bg = 'gray', fg = 'white', text = "Troco")
        self.lb_troco.place(relx= 0.75, rely= 0.8)

        self.troco_entry = Entry(self.frame_1)
        self.troco_entry.place(relx= 0.75, rely= 0.9, relwidth=0.22)

Caixa()