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

global Driver1, Driver2, Car1, Car2
Driver1, Driver2, Car1, Car2 = False, False, False, False

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
    return
    # Funcion para cargar canciones del juego
    winsound.PlaySound(Nombre, winsound.SND_ASYNC + winsound.SND_LOOP)


def off():
    # Funcion que apaga la cancion una vez que entre a cualquiera de las demas pantallas
    winsound.PlaySound(None, winsound.SND_ASYNC + winsound.SND_LOOP)


cargar_cancion('menu_song.wav')


def drivers_window():
    drivers = Toplevel()
    drivers.minsize(1500, 800)
    drivers.resizable(width=NO, height=NO)
    drivers.title('Drivers')

    Canvas_drivers = Canvas(drivers, width=1500, height=800, bg='light blue')
    Canvas_drivers.place(x=0, y=0)


    hamilton = cargarImg('Hamilton_png')





    def recorrer():
        with open('Drivers.txt', 'r') as file:
            lista = file.read().split('\n')
            newlista = []
            count = 0
            while count < len(lista):
                newlista += [lista[count].split(',')]
                count += 1
            file.close()
            return newlista


    print(recorrer())

    newlista = recorrer()





    def back():
        drivers.withdraw()
        drivers_cars_window()

    btn_back = Button(Canvas_drivers, text='Back', command=back)
    btn_back.place(x=500, y=500)

    drivers.mainloop()


def cars_window():
    cars = Toplevel()
    cars.minsize(1500, 800)
    cars.resizable(width=NO, height=NO)
    cars.title('Cars')

    Canvas_cars = Canvas(cars, width=1500, height=800, bg='light blue')
    Canvas_cars.place(x=0, y=0)

    def back():
        cars.withdraw()
        drivers_cars_window()

    btn_back = Button(Canvas_cars, text='Back', command=back)
    btn_back.place(x=500, y=500)

    cars.mainloop()


def drivers_cars_window():
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
        test_driver()

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
            time.sleep(10)

    def sense_screen(luminosidad):
        if luminosidad == "1":
            print('luz')
            myCar.send('lf:0;')
            Canvas_test.itemconfig('bright', state=HIDDEN)
            Canvas_test.itemconfig('no_bright', state=NORMAL)
            Canvas_test.itemconfig('sun_brightless', state=HIDDEN)
            Canvas_test.itemconfig('sun_bright', state=NORMAL)
        else:
            print('No hay luz')
            myCar.send('lf:1;')
            Canvas_test.itemconfig('sun_brightless', state=NORMAL)
            Canvas_test.itemconfig('sun_bright', state=HIDDEN)
            Canvas_test.itemconfig('no_bright', state=HIDDEN)
            Canvas_test.itemconfig('bright', state=NORMAL)

    """Inicio de thread para el comando sense"""

    # sense_thread = threading.Thread(target=sense)
    # sense_thread.start()

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


    def celebration():
        global Driver1, Driver2
        if Driver1:
            myCar.send('Celebration1;')
        if Driver2:
            myCar.send('Celebration2;')

    test.bind('q', lights)
    test.bind('e', lights)

    def commands():
        test.destroy()
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

root.mainloop()
