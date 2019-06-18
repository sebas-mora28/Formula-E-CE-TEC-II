about_text = """
TECNOLOGICO DE COSTA RICA 

Ingeniería en Computadores 
Taller de programación

    Estudiantes: 
Sebastián Mora Godínez
Santiago Brenes Torres

    Profesor: 
Pedro Gutiérrez García

Grupo 03, I semestre 2019

    Costa Rica
    
    versión 2.0.0
"""

from tkinter import *  # tk()
from tkinter import ttk  # ProgressBar
from WiFiClient import NodeMCU  # NodeCMU
import time  # time.sleep()
import os  # path()
import threading  # Thread
import winsound  # Reproducir musica
from tkinter import messagebox


global Driver1, Driver2, Car1, Car2, list_drivers,RGP,REP,descendiente, ascendiente,indice,newlista, newlista_cars, lista_cars, logo_running, bwm_logo, mercedes_logo, audi_logo, ascendiente_cars, descendiente_cars
Driver1, Driver2, Car1, Car2 = False, False, False, False
newlista=[]
list_drivers = []
RGP = True
REP = True
ascendiente= True
descendiente= True
indice = 6
newlista_cars = []
lista_cars = []
logo_running = True
bmw_logo = False
mercedes_logo= True
audi_logo = False
ascendiente_cars = True
descendiente_cars = True



# Ventana del menu principal
root = Tk()
root.minsize(1400, 700)
root.resizable(width=NO, height=NO)
root.title('Telemetry')

# Canvas del menu principal
Canvas_menu = Canvas(root, width=1400, height=700, bg="#000000")
Canvas_menu.place(x=0, y=0)


def cargarImg(nombre):
    # Funcion para cargar las imagenes desde la carpeta imagenes
    ruta = os.path.join('imagenes', nombre)
    imagen = PhotoImage(file=ruta)
    return imagen


#### Cargar la imagen del fondo del menu principal###
Fondo = cargarImg('Fondo.png')
Canvas_menu.create_image(705, 350, image=Fondo)

image_test = cargarImg('test_driver.png')
image_about = cargarImg('About.png')
image_drivers = cargarImg('Drivers.png')
image_quit = cargarImg('Quit.png')


def cargar_cancion(Nombre):
    # Funcion para cargar canciones del juego
    winsound.PlaySound(Nombre, winsound.SND_ASYNC + winsound.SND_LOOP)


def off():
    # Funcion que apaga la cancion una vez que entre a cualquiera de las demas pantallas
    winsound.PlaySound(None, winsound.SND_ASYNC + winsound.SND_LOOP)
cargar_cancion('menu_song.wav')


bmw_logo_ = cargarImg('bmw_logo.png')
mercedes_logo_ = cargarImg('mercedes_logo.png')
audi_logo_ = cargarImg('Audi_logo.png')
Canvas_menu.create_text(1300, 20, text='Season:', font=('Arial', 15), fill='white')
Canvas_menu.create_text(1300, 40, text='2019',  font=('Arial', 15), fill='white')
Canvas_menu.create_text(1300, 100, text='Indice ganador:', font=('Arial', 15), fill='white')
Canvas_menu.create_text(1300, 125, text='',  font=('Arial', 15), fill='white', tags='indice_ganador')
Canvas_menu.create_image(1120, 80, image=bmw_logo_, state=NORMAL, tags=['bwm', 'logo'])
Canvas_menu.create_image(1120, 80, image=mercedes_logo_, state=HIDDEN, tags=['mercedes', 'logo'])
Canvas_menu.create_image(1120, 80, image=audi_logo_, state=HIDDEN, tags=['audi', 'logo'])

def change_logo(logo):
    """Funcion que permite cambiar la escuderia en la pantalla de menu"""
    global audi_logo, mercedes_logo, bmw_logo
    if (logo=='bwm'):
        bmw_logo = True
        mercedes_logo = False
        audi_logo = False
    if (logo=='audi'):
        audi_logo = True
        mercedes_logo = False
        bmw_logo = False
    if (logo=='mercedes'):
        mercedes_logo= True
        bmw_logo = False
        audi_logo = False


def escuderias():
    """Funcion que permite mostrar los diferentes logos de las escuderías para ser
    elegidos desde el menu"""
    global logo_running
    index = 0
    logos = [['bwm', 245], ['mercedes', 547], ['audi', 345]]
    while True:
        if not logo_running:
            break
        if index>2:
            index = 0
        Canvas_menu.itemconfig('logo', state=HIDDEN)
        Canvas_menu.itemconfig(logos[index][0], state=NORMAL)
        btn_logo.config(text=logos[index][0], command=lambda: change_logo(logos[index][0]))
        Canvas_menu.itemconfig('indice_ganador', text= logos[index][1])
        time.sleep(3)
        index += 1


logos = threading.Thread(target=escuderias)
logos.start()



def drivers_window():
    """Pantalla de la tabla de posiciones de los pilotos"""
    drivers = Toplevel()
    drivers.minsize(1500, 1013)
    drivers.resizable(width=NO, height=NO)
    drivers.title('Drivers')

    Canvas_drivers = Canvas(drivers, width=1500, height=800, bg='light blue')
    Canvas_drivers.place(x=0, y=0)

    def editar_(indice):
        """Funcion que abre una pantalla y permite editar los datos de los pilotos"""
        global newlista
        editar = Toplevel()
        editar.minsize(700, 700)
        editar.resizable(width=NO, height=NO)
        editar.title('Editar')

        Canvas_editar = Canvas(editar, width=700, height=700, bg='#E25D17')
        Canvas_editar.place(x=0, y=0)

        Canvas_editar.create_text(100, 90, text='Nombre', font=('Arial',20))
        Canvas_editar.create_text(83, 200, text='Edad', font=('Arial',20))
        Canvas_editar.create_text(130, 300, text='Nacionalidad', font=('Arial', 20))
        Canvas_editar.create_text(100, 400, text='Posición', font=('Arial',20))
        Canvas_editar.create_text(83, 500, text='RGP', font=('Arial', 20))
        Canvas_editar.create_text(83, 600, text='REP', font=('Arial', 20))


        Nombre = Entry(Canvas_editar, width= 30, font=('Arial',15))
        Nombre.place(x=50, y=110)
        Edad = Entry(Canvas_editar, width= 30, font=('Arial',15))
        Edad.place(x=50, y=220)
        Nacionalidad = Entry(Canvas_editar, width= 30, font=('Arial',15))
        Nacionalidad.place(x=50, y=320)
        Posición = Entry(Canvas_editar, width= 30, font=('Arial',15))
        Posición.place(x=50, y=420)
        REP = Entry(Canvas_editar, width= 30, font=('Arial',15))
        REP.place(x=50, y=520)
        RGP = Entry(Canvas_editar, width= 30, font=('Arial',15))
        RGP.place(x=50, y=620)
        
        """Se inserta los datos prederminados en el caso en que solamente se realice cambios a
        solamente uno de las opciones la lista no quede en blanco"""
        Nombre.insert(0,str(newlista[indice][1]))
        Edad.insert(0,str(newlista[indice][3]))
        Nacionalidad.insert(0,str(newlista[indice][2]))
        Posición.insert(0,str(newlista[indice][4]))
        REP.insert(0,str(newlista[indice][5]))
        RGP.insert(0,str(newlista[indice][6]))



        def new_changes(indice):
            """Funcion que guarda los nuevos cambios efectuados en la pantalla edit"""
            global newlista
            new_info = [newlista[indice][0], Nombre.get(),Nacionalidad.get(),Edad.get(),Posición.get(),REP.get(),RGP.get()]
            newlista[indice] = new_info
            with open('Drivers.txt','w') as file:
                new_text = ('\n').join([','.join(drivers) for drivers in newlista])
                file.write(new_text)
                file.close()
            editar.destroy()
            cargar()

        btn_save = Button(Canvas_editar,text='Save',font=('Arial',15), command=lambda:new_changes(indice))
        btn_save.place(x=500, y=350)

        editar.mainloop()


    def ascendiente_aux(lista,ind):
        num = len(lista)
        for i in range(len(lista)):
            for j in range(0,num-i-1):
                if int(lista[j][ind]) >int(lista[j+1][ind]):
                    temp = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = temp
            
        return lista


    def descendiente_aux(lista):
        return lista[::-1]

    

    def recorrer():
        """Funcion que lee el txt y lo convierte a una matriz"""
        global ascendiente, descendiente, indice, newlista
        with open('Drivers.txt', 'r') as file:
            lista = file.read().split('\n')
            newlist = []
            index = 0
            while index < len(lista):
                newlist += [lista[index].split(',')]
                index += 1
            file.close()
            newlista = ascendiente_aux(newlist,indice)
            if not ascendiente:
                newlista= descendiente_aux(newlist)

    def create_lambda(X):
        funcion = lambda: editar_(X)
        return funcion


    def cargarBotones(newlista_drivers):
        """Funcion que carga los botones cada vez que es llamada"""
        global newlista,list_drivers
            
        
        list_drivers= [cargarImg(newlista[0][0]),
                    cargarImg(newlista[1][0]),
                    cargarImg(newlista[2][0]),
                    cargarImg(newlista[3][0]),
                    cargarImg(newlista[4][0]),
                    cargarImg(newlista[5][0]),
                    cargarImg(newlista[6][0]),
                    cargarImg(newlista[7][0]),
                    cargarImg(newlista[8][0]),
                    cargarImg(newlista[9][0])]

        ind = 0
        x = 150
        for i in range(2):
            y = 150
            for j in range(5):
                funcion = create_lambda(ind)
                Button(Canvas_drivers, image=list_drivers[ind], command=funcion).place(x=x, y=y)
                y += 125
                ind += 1
            x += 700


    fondo = cargarImg('fondo_drivers.png')
    def cargar():
        """Elimina todos los elementos que hay en el canvas y los vuelve a implementar
        con los datos actualizados"""
        global newlista

        Canvas_drivers.delete('all')

        Canvas_drivers.create_image(250, 300, image=fondo)
        recorrer()
        cargarBotones(newlista)

        Canvas_drivers.create_text(310,135, text = 'Nombre', font=('Arial',15, 'bold'), fill='Red')
        Canvas_drivers.create_text(1000, 135, text='Nombre', font=('Arial', 15, 'bold'), fill='Red')
        Canvas_drivers.create_text(440,135, text = 'Edad', font=('Arial', 15, 'bold'), fill='Red')
        Canvas_drivers.create_text(1100, 135, text='Edad', font=('Arial', 15, 'bold'), fill='Red')
        Canvas_drivers.create_text(563, 135, text='Nacionalidad', font=('Arial', 15, 'bold'), fill='Red')
        Canvas_drivers.create_text(1200, 135, text='Nacionalidad', font=('Arial', 15, 'bold'), fill='Red')
        Canvas_drivers.create_text(665, 135, text='RPG', font=('Arial', 15, 'bold'), fill='Red')
        Canvas_drivers.create_text(1305, 135, text='RPG', font=('Arial', 15, 'bold'), fill='Red')
        Canvas_drivers.create_text(760, 135, text='REG', font=('Arial', 15, 'bold'), fill='Red')
        Canvas_drivers.create_text(1400, 135, text='REP', font=('Arial', 15, 'bold'), fill='Red')

        Canvas_drivers.create_text(310,200, text =newlista[0][1] ,font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(310, 320, text=newlista[1][1],font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(310, 440, text=newlista[2][1],font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(310, 560, text=newlista[3][1],font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(310, 690, text=newlista[4][1],font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1000, 200, text=newlista[5][1],font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1000, 320, text=newlista[6][1],font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1000, 440, text=newlista[7][1],font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1000, 560, text=newlista[8][1],font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1000, 690, text=newlista[9][1],font=('Arial',15,'bold'),justify=CENTER)

        Canvas_drivers.create_text(440,200, text =newlista[0][3], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(440, 320, text= newlista[1][3], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(440, 440, text= newlista[2][3], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(440, 560, text= newlista[3][3], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(440, 690, text= newlista[4][3], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1100, 200, text=newlista[5][3], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1100, 320, text=newlista[6][3], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1100, 440, text=newlista[7][3], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1100, 560, text=newlista[8][3], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1100, 690, text=newlista[9][3], font=('Arial',15,'bold'),justify=CENTER)


        Canvas_drivers.create_text(560,200, text = newlista[0][2], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(560, 320, text= newlista[1][2], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(560, 440, text= newlista[2][2], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(560, 560, text= newlista[3][2], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(560, 690, text= newlista[4][2], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1200, 200, text=newlista[5][2], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1200, 320, text=newlista[6][2], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1200, 440, text=newlista[7][2], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1200, 560, text=newlista[8][2], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1200, 690, text=newlista[9][2], font=('Arial',15,'bold'),justify=CENTER)


        Canvas_drivers.create_text(660,200, text =newlista[0][5], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(660, 320, text=newlista[1][5], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(660, 440, text=newlista[2][5], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(660, 560, text=newlista[3][5], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(660, 690, text=newlista[4][5], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1300, 200, text=newlista[5][5], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1300, 320, text=newlista[6][5], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1300, 440, text=newlista[7][5], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1300, 560, text=newlista[8][5], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1300, 690, text=newlista[9][5], font=('Arial',15,'bold'),justify=CENTER)

        Canvas_drivers.create_text(760,200, text =newlista[0][6], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(760, 320, text=newlista[1][6], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(760, 440, text=newlista[2][6], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(760, 560, text=newlista[3][6], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(760, 690, text=newlista[4][6], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1400, 200, text=newlista[5][6], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1400, 320, text=newlista[6][6], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1400, 440, text=newlista[7][6], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1400, 560, text=newlista[8][6], font=('Arial',15,'bold'),justify=CENTER)
        Canvas_drivers.create_text(1400, 690, text=newlista[9][6], font=('Arial',15,'bold'),justify=CENTER)


    cargar()


    def ascendiente():
        global ascendiente, descendiente
        if ascendiente:
            descendiente = False
            cargar()
        else:
            ascendiente = True
            descendiente = False
            cargar()
            

    def descendiente():
        global ascendiente,descendiente
        if descendiente:
            ascendiente = False
            cargar()
        else:
            ascendiente = False
            descendiente = True
            cargar()


    
    def RGP_():
        global indice, RGP,REP
        if RGP:
            REP=False
            cargar()
        else:
            REP = False
            RGP=True 
            indice = 5
            cargar()

    def REP_():
        global indice,RGP,REP
        if REP:
            RGP =False
            cargar()
        else:
            REP = True
            RGP = False 
            indice = 6
            cargar() 
            

            

    btn_ascendente = Button(Canvas_drivers, text='Ascendente',font=('Arial',15),command=ascendiente)
    btn_ascendente.place(x=300, y=30)

    btn_descendente = Button(Canvas_drivers, text='Decendente',font=('Arial',15),command=descendiente)
    btn_descendente.place(x=450, y=30)

    btn_RGP = Button(Canvas_drivers, text='RGP',font=('Arial',15),command=RGP_)
    btn_RGP.place(x=700, y=30)

    btn_REG = Button(Canvas_drivers, text='REP',font=('Arial',15),command=REP_)
    btn_REG.place(x=800, y=30)
       

    def back():
        drivers.withdraw()
        drivers_cars_window()

    btn_back = Button(Canvas_drivers, text='Back',font=('Arial',15),command=back)
    btn_back.place(x=50, y=30)
    
    drivers.mainloop()



def cars_window():
    """Pantalla de la tabla de posiciones de los carros"""
    cars = Toplevel()
    cars.minsize(1000, 900)
    cars.resizable(width=NO, height=NO)
    cars.title('Cars')

    Canvas_cars = Canvas(cars, width=1000, height=900, bg='light blue')
    Canvas_cars.place(x=0, y=0)

    def editar(indice):
        """Funcion que abre una pantalla y permite editar los datos de los pilotos"""
        global newlista_cars
        editar = Toplevel()
        editar.minsize(700, 500)
        editar.resizable(width=NO, height=NO)
        editar.title('Editar')

        Canvas_editar = Canvas(editar, width=700, height=700, bg='#E25D17')
        Canvas_editar.place(x=0, y=0)

        Canvas_editar.create_text(80, 50, text='Marca', font=('Arial', 20))
        Canvas_editar.create_text(83, 180, text='Modelo', font=('Arial', 20))
        Canvas_editar.create_text(100, 280, text='Temporada', font=('Arial', 20))
        Canvas_editar.create_text(100, 380, text='Eficiencia', font=('Arial', 20))


        Marca = Entry(Canvas_editar, width=30, font=('Arial', 15))
        Marca.place(x=40, y=80)
        Modelo = Entry(Canvas_editar, width=30, font=('Arial', 15))
        Modelo.place(x=40, y=200)
        Temporada = Entry(Canvas_editar, width=30, font=('Arial', 15))
        Temporada.place(x=40, y=300)
        Eficiencia = Entry(Canvas_editar, width=30, font=('Arial', 15))
        Eficiencia.place(x=40, y=400)

        Marca.insert(0, str(newlista_cars[indice][1]))
        Modelo.insert(0, str(newlista_cars[indice][2]))
        Temporada.insert(0, str(newlista_cars[indice][3]))
        Eficiencia.insert(0, str(newlista_cars[indice][4]))


        def new_changes():
            """Funcion que guarda los cambios efectuados"""
            global newlista_cars
            newlista_cars[indice] = [newlista_cars[indice][0], Marca.get(), Modelo.get(), Temporada.get(), Eficiencia.get()]
            with open('Cars.txt','w') as file:
                newlista = ('\n').join([(',').join(cars) for cars in newlista_cars])
                file.write(newlista)
            file.close()
            editar.destroy()
            update()


        btn_save = Button(Canvas_editar, text='Save', font=('Arial', 12), command=new_changes)
        btn_save.place(x=500, y=300)




    def ascendiente(newlista):
        leen = len(newlista)
        for i in range(leen):
            for j in range(leen-i-1):
                if (int(newlista[j][4])< int(newlista[j+1][4])):
                    tem = newlista[j]
                    newlista[j] = newlista[j+1]
                    newlista[j+1] = tem
        return newlista

    def descendiente(newlista):
        return newlista[::-1]


    def recorrer():
        """Lee el txt y lo convierte en una matriz"""
        global newlista_cars, ascendiente_cars
        with open('Cars.txt', 'r') as file:
            lista = file.read().split('\n')
            newlista = []
            count = 0
            while count<len(lista):
                newlista += [lista[count].split(',')]
                count +=1
        file.close()
        newlista_cars = ascendiente(newlista)
        if not ascendiente_cars:
            newlista_cars = descendiente(newlista)

    def crear_lambda(indice):
        return lambda: editar(indice)

    def cargar_botones(newlista_cars):
        global lista_cars

        lista_cars = [cargarImg(newlista_cars[0][0]),
                      cargarImg(newlista_cars[1][0]),
                      cargarImg(newlista_cars[2][0]),
                      cargarImg(newlista_cars[3][0]),
                      cargarImg(newlista_cars[4][0]),
                      cargarImg(newlista_cars[5][0]),
                      cargarImg(newlista_cars[6][0]),
                      cargarImg(newlista_cars[7][0]),
                      cargarImg(newlista_cars[8][0]),
                      cargarImg(newlista_cars[9][0])]

        indice = 0
        y = 70
        for i in range(10):
            funcion = crear_lambda(indice)
            Button(Canvas_cars, image=lista_cars[indice], command=funcion).place(x=200, y=y)
            y += 75
            indice += 1

    background = cargarImg('fondo_drivers.png')
    def cargar():
        """Funcion que elimina todos los elementos del canvas y los vuelve a implementar
        con los datos actualizados"""
        global newlista_carss

        Canvas_cars.delete('all')

        Canvas_cars.create_image(200,300, image= background)

        recorrer()

        cargar_botones(newlista_cars)


        Canvas_cars.create_text(420, 50, text='Marca', font=('Arial', 15, 'bold'), fill='Red')
        Canvas_cars.create_text(600, 50, text='Modelo', font=('Arial', 15, 'bold'), fill='Red')
        Canvas_cars.create_text(750, 50, text= 'Season', font=('Arial', 15, 'bold'), fill='Red')
        Canvas_cars.create_text(900, 50, text='Eficiciencia', font=('Arial', 15, 'bold'), fill='Red')

        Canvas_cars.create_text(420, 85, text=newlista_cars[0][1],font=('Arial',15,'bold'))
        Canvas_cars.create_text(420, 165, text=newlista_cars[1][1], font=('Arial',15,'bold'))
        Canvas_cars.create_text(420, 240, text=newlista_cars[2][1], font=('Arial',15,'bold'))
        Canvas_cars.create_text(420, 310, text=newlista_cars[3][1], font=('Arial',15,'bold'))
        Canvas_cars.create_text(420, 390, text=newlista_cars[4][1], font=('Arial',15,'bold'))
        Canvas_cars.create_text(420, 470, text=newlista_cars[5][1], font=('Arial',15,'bold'))
        Canvas_cars.create_text(420, 540, text=newlista_cars[6][1], font=('Arial',15,'bold'))
        Canvas_cars.create_text(420, 610, text=newlista_cars[7][1], font=('Arial',15,'bold'))
        Canvas_cars.create_text(420, 690, text=newlista_cars[8][1], font=('Arial',15,'bold'))
        Canvas_cars.create_text(420, 760, text=newlista_cars[9][1], font=('Arial',15,'bold'))

        Canvas_cars.create_text(600, 85, text=newlista_cars[0][2], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(600, 165, text=newlista_cars[1][2], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(600, 240, text=newlista_cars[2][2], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(600, 310, text=newlista_cars[3][2], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(600, 390, text=newlista_cars[4][2], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(600, 470, text=newlista_cars[5][2], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(600, 540, text=newlista_cars[6][2], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(600, 610, text=newlista_cars[7][2], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(600, 690, text=newlista_cars[8][2], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(600, 760, text=newlista_cars[9][2], font=('Arial', 15, 'bold'))

        Canvas_cars.create_text(750, 85, text=newlista_cars[0][3], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(750, 165, text=newlista_cars[1][3], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(750, 240, text=newlista_cars[2][3], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(750, 310, text=newlista_cars[3][3], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(750, 390, text=newlista_cars[4][3], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(750, 470, text=newlista_cars[5][3], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(750, 540, text=newlista_cars[6][3], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(750, 610, text=newlista_cars[7][3], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(750, 690, text=newlista_cars[8][3], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(750, 760, text=newlista_cars[9][3], font=('Arial', 15, 'bold'))

        Canvas_cars.create_text(900, 85, text=newlista_cars[0][4], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(900, 165, text=newlista_cars[1][4], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(900, 240, text=newlista_cars[2][4], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(900, 310, text=newlista_cars[3][4], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(900, 390, text=newlista_cars[4][4], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(900, 470, text=newlista_cars[5][4], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(900, 540, text=newlista_cars[6][4], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(900, 610, text=newlista_cars[7][4], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(900, 690, text=newlista_cars[8][4], font=('Arial', 15, 'bold'))
        Canvas_cars.create_text(900, 760, text=newlista_cars[9][4], font=('Arial', 15, 'bold'))


    cargar()


    def ascendiente_():
        global ascendiente_cars, descendiente_cars
        if ascendiente_cars:
            descendiente_cars = False
            cargar()
        else:
            ascendiente_cars = True
            descendiente_cars = False
            cargar()

    def descendiente_():
        global ascendiente_cars, descendiente_cars
        if descendiente_cars:
            ascendiente_cars = False
            cargar()
        else:
            descendiente_cars = True
            ascendiente_cars = False
            cargar()



    btn_ascendiente = Button(Canvas_cars ,text='Ascendiente', font=('Arial',15), command= ascendiente_)
    btn_ascendiente.place(x=20, y=300)

    btn_ascendiente = Button(Canvas_cars, text='Descendiente', font=('Arial', 15), command=descendiente_)
    btn_ascendiente.place(x=20, y=500)



    def back():
        cars.withdraw()
        drivers_cars_window()

    btn_back = Button(Canvas_cars, text='Back', font=('Arial', 15), command=back)
    btn_back.place(x=20, y=700)

    cars.mainloop()


def drivers_cars_window():
    """Pantalla que permite elegir cual de las tablas de posiciones desea ver"""
    root.withdraw()
    driverscars = Toplevel()
    driverscars.minsize(1000, 500)
    driverscars.resizable(width=NO, height=NO)
    driverscars.title('Drivers and Cars')

    Canvas_drivers_cars = Canvas(driverscars, width=1000, height=500, bg='light blue')
    Canvas_drivers_cars.place(x=0, y=0)

    background_drivers_cars = cargarImg('fondo_drivers_cars.png')
    Canvas_drivers_cars.create_image(500, 285, image=background_drivers_cars)

    drivers_image = cargarImg('formula1_driver.png')
    cars_image = cargarImg("formula1_car.png")

    Canvas_drivers_cars.create_text(730, 90, text='Drivers', font=('Magneto', 30), fill='#FFFFFF')
    Canvas_drivers_cars.create_text(250, 90, text='Cars', font=('Magneto', 30), fill='#FFFFFF')

    def start_drivers():
        driverscars.withdraw()
        drivers_window()

    def start_cars():
        driverscars.withdraw()
        cars_window()

    def back():
        driverscars.withdraw()
        root.deiconify()

    btn_back = Button(Canvas_drivers_cars, text='Back', font=('Arial', 15, 'bold'), command=back)
    btn_back.place(x=50, y=425)

    btn_cars = Button(Canvas_drivers_cars, image=cars_image, command=start_cars)
    btn_cars.place(x=50, y=125)

    btn_drivers = Button(Canvas_drivers_cars, image=drivers_image, command=start_drivers)
    btn_drivers.place(x=550, y=125)

    driverscars.mainloop()


def about():
    """Pnatalla que muestra informacion acerca del proyecto"""
    root.withdraw()
    about = Toplevel()
    about.minsize(1000, 500)
    about.resizable(width=NO, height=NO)
    about.title('About')

    Canvas_about = Canvas(about, width=1000, heigh=500, bg='red')
    Canvas_about.place(x=0, y=0)

    fondo_about = cargarImg('fondo_about.png')
    foto_Sebastián = cargarImg('foto_sebastián.png')

    Canvas_about.create_image(300, 150, image=fondo_about)
    Canvas_about.create_image(460, 150, image=foto_Sebastián)

    Canvas_about.create_text(780, 230, text=about_text, font=('Arial', 13, 'bold'), justify=CENTER)

    def back():
        about.withdraw()
        root.deiconify()

    btn_back = Button(Canvas_about, text="Back", font=('Arial', 15, 'bold'), bg='#EB1515', command=back)
    btn_back.place(x=50, y=400)

    about.mainloop()


def choose():
    """Pantalla que permite elegir el piloto y el auto a mostrar en el test drive"""
    root.withdraw()
    choose = Toplevel()
    choose.minsize(1000, 600)
    choose.resizable(width=NO, height=NO)
    choose.title('Choose')

    Canvas_choose = Canvas(choose, width=1000, height=600, bg='light blue')
    Canvas_choose.place(x=0, y=0)

    fondo = cargarImg('Fondo_choose.png')
    Canvas_choose.create_image(500, 300, image=fondo)

    def Driver(Type):
        global Driver1, Driver2
        if Type:
            Driver1 = True
            Driver2 = False
        else:
            Driver2 = True
            Driver1 = False

    def Car(Type):
        global Car1, Car2
        if Type:
            Car1 = True
            Car2 = False
        else:
            Car2 = True
            Car1 = False

    Canvas_choose.create_text(500, 50, text='Choose your driver', font=('Magneto', 25), fill='#000000')
    Canvas_choose.create_text(500, 350, text='Choose your car', font=('Magneto', 25), fill='#000000')
    Driver1_image = cargarImg('Hamilton.png')
    btn_driver1 = Button(Canvas_choose, image=Driver1_image, command=lambda: Driver(True))
    btn_driver1.place(x=250, y=100)

    Driver2_image = cargarImg('Charles.png')
    btn_driver2 = Button(Canvas_choose, image=Driver2_image, command=lambda: Driver(False))
    btn_driver2.place(x=630, y=100)

    Car1_image = cargarImg('Car1.png')
    btn_car1 = Button(Canvas_choose, image=Car1_image, command=lambda: Car(True))
    btn_car1.place(x=220, y=400)

    Car2_image = cargarImg('Car2.png')
    btn_car2 = Button(Canvas_choose, image=Car2_image, command=lambda: Car(False))
    btn_car2.place(x=600, y=400)

    def start():
        if (Driver1 or Driver2) and (Car1 or Car2):
            choose.withdraw()
            test_driver()
        else:
            messagebox.showinfo('Vuelve a elegir', 'Debes elegir tanto un vehículo como un piloto para continuar')

    btn_start = Button(Canvas_choose, text='Start', font=('Magneto', 15), relief='sunken', command=start)
    btn_start.place(x=900, y=500)

    def back():
        global Car1, Car2, Driver1, Driver2
        Car1, Car2, Driver1, Driver2 = False, False, False, False
        choose.withdraw()
        root.deiconify()

    btn_back = Button(Canvas_choose, text='Back', font=('Magneto', 15), relief='sunken', command=back)
    btn_back.place(x=30, y=500)

    choose.mainloop()


def command_display():
    """Funcion que abre una pantalla donde se puede elegir entre los diferentes
    comandos disponibles"""
    command = Toplevel()
    command.minsize(500, 500)
    command.resizable(width=NO, height=NO)
    command.title('Commands')

    Canvas_commands = Canvas(command, width=500, height=500)
    Canvas_commands.place(x=0, y=0)

    background = cargarImg('background_command.png')

    Canvas_commands.create_image(300, 400, image=background)
    Canvas_commands.create_text(250, 50, text="Commands", font=('Magneto', 20))

    myCar = NodeMCU()
    myCar.start()

    def send_command(command):
        if command == 'Circle':
            myCar.send(command + ';')
        if command == 'ZigZag':
            myCar.send(command + ';')
        if command == 'Infinite':
            myCar.send(command + ';')
        if command == 'Especial':
            myCar.send(command + ';')

    def back():
        command.withdraw()

    btn_back = Button(Canvas_commands, text='Back', font=('Magneto', 15), command=back)
    btn_back.place(x=20, y=400)

    btn_circle = Button(Canvas_commands, text='Circle', font=('Magneto', 15), relief='sunken', borderwidth=3, command=lambda: send_command('Circle'))
    btn_circle.place(x=80, y=120)

    btn_zigzag = Button(Canvas_commands, text='ZigZag', font=('Magneto', 15), relief='sunken', borderwidth=3, command=lambda: send_command('ZigZag'))
    btn_zigzag.place(x=278, y=120)


    btn_infinite = Button(Canvas_commands, text='Infnite', font=('Magneto', 15), relief='sunken', borderwidth=3, command=lambda: send_command('Infinite'))
    btn_infinite.place(x=70, y=230)

    btn_especial = Button(Canvas_commands, text='Especial', font=('Magneto', 15),relief='sunken', borderwidth=3, command=lambda: send_command('Especial'))
    btn_especial.place(x=270, y=230)



    command.mainloop()


#### Ventana del test driver###
def test_driver():
    off()
    cargar_cancion('test_song2.wav')
    test = Toplevel()
    test.minsize(1200, 700)
    test.resizable(width=NO, height=NO)
    test.title('Test Driver')

    Canvas_test = Canvas(test, width=1200, heigh=700, bg="light blue")
    Canvas_test.place(x=0, y=0)

    fondo = cargarImg('fondo_carro.png')
    Canvas_test.create_image(600, 350, image=fondo)

    ### Imagenes para la interfaz###
    Car = cargarImg('Car.png')
    Wheel_right = cargarImg('wheel_right.png')
    Wheel_right2 = cargarImg('wheel_right2.png')
    Wheel_left = cargarImg('wheel_left.png')
    Wheel_left2 = cargarImg('wheel_left2.png')

    front_lights = cargarImg('front_lights.png')
    back_lights = cargarImg('back_lights.png')
    blink_lights = cargarImg('blink.png')

    velocimetro = cargarImg('velocimetro.png')
    aguja1 = cargarImg('aguja_0.png')
    aguja2 = cargarImg('aguja_10.png')
    aguja3 = cargarImg('aguja_20.png')
    aguja4 = cargarImg('aguja_30.png')
    aguja5 = cargarImg('aguja_40.png')
    aguja6 = cargarImg('aguja_50.png')
    aguja7 = cargarImg('aguja_60.png')
    aguja8 = cargarImg('aguja_70.png')
    aguja9 = cargarImg('aguja_80.png')
    aguja10 = cargarImg('aguja_90.png')
    aguja11 = cargarImg('aguja_100.png')
    aguja12 = cargarImg('aguja_110.png')
    aguja13 = cargarImg('aguja_120.png')
    aguja14 = cargarImg('aguja_130.png')
    aguja15 = cargarImg('aguja_140.png')
    aguja16 = cargarImg('aguja_150.png')
    aguja17 = cargarImg('aguja_160.png')

    moon_brightless = cargarImg('moon_brightless.png')
    moon_bright = cargarImg('moon_bright.png')

    sun_brightless = cargarImg('sun_bright2.png')
    sun_bright = cargarImg('sun_bright.png')

    driver1 = cargarImg('Hamilton_.png')
    driver2 = cargarImg('Charles_.png')

    car1 = cargarImg('Car1_.png')
    car2 = cargarImg('Car2_.png')
    tabla = cargarImg('Tabla.png')

    ## Imagenes del carro con los diferentes comandos existentes ##
    Canvas_test.create_image(150, 200, image=Car, tags=['No_commands', 'Car'], state=NORMAL)
    Canvas_test.create_image(183, 80, image=Wheel_right, tags=['wheel_right'], state=HIDDEN)
    Canvas_test.create_image(45, 115, image=Wheel_right2, tags=['wheel_right'], state=HIDDEN)
    Canvas_test.create_image(43, 80, image=Wheel_left, tags=['wheel_left'], state=HIDDEN)
    Canvas_test.create_image(183, 115, image=Wheel_left2, tags=['wheel_left'], state=HIDDEN)
    Canvas_test.create_image(160, 60, image=front_lights, tags=['front_lights'], state=HIDDEN)
    Canvas_test.create_image(66, 60, image=front_lights, tags=['front_lights'], state=HIDDEN)
    Canvas_test.create_image(160, 300, image=back_lights, tags=['back_lights'], state=HIDDEN)
    Canvas_test.create_image(66, 300, image=back_lights, tags=['back_lights'], state=HIDDEN)
    Canvas_test.create_image(160, 50, image=blink_lights, tags=['blink_right'], state=HIDDEN)
    Canvas_test.create_image(66, 50, image=blink_lights, tags=['blink_left'], state=HIDDEN)

    Canvas_test.create_image(1000, 125, image=velocimetro, state=NORMAL)

    ### Agujas del velocimetro ##
    Canvas_test.create_image(940, 200, image=aguja1, tags=['Aguja0', 'Out'], state=NORMAL)  # 0
    Canvas_test.create_image(996, 130, image=aguja2, tags=['Aguja10', 'Out'], state=HIDDEN)  # 10
    Canvas_test.create_image(998, 125, image=aguja3, tags=['Aguja20', 'Out'], state=HIDDEN)  # 20
    Canvas_test.create_image(1005, 117, image=aguja4, tags=['Aguja30', 'Out'], state=HIDDEN)  # 30
    Canvas_test.create_image(1000, 125, image=aguja5, tags=['Aguja40', 'Out'], state=HIDDEN)  # 40
    Canvas_test.create_image(1004, 127, image=aguja6, tags=['Aguja50', 'Out'], state=HIDDEN)  # 50
    Canvas_test.create_image(1005, 123, image=aguja7, tags=['Aguja60', 'Out'], state=HIDDEN)  # 60
    Canvas_test.create_image(1012, 125, image=aguja8, tags=['Aguja70', 'Out'], state=HIDDEN)  # 70
    Canvas_test.create_image(1005, 135, image=aguja9, tags=['Aguja80', 'Out'], state=HIDDEN)  # 80
    Canvas_test.create_image(998, 125, image=aguja10, tags=['Aguja90', 'Out'], state=HIDDEN)  # 90
    Canvas_test.create_image(1005, 123, image=aguja11, tags=['Aguja100', 'Out'], state=HIDDEN)  # 100
    Canvas_test.create_image(1004, 123, image=aguja12, tags=['Aguja110', 'Out'], state=HIDDEN)  # 110
    Canvas_test.create_image(1005, 125, image=aguja13, tags=['Aguja120', 'Out'], state=HIDDEN)  # 120
    Canvas_test.create_image(1010, 112, image=aguja14, tags=['Aguja130', 'Out'], state=HIDDEN)  # 130
    Canvas_test.create_image(1010, 120, image=aguja15, tags=['Aguja140', 'Out'], state=HIDDEN)  # 140
    Canvas_test.create_image(1015, 130, image=aguja16, tags=['Aguja150', 'Out'], state=HIDDEN)  # 150
    Canvas_test.create_image(1070, 200, image=aguja17, tags=['Aguja160', 'Out'], state=HIDDEN)  # 160

    ## Imagenes que indican si en el ambiente se encuentra de dia o de noche ##
    Canvas_test.create_image(820, 95, image=moon_brightless, tags=['no_bright'], state=NORMAL)
    Canvas_test.create_image(820, 95, image=moon_bright, tags=['bright'], state=HIDDEN)

    Canvas_test.create_image(817, 180, image=sun_brightless, tags=['sun_brightless'], state=NORMAL)
    Canvas_test.create_image(817, 180, image=sun_bright, tags=['sun_bright'], state=HIDDEN)

    # Imagenes del personaje y vehículos elejidos
    Canvas_test.create_image(1000, 600, image=tabla)
    Canvas_test.create_image(883, 600, image=driver1, tags=['Hamilton', 'Drivers'], state=HIDDEN)
    Canvas_test.create_image(883, 600, image=driver2, tags=['Charles', 'Drivers'], state=HIDDEN)

    Canvas_test.create_image(1053, 600, image=car1, tags=['Car1', 'Cars'], state=HIDDEN)
    Canvas_test.create_image(1054, 601, image=car2, tags=['Car2', 'Cars'], state=HIDDEN)

    ## Llamado del thread del WI-Fi cliente que permite enviar los comandos desde este archivo.
    myCar = NodeMCU()
    myCar.start()

    ############ Funciones para la potencia del motor###############
    global power, press_forward, press_back, DirRight, DirLeft, blink_press, moving, flag_blink_left, flag_blink_right, front, back, blink
    power = 0
    press_forward = True
    press_back = True
    DirRight = True
    DirLeft = True
    blink_press = True
    moving = True
    flag_blink_left = True
    flag_blink_right = True
    front = True
    blink = True

    def insert_character():
        global Car1, Car2, Driver1, Driver2
        if Driver1:
            Canvas_test.itemconfig('Hamilton', state=NORMAL)
        if Driver2:
            Canvas_test.itemconfig('Charles', state=NORMAL)
        if Car1:
            Canvas_test.itemconfig('Car1', state=NORMAL)
        if Car2:
            Canvas_test.itemconfig('Car2', state=NORMAL)

    insert_character()

    ### Progessbar ##
    def llenar():
        global power
        velocidad = power
        if velocidad >= 800:
            velocidad = 1000
        pwm['value'] = velocidad // 10

    color_pwm = ttk.Style()
    color_pwm.theme_use('clam')
    color_pwm.configure('red.Vertical.TProgressbar', background='red', foreground='red')
    pwm = ttk.Progressbar(Canvas_test, style='red.Vertical.TProgressbar', length=200, orient=VERTICAL)
    pwm.place(x=1150, y=20)

    ###########  Velocimetro ##################
    def velocimetro2():
        global power
        if power == 0:
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja0', state=NORMAL)
        if (power < 800):
            Canvas_test.itemconfig('Aguja160', state=HIDDEN)
        if (power == 100):
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja10', state=NORMAL)
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja20', state=NORMAL)
            time.sleep(0.0009)
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja30', state=NORMAL)
        if (power == 200):
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja40', state=NORMAL)
            time.sleep(0.0009)
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja50', state=NORMAL)
        if (power == 300):
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja60', state=NORMAL)
            time.sleep(0.0009)
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja70', state=NORMAL)
        if (power == 400):
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja80', state=NORMAL)
            time.sleep(0.0009)
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja90', state=NORMAL)
        if (power == 500):
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja100', state=NORMAL)
            time.sleep(0.0009)
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja110', state=NORMAL)
        if (power == 600):
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja120', state=NORMAL)
            time.sleep(0.0009)
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja130', state=NORMAL)
        if (power == 700):
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja140', state=NORMAL)
            time.sleep(0.0009)
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja150', state=NORMAL)
        if (power >= 800):
            Canvas_test.itemconfig('Out', state=HIDDEN)
            Canvas_test.itemconfig('Aguja160', state=NORMAL)

    def sense():
        # Funcion obtenida del TelemetryLog para obtener el comando enviado
        indice = 0
        myCar.loop = True
        while (myCar.loop):
            print('Entra')
            myCar.send('sense;')
            while (indice < len(myCar.log)):
                mnsSend = myCar.log[indice][1][-3]
                if (mnsSend == "1" or "0"):
                    print(mnsSend)
                    sense_screen(mnsSend)
                indice += 1
            time.sleep(25)

    def sense_screen(luminosidad):
        if luminosidad == "1":
            print('luz')
            Canvas_test.itemconfig('bright', state=HIDDEN)
            Canvas_test.itemconfig('no_bright', state=NORMAL)
            Canvas_test.itemconfig('sun_brightless', state=HIDDEN)
            Canvas_test.itemconfig('sun_bright', state=NORMAL)
        else:
            print('No hay luz')
            Canvas_test.itemconfig('sun_brightless', state=NORMAL)
            Canvas_test.itemconfig('sun_bright', state=HIDDEN)
            Canvas_test.itemconfig('no_bright', state=HIDDEN)
            Canvas_test.itemconfig('bright', state=NORMAL)

    """Inicio de thread para el comando sense"""

    sense_thread = threading.Thread(target=sense)
    sense_thread.start()

    ############# Potencia del motor #################

    def WS_press(event):
        """Funcion que reconoce la tecla que está siendo presionada para llamar al thread correspondiente"""
        global moving, press_forward, press_back
        key = event.char
        if (key == "w"):
            if not (moving):
                return
            else:
                moving = False
                press_forward = True
                aceleration_forward = threading.Thread(target=forward_increase)
                aceleration_forward.start()
        if (key == "s"):
            if not (moving):
                return
            else:
                moving = False
                press_back = True
                aceleration_back = threading.Thread(target=back_increase)
                aceleration_back.start()
        else:
            return

    test.bind("<KeyPress-w>", WS_press)
    test.bind("<KeyPress-s>", WS_press)

    def forward_increase():
        # Funcion que incrementa la velocidad del motor
        global power, press_forward, press_back
        print("Adelante")
        while (power <= 900 and press_forward):
            power += 100
            print(power)
            message = "pwm:" + str(power) + ";"
            myCar.send(message)
            velocimetro2()
            llenar()
            time.sleep(0.200)

    def back_increase():
        # Funcion que aumenta la potencia del motor en reversa
        global power, press_back
        print('Atras')
        press_back = True
        Canvas_test.itemconfig('back_lights', state=NORMAL)
        while (power <= 900 and press_back):
            power += 100
            message = "pwm:" + "-" + str(power) + ";"
            print(power)
            myCar.send(message)
            velocimetro2()
            llenar()
            time.sleep(0.200)

    def WS_release(event):
        """Funcnion que reconoce la tecla que dejó de ser presionada para llamar al thread correspondiente"""
        global press_forward, press_back, moving, moving
        key = event.char
        if key == 'w':
            if moving:
                return
            else:
                moving = True
                press_forward = False
                deceleration_forward = threading.Thread(target=forward_decrease)
                deceleration_forward.start()
        if key == "s":
            if moving:
                print('Entra')
                return
            else:
                moving = True
                press_back = False
                deceleration_back = threading.Thread(target=back_decrease)
                deceleration_back.start()
        else:
            return

    test.bind("<KeyRelease-w>", WS_release)
    test.bind('<KeyRelease-s>', WS_release)

    def forward_decrease():
        # Funcion que disminuye la potencia del motor
        global power, press_forward
        while (power != 0 and not press_forward):
            power -= 100
            print(power)
            message = "pwm:" + str(power) + ";"
            myCar.send(message)
            velocimetro2()
            llenar()
            time.sleep(0.200)

    def back_decrease():
        # Funcion que disminuye la potencia del motor en reversa
        global power, press_back
        while (power != 0 and not press_back):
            power -= 100
            print(power)
            message = "pwm:" + "-" + str(power) + ";"
            myCar.send(message)
            velocimetro2()
            llenar()
            time.sleep(0.200)
        else:
            myCar.send("pwm:0;")
            Canvas_test.itemconfig('back_lights', state=HIDDEN)

    ############  Dirección del motor #########################

    def direction_left(event):
        # Funcion que realiza la accion de girar hacia la izquierda
        global DirLeft, DirRight
        if (DirLeft and DirRight):
            Canvas_test.itemconfig('wheel_left', state=NORMAL)
            myCar.send("dir:-1;")
            print("left")
            DirLeft = False

    def direction_right(event):
        # Funcion que realiza la accion de girar hacia la derecha
        global DirRight, DirLeft
        if (DirRight and DirLeft):
            Canvas_test.itemconfig('wheel_right', state=NORMAL)
            myCar.send("dir:1;")
            print("right")
            DirRight = False

    def direction_straight(event):
        # Funcion que una vez se deja de presionar alguna de las teclas de direccion, vuelva a la posicion 0
        global DirRight, DirLeft
        key = event.char
        if (key == "a" and DirRight):
            DirLeft = True
            Canvas_test.itemconfig('wheel_left', state=HIDDEN)
            myCar.send('dir:0;')
        if (key == "d" and DirLeft):
            DirRight = True
            Canvas_test.itemconfig('wheel_right', state=HIDDEN)
            myCar.send('dir:0;')

    test.bind("<KeyPress-a>", direction_left)
    test.bind("<KeyPress-d>", direction_right)
    test.bind("<KeyRelease-a>", direction_straight)
    test.bind("<KeyRelease-d>", direction_straight)

    #############  Luces frontales, reversa e interminentes ###############

    def lights_front(event):
        # Funcion que enciende las luces de adelante
        global front
        if (front):
            Canvas_test.itemconfig('front_lights', state=NORMAL)
            message = "lf:1;"
            myCar.send(message)
            time.sleep(0.5)
            front = False
        else:
            Canvas_test.itemconfig('front_lights', state=HIDDEN)
            message = "lf:0;"
            myCar.send(message)
            time.sleep(0.5)
            front = True

    test.bind("f", lights_front)

    def Blinking(Command, name):
        # Funcion que enciende las intermitentes de la izquierda
        global blink
        lights_on = True
        print(name)
        while (blink):
            if (lights_on):
                Canvas_test.itemconfig(name, state=NORMAL)
                message = str(Command) + ":1;"
                myCar.send(message)
                time.sleep(0.5)
                lights_on = False
                print("on")
            else:
                Canvas_test.itemconfig(name, state=HIDDEN)
                message = str(Command) + ':0;'
                myCar.send(message)
                time.sleep(0.5)
                lights_on = True
                print("off")

    def lights(event):
        # Funcion que permite iniciarlos thread de las funciones de los intermitentes
        global blink_press, blink, flag_blink_left, flag_blink_right
        key = event.char
        print(key)
        print(flag_blink_right)
        if (key == "q" and flag_blink_left):
            if blink_press:
                print('light left on')
                blink_left = threading.Thread(target=Blinking, args=['ll', 'blink_left'])
                blink_left.start()
                blink = True
                blink_press = False
                flag_blink_right = False
            else:
                print('light left off')
                myCar.send('ll:0;')
                Canvas_test.itemconfig('blink_left', state=HIDDEN)
                blink = False
                blink_press = True
                flag_blink_right = True
        elif (key == "e" and flag_blink_right):
            if blink_press:
                print("light right on")
                blink_right = threading.Thread(target=Blinking, args=['lr', 'blink_right'])
                blink_right.start()
                blink = True
                blink_press = False
                flag_blink_left = False
            else:
                print("light right off")
                myCar.send('lr:0;')
                Canvas_test.itemconfig('blink_right', state=HIDDEN)
                blink = False
                blink_press = True
                flag_blink_left = True
        else:
            print("A blinking light is already on")

    Canvas_test.create_image(1000, 370, tags='Escuderia')

    def change_escuderia():
        global audi_logo, mercedes_logo, bwm_logo
        if audi_logo:
            Canvas_test.itemconfig('Escuderia', image=audi_logo_)
        if mercedes_logo:
            Canvas_test.itemconfig('Escuderia', image=mercedes_logo_)
        if bmw_logo:
            Canvas_test.itemconfig('Escuderia', image=bmw_logo_)

    change_escuderia()



    def celebration():
        global Driver1, Driver2
        if Driver1:
            myCar.send('Celebration1;')
        if Driver2:
            myCar.send('Celebration2;')

    test.bind('q', lights)
    test.bind('e', lights)

    def commands():
        command_display()

    def volver_menu():
        global Car1, Car2, Driver1, Driver2
        Car1, Car2, Driver1, Driver2 = False, False, False, False
        myCar.loop = False
        off()
        cargar_cancion('menu_song.wav')
        test.withdraw()
        root.deiconify()

    btn_back = Button(Canvas_test, text='Back', font=('Magneto', 15), fg='#000000', relief='sunken',
                      command=volver_menu, width=5)
    btn_back.place(x=50, y=600)

    btn_commands = Button(Canvas_test, text='Commands', font=('Magneto', 16), relief='sunken', command=commands)
    btn_commands.place(x=1020, y=470)

    btn_celebration = Button(Canvas_test, text='Celebration', font=('Magneto', 16), relief='sunken', command=celebration)
    btn_celebration.place(x=830, y=470)

    test.mainloop()


def quit_menu():
    global logo_running
    logo_running = False
    root.destroy()
    off()


btn_test_driver = Button(Canvas_menu, image=image_test, bg='black', fg='black', command=choose)
btn_test_driver.place(x=79, y=177)

btn_about = Button(Canvas_menu, image=image_about, bg='black', fg='black', command=about)
btn_about.place(x=483, y=177)

btn_drivers_cars = Button(Canvas_menu, image=image_drivers, bg='black', fg='black', command=drivers_cars_window)
btn_drivers_cars.place(x=772, y=177)

btn_drivers = Button(Canvas_menu, image=image_quit, bg='black', fg='black', command=quit_menu)
btn_drivers.place(x=1066, y=177)

btn_logo = Button(Canvas_menu, text='', font=('Magneto', 15, 'bold'), bg='#2B5438', fg='white', command=lambda:change_logo(''))
btn_logo.place(x=870, y=110)


root.mainloop()
