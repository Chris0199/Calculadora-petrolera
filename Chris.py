import tkinter as tk

ventana = tk.Tk()
ventana.title("Conversor")
ventana.geometry("400x500+700+100")
ventana.minsize(width=400, height=500)
ventana.configure(bg="white")
def convertir():

    try:
        presion = entrada_presion.get()
        resultado1 = (float(presion)*750.062)
        resultado2 = (float(presion)*51.7149)
        rotulo_resultado1.config(text=resultado1)
        rotulo_resultado2.config(text=resultado2)
            
    except ValueError:
        pass

rotulo_titulo = tk.Label(ventana, 
	text="CONVERSOR PRESION",
    bg="white", fg="black",
    font= "consolas 20 bold",
    relief = tk.GROOVE, bd=2,
    padx=10, pady=10)
rotulo_titulo.pack(padx=20, pady=20)

cuadro1 = tk.Frame(ventana,
    bg="white")

rotulo_presion = tk.Label(cuadro1,
    text="Presion bar:",
    bg="white",
    font="consolas 18 bold",
    width=12,
    anchor=tk.W)
rotulo_presion.pack(side=tk.LEFT, padx=10, pady=10)

entrada_presion = tk.Entry(cuadro1,
    bg="white", fg="black",
    font="consolas 18 bold",
    relief=tk.SUNKEN,
    width=10,
    justify=tk.RIGHT,
    state="normal")
entrada_presion.pack(side=tk.LEFT, padx=10, pady=10)

cuadro1.pack(pady=10)


cuadro2 = tk.Frame(ventana,
    bg="white")

rotulo_torr = tk.Label(cuadro2,
    text="Presion torr:",
    bg="white",
    font="consolas 18 bold",
    width=12,
    anchor=tk.W)
rotulo_torr.pack(side=tk.LEFT, padx=10, pady=10)

rotulo_resultado1 = tk.Label(cuadro2,
    text="",
    bg="red",
    font="consolas 18 bold",
    width=10,
    relief = tk.GROOVE,
    anchor=tk.E)
rotulo_resultado1.pack(side=tk.LEFT, padx=10, pady=10)

cuadro2.pack(pady=10)

cuadro3 = tk.Frame(ventana,
    bg="white")

rotulo_psi = tk.Label(cuadro3,
    text="Presion psi:",
    bg="white",
    font="consolas 18 bold",
    width=12,
    anchor=tk.W)
rotulo_psi.pack(side=tk.LEFT, padx=10, pady=10)

rotulo_resultado2 = tk.Label(cuadro3,
    text="",
    bg="blue",
    font="consolas 18 bold",
    width=10,
    relief = tk.GROOVE,
    anchor=tk.E)
rotulo_resultado2.pack(side=tk.LEFT, padx=10, pady=10)

cuadro3.pack(pady=10)

cuadro4 = tk.Frame(ventana,
    bg="white")

boton_borrar = tk.Button(cuadro4,
    text="Borrar",
    bg="white",
    font="consolas 18 bold",
    width=10)
boton_borrar.pack(side=tk.LEFT, padx=20, pady=20)

boton_convertir = tk.Button(cuadro4,
    text="Convertir",
    bg="green",
    font="consolas 18 bold",
    width=10,
    state="normal",
    command=convertir)
boton_convertir.pack(side=tk.LEFT, padx=20, pady=20)

cuadro4.pack(pady=10)


entrada_presion.focus()

ventana.mainloop()
