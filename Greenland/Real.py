global loading
loading = ""
global user_choice
user_choice = ""
global user_choice2
user_choice2 = ""
global user_choice3
user_choice3 = ""
global user_choice4
user_choice4 = ""
global user_choice5
user_choice5 = ""
global password
password = ""
#ability
global health
health = 100
global energy
energy = 100
luck = 50
#inventory
global key1
key1 = 0
global key2
key2 = 0
global meat
meat = 0
global axe
axe = 0
global knife
knife = 0
global cereal_bar
cereal_bar = 0
global pass_code1
pass_code1 = 0
global photo_1
photo_1 = 0
global book_1
book_1 = 0
global sexyphoto1
sexyphoto1 = 0
global photo_2
photo_2 = 0
global broken_tangerine
broken_tangerine = 0
global rag
rag = 0
global wet_rag
wet_rag = 0
global book_2
book_2 = 0
global gun
gun = 0
global ammo
ammo = 0
global key3
key3 = 0
global photo_3
photo_3 = 0
global paper1
paper1 = 0
global key4
key4 = 0
global photo_4
photo_4 = 0
global paper3
paper3 = 0
#Door
global ik_door
ik_door = 0
global ik_door1
ik_door1 = 0
global ik_door2
ik_door2 = 0
global ik_door3
ik_door3 = 0
global ik_door4
ik_door4 = 0
global ik_door5
ik_door5 = 0
#gg's
global gg1
gg1 = 0
global gg2
gg2 = 0
global gg3
gg3 = 0
global gg4
gg4 = 0
global gg5
gg5 = 0
global gg6
gg6 = 0
global gg7
gg7 = 0
global gg8
gg8 = 0
global gg9
gg9 = 0
global gg10
gg10 = 0
global gg11
gg11 = 0
global gg12
gg12 = 0
global gg13
gg13 = 0
global gg14
gg14 = 0
global gg15
gg15 = 0
global gg16
gg16 = 0
global gg17
gg17 = 0
global gg18
gg18 = 0
global gg19
gg19 = 0
#feature
global ik_feature
ik_feature = 0
#colors
#import os
#os.system("")
#input("\u001b[33m ahoj")

#interactible items
def end():
    devide()
    import time
    time.sleep(3)
    print(">>Máš 0 životu<<")
    file_book2 = open("Features/Core/End.txt")
    print(file_book2.read())
    file_book2.close
    input("")
    import os
    os._exit(0)
def final():
    devide()
    import time
    time.sleep(3)
    print("Otevřel jsi dveře")
    import time
    time.sleep(3)
    print("Byl jsi venku")
    import time
    time.sleep(3)
    print("Najednou se k tobě přibliží nějakej můž")
    import time
    time.sleep(3)
    print("Cizí můž: Měl jsi tam zůstat blbečku!")
    import time
    time.sleep(3)
    print("Vytahl nůž a nachystal se tě pobodnout")
    if gun == 1:
        import time
        time.sleep(3)
        print("Ale ty jsi rychle vytahl zbraň")
        if ammo > 0:
            import random
            item_list = [1,2,3,4]
            bang = random.choice(item_list)
            while ammo > 0:
                import time
                time.sleep(2)
                print("Střilel jsi")
                import time
                time.sleep(3)
                print("*bang!")
                if bang == 1 or 2:
                    devide()
                    import time
                    time.sleep(3)
                    print("Zastřilel jsi ho")
                    import time
                    time.sleep(3)
                    print("Cizí můž umřel")
                    import time
                    time.sleep(3)
                    print("Prohledal sis ho ale nic jsi nenašel")
                    import time
                    time.sleep(3)
                    print("Podival ses kolem sebe")
                    import time
                    time.sleep(3)
                    print("Viděl jsi v dálce kouř")
                    import time
                    time.sleep(3)
                    devide()
                    file_book2 = open("Features/Core/Real end.txt")
                    print(file_book2.read())
                    file_book2.close
                    input(">>")
                    workers()
                if bang == 3 or 4:
                    devide()
                    import time
                    time.sleep(3)
                    print("On uhnul")
            if ammo == 0:
                import time
                time.sleep(3)
                print("Pobodal tě")
                import time
                time.sleep(3)
                print("Cizí můž: Skončiš stejně jako tvůj kamarad!")
                import time
                time.sleep(3)
                print("Cizí můž: Na pudě!")
                import time
                time.sleep(3)
                devide()
                file_book2 = open("Features/Core/Real end.txt")
                print(file_book2.read())
                file_book2.close
                input(">>")
                workers()
        if ammo == 0:
            import time
            time.sleep(3)
            print("Pobodal tě")
            import time
            time.sleep(3)
            print("Cizí můž: Skončiš stejně jako tvůj kamarad!")
            import time
            time.sleep(3)
            print("Cizí můž: Na pudě!")
            import time
            time.sleep(3)
            devide()
            file_book2 = open("Features/Core/Real end.txt")
            print(file_book2.read())
            file_book2.close
            input(">>")
            workers()
    if gun == 0:
        import time
        time.sleep(3)
        print("Pobodal tě")
        import time
        time.sleep(3)
        print("Cizí můž: Skončiš stejně jako tvůj kamarad!")
        import time
        time.sleep(3)
        print("Cizí můž: Na pudě!")
        import time
        time.sleep(3)
        devide()
        file_book2 = open("Features/Core/Real end.txt")
        print(file_book2.read())
        file_book2.close
        input(">>")
        workers()
def workers():
    devide()
    import time
    time.sleep(2)
    print(">>Pracovali na tom:<<")
    import time
    time.sleep(2)
    print("  Daniel Tarelunga")
    import time
    time.sleep(2)
    print("")
    import time
    time.sleep(2)
    print("\u001b[33m   _____                     _ _                 _ \n"
                        "  / ____|                   | | |               | |\n"
                        " | |  __ _ __ ___  ___ _ __ | | | __ _ _ __   __| |\n"
                        " | | |_ | '__/ _ \/ _ \ '_ \| | |/ _` | '_ \ / _` |\n"
                        " | |__| | | |  __/  __/ | | | | | (_| | | | | (_| |\n"
                        "  \_____|_|  \___|\___|_| |_|_|_|\__,_|_| |_|\__,_|\n"
                        ">>                      Konec                      <<")
    input(">>")
    import os
    os._exit(0)
def date():
    from datetime import date

    today = date.today()

    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    print("d1 =", d1)

#Room 1 ----------------------------------------------------------------------------------------------------------------
def passcode1():
    devide()
    file_book2 = open("Features/Passcode/Passcode 1.txt")
    print(file_book2.read())
    file_book2.close
    input(">>Stiskni jakoukoliv klavesu<<\n"
          ">>")
no7 = 0
def page2():
    global no7
    if user_choice4 == "d":
        if no7 == 0:
            devide()
            print(">>Tohle neni normalní kniha<<")
            import time
            time.sleep(2)
            print(">>Je v ní krabička ktera se otvira pomoci nějakeho kodu<<")
            import time
            time.sleep(2)
            devide()
            file_book2 = open("Features/Book 1/Book 2.txt")
            print(file_book2.read())
            file_book2.close
            password = input("Zadej kod:")
            from datetime import date
            today = date.today()
            #dd/mm/YY
            d1 = today.strftime("%d/%m/%Y")
            if password == d1:
                import time
                time.sleep(2)
                loading()
                import time
                time.sleep(2)
                loading()
                import time
                time.sleep(2)
                loading()
                import time
                time.sleep(2)
                print(">>Spravně<<")
                devide()
                import time
                time.sleep(2)
                print(">>Štěstí +10<<")
                global luck
                luck = luck + 10
                import time
                time.sleep(2)
                print(">>Klič 1 +1<<")
                global key1
                key1 = key1 + 1
                no7 = no7 + 1
                import time
                time.sleep(2)
            elif password != d1:
                import time
                time.sleep(2)
                loading()
                import time
                time.sleep(2)
                loading()
                import time
                time.sleep(2)
                loading()
                import time
                time.sleep(2)
                print(">>Špatně<<")
                devide()
                print(">>Štěstí -10<<")
                luck = luck - 10
                import time
                time.sleep(2)
        else:
            devide()
            print(">>Už jsi tady byl<<")
            import time
            time.sleep(2)
def book1():
    global user_choice4
    user_choice4 = ""
    #user_choice4 = input(">>")
    global password
    password = ""
    from datetime import date
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    while password != d1:
        import time
        time.sleep(2)
        devide()
        file_book1 = open("Features/Book 1/Book 1.txt")
        print(file_book1.read())
        file_book1.close()
        screen_book()
        user_choice4 = input(">>")
        if user_choice4 == "d":
            page2()
        elif user_choice4 == "a":
            devide()
            print(">>Tahle možnost je zatím nedostupna<<")
        elif user_choice4 == "s":
            password = d1
        if user_choice4 != "a":
            if user_choice4 != "s":
                if user_choice4 != "d":
                    devide()
                    print(">>Zadali jste špatnej znak<<")

def photo1():
    devide()
    file_book2 = open("Features/Photoes/Photo 1.txt")
    print(file_book2.read())
    file_book2.close
    input(">>Stiskni jakoukoliv klavesu<<\n"
          ">>")

def photo2():
    devide()
    file_book2 = open("Features/Photoes/Photo 2.txt")
    print(file_book2.read())
    file_book2.close
    input(">>Stiskni jakoukoliv klavesu<<\n"
          ">>")
def sexyphoto_1():
    devide()
    file_book2 = open("Features/Photoes/Secret/Wierd Photo 1.txt")
    print(file_book2.read())
    file_book2.close
    input(">>Stiskni jakykoukoliv klavesu<<\n"
          ">>")
def locker1():
    print("")
def bed1():
    user_choice2 = ""
    while user_choice2 != "b":
        devide()
        print(">>Postel<<")
        print("Možnosti:\n"
          "1) Polštař\n"
          "2) Peřina\n"
          "3) Pod postel\n"
          "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            pillow1()
            kill()
        elif user_choice2 == "2":
            blanket1()
            kill()
        elif user_choice2 == "3":
            underbed1()
            kill()
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "4":
            if user_choice2 != "b":
                if user_choice2 != "i":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadal jsi špatnej znak<<")
                    import time
                    time.sleep(2)
        if health <= 0:
            end()



def warderobe1():
    global user_choice5
    while user_choice5 != "b":
        devide()
        print(">>Skřiň<<")
        print("Možnosti:\n"
            "1) Polička č.1\n"
            "2) Polička č.2\n"
            "3) Šuplík č.1\n"
            "4) Šuplik č.2\n"
            "b) Zpatky\n")
        screen()
        user_choice5 = input(">>")
        if user_choice5 == "1":
            raft1()
            kill()
        elif user_choice5 == "2":
            raft2()
            kill()
        elif user_choice5 == "3":
            raft3()
            kill()
        elif user_choice5 == "4":
            raft4()
            kill()
        elif user_choice5 == "5":
            raft6()
            kill()
        elif user_choice5 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice5 > "6":
            if user_choice5 != "b":
                if user_choice5 != "i":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadal jsi špatnej znak<<")
                    import time
                    time.sleep(2)

        if health <= 0:
            end()



def table1():
    user_choice2 = ""
    while user_choice2 != "b":
        devide()
        print(">>Stůl<<")
        print("Možnosti:\n"
            "1) Na stůl\n"
            "2) Šuplík\n"
            "3) Pod stolem\n"
            "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            ontable()
            kill()
        elif user_choice2 == "2":
            drawer()
            kill()
        elif user_choice2 == "3":
            undertable1()
            kill()
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "4":
            if user_choice2 != "b":
                if user_choice2 != "i":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadal jsi špatnej znak<<")
                    import time
                    time.sleep(2)
        if health <= 0:
            end()

global no8
no8 = 0
def ontable():
    import time
    time.sleep(2)
    global no8
    if no8 == 0:
        devide()
        print("Fotka 2 +1")
        global photo_2
        photo_2 = photo_2 + 1
        no8 = no8 + 1
        import time
        time.sleep(2)
    elif no8 > 0:
        devide()
        import time
        time.sleep(2)
        print(">>Už jsi tady byl<<")
        import time
        time.sleep(2)

def drawer():
    devide()
    import time
    time.sleep(2)
    print(">>Tady nic není<<")
    import time
    time.sleep(2)

global no9
no9 = 0
def undertable1():
    global no9
    if no9 == 0:
        devide()
        import time
        time.sleep(2)
        print("Máso +1")
        global meat
        meat = meat + 1
        no9 = no9 + 1
        import time
        time.sleep(2)
    elif no9 > 0:
        devide()
        import time
        time.sleep(2)
        print(">>Už jsi tady byl<<")

def chest1():
    devide()
    import time
    time.sleep(2)
    print(">>Truhla<<")
    print(">>Papírek +1<<")
    global pass_code1
    pass_code1 = pass_code1 + 1
    import time
    time.sleep(2)
    kill()
    if health <= 0:
        end()

def pillow1():
    devide()
    print(">>Tady nic není<<")
    import time
    time.sleep(2)

no1 = 0
def blanket1():
    global no1
    if no1 == 0:
        devide()
        print("Tyčinka +1")
        global cereal_bar
        cereal_bar = cereal_bar + 1
        no1 = no1 + 1
        import time
        time.sleep(2)
    else:
        devide()
        print(">>Už jsi tady byl<<")
        import time
        time.sleep(2)

no3 = 0
def raft1():
    global no3
    if no3 == 0:
        devide()
        print("Nůž +1")
        global knife
        knife = knife + 1
        no3 = no3 + 1
        import time
        time.sleep(2)
    else:
        devide()
        print(">>Už jsi tady byl<<")
        import time
        time.sleep(2)

no4 = 0
def raft2():
    global no4
    if no4 == 0:
        devide()
        print("Tičinka +1")
        global cereal_bar
        cereal_bar = cereal_bar + 1
        no4 = no4 + 1
        import time
        time.sleep(2)
    else:
        devide()
        print(">>Už jsi tady byl<<")
        import time
        time.sleep(2)

def raft3():
    devide()
    print(">>Tady nic není<<")
    import time
    time.sleep(2)

no5 = 0
def raft4():
    global no5
    if no5 == 0:
        devide()
        print("Fotka + 1")
        global photo_1
        photo_1 = + 1
        no5 = no5 + 1
        import time
        time.sleep(2)
    else:
        devide()
        print(">>Už jsi tady byl<<")
        import time
        time.sleep(2)

no6 = 0
sexyphoto1 = 0
def raft6():
    global no6
    global sexyphoto1
    if no6 == 0:
        devide()
        import time
        time.sleep(2)
        print(">>Tajnej šuplík<<")
        import time
        time.sleep(2)
        print(">>Sexy fotka +1<<")
        import time
        time.sleep(2)
        print(">>Easter egg<<")
        import time
        time.sleep(2)
        print(">>Napiš 100 v inventaři<<")
        import time
        time.sleep(2)
        sexyphoto1 = sexyphoto1 + 1
        no6 = no6 + 1
        import time
        time.sleep(2)
    else:
        devide()
        print(">>Už jsi tady byl<<")
        import time
        time.sleep(2)

def door1():
    file_book2 = open("Features/Door/Passcode 1.txt")
    print(file_book2.read())
    file_book2.close
    devide()
    print(">>Napiš heslo:")

no2 = 0
def underbed1():
    global no2
    if no2 == 0:
        devide()
        print("Kniha1 +1")
        global book_1
        book_1 = + 1
        no2 = no2 + 1
        import time
        time.sleep(2)
    else:
        devide()
        print(">>Už jsi tady byl<<")
        import time
        time.sleep(2)

#Hall ------------------------------------------------------------------------------------------------------------------
def door2():
    if key2 == 0:
        devide()
        import time
        time.sleep(2)
        print(">>Nemaš klič 2<<")
        import time
        time.sleep(2)
    elif key2 == 1:
        room22()
def door3():
    global gg3
    if gg3 == 0:
        devide()
        import time
        time.sleep(2)
        print("Otevřel jsi dveře")
        import time
        time.sleep(2)
        print("Zjistil jsi že je to kuchyňě")
        import time
        time.sleep(2)
        gg3 = gg3 + 1
        kitchen1()
        global ik_door3
        ik_door3 = ik_door3 + 1
    elif gg3 == 1:
        kitchen1()
def roof2():
    if axe == 0:
        devide()
        import time
        time.sleep(2)
        print("Šel jsi po žebříku nahoru a byly tam dveře")
        import time
        time.sleep(2)
        print("Ty dveře byly zamčeny rozbitym zámkem")
        import time
        time.sleep(2)
    elif axe >= 1:
        global gg4
        if gg4 == 0:
            devide()
            import time
            time.sleep(2)
            print("Šel jsi po žebříku nahoru a byly tam dveře")
            import time
            time.sleep(2)
            print("Vzal jsi to sekeru a zničil jsi ten zámek")
            import time
            time.sleep(2)
            print("Otevřel jsi ty dveře, a zjistil jsi že jseš na půdě.")
            import time
            time.sleep(2)
            print("Viděl jsi tam mrtvolu")
            import time
            time.sleep(2)
            gg4 = gg4 + 1
        if gg4 == 1:
            roof1()

def drawer1():
    user_choice2 = ""
    global ammo
    global cereal_bar
    global health
    while user_choice2 != "b":
        devide()
        import time
        time.sleep(2)
        print("Možnosti:\n"
              "1) Polička č.1\n"
              "2) Polička č.2\n"
              "3) Polička č.3\n"
              "4) Poli4ka č.4\n"
              "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            devide()
            import time
            time.sleep(2)
            print(">>Tady nic není<<")
            kill()
            import time
            time.sleep(2)
        elif user_choice2 == "2":
            devide()
            import time
            time.sleep(2)
            print(">>Náboje +1<<")
            kill()
            ammo = ammo + 1
            import time
            time.sleep(2)
        elif user_choice2 == "3":
            devide()
            import time
            time.sleep(2)
            print(">>Tyčinka +1<<")
            kill()
            cereal_bar = cereal_bar + 1
            import time
            time.sleep(2)
        elif user_choice2 == "4":
            devide()
            import time
            time.sleep(2)
            print(">>Tady nic neni<<")
            kill()
            import time
            time.sleep(2)
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "4":
            if user_choice2 != "b":
                if user_choice2 != "i":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
        if health <= 0:
            end()
global no10
no10 = 0
def emergency():
    global no10
    devide()
    import time
    time.sleep(2)
    if no10 == 1:
        print(">>Už jsi tady byl<<")
        import time
        time.sleep(2)
    if no10 == 0:
        if luck >= 50:
            print(">>Zničil jsi sklo<<")
            import time
            time.sleep(2)
            print(">>Sekera +1<<")
            import time
            time.sleep(2)
            global axe
            axe = axe + 1
            no10 = no10 + 1
        elif luck < 50:
            print(">>Zničil jsi sklo<<\n"
                 ">>Životy -50<<\n"
                 "Sekera +1")
            import time
            time.sleep(2)
            axe = axe + 1
            no10 = no10 + 1
#kitchen ---------------------------------------------------------------------------------------------------------------
def fridge():
    global broken_tangerine
    global meat
    global gg6
    global gg7
    user_choice2 = ""
    while user_choice2 != "b":
        devide()
        import time
        time.sleep(2)
        print(">>Lednička<<\n"
              "Možnosti:\n"
              "1) Polička č.1\n"
              "2) Polička č.2\n"
              "3) Polička č.3\n"
              "4) Mrazak\n"
              "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            if gg6 == 0:
                devide()
                import time
                time.sleep(2)
                print("Zkažena mandarinka +5")
                broken_tangerine = broken_tangerine + 5
                gg6 = gg6 + 1
                kill()
            elif gg6 == 1:
                devide()
                import time
                time.sleep(2)
                print(">>Už jsi tady byl<<")
                kill()
        elif user_choice2 == "2":
            devide()
            import time
            time.sleep(2)
            print(">>Tady nic není<<")
            import time
            time.sleep(2)
            kill()
        elif user_choice2 == "3":
            if gg7 == 1:
                devide()
                import time
                time.sleep(2)
                print(">>Už jsi tady byl<<")
                import time
                time.sleep(2)
                kill()
            if gg7 == 0:
                devide()
                import time
                time.sleep(2)
                print("Maso +2")
                meat = meat + 2
                gg7 = gg7 + 1
                kill()
        elif user_choice2 == "4":
            icemaker()
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "4":
            if user_choice2 != "b":
                if user_choice2 != "i":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
        if health <= 0:
            end()
def icemaker():
    user_choice2 = ""
    global gg5
    while user_choice2 != "b":
        if gg5 == 0:
            devide()
            import time
            time.sleep(2)
            print("V mražaku se nachazi magnetofon s nahravkou")
            import time
            time.sleep(2)
            gg5 = gg5 + 1
        devide()
        import time
        time.sleep(2)
        print(">>Mrazak<<\n"
              "Možnosti:\n"
              "1) Postit nahravku\n"
              "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            devide()
            import time
            time.sleep(2)
            import os
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "Music/Program/Real_music.py"
            abs_file_path = os.path.join(script_dir, rel_path)
            os.system(abs_file_path)
            kill()
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "1":
            if user_choice2 != "i":
                if user_choice2 != "b":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
        if health <= 0:
            end()
def sink():
    global user_choice2
    global wet_rag
    global gg9
    if gg8 == 0:
        devide()
        import time
        time.sleep(2)
        print("Zjistil jsi že umývadlo je plny vody")
        import time
        time.sleep(2)
    while user_choice2 != "b":
        devide()
        import time
        time.sleep(2)
        print(">>Umývadlo<<\n"
              "Možnosti:\n"
              "1) Divat se na vodu")
        if ik_feature == 1:
            print("2) Umočít hadr ve vodě")
        print("b) Zpatky")
        print("")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            devide()
            import time
            time.sleep(2)
            print(">>Ano, voda vypada jak voda<<")
            import time
            time.sleep(2)
        if rag >= 1:
            if user_choice2 == "2":
                if gg9 == 0:
                    devide()
                    import time
                    time.sleep(2)
                    print("Namočil jsi hadr")
                    import time
                    time.sleep(2)
                    print(">>Mokrej hadr +1<<")
                    import time
                    time.sleep(2)
                    wet_rag = wet_rag + 1
                    gg9 = gg9 + 1
                    kill()
                elif gg9 == 1:
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Už jsi tady byl<<")
                    import time
                    time.sleep(2)
                    kill()
        elif user_choice2 == "i":
            devide()
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "1":
            if user_choice2 != "i":
                if user_choice2 != "b":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
        if rag >= 1:
            if user_choice2 > "2":
                if user_choice2 != "i":
                    if user_choice2 != "b":
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Zadali jste špatnej znak<<")
                        import time
                        time.sleep(2)
        if health <= 0:
            end()
def shelf():
    global gun
    global ammo
    global gg10
    global book_2
    user_choice2 = ""
    while user_choice2 != "b":
        devide()
        import time
        time.sleep(2)
        print(">>Polička<<\n"
              "Možnosti:\n"
              "1) Kniha\n"
              "2) Škrabanec\n"
              "3) Pistole\n"
              "4) Náboje\n"
              "5) Mouka\n"
              "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            if book_2 == 0:
                devide()
                import time
                time.sleep(2)
                print(">>Kniha 2 +1<<")
                book_2 = book_2 + 1
                kill()
                import time
                time.sleep(2)
            elif book_2 == 1:
                devide()
                import time
                time.sleep(2)
                print(">>Už jsi tady byl<<")
                kill()
                import time
                time.sleep(2)
        elif user_choice2 == "2":
            morse_code()
        elif user_choice2 == "3":
            if gun == 0:
                devide()
                import time
                time.sleep(2)
                print(">>Pistole +1<<")
                import time
                time.sleep(2)
                gun = gun + 1
                kill()
            elif gun == 1:
                devide()
                import time
                time.sleep(2)
                print(">>Už jsi tady byl<<")
                import time
                time.sleep(2)
                kill()
        elif user_choice2 == "4":
            if gg10 == 0:
                devide()
                import time
                time.sleep(2)
                print(">>Náboje +3<<")
                import time
                time.sleep(2)
                ammo = ammo + 3
                gg10 = gg10 + 1
                kill()
            elif gg10 == 1:
                devide()
                import time
                time.sleep(2)
                print(">>Už jsi tady byl<<")
                import time
                time.sleep(2)
                kill()
        elif user_choice2 == "5":
            flour()
            kill()
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "5":
            if user_choice2 != "b":
                if user_choice2 != "i":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
        if health <= 0:
            end()
def morse_code():
    devide()
    import time
    time.sleep(2)
    print("|.-.|..-|-.||.-|.--|.-|-.--| !")
    input(">>")
def flour():
    global key2
    user_choice2 = ""
    while user_choice2 != "b":
        devide()
        import time
        time.sleep(2)
        print("Možnosti:\n"
              "1) Sýpat mouku\n"
              "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            devide()
            import time
            time.sleep(2)
            import random
            item_list = [1,2,3,4]
            flour_prouct = random.choice(item_list)
            if flour_prouct <= 3:
                if key2 == 0:
                    print(">>Zatím nic nepada<<")
                    import time
                    time.sleep(2)
                elif key2 == 1:
                    print(">>Už jsi tady byl<<")
                    import time
                    time.sleep(2)
            elif flour_prouct == 4:
                if key2 == 0:
                    print(">>Klič 2 +1<<")
                    import time
                    time.sleep(2)
                    key2 = key2 + 1
                elif key2 == 1:
                    print(">>Už jsi tady byl<<")
                    import time
                    time.sleep(2)
        if user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "1":
            if user_choice2 != "b":
                if user_choice2 != "i":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
def book2pg1():
    user_choice2 = ""
    while user_choice2 != "s":
        devide()
        import time
        time.sleep(2)
        file_book2 = open("Features/Book 2/Book 1.txt")
        print(file_book2.read())
        file_book2.close
        print("")
        screen_book()
        user_choice2 = input(">>")
        if user_choice2 == "d":
            book2pg2()
        elif user_choice2 == "a":
            devide()
            import time
            time.sleep(2)
            print(">>Tahle možnost je zatím nedostupna<<")
            import time
            time.sleep(2)
        if user_choice2 != "a":
            if user_choice2 != "d":
                if user_choice2 != "s":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
def book2pg2():
    user_choice2 = ""
    while user_choice2 != "a":
        devide()
        import time
        time.sleep(2)
        file_book2 = open("Features/Book 2/Book 2.txt")
        print(file_book2.read())
        file_book2.close
        print("")
        screen_book2()
        user_choice2 = input(">>")
        if user_choice2 == "d":
            book2pg3()
        if user_choice2 != "a":
            if user_choice2 != "d":
                devide()
                import time
                time.sleep(2)
                print(">>Zadali jste špatnej znak<<")
                import time
                time.sleep(2)
def book2pg3():
    user_choice2 = ""
    while user_choice2 != "a":
        devide()
        import time
        time.sleep(2)
        file_book2 = open("Features/Book 2/Book 3.txt")
        print(file_book2.read())
        file_book2.close
        print("")
        screen_book2()
        user_choice2 = input(">>")
        if user_choice2 == "d":
            devide()
            import time
            time.sleep(2)
            print(">>Už nejsou žadný strany<<")
            import time
            time.sleep(2)
        if user_choice2 != "a":
            if user_choice2 != "d":
                devide()
                import time
                time.sleep(2)
                print(">>Zadali jste špatnej znak<<")
                import time
                time.sleep(2)
def table2():
    user_choice2 = ""
    while user_choice2 != "b":
        devide()
        import time
        time.sleep(2)
        print(">>Stůl<<\n"
              "Možnosti:\n"
              "1) Na stole\n"
              "2) Pod stůl\n"
              "3) Šuplík\n"
              "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            devide()
            import time
            time.sleep(2)
            print(">>Tady nic není<<")
            import time
            time.sleep(2)
            kill()
        elif user_choice2 == "2":
            devide()
            import time
            time.sleep(2)
            print(">>Tady nic není<<")
            import time
            time.sleep(2)
            kill()
        elif user_choice2 == "3":
            devide()
            import time
            time.sleep(2)
            print(">>Tady nic není<<")
            import time
            time.sleep(2)
            kill()
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "3":
            if user_choice2 != "i":
                if user_choice2 != "b":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
        if health <= 0:
            end()
def picture():
    user_choice2 = ""
    while user_choice2 != "b":
        devide()
        import time
        time.sleep(2)
        file_book2 = open("Features/Wall picture/Wall picture.txt")
        print(file_book2.read())
        file_book2.close
        print(">>Obrázek<<\n"
              "Možnosti:\n"
              "1) Zatahnout za zvohlej roh\n"
              "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            if key3 == 1:
                devide()
                import time
                time.sleep(2)
                print(">>Už jsi tady byl<<")
                kill()
                import time
                time.sleep(2)
            elif key3 == 0:
                safe()
                kill()
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "1":
            if user_choice2 != "b":
                if user_choice2 != "i":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
        if health <= 0:
            end()
def safe():
    global loading
    global key3
    global photo_3
    global cereal_bar
    global luck
    devide()
    import time
    time.sleep(2)
    file_book2 = open("Features/Safe/Safe.txt")
    print(file_book2.read())
    file_book2.close
    print("")
    user_choice2 = input(">>")
    devide()
    loop = "123"
    for loading in loop:
        loading = print("===================================================")
        import time
        time.sleep(2)
    if user_choice2 == "Bella Ciao"or"bella ciao"or"Bella ciao"or"bella Ciao":
        print(">>Spravně<<")
        devide()
        import time
        time.sleep(2)
        print(">>Klič 3 +1<<")
        import time
        time.sleep(2)
        print(">>Fotka 3 +1<<")
        import time
        time.sleep(2)
        print(">>Tyčinka +1<<")
        import time
        time.sleep(2)
        print(">>Štěstí +10<<")
        import time
        time.sleep(2)
        key3 = key3 + 1
        photo_3 = photo_3 + 1
        cereal_bar = cereal_bar + 1
        luck = luck + 10
    elif user_choice2 != "Bella Ciao"or"bella ciao"or"Bella ciao"or"bella Ciao":
        print(">>Špatně<<")
        import time
        time.sleep(2)
        print(">>Luck -10<<")
        import time
        time.sleep(2)
        luck = luck - 10
def photo3():
    devide()
    import time
    time.sleep(2)
    file_book2 = open("Features/Photoes/Photo 3.txt")
    print(file_book2.read())
    file_book2.close
    input(">>")
def window1():
    global gg11
    global ik_door4
    if gg11 == 3:
        devide()
        import time
        time.sleep(2)
        print("Počkej...")
        import time
        time.sleep(2)
        print("Vidíš v dálce kouř")
        import time
        time.sleep(2)
    if gg11 == 2:
        devide()
        import time
        time.sleep(2)
        print("Jop, furt to stejny")
        import time
        time.sleep(2)
        gg11 = gg11 + 1
    if gg11 == 1:
        devide()
        import time
        time.sleep(2)
        print("Podíval ses z okna")
        import time
        time.sleep(2)
        print("Byli za něma mřiže takže jsi nemohl utect")
        import time
        time.sleep(2)
        print("Podíval ses v dálce ale nic jsi neviděl")
        import time
        time.sleep(2)
        gg11 = gg11 + 1
    if gg11 == 0:
        devide()
        import time
        time.sleep(2)
        print("Šel jsi k oknu")
        import time
        time.sleep(2)
        print("Najednou se pod tebou propadla podlaha")
        import time
        time.sleep(2)
        ik_door4 = ik_door4 + 1
        gg11 = gg11 + 1
def floor():
    global gg13
    user_choice2 =""
    if gg13 == 0:
        devide()
        import time
        time.sleep(2)
        print(">>Nachazi se tu trezor<<")
        import time
        time.sleep(2)
        gg13 = gg13 + 1
    while gg10 != 100:
        if paper1 == 1:
            devide()
            import time
            time.sleep(2)
            print(">>Už jsi tady byl<<")
            import time
            time.sleep(2)
            kitchen1()
        elif paper1 == 0:
            kill()
            safe1pt_1()
        if health <= 0:
            end()
def safe1pt_1():
    user_choice2 = ""
    devide()
    import time
    time.sleep(2)
    file_book2 = open("Features/Safe/Floor Safe/Safe 1.txt")
    print(file_book2.read())
    file_book2.close
    print("Možnosti: 12, 6, 9, 3")
    print("")
    print("| >> b: Zpatky << |")
    user_choice2 = input(">>")
    if user_choice2 == "12":
        safe1pt_2()
    if user_choice2 == "b":
        kitchen1()
    if user_choice2 != "12":
        if user_choice2 != "b":
            devide()
            import time
            time.sleep(2)
            print(">>*clack<<")
            import time
            time.sleep(2)
def safe1pt_2():
    user_choice2 = ""
    devide()
    import time
    time.sleep(2)
    print("*click")
    import time
    time.sleep(2)
    devide()
    import time
    time.sleep(2)
    file_book2 = open("Features/Safe/Floor Safe/Safe 2.txt")
    print(file_book2.read())
    file_book2.close
    print("")
    print("| >> b: Zpatky << |")
    user_choice2 = input(">>")
    if user_choice2 == "6":
        safe1pt_3()
    if user_choice2 == "b":
        kitchen1()
    if user_choice2 != "6":
        if user_choice2 != "b":
            devide()
            import time
            time.sleep(2)
            print(">>*clack<<")
            import time
            time.sleep(2)
def safe1pt_3():
    user_choice2 = ""
    devide()
    import time
    time.sleep(2)
    print("*click")
    import time
    time.sleep(2)
    devide()
    import time
    time.sleep(2)
    file_book2 = open("Features/Safe/Floor Safe/Safe 3.txt")
    print(file_book2.read())
    file_book2.close
    print("")
    print("| >> b: Zpatky << |")
    user_choice2 = input(">>")
    if user_choice2 == "9":
        safe1pt_4()
    if user_choice2 == "b":
        kitchen1()
    if user_choice2 != "9":
        if user_choice2 != "b":
            devide()
            import time
            time.sleep(2)
            print(">>*clack<<")
            import time
            time.sleep(2)
def safe1pt_4():
    user_choice2 = ""
    global paper1
    devide()
    import time
    time.sleep(2)
    print("*click")
    import time
    time.sleep(2)
    devide()
    import time
    time.sleep(2)
    file_book2 = open("Features/Safe/Floor Safe/Safe 4.txt")
    print(file_book2.read())
    file_book2.close
    print("")
    print("| >> b: Zpatky << |")
    user_choice2 = input(">>")
    if user_choice2 == "3":
        devide()
        import time
        time.sleep(2)
        print("*click")
        import time
        time.sleep(2)
        devide()
        import time
        time.sleep(2)
        print(">>Kousek papíru +1<<")
        import time
        time.sleep(2)
        paper1 = paper1 + 1
        kitchen1()
    if user_choice2 == "b":
        kitchen1()
    if user_choice2 != "3":
        if user_choice2 != "b":
            devide()
            import time
            time.sleep(2)
            print(">>*clack<<")
            import time
            time.sleep(2)
def door4():
    devide()
    import time
    time.sleep(2)
    user_choice2 = ""
    file_book2 = open("Features/Door/Passcode 2.txt")
    print(file_book2.read())
    file_book2.close
    print("")
    print("|>> b: Zpatky <<|")
    user_choice2 = input(">>")
    kill()
    if user_choice2 == "b":
        import time
        time.sleep(2)
        kitchen1()
    devide()
    loop = "123"
    for loading in loop:
        loading = print("===================================================")
        import time
        time.sleep(2)
    if user_choice2 == "80085":
        devide()
        import time
        time.sleep(2)
        print(">>Spravně<<")
        import time
        time.sleep(2)
        final()
    elif user_choice2 !="80085":
        devide()
        import time
        time.sleep(2)
        print(">>Špatně<<")
        import time
        time.sleep(2)
#room 2 ----------------------------------------------------------------------------------------------------------------
def room2_bed1():
    user_choice2 = ""
    global gg14
    global cereal_bar
    global photo_4
    global key4
    while user_choice2 != "b":
        devide()
        import time
        time.sleep(2)
        print(">>Postel 1<<\n"
              "Možnosti:\n"
              "1) Polštař\n"
              "2) Na postel\n"
              "3) Pod postel\n"
              "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            if gg14 == 1:
                devide()
                import time
                time.sleep(2)
                print(">>Už jsi tady byl<<")
                kill()
                import time
                time.sleep(2)
            if gg14 == 0:
                devide()
                import time
                time.sleep(2)
                print(">>Klič 4 +1<<")
                kill()
                import time
                time.sleep(2)
                key4 = key4 + 1
                gg14 = gg14 + 1
        elif user_choice2 == "2":
            if gg15 == 1:
                devide()
                import time
                time.sleep(2)
                print(">>Už jsi tady byl<<")
                kill()
                import time
                time.sleep(2)
            if gg15 == 0:
                devide()
                import time
                time.sleep(2)
                print(">>Tyčinka +1<<")
                kill()
                cereal_bar = cereal_bar + 1
                import time
                time.sleep(2)
        elif user_choice2 == "3":
            if gg16 == 1:
                devide()
                import time
                time.sleep(2)
                print(">>Už jsi tady byl<<")
                kill()
                import time
                time.sleep(2)
            if gg16 == 0:
                devide()
                import time
                time.sleep(2)
                print(">>Fotka 4 +1<<")
                kill()
                photo_4 = photo_4 + 1
                import time
                time.sleep(2)
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "3":
            if user_choice2 != "b":
                if user_choice2 != "i":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
        if health <= 0:
            end()
def photo4():
    devide()
    import time
    time.sleep(2)
    file_book2 = open("Features/Photoes/Photo 4.txt")
    print(file_book2.read())
    file_book2.close
    input(">>")
def room2_bed2():
    user_choice2 = ""
    global cereal_bar
    while user_choice2 != "b":
        devide()
        import time
        time.sleep(2)
        print(">>Postel<<\n"
              "Možnosti:\n"
              "1) Polštař\n"
              "2) Na postel\n"
              "3) Pod postel\n"
              "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            devide()
            import time
            time.sleep(2)
            print(">>Tyčinka +1<<")
            cereal_bar = cereal_bar + 1
            kill()
            import time
            time.sleep(2)
        elif user_choice2 == "2":
            devide()
            import time
            time.sleep(2)
            print(">>Tady nic neni<<")
            kill()
            import time
            time.sleep(2)
        elif user_choice2 == "3":
            user_choice2 = ""
            if gg17 == 0:
                devide()
                import time
                time.sleep(2)
                print("Zjistil jsi že tady se nachazi trůhla")
                import time
                time.sleep(2)
            while user_choice2 != "b":
                devide()
                import time
                time.sleep(2)
                print(">>Pod postel<<\n"
                      "Možnosti:\n"
                      "1) Otevřít trůhlu\n"
                      "b) Zpatky\n")
                screen()
                user_choice2 = input(">>")
                if user_choice2 == "1":
                    chest2()
                    kill()
                if user_choice2 == "i":
                    import time
                    time.sleep(2)
                    inventory()
                if user_choice2 > "1":
                    if user_choice2 != "i":
                        if user_choice2 != "b":
                            devide()
                            import time
                            time.sleep(2)
                            print(">>Zadali jste špatnej znak<<")
                            import time
                            time.sleep(2)
                if health <= 0:
                    end()
        if user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "3":
            if user_choice2 != "i":
                if user_choice2 != "b":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
        if health <= 0:
            end()
def chest2():
    global ik_feature
    global key4
    if key4 == 1:
        devide()
        import time
        time.sleep(2)
        print("Otevřel jsi trůhlu")
        import time
        time.sleep(2)
        print("Na dně toho trůhla bylo nalepeny papírek")
        import time
        time.sleep(2)
        file_book2 = open("Features/Passcode/Passcode 2.txt")
        print(file_book2.read())
        file_book2.close
        ik_feature = ik_feature + 1
        input(">>")
    if key4 == 0:
        devide()
        import time
        time.sleep(2)
        print(">>Nemáš klič 4<<")
        import time
        time.sleep(2)
def drawer2():
    user_choice2 = ""
    global cereal_bar
    if gg18 == 0:
        devide()
        import time
        time.sleep(2)
        print("Otevřel jsi dveře skřiňi")
        import time
        time.sleep(2)
        print("Zjistil jsi že 2 poličky spadli")
        import time
        time.sleep(2)
    while user_choice2 != "b":
        devide()
        import time
        time.sleep(2)
        print(">>Skříň<<\n"
              "Možnosti:\n"
              "1) Polička 1\n"
              "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            devide()
            import time
            time.sleep(2)
            print(">>Tyčinka +1<<")
            kill()
            cereal_bar = cereal_bar + 1
            import time
            time.sleep(2)
        if user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "1":
            if user_choice2 != "b":
                if user_choice2 != "i":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
        if health <= 0:
            end()
def picture2():
    devide()
    import time
    time.sleep(2)
    file_book2 = open("Features/Wall picture/Wall picture 1.txt")
    print(file_book2.read())
    file_book2.close
    input(">>")
def door5():
    if ik_feature == 0:
        devide()
        import time
        time.sleep(2)
        print("Jejda, nevím kde jsem dal klíče")
        kill()
        import time
        time.sleep(2)
    elif ik_feature == 1:
        import time
        time.sleep(2)
        kill()
        chodba1()
    if health <= 0:
        end()
#roof ------------------------------------------------------------------------------------------------------------------
def deadman():
    user_choice2 = ""
    global paper3
    global health
    while user_choice2 != "b":
        devide()
        import time
        time.sleep(2)
        print(">>Mrtvola<<\n"
              "Možnosti:\n"
              "1) Prohlednout kapse\n"
              "2) Prohlednout nahrdelnik\n"
              "3) Prohlednout ránu\n"
              "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            if paper3 == 0:
                devide()
                import time
                time.sleep(2)
                print(">>Papír 3 +1<<")
                paper3 = paper3 + 1
                kill()
                import time
                time.sleep(2)
            if user_choice2 == 1:
                devide()
                import time
                time.sleep(2)
                print(">>Už jsi tady byl<<")
                kill()
                import time
                time.sleep(2)
        elif user_choice2 == "2":
            devide()
            import time
            time.sleep(2)
            print(">>Tady nic není<<")
            kill()
            import time
            time.sleep(2)
        elif user_choice2 == "3":
            devide()
            import time
            time.sleep(2)
            print("Podival ses na tu ranu")
            import time
            time.sleep(2)
            print("Zjistil jsi že byl pobodan")
            kill()
            import time
            time.sleep(2)
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "3":
            if user_choice2 != "b":
                if user_choice2 != "i":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
        if health <= 0:
            end()
def chest3():
    global paper1
    global health
    if key3 == 1:
        devide()
        import time
        time.sleep(2)
        print(">>Kousek papíru +1<<")
        paper1 = paper1 + 1
        kill()
        import time
        time.sleep(2)
    if key3 == 0:
        devide()
        import time
        time.sleep(2)
        print(">>Nemáš klíč 3<<")
        import time
        time.sleep(2)
    if health <= 0:
        end()
def table3():
    user_choice2 = ""
    global cereal_bar
    global gg19
    global health
    while user_choice2 != "b":
        devide()
        import time
        time.sleep(2)
        print(">>Stůl<<\n"
              "Možnosti:\n"
              "1) Na stůl\n"
              "2) Pod stolem\n"
              "b) Zpatky\n")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            if gg19 == 0:
                devide()
                import time
                time.sleep(2)
                print(">>Tyčinka +2<<")
                cereal_bar = cereal_bar + 2
                gg19 = gg19 + 1
                import time
                time.sleep(2)
            if gg19 == 1:
                devide()
                import time
                time.sleep(2)
                print(">>Už jsi tady byl<<")
                import time
                time.sleep(2)
        elif user_choice2 == "2":
            devide()
            import time
            time.sleep(2)
            print(">>Tady nic není<<")
            import time
            time.sleep(2)
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "2":
            if user_choice2 != "i":
                if user_choice2 != "b":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Zadali jste špatnej znak<<")
                    import time
                    time.sleep(2)
        if health <= 0:
            end()
def painting():
    devide()
    import time
    time.sleep(2)
    file_book2 = open("Features/Wall picture/Wall picture 2.txt")
    print(file_book2.read())
    file_book2.close
    input(">>")
#rooms -----------------------------------------------------------------------------------------------------------------
def room1():
    import time
    time.sleep(2)
    print(">>Nachaziš se v pokoji č.1<<\n"
          "Věci kolem tebe:\n"
          "1) Postel\n"
          "2) Skřiň\n"
          "3) Stůl\n"
          "4) Truhla")
    if ik_door3 == 0:
        print("5) Dveře")
    elif ik_door3 == 1:
        print("5) Chodba")

def room2():
    global gg12
    if gg12 == 0:
        devide()
        import time
        time.sleep(2)
        print("Otevřel jsi dveře")
        import time
        time.sleep(2)
        print("Šel jsi dovnitř a dveře se za sebou zavřeli")
        import time
        time.sleep(2)
        print("Snažil jsi je otevřít ale byly zamčeny")
        import time
        time.sleep(2)
        gg12 = gg12 + 1
    devide()
    import time
    time.sleep(2)
    print(">>Nachaziš se v pokoji č.2<<\n"
          "Možnosti:\n"
          "1) Postel 1\n"
          "2) Postel 2\n"
          "3) Skříň\n"
          "4) Obraz\n"
          "5) Dveře\n")
def kitchen():
    devide()
    import time
    time.sleep(2)
    print(">>Nachaziš se v kuchyňi<<\n"
          "1) Chodba\n"
          "2) Lednička\n"
          "3) Umyvadlo\n"
          "4) Polička\n"
          "5) Stůl\n"
          "6) Obraz\n"
          "7) Okno")
    if ik_door4 == 1:
        print("8) Podlaha")
    if ik_door4 == 0:
        print("8) Dveře")
    if ik_door4 == 1:
        print("9) Dveře")

def roof():
    devide()
    import time
    time.sleep(2)
    print(">>Nachaziš se na půdě<<\n"
          "1) Mrtvola\n"
          "2) Trůhla\n"
          "3) Stůl\n"
          "4) Obraz\n"
          "5) Chodba")
def chodba():
    devide()
    print(">>Nachaziš se na chodbě<<\n"
          "Věci kolem tebe:\n"
          "1) Pokoj č.1")
    if ik_door == 0:
        print("2) Dveře 1")
    elif ik_door == 1:
        print("2) Pokoj č.2")
    if ik_door1 == 0:
        print("3) Dveře 2")
    elif ik_door1 == 1:
        print("3) Kuchyně")
    if ik_door2 == 0:
        print("4) Žebřík")
    elif ik_door2 == 1:
        print("4) Půda")
    print("5) Skřiň")
    print("6) Požarní skřiň")






#interface
def loading():
    print("===================================================")
def devide():
    print("---------------------------------------------------")
def kill():
    global health
    global energy
    if energy > 0:
        energy = energy - 10
    if energy <= 0:
        health = health - 10
def screen():
    global health
    global energy
    global luck
    print("| >> Životy:" ,health, "<< | >> Energie:" ,energy,"<< | >> Štěstí:" ,luck,"<< | >> Inventař(i) << |")
def screen_book():
    print("| >> d: Dalši strana << | >> a: Přední strana << | >> s: Zpatky << |")
def screen_book2():
    print("| >> d: Dalši strana << | >> a: Přední strana << |")
def inventory():
    user_choice4 = ""
    while user_choice4 != "b":
        devide()
        import time
        time.sleep(2)
        global meat
        global cereal_bar
        global energy
        global broken_tangerine
        global rag
        global wet_rag
        global health
        print(">>Inventař:\n"
          "1) Kliče\n"
          "2) Maso =",meat,"\n"
          "3) Sekera =",axe,"\n"
          "4) Nůž =",knife,"\n"
          "5) Tyčinka =",cereal_bar,"\n"
          "6) Papírky\n"
          "7) Knihy\n"
          "8) Fotky\n"
          "9) Pistole =",gun,"")
        if wet_rag == 0:
            print("10) Hadr =",rag,"")
        elif wet_rag == 1:
            print("10) Mokrej hadr =",wet_rag,"")
        if broken_tangerine >= 1:
            print("11) Zkažena mandarinka =",broken_tangerine)
        print("b) Zpatky\n")
        screen()
        user_choice4 = input(">>")
        if user_choice4 == "1":
            user_choice2 = ""
            while user_choice2 != "b":
                devide()
                import time
                time.sleep(2)
                print(">>Kliče<<\n"
                      "Možnosti:\n"
                      "1) Klič 1 =",key1,"\n"
                      "2) Klič 2 =",key2,"\n"
                      "3) Klič 3 =",key3,"\n"
                      "4) Klič 4 =",key4,"\n"
                      "b) Zpatky\n")
                screen()
                user_choice2 = input(">>")
                if user_choice2 == "1":
                    if key1 == 1:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Máš klič 1<<")
                        import time
                        time.sleep(2)
                    elif key1 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemáš klíč 1<<")
                        import time
                        time.sleep(2)
                if user_choice2 == "2":
                    if key2 == 1:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Máš klič 2<<")
                        import time
                        time.sleep(2)
                    elif key2 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemáš klíč 2<<")
                        import time
                        time.sleep(2)
                if user_choice2 == "3":
                    if key3 == 1:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Máš klič 3<<")
                        import time
                        time.sleep(2)
                    elif key3 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemáš klič 3<<")
                        import time
                        time.sleep(2)
                if user_choice2 == "4":
                    if key4 == 1:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Máš klič 4<<")
                        import time
                        time.sleep(2)
                    elif key4 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemáš klič 3<<")
                        import time
                        time.sleep(2)
                if user_choice2 > "4":
                    if user_choice2 != "b":
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Zadali jste špatnej znak<<")
                        import time
                        time.sleep(2)
        elif user_choice4 == "2":
            if meat > 0:
                devide()
                import time
                time.sleep(2)
                print("Energie +40")
                global energy
                energy = energy + 40
                meat = meat - 1
                import time
                time.sleep(2)
            elif meat == 0:
                devide()
                print(">>Nemaš máso<<")
                import time
                time.sleep(2)
        elif user_choice4 == "3":
            devide()
            import time
            time.sleep(2)
            if axe > 0:
                print(">>Máš sekeru<<")
                import time
                time.sleep(2)
            elif axe == 0:
                print(">>Nemáš žadnou sekeru<<")
                import time
                time.sleep(2)
        elif user_choice4 == "4":
            devide()
            import time
            time.sleep(2)
            if knife > 0:
                print(">>Máš nuž<<")
                import time
                time.sleep(2)
            elif knife == 0:
                print(">>Nemáš nuž<<")
                import time
                time.sleep(2)
        elif user_choice4 == "5":
            if cereal_bar > 0:
                devide()
                import time
                time.sleep(2)
                print("Energie +30")
                energy = energy + 30
                cereal_bar = cereal_bar - 1
                import time
                time.sleep(2)
            elif cereal_bar == 0:
                devide()
                print(">>Nemáš tyčinky<<")
                import time
                time.sleep(2)
        elif user_choice4 == "6":
            user_choice2 = ""
            while user_choice2 != "b":
                devide()
                import time
                time.sleep(2)
                print(">>Papíry<<\n"
                      "Možnosti:\n"
                      "1) Papír 1 =",pass_code1,"")
                if paper1 == 0 or 1:
                    print("2) Kousek papíru =",paper1,"")
                elif paper1 == 2:
                    print("2) Papír 2 =",paper1,"")
                print("3) Papír 3 =",paper3,"")
                print("b) Zpatky\n")
                screen()
                user_choice2 = input(">>")
                if user_choice2 == "1":
                    if pass_code1 == 1:
                        passcode1()
                    elif pass_code1 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemáš papír 1<<")
                        import time
                        time.sleep(2)
                elif user_choice2 == "2":
                    if paper1 == 1:
                        devide()
                        import time
                        time.sleep(2)
                        file_book2 = open("Features/Passcode/Final passcode/Passcode 1.txt")
                        print(file_book2.read())
                        file_book2.close
                        input(">>")
                    elif paper1 == 2:
                        devide()
                        import time
                        time.sleep(2)
                        file_book2 = open("Features/Passcode/Final passcode/Passcode 2.txt")
                        print(file_book2.read())
                        file_book2.close
                        input(">>")
                    elif paper1 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemáš papír 2<<")
                        import time
                        time.sleep(2)
                elif user_choice2 == "3":
                    if paper3 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemáš papír 3<<")
                        import time
                        time.sleep(2)
                    if paper3 == 1:
                        devide()
                        import time
                        time.sleep(2)
                        file_book2 = open("Features/Passcode/Passcode 3.txt")
                        print(file_book2.read())
                        file_book2.close
                        input(">>")
                if user_choice2 > "3":
                    if user_choice2 != "b":
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Zadali jste špatnej znak<<")
                        import time
                        time.sleep(2)
        elif user_choice4 == "7":
            user_choice2 = ""
            while user_choice2 != "b":
                devide()
                import time
                time.sleep(2)
                print(">>Knihy<<\n"
                      "Možnosti:\n"
                      "1) Kniha 1 =",book_1,"\n"
                      "2) Kniha 2 =",book_2,"\n"
                      "b) Zpatky\n")
                screen()
                user_choice2 = input(">>")
                if user_choice2 == "1":
                    if book_1 == 1:
                        book1()
                    elif book_1 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemáš knihu 1<<")
                        import time
                        time.sleep(2)
                if user_choice2 == "2":
                    if book_2 == 1:
                        book2pg1()
                    elif book_2 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemáš knihu 2<<")
                        import time
                        time.sleep(2)
                if user_choice2 > "2":
                    if user_choice2 != "b":
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Zadali jste špatnej znak<<")
                        import time
                        time.sleep(2)
        elif user_choice4 == "8":
            user_choice2 = ""
            while user_choice2 != "b":
                devide()
                import time
                time.sleep(2)
                print(">>Fotky<<\n"
                      "Možnosti:\n"
                      "1) Fotka 1 =",photo_1,"\n"
                      "2) Fotka 2 =",photo_2,"\n"
                      "3) Fotka 3 =",photo_3,"\n"
                      "4) Fotka 4 =",photo_4,"\n"
                      "b) Zpatky\n")
                screen()
                user_choice2 = input(">>")
                if user_choice2 == "1":
                    if photo_1 == 1:
                        photo1()
                    elif photo_1 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemaš fotku 1<<")
                        import time
                        time.sleep(2)
                if user_choice2 == "2":
                    if photo_2 == 1:
                        photo2()
                    elif photo_2 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemáš fotku 2<<")
                        import time
                        time.sleep(2)
                if user_choice2 == "3":
                    if photo_3 == 1:
                        photo3()
                    elif photo_3 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemaš fotku 3<<")
                        import time
                        time.sleep(2)
                if user_choice2 == "4":
                    if photo_4 == 1:
                        photo4()
                    if photo_4 == 0:
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Nemáš fotku 4<<")
                        import time
                        time.sleep(2)
                if user_choice2 > "3":
                    if user_choice2 != "b":
                        devide()
                        import time
                        time.sleep(2)
                        print(">>Zadali jste špatnej znak<<")
                        import time
                        time.sleep(2)
        elif user_choice4 == "9":
            devide()
            import time
            time.sleep(2)
            if gun == 0:
                print(">>Nemáš pistoli<<")
                import time
                time.sleep(2)
            elif gun == 1:
                print(">>Máš pistoli s",ammo,"náboje<<")
                import time
                time.sleep(2)
        elif user_choice4 == "10":
            global health
            if wet_rag == 0:
                if rag >= 1:
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Máš hadr<<")
                    import time
                    time.sleep(2)
                elif rag == 0:
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Nemáš hadr<<")
                    import time
                    time.sleep(2)
            if wet_rag == 1:
                devide()
                import time
                time.sleep(2)
                print("Možnosti:\n"
                      "1) Dát si kolem hlavy\n"
                      "b) Zpatky\n")
                screen()
                user_choice4 = input(">>")
                if user_choice4 == "1":
                    devide()
                    import time
                    time.sleep(2)
                    print(">>Životy +50<<")
                    import time
                    time.sleep(2)
                    print(">>Energie +50<<")
                    import time
                    time.sleep(2)
                    health = health + 50
                    energy = energy + 50
        elif user_choice4 == "11":
            if broken_tangerine > 0:
                devide()
                import time
                time.sleep(2)
                print(">>Máš",broken_tangerine,"Zkaženich mandarinek<<")
        elif user_choice4 == "100":
            import time
            time.sleep(2)
            if sexyphoto1 == 1:
                sexyphoto_1()
                import time
                time.sleep(2)
            elif sexyphoto1 == 0:
                devide()
                import time
                time.sleep(2)
                print(">>Zatím tohle ještě nepiš ;)<<")
                import time
                time.sleep(2)
        if user_choice4 != "10":
            if user_choice4 != "b":
                if user_choice4 != "s":
                    if user_choice4 != "9":
                        if user_choice4 != "8":
                            if user_choice4 != "7":
                                if user_choice4 != "6":
                                    if user_choice4 != "5":
                                        if user_choice4 != "4":
                                            if user_choice4 != "3":
                                                if user_choice4 != "2":
                                                    if user_choice4 != "1":
                                                        if user_choice4 != "100":
                                                            if user_choice4 != "11":
                                                                devide()
                                                                import time
                                                                time.sleep(2)
                                                                print(">>Zadal jsi špatnej znak<<")
                                                                import time
                                                                time.sleep(2)

#Pokud si doopravdy čtete můj kod... tak je hodně špatnej. Ja vím.
#Radši si to ani nčtěte a zahrejte si to anebo využijte ten čas pro něco užitečneho
#Pokud mě chcete naučit par triku tak tady máte moje telefoni číslo: 775 696 129
                                               #můj email: danilegos.t@gmail.com

def start():
    options = ["1","2","3","4","5","6"]
    print("Jmenuješ se Danny Rushmore, a jseš polárník. Šel jsi prozkoumat novou nezmapovanou oblast\n"
            "Fitzpetrikův kuloár v Kanadě. Jak jsi tu oblast prozkoumal, tak ses propadl ve sněhu\n"
            "a ztratil jsi vědomi. Probudíš se v nějakém pokoji. Vůbec nevíš, jak ses tam dostal,\n"
            "ale víš že se máš z toho dostat ven.")
    devide()
    print("Ovladaní:\n"
          "- Stiskni tlačitko (i) aby ses mohl podivat do inventaře\n"
          "- Aby jsi udělal nějakou akci stiskni to čísla podle zadaní\n"
          "- Pokud nemaš energie tak každej vyběr ti ubíra 10 život\n"
          "- Aby si získal energii tak musiš jíst nějaky jídlo(maso, tyčinka,atd.)\n"
          "- Pokud umřeš hra začína od znova\n"
          "Cíl hry:\n"
          "- Musiš se dostat živej z ty budovy\n"
          "Doporučení:\n"
          "- Hrejte to v Comand Promptu\n"
          "- Jsou tady i Eastereggy\n"
          "- Hrejte to se zaplym zvůkem")
    import os
    os.system("")
    user_choice = input("\u001b[33m   _____                     _ _                 _ \n"
                        "  / ____|                   | | |               | |\n"
                        " | |  __ _ __ ___  ___ _ __ | | | __ _ _ __   __| |\n"
                        " | | |_ | '__/ _ \/ _ \ '_ \| | |/ _` | '_ \ / _` |\n"
                        " | |__| | | |  __/  __/ | | | | | (_| | | | | (_| |\n"
                        "  \_____|_|  \___|\___|_| |_|_|_|\__,_|_| |_|\__,_|\n"
                        ">>           Stiskni jakoukoliv klavesu          <<\n"
                        ">>")
    #import os
    #os.system("")
    print("\u001b[0m ")
    del user_choice
    print("Načítam hru...")
    import time
    time.sleep(3)
    room11()

def room11():
    global user_choice2
    user_choice2 = ""
    global user_choice3
    user_choice3 = ""
    while user_choice3 != "5353":
        devide()
        room1()
        print("")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            import time
            time.sleep(2)
            bed1()
        elif user_choice2 == "2":
            import time
            time.sleep(2)
            warderobe1()
        elif user_choice2 == "3":
            import time
            time.sleep(2)
            table1()
        elif user_choice2 == "4":
            import time
            time.sleep(2)
            if key1 == 1:
                devide()
                print("*click")
                import time
                time.sleep(2)
                chest1()
            else:
                print("*clack")
                import time
                time.sleep(2)
                devide()
                print(">>K otevření truhly potřebuješ klič 1<<")
                import time
                time.sleep(3)
        if user_choice2 == "5":
            global luck
            global gg2
            if gg2 == 0:
                devide()
                import time
                time.sleep(2)
                door1()
                user_choice3 = input(">>")
                if user_choice3 == "5353":
                    devide()
                    import time
                    time.sleep(2)
                    loading()
                    import time
                    time.sleep(2)
                    loading()
                    import time
                    time.sleep(2)
                    loading()
                    import time
                    time.sleep(2)
                    print(">>Spravně<<")
                    import time
                    time.sleep(2)
                    print(">>Štěsti +10<<")
                    import time
                    time.sleep(2)
                    devide()
                    import time
                    time.sleep(2)
                    print("*click")
                    import time
                    time.sleep(2)
                    gg2 = gg2 + 1
                    global ik_door3
                    ik_door3 = ik_door3 + 1
                    luck = luck + 10
                elif user_choice3 != "5353":
                    if user_choice3 != "6969":
                        devide()
                        import time
                        time.sleep(2)
                        loading()
                        import time
                        time.sleep(2)
                        loading()
                        import time
                        time.sleep(2)
                        loading()
                        print(">>Špatně<<")
                        import time
                        time.sleep(2)
                        print(">>Štěstí -10<<")
                        luck = luck - 10
                        import time
                        time.sleep(2)
                if user_choice3 == "6969":
                    devide()
                    import time
                    time.sleep(1)
                    print("*beep")
                    import time
                    time.sleep(3)
                    print("*beep")
                    import time
                    time.sleep(2)
                    print("*beep")
                    import time
                    time.sleep(1)
                    print("*beep")
                    import time
                    time.sleep(0.5)
                    print("*beep")
                    import time
                    time.sleep(0.5)
                    print("BOOOM!")
                    end()
            if gg2 == 1:
                global energy
                energy = energy - 10
                chodba1()
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "5":
            if user_choice2 != "i":
                devide()
                print(">>Zadal jste špatnej znak<<")
                import time
                time.sleep(2)
def chodba1():
    global gg1
    if gg1 == 0:
        devide()
        import time
        time.sleep(2)
        print("Otevřel jsi dveře. Citíl jsi nepřijemny smrad.")
        import time
        time.sleep(2)
        print("Viděl jsi dalši 2 dveře a 1 žebřík.")
        import time
        time.sleep(2)
        gg1 = gg1 + 1
    while gg3 != 100:
        chodba()
        print("")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            import time
            time.sleep(2)
            global energy
            energy = energy - 10
            room11()
        elif user_choice2 == "2":
            door2()
        elif user_choice2 == "3":
            door3()
        elif user_choice2 == "4":
            roof2()
        elif user_choice2 == "5":
            drawer1()
        elif user_choice2 == "6":
            emergency()
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "6":
            if user_choice2 != "i":
                devide()
                import time
                time.sleep(2)
                print(">>Zadal jste špatnej znak<<")
                import time
                time.sleep(2)
def room22():
    global ik_door
    user_choice2 = ""
    ik_door = 1
    while gg4 != 100:
        room2()
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            room2_bed1()
        elif user_choice2 == "2":
            room2_bed2()
        elif user_choice2 == "3":
            drawer2()
        elif user_choice2 == "4":
            picture2()
        elif user_choice2 == "5":
            door5()
        if user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "5":
            if user_choice2 != "i":
                devide()
                import time
                time.sleep(2)
                print(">>Zadli jste špatnej znak<<")
                import time
                time.sleep(2)
def roof1():
    while gg4 != 100:
        roof()
        print("")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            deadman()
        elif user_choice2 == "2":
            chest3()
        elif user_choice2 == "3":
            table3()
        elif user_choice2 == "4":
            painting()
        elif user_choice2 == "5":
            import time
            time.sleep(2)
            chodba1()
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if user_choice2 > "5":
            if user_choice2 != "i":
                devide()
                import time
                time.sleep(2)
                print(">>Zadali jste špatnej znak<<")
                import time
                time.sleep(2)
def kitchen1():
    global health
    while gg4 != 100:
        global ik_door4
        global ik_door1
        ik_door1 = 1
        kitchen()
        print("")
        screen()
        user_choice2 = input(">>")
        if user_choice2 == "1":
            chodba1()
        elif user_choice2 == "2":
            fridge()
        elif user_choice2 == "3":
            sink()
        elif user_choice2 == "4":
            shelf()
        elif user_choice2 == "5":
            table2()
        elif user_choice2 == "6":
            picture()
        elif user_choice2 == "7":
            window1()
        elif user_choice2 == "8":
            if ik_door4 == 0:
                door4()
        elif user_choice2 == "9":
            if ik_door4 == 1:
                door4()
        elif user_choice2 == "i":
            import time
            time.sleep(2)
            inventory()
        if ik_door4 == 1:
            if user_choice2 != "9":
                if user_choice2 != "8":
                    if user_choice2 != "7":
                        if user_choice2 != "6":
                            if user_choice2 != "5":
                                if user_choice2 != "4":
                                    if user_choice2 != "3":
                                        if user_choice2 != "2":
                                            if user_choice2 != "1":
                                                if user_choice2 != "i":
                                                    devide()
                                                    import time
                                                    time.sleep(2)
                                                    print(">>Zadali jste špatnej znak<<")
                                                    import time
                                                    time.sleep(2)
        if user_choice2 != "8":
            if user_choice2 != "7":
                if user_choice2 != "6":
                    if user_choice2 != "5":
                        if user_choice2 != "4":
                            if user_choice2 != "3":
                                if user_choice2 != "2":
                                    if user_choice2 != "1":
                                        if user_choice2 != "i":
                                            devide()
                                            import time
                                            time.sleep(2)
                                            print(">>Zadali jste špatnej znak<<")
                                            import time
                                            time.sleep(2)
        if health <= 0:
            end()
        if ik_door4 == 1:
            if user_choice2 == "8":
                floor()






















    input()


start()



