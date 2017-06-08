# coding=utf-8


"""

(v) Correções na GUI.
(v) Adicionado mensagens de erros e exceções.
(v) Base de Criptografia v1.0
(v) Poucos Bugs. Menores corrigidos.
(v) Corrigido na versão:
(*) Bug, encriptador com base 60 não decripta. + Corrigido, limitado à 30.

"""


# Importando Recursos:
from tkinter    import *
from functools  import partial


window = Tk()


# Definindo funções:


def crypt_this(text, idd):
    result = ''
    for i in text:
        i       = chr(ord(i) + idd + 2)
        result  = result + i
    print(result)
    lb4_result["bg"]                        = "BlanchedAlmond"
    lb4_result["text"]                      = result
    return result


def decrypt_this(text, idd):
    result = ''
    for i in text:
        i = chr(ord(i) - idd - 2)
        result = result + i
    print(result)
    lb4_result["bg"]                        = "BlanchedAlmond"
    lb4_result["text"]                      = result
    return result


def vernumeric1(text, idd):
    try:
        text = text.get()
        idd = idd.get()
        idd = int(idd)
        if idd > 30 or idd < 1:
            lb4_result["text"]              = "Erro 02: Número maior que 30, ou menor que 1."
            lb4_result["bg"]                = "Firebrick"
        else:
            crypt_this(text, idd)
    except:
        lb4_result["text"]                  = "Erro 01: Digite um número!"
        lb4_result["bg"]                    = "Firebrick"


def vernumeric2(text, idd):
    try:
        text = text.get()
        idd = idd.get()
        idd = int(idd)
        if idd > 30 or idd < 1:
            lb4_result["text"]              = "Erro 02: Número maior que 30, ou menor que 1."
            lb4_result["bg"]                = "Firebrick"
        else:
            decrypt_this(text, idd)
    except:
        lb4_result["text"]                  = "Erro 01: Digite um número!"
        lb4_result["bg"]                    = "Firebrick"


####################
# Criando os Labels:
####################


lb1_explain     = Label(window, text="Bem vindo ao MyCryptoon v0.3.2S!\n"
                                 "\nDigite algo na imbox abaixo"
                                 "\npara Crypt ou Decrypt: ",                   bg="LightSalmon")

lb2_askidd      = Label(window, text="Digite o ID de criptografia\n"
                                "entre 1 e 30, por favor:",                     bg="SandyBrown")

lb3_exresult    = Label(window, text="Resultado:",                              bg="SandyBrown")

lb4_result      = Label(window, text="..........",                              bg="BlanchedAlmond")


# Criando os Entrys:


ed1_text        = Entry(window,                                                 bg="Seashell1")
ed2_idd         = Entry(window,                                                 bg="Seashell1")


# Criando os Buttons:


bt1_crypt       = Button(window, width=20, text="Criptografar",                 bg="Snow")
bt2_decrypt     = Button(window, width=20, text="Descriptografar",              bg="Snow")


# Posicionando os Widgets:


lb1_explain.pack    (side=TOP,      fill=BOTH,      expand=1)   # 1,1
ed1_text.pack       (side=TOP,      fill=BOTH,      expand=1)   # 2,1
lb2_askidd.pack     (side=TOP,      fill=BOTH,      expand=1)   # 3,1
ed2_idd.pack        (side=TOP,      fill=BOTH,      expand=1)   # 4,1
lb3_exresult.pack   (side=TOP,      fill=BOTH,      expand=1)   # 5,1
lb4_result.pack     (side=TOP,      fill=BOTH,      expand=1)   # 6,1
bt1_crypt.pack      (side=LEFT,     anchor=CENTER)              # 10,1 anchor C
bt2_decrypt.pack    (side=RIGHT,    anchor=CENTER)              # 10,1 anchor C


# Chamando as funções com Partial de Functools:


bt1_crypt["command"]    = partial(vernumeric1, ed1_text, ed2_idd)
bt2_decrypt["command"]  = partial(vernumeric2, ed1_text, ed2_idd)


# Desenhando a janela:


window.title                                                                    ( "MyCryptoon v0.3S" )
window["bg"]                                                                    = "SkyBlue"
window.geometry                                                                 ( "376x320+200+200"  )
window.mainloop                                                                 (                    )