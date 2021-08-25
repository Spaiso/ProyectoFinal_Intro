from tkinter import *
from tkinter import messagebox as MessageBox
#import time

diccionarioCredenciales={"UsuarioMaster":"Sebastian", "ContraseñaMaster":"Sebas123"}
usuariosAdmin=[]
contrasAdmin=[]
placasEspeciales=[]
espaciosDefault=20
espacios=[]*espaciosDefault
precioDefault=2000
precioEspecial=1000

root = Tk()
root.title ("Sistema de Parqueo")

#Espacio de Funciones

#Funcion para confirmar la cantidad de espacios
def ConfirmarCant():
    global NuevaCant
    global espaciosDefault
    espaciosDefault=NuevaCant.get()
    MessageBox.showinfo("Confirmacion", "La cantidad de espacios fue actualizada")
    MessageBox.showinfo("Nueva Cantidad", espaciosDefault)


#Funcion para definir la cantidad de espacios
def CambCant():
    global NuevaCant
    global espacios
    global espaciosDefault
    NuevaCant=IntVar()
    VentCant=Toplevel(VentAjustes)
    VentCant.geometry("400x200")
    VentCant.title("Cantidad de Espacios")
    lblNuevaCant=Label(VentCant, text="Nueva Cantidad:", font=("Marlett FB",17)).place(x=10, y=20)
    Entry(VentCant, font=(17), textvariable=NuevaCant).place(x=200, y=25)
    AgregarCant = Button(VentCant, text= "Confirmar",padx=30, pady=15, fg="black", bg="#FFFFFF", command=ConfirmarCant).place(x=140, y=90)

#Funcion para el boton que consulta los espacios disponibles
def consultarEsp():
    MessageBox.showinfo("Espacios Disponibles", espaciosDefault)

#Funcion para confirmar el precio por hora
def ConfirmarPrecio():
    global NuevoPrecio
    global precioDefault
    precioDefault=NuevoPrecio.get()
    MessageBox.showinfo("Nuevo Precio Definido",precioDefault)

#Funcion para modificar el precio por hora
def AjustarPrecio():
    global NuevoPrecio
    NuevoPrecio=IntVar()
    VentPrecio=Toplevel(VentAjustes)
    VentPrecio.geometry("400x200")
    VentPrecio.title("Ajustar PrecioxHora")
    lblNuevoPrecio=Label(VentPrecio, text="Nuevo Precio:", font=("Marlett FB",17)).place(x=30, y=20)
    Entry(VentPrecio, font=(17), textvariable=NuevoPrecio).place(x=190, y=25)
    AgregarPrecio = Button(VentPrecio, text= "Confirmar",padx=30, pady=15, fg="black", bg="#FFFFFF", command=ConfirmarPrecio).place(x=140, y=90)

#Funciones para confirmar, eliminar o listar los usuarios especiales

def ConfirmarEsp():
    global placasEspeciales
    global NuevaPlaca
    placasEspeciales.append(NuevaPlaca.get())
    MessageBox.showinfo("Usuario Agregado", "El usuario especial fue agregado exitosamente")

def ConfirmarEliminarEsp():
    global NuevaPlaca
    global placasEspeciales
    if (NuevaPlaca.get()) in placasEspeciales:
        placasEspeciales.remove(NuevaPlaca.get())
        MessageBox.showinfo("Usuario Eliminado", "El usuario fue eliminado de la lista de especiales exitosamente")
    else:
        MessageBox.showerror("Error", "Usuario no encontrado, verifique en la lista de usuarios el nombre correcto")

def ListarEsp():
    global placasEspeciales
    MessageBox.showinfo("Lista Usuarios", placasEspeciales)

#Funcion para cambiar los usuarios Especiales
def ModEspeciales():
    global NuevaPlaca
    NuevaPlaca=StringVar()
    VentEspeciales=Toplevel(VentAjustes)
    VentEspeciales.geometry("440x230")
    VentEspeciales.title("Ajustar Usuarios")
    lblNuevaPlaca=Label(VentEspeciales, text="Nueva Placa:", font=("Marlett FB",17)).place(x=50, y=20)
    Entry(VentEspeciales, font=(17), textvariable=NuevaPlaca).place(x=210, y=25)
    AgregarAdmin = Button(VentEspeciales, text= "Agregar",padx=30, pady=15, fg="black", bg="#FFFFFF", command=ConfirmarEsp).place(x=60, y=90)
    EliminarAdmin = Button(VentEspeciales, text= "Eliminar",padx=30, pady=15, fg="black", bg="#FFFFFF", command=ConfirmarEliminarEsp).place(x=270, y=90)
    MostrarAdmins = Button(VentEspeciales, text= "Mostrar Lista de \n Usuarios Especiales",padx=30, pady=15, fg="black", bg="#FFFFFF", command=ListarEsp).place(x=140, y=150)

#Funciones para confirmar, eliminar o listar los administradores
def ConfirmarAdmin():
    global usuariosAdmin
    global contrasAdmin
    global NuevoUser
    if NuevoUser.get() not in usuariosAdmin:
        usuariosAdmin.append(NuevoUser.get())
        contrasAdmin.append(NuevaPass.get())
        MessageBox.showinfo("Usuario Agregado", "El usuario fue agregado exitosamente")
    else:
        MessageBox.showerror("Error", "Usuario ya en lista, consulte la lista")

def ConfirmarEliminarAdmin():
    global NuevoUser
    global usuariosAdmin
    if (NuevoUser.get()) in usuariosAdmin:
        usuariosAdmin.remove(NuevoUser.get())
        MessageBox.showinfo("Usuario Eliminado", "El usuario fue eliminado exitosamente")
    else:
        MessageBox.showerror("Error", "Usuario no encontrado, verifique en la lista de usuarios el nombre correcto")

def ListarAdmins():
    global usuariosAdmin
    MessageBox.showinfo("Lista Administradores", usuariosAdmin)

#Funcion para cambiar los Administradores que pueden logear
def ModAdmin():
    global NuevoUser
    NuevoUser=StringVar()
    global NuevaPass
    NuevaPass=StringVar()
    VentAdmin=Toplevel(VentAjustes)
    VentAdmin.geometry("440x230")
    VentAjustes.title("Ajustar Administradores")
    lblNuevoUser=Label(VentAdmin, text="Nuevo Usuario:", font=("Marlett FB",17)).place(x=8, y=20)
    Entry(VentAdmin, font=(17), textvariable=NuevoUser).place(x=230, y=25)
    lblNuevaPass=Label(VentAdmin, text="Nueva Contraseña:", font=("Marlett FB",17)).place(x=8, y=50)
    Entry(VentAdmin, font=(17), textvariable=NuevaPass).place(x=230, y=55)
    AgregarAdmin = Button(VentAdmin, text= "Agregar",padx=30, pady=15, fg="black", bg="#FFFFFF", command=ConfirmarAdmin).place(x=60, y=90)
    EliminarAdmin = Button(VentAdmin, text= "Eliminar",padx=30, pady=15, fg="black", bg="#FFFFFF", command=ConfirmarEliminarAdmin).place(x=270, y=90)
    MostrarAdmins = Button(VentAdmin, text= "Mostrar Lista \n de Administradores",padx=30, pady=15, fg="black", bg="#FFFFFF", command=ListarAdmins).place(x=140, y=150)

    

#Funcion que valida las credenciales y abre la ventana de ajustes
def VerificarLogin():
    global VerificarLogin
    global VentAjustes
    global usuariosAdmin
    global contrasAdmin
    global diccionarioCredenciales
    if entradaUser.get() == (diccionarioCredenciales["UsuarioMaster"]) and entradaContra.get() == (diccionarioCredenciales["ContraseñaMaster"]) or entradaUser.get() in usuariosAdmin and entradaContra.get() in contrasAdmin:
        VentAjustes=Toplevel(VentLogin)
        VentAjustes.geometry("300x300")
        VentAjustes.title("Ajustes de Admin")
        ModifAdmins=Button(VentAjustes, text="Modificar \n Administradores",  font=("Marlett FB",17), command=ModAdmin).pack()
        ModifEspeciales=Button(VentAjustes, text="Modificar \n Usuarios Especiales",  font=("Marlett FB",17), command=ModEspeciales).pack()
        ModifPrecio=Button(VentAjustes, text="Ajustar \n Precio por Hora",  font=("Marlett FB",17), command=AjustarPrecio).pack()
        ModifCampos=Button(VentAjustes, text="Ajustar Cantidad \n de Espacios",  font=("Marlett FB",17), command=CambCant).pack()

    else:MessageBox.showerror("Error", "Usuario y/o contraseña incorrectos, intente de nuevo.")

    

#Funcion para abrir la ventana de Log In
def abrirLogin():
    global canvasAjustes,FrameAjustes, lblUser, lblContra, txtUser, txtContra, entradaContra, entradaUser, VentLogin
    VentLogin = Toplevel(root)
    VentLogin.geometry("440x200")
    VentLogin.title("Inicio de Sesion")
    lblUser=Label(VentLogin, text="Digite su Usuario:", font= ("Marlett FB",10)).place(x=60, y=40)
    lblContra=Label(VentLogin, text= "Digte su Contraseña:", font= ("Marlett FB",10)).place(x=38, y=95)
    entradaUser=StringVar()
    txtUser=Entry (VentLogin, textvariable=entradaUser).place (x=180, y=42)
    entradaContra=StringVar()
    txtContra=Entry (VentLogin, textvariable=entradaContra).place (x=180, y=97)
    Verificar = Button(VentLogin, text= "Log In",padx=15,
                     pady=5, fg="black", bg="#FFFFFF", command=VerificarLogin).place(x=330, y=60)
    Verificar.pack()

    #Funcion para agregar vehiculo
def agregarAuto():
    global espacios
    global espaciosUsados
    global horaRegistrada
    global precioPagar
    if entradaPlaca.get() not in espacios:
        espacios.append(entradaPlaca.get())
        MessageBox.showinfo("Vehiculo Agregado", "El vehiculo fue agregado exitosamente")
    else:
        MessageBox.showerror("Error", "Vehiculo ya Registrado")
    print (espacios)

    #Funcion para retirar vehiculo
def retirarVehiculo():
    global espacios
    global horasEstadia
    global placasEspeciales
    global precioEspecial
    global precioDefault
    global precioPagar
    horasEstadia=salidaIngresada.get()-horaEntIngresada.get()
    if entradaPlaca.get() in espacios:
        if entradaPlaca.get() in placasEspeciales:
            precioPagar=horasEstadia*precioEspecial
            espacios.remove(entradaPlaca.get())
            MessageBox.showinfo("Salida", "Usuario Especial! Su precio a pagar es de:")
            MessageBox.showinfo("Precio a Pagar", precioPagar)

        else:
            precioPagar=horasEstadia*precioDefault
            espacios.remove(entradaPlaca.get())
            MessageBox.showinfo("Salida", "Muchas gracias! Vuelva pronto, su precio a pagar es de:")
            MessageBox.showinfo("Precio a Pagar", precioPagar)
    else:
        MessageBox.showerror("Error", "La placa digitada no esta en el parqueo, intente de nuevo")
    print (espacios)


#A Partir de aqui, no hay mas funciones

#Codigo para las especificaciones de la ventana principal
canvas = Canvas(root, height=200, width=440, bg="#A8D2D2")
canvas.pack()
Frame=Frame(root, bg="#FFFFFF")
Frame.place(relwidth=0.96, relheight=0.9, relx=0.02, rely=0.030)
#Entrada de Datos de la ventana principal.
lblPlaca=Label(text="Digite su Placa:", font= ("Marlett FB",15)).place(x=30, y=40)
entradaPlaca=StringVar()
txtPlaca=Entry (root, textvariable=entradaPlaca, font=(13)). place (x=200, y=42)
lblHoraEntrada=Label(text="Hora de entrada:", font=("Marlett FB",12)).place (x=50, y=88)
horaEntIngresada=IntVar()
txtEntrada=Entry (root, textvariable=horaEntIngresada, font=(12)).place (x=200, y=88)
lblHoraSalida=Label (text="Hora de Salida:", font=(12)).place (x=55, y=130)
salidaIngresada=IntVar()
txtSalida=Entry (root, textvariable=salidaIngresada, font=(12)).place (x=200, y=130)
#Botones para acciones de la ventana
ingresar=Button(root, text="Ingresar \n Auto", padx=15, pady=9, fg="black", bg="#FFFFFF", command=agregarAuto).place(x=90, y=170)
retirar=Button(root, text="Retirar \n Auto", padx=15, pady=9, fg="black", bg="#FFFFFF", command=retirarVehiculo).place(x=270, y=170)
ajustes = Button(root, text= "Ajustes",padx=15,
                     pady=5, fg="black", bg="#FFFFFF", command=abrirLogin)
ajustes.pack()


root.mainloop()

