from tkinter import * 
from tkinter import Tk, ttk
from tkinter import messagebox
import sqlite3


# cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters
co5 = "#add8e6"   # azul claro / blue 


#ESSE É A JANELA DO LOGIN, DEIXA ELE CENTRALIZADO E O ESTILO UM POUCO DIFERENTE PRA N DEIXAR IGUAL DO VÍDEO
#DEIXAR SER LOGADO APENAS APERTANDO ENTER
janela = Tk()
janela.title('LibraCar')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=False, height=False)

frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

l_nome = Label(frame_cima, text='LibraCar', anchor=NE,font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=275, anchor=NW,font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=10, y=45)

l_nome = Label(frame_baixo, text='Usuário *', anchor=NW,font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=15, justify='left', font=("", 15), highlightthickness=1, relief='solid' )
e_nome.place(x=14, y=50)

l_pass=Label(frame_baixo, text='Senha *', anchor=NW,font=('Ivy 10'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=15, justify='left', font=("", 15), highlightthickness=1, relief='solid' )
e_pass.place(x=14, y=130)

credenciais =['adm', '123']
def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()
    
    if nome =='admin' and senha=='admin':
        messagebox.showinfo('login','Seja Bem Vindo Administrador !')
    elif credenciais[0] == nome and credenciais[1]==senha:   
        messagebox.showinfo('login','Seja Bem Vindo a LibraCar !')
        
        for widget in frame_baixo.winfo_children():
           widget.destroy()

        for widget in frame_cima.winfo_children():
           widget.destroy()
        
        janela2()   
         

    else: 
        messagebox.showwarning('ERRO!','Verifique o login e Senha') 


def janela2 (title='LibraCar',geometry='310x300',background=co2): # DEIXAR AQUI FULL SCREEN
    #ESSES BOTOES ABAIXO DEIXAR QUADRADO NO LADO SUPERIOR DIREITO
    #DEIXAR ALGUM COMANDO PRA ATIVAR O BOTAO, POR EXEMPLO ALT + V PARA ENTRAR EM CADASTRO DE VEÍCULOS
    b1_confirma = Button(command=janela_1, text='Cadastro Veiculo', width=35, height=2,font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
    b1_confirma.place(x=25, y=80)
    b2_confirma = Button(command=janela_2, text='Cadastro Clientes', width=35, height=2,font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
    b2_confirma.place(x=25, y=130)
    b3_confirma = Button(command=janela_3, text='Caixa', width=35, height=2,font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
    b3_confirma.place(x=25, y=180)

def janela_1():
    import veiculo
def janela_2():
    import cliente
def janela_3():
    import caixa



#Botão Ok
b_confirma = Button(frame_baixo, command=verificar_senha, text='Entrar', width=35, height=2,font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirma.place(x=15, y=180)


janela.mainloop()

