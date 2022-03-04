def pachet1():
    intrebare1 = 0
    intrebare2 = 0
    jumate1 = "analizei complexe matematice"
    jumate2 = "unui joc bun pe calculator"

    print("Ti-ar place sa inveti despre ontologia cuvintelor in detrimentul analizei complexe matematice?\ny/n")
    myinput = input()
    if myinput == 'y' or myinput == 'Y':
        intrebare1 = 1
        jumate1 = "sa inveti despre ontologia cuvintelor"

    print("Stai mai mult cu telefonul in mana in detrimentul unui joc bun pe calculator?\ny/n")
    myinput = input()
    if myinput == 'y' or myinput == 'Y':
        intrebare2 = 1
        jumate2 = "mult cu telefonul in mana"
    print("Ti-ar place",jumate1, "in detrimentul", jumate2, "?\ny/n")
    myinput = input()
    if myinput == 'y' or myinput == 'Y':
        if intrebare1 == 1:
            print("Am ales pentru tine materia: Programare bazată pe reguli")
        if intrebare1 == 0:
            print("Am ales pentru tine materia: Aspecte computaţionale în teoria numerelor")
    else:
        if intrebare2 == 1:
            print("Am ales pentru tine materia: Tehnici de programare pe platforma Android")
        if intrebare2 == 0:
            print("Am ales pentru tine materia: Proiectarea jocurilor")

def pachet2():
    intrebare1 = 0
    intrebare2 = 0
    jumate1 = "intelegerii tehonogiei cloud"
    jumate2 = "modului de a comunica in mediul profesional"

    print("Stai mai mult pe retelele sociale in detrimentul intelegerii tehonogiei cloud?\ny/n")
    myinput = input()
    if myinput == 'y' or myinput == 'Y':
        intrebare1 = 1
        jumate1 = "retelele sociale"

    print("Ti-ar place sa inveti dedesubturile limbajului natural in detrimentul modului de a comunica in mediul profesional?\ny/n")
    myinput = input()
    if myinput == 'y' or myinput == 'Y':
        intrebare2 = 1
        jumate2 = "sa inveti dedesubturile limbajului natural"
    print("Ti-ar place",jumate1, "in detrimentul", jumate2, "?\ny/n")
    myinput = input()
    if myinput == 'y' or myinput == 'Y':
        if intrebare1 == 1:
            print("Am ales pentru tine materia: Analiza reţelelor media sociale ")
        if intrebare1 == 0:
            print("Am ales pentru tine materia: Cloud Computing")
    else:
        if intrebare2 == 1:
            print("Am ales pentru tine materia: Tehnici de ingineria limbajului natural")
        if intrebare2 == 0:
            print("Am ales pentru tine materia: Psihologia comunicării profesionale în domeniul IT-lui")

def pachet3():
    intrebare1 = 0
    intrebare2 = 0
    jumate1 = "participarii in consursuri captvante de informatica"
    jumate2 = "atacurile cibernetice asupra cardurilor"

    print("Ti-ar place sa inveti tainele retelelor perti in detrimentul participarii in consursuri captvante de informatica?\ny/n")
    myinput = input()
    if myinput == 'y' or myinput == 'Y':
        intrebare1 = 1
        jumate1 = "sa inveti tainele retelelor perti"

    print("doresti sa inveti despre atacurile cibernetice asupra cardurilor in detrimentul aprofundarii cunostintelor despre framework-ul .NET?\ny/n")
    myinput = input()
    if myinput == 'y' or myinput == 'Y':
        intrebare2 = 1
        jumate2 = "aprofundarii cunostintelor despre framework-ul .NET"
    print("Ti-ar place",jumate1, "in detrimentul", jumate2, "?\ny/n")
    myinput = input()
    if myinput == 'y' or myinput == 'Y':
        if intrebare1 == 1:
            print("Am ales pentru tine materia: Reţele Petri şi aplicaţi")
        if intrebare1 == 0:
            print("Am ales pentru tine materia: Programare competitivă")
    else:
        if intrebare2 == 1:
            print("Am ales pentru tine materia: Smart Card-uri şi Aplicaţii")
        if intrebare2 == 0:
            print("Am ales pentru tine materia: Topici speciale de programare .NET")

def rulare():
    pachet1()
    pachet2()
    pachet3()

rulare()