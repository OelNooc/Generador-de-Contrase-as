import string
import random
import os
import tkinter
import webbrowser
from tkinter import *



## para crear la contraseña
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## largo de la contraseña
	
	length = float(txt1.get())

	## cantidad de los distintos tipos de caracteres
	alphabets_count = float(txt2.get())
	digits_count = float(txt3.get())
	special_characters_count = float(txt4.get())

	characters_count = alphabets_count + digits_count + special_characters_count

	## verificar el largo con el total de caracteres
	## colocar en la casilla 5 "La cantidad total de caracteres es mayor a la ingresada inicialmente"
	if characters_count > length:
		txt5.insert(0, "La cantidad total de caracteres es mayor a la ingresada inicialmente")
		return


	## generar la contraseña
	Contraseña = []
	
	## escoger letras aletorias
	for i in range(int(alphabets_count)):
		Contraseña.append(random.choice(alphabets))


	## escoger números aletorios
	for i in range(int(digits_count)):
		Contraseña.append(random.choice(digits))


	## escoger caracteres especiales aletorios
	for i in range(int(special_characters_count)):
		Contraseña.append(random.choice(special_characters))


	## si la suma total de caracteres es menor al largo de la contraseña
	## agregar caracteres aletorios para igualar el largo inicial
	if characters_count < length:
		random.shuffle(characters)
		for i in range(int(length) - int(characters_count)):
			Contraseña.append(random.choice(characters))


	## mezclar la contraseña obtenida
	random.shuffle(Contraseña)

	## convertir la lista en string
	## ingresar la lista en la casilla de texto5
    
	txt5.insert(0,"".join(Contraseña))

def reboot():
	## borra los valores entregados
	txt1.delete(0, "end")
	txt2.delete(0, "end")
	txt3.delete(0, "end")
	txt4.delete(0, "end")
	txt5.delete(0, "end")
	txt6.delete(0, "end")

def w_a():
	##crea o edita .txt generado con la contraseña y el sitio
	f= open("./Contraseñas.txt", "a")
	f.write(os.linesep)
	sitio = txt6.get()
	cont = txt5.get()
	f.write("Tu contraseña generada para" + " " + sitio + " " + "es:" + " " + cont)
	f.close()
	
def callback(url):
	##abre una pestaña nueva en el navegador predeterminado
	webbrowser.open_new(url)


ventana = Tk ()
ventana.geometry ("600x400")
ventana.title ("Generador de Contraseñas")
ventana.iconbitmap("C:\\Users\\leomu\\Desktop\\Programación\\Generador de contraseñas\\candado.ico")


lbl = Label (ventana, text="Generador de contraseñas alfanuméricas seguras") 
lbl.pack()

lbl0 = Label (ventana, text="Creado por OelNooc", fg = "blue", cursor = "hand2" )
lbl0.place(relx=0.75, rely=0.04, relwidth=0.3, relheight=0.15)
lbl0.bind("<Button-1>", lambda e: callback("https://github.com/OelNooc"))

lbl1 = Label (ventana, text="Cantidad Total de Caracteres")
lbl1.place(relx=0.03, rely=0.04, relwidth=0.3, relheight=0.15)

txt1 = Entry(ventana, bg="pink")
txt1.place(relx=0.3, rely=0.04, relwidth=0.22, relheight=0.1)

lbl2 = Label (ventana, text="Cantidad de Letras")
lbl2.place(relx=0.03, rely=0.17, relwidth=0.3, relheight=0.15)

txt2 = Entry(ventana, bg="pink")
txt2.place(relx=0.3, rely=0.17, relwidth=0.22, relheight=0.1)

lbl3 = Label (ventana, text="Cantidad de Números")
lbl3.place(relx=0.03, rely=0.3, relwidth=0.3, relheight=0.15)

txt3 = Entry(ventana, bg="pink")
txt3.place(relx=0.3, rely=0.3, relwidth=0.22, relheight=0.1)

lbl4 = Label (ventana, text="Cantidad de Caracteres Especiales")
lbl4.place(relx=0.03, rely=0.43, relwidth=0.3, relheight=0.15)

txt4 = Entry(ventana, bg="pink")
txt4.place(relx=0.3, rely=0.43, relwidth=0.22, relheight=0.1)

lbl5 = Label (ventana, text="Contraseña Generada")
lbl5.place(relx=0.03, rely=0.56, relwidth=0.3, relheight=0.15)

txt5 = Entry(ventana, bg="pink")
txt5.place(relx=0.3, rely=0.56, relwidth=0.22, relheight=0.1)

lbl6 = Label (ventana, text="Sitio/Juego/Programa")
lbl6.place(relx=0.03, rely=0.69, relwidth=0.3, relheight=0.15)

txt6 = Entry(ventana, bg="pink")
txt6.place(relx=0.3, rely=0.69, relwidth=0.22, relheight=0.1)

btn = Button (ventana, text="Comenzar", command = generate_random_password)
btn.place(relx=0.25, rely= 0.86, relwidth=0.2, relheight=0.12)

btn = Button (ventana, text="Borrar", command = reboot)
btn.place(relx=0.5, rely= 0.86, relwidth=0.2, relheight=0.12)

btn = Button (ventana, text="Crear/Editar .txt", command = w_a)
btn.place(relx=0.75, rely= 0.86, relwidth=0.2, relheight=0.12)

ventana.mainloop ()