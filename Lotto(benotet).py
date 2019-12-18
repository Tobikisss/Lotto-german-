from random import randint

programwahl=str(input('Wählen sie das, was das Programm machen soll.\n"Def" um die Lottozahlen und ihre Zahlen ziehen zu lassen.\n"Auto" um die Zahlen von selbst miteinadner vergleichen zu lassen und ihnen die Anzahl an richtig getippten aunzugeben.\n"Fullauto" um das Programm von selbst laufen zu lassen und ihnen die Prozentuale Gewinnchance mitzuteilen.\n Bitte Eingeben: '))
#Programm um Lotto manuell zu spielen.
if programwahl=='Def':
    #Eingabe des Users an dem was er als Zahlen setzen will
    usr=[]
    z=1
    print('Welche Zahlen setzen sie (es dürfen NICHT 2-mal die Gleichen Zahlen gesetzt weren)?')
    for i in range (6):
        userzahlen=int(input(z))
        usr.append(userzahlen)
        z=z+1
    #Festlegung der Lottozahlen
    z1=randint(1,49)
    z2=randint(1,49)
    while z2==z1:
        z2=randint(1,49)
    z3=randint(1,49)
    while z3==z2 or z3==z1:
        z3=randint(1,49)
    z4=randint(1,49)
    while z4==z1 or z4==z2 or z4==z3:
        z4=randint(1,49)
    z5=randint(1,49)
    while z5==z1 or z5==z2 or z5==z3 or z5==z4:
        z5=randint(1,49)
    z6=randint(1,49)
    while z6==z1 or z6==z2 or z6==z3 or z6==z4 or z6==z5:
        z6=randint(1,49)
    Lottozahlen=[z1,z2,z3,z4,z5,z6]
    print('ihre Eingabe: ',usr,'\ndie Lotto-Zahlen: ', Lottozahlen)

#Programm um Automatisch lotto zu spielen
elif programwahl=='Auto':
    #Eingabe des Users an dem was er als Zahlen setzen will
    usr=[]
    z=1
    Tippedrightcount=0
    print('Welche Zahlen setzen sie (es dürfen NICHT 2-mal die Gleichen Zahlen gesetzt weren)?')
    for i in range (6):
        userzahlen=int(input(z))
        usr.append(userzahlen)
        z=z+1
    #Festlegung der Lottozahlen
    z1=randint(1,49)
    z2=randint(1,49)
    while z2==z1:
        z2=randint(1,49)
    z3=randint(1,49)
    while z3==z2 or z3==z1:
        z3=randint(1,49)
    z4=randint(1,49)
    while z4==z1 or z4==z2 or z4==z3:
        z4=randint(1,49)
    z5=randint(1,49)
    while z5==z1 or z5==z2 or z5==z3 or z5==z4:
        z5=randint(1,49)
    z6=randint(1,49)
    while z6==z1 or z6==z2 or z6==z3 or z6==z4 or z6==z5:
        z6=randint(1,49)
    Lottozahlen=[z1,z2,z3,z4,z5,z6]
    if z1==usr[0] or z1==usr[1] or z1==usr[2] or z1==usr[3] or z1==usr[4] or z1==usr[5]:
        Tippedrightcount=Tippedrightcount+1
    if z2==usr[0] or z2==usr[1] or z2==usr[2] or z2==usr[3] or z2==usr[4] or z2==usr[5]:
        Tippedrightcount=Tippedrightcount+1
    if z3==usr[0] or z3==usr[1] or z3==usr[2] or z3==usr[3] or z3==usr[4] or z3==usr[5]:
        Tippedrightcount=Tippedrightcount+1
    if z4==usr[0] or z4==usr[1] or z4==usr[2] or z4==usr[3] or z4==usr[4] or z4==usr[5]:
        Tippedrightcount=Tippedrightcount+1
    if z5==usr[0] or z5==usr[1] or z5==usr[2] or z5==usr[3] or z5==usr[4] or z5==usr[5]:
        Tippedrightcount=Tippedrightcount+1
    if z6==usr[0] or z6==usr[1] or z6==usr[2] or z6==usr[3] or z6==usr[4] or z6==usr[5]:
        Tippedrightcount=Tippedrightcount+1
    print('ihre Eingabe: ',usr,'\ndie Lotto-Zahlen: ', Lottozahlen,'\n\nSie haben ',Tippedrightcount,' richt getippt.')
#Programm Welches Automatisch lotto spielt und die chance einen richtig zu setzen berechnet
elif programwahl=='Fullauto':
    #festlegung an versuchen welche das Programm hat
    usr=[]
    z=1
    Tippedrightcount=0
    versuche=int(input('Wieoft soll das Lottospiel simuliert werden?'))
    #festlegung an den Zahlen auf die der Spieler setzt
    print('Welche Zahlen setzen sie (es dürfen NICHT 2-mal die Gleichen Zahlen gesetzt weren)?')
    for i in range (6):
        userzahlen=int(input(z))
        usr.append(userzahlen)
        z=z+1
    #Random Lottozahlen werden gezogen
    for i in range(versuche):
        z1=randint(1,49)
        z2=randint(1,49)
        while z2==z1:
            z2=randint(1,49)
        z3=randint(1,49)
        while z3==z2 or z3==z1:
            z3=randint(1,49)
        z4=randint(1,49)
        while z4==z1 or z4==z2 or z4==z3:
            z4=randint(1,49)
        z5=randint(1,49)
        while z5==z1 or z5==z2 or z5==z3 or z5==z4:
            z5=randint(1,49)
        z6=randint(1,49)
        while z6==z1 or z6==z2 or z6==z3 or z6==z4 or z6==z5:
            z6=randint(1,49)
        Lottozahlen=[z1,z2,z3,z4,z5,z6]
        #es wird geguckt wieoft der user einen richtig gesetzt hat
        if z1==usr[0] or z1==usr[1] or z1==usr[2] or z1==usr[3] or z1==usr[4] or z1==usr[5]:
            Tippedrightcount=Tippedrightcount+1
        if z2==usr[0] or z2==usr[1] or z2==usr[2] or z2==usr[3] or z2==usr[4] or z2==usr[5]:
            Tippedrightcount=Tippedrightcount+1
        if z3==usr[0] or z3==usr[1] or z3==usr[2] or z3==usr[3] or z3==usr[4] or z3==usr[5]:
            Tippedrightcount=Tippedrightcount+1
        if z4==usr[0] or z4==usr[1] or z4==usr[2] or z4==usr[3] or z4==usr[4] or z4==usr[5]:
            Tippedrightcount=Tippedrightcount+1
        if z5==usr[0] or z5==usr[1] or z5==usr[2] or z5==usr[3] or z5==usr[4] or z5==usr[5]:
            Tippedrightcount=Tippedrightcount+1
        if z6==usr[0] or z6==usr[1] or z6==usr[2] or z6==usr[3] or z6==usr[4] or z6==usr[5]:
            Tippedrightcount=Tippedrightcount+1
    #Ausgabe
    if not Tippedrightcount==0:
        print('ihre Eingabe: ',usr,'\ndie Lotto-Zahlen: ', Lottozahlen,'\n\nSie haben ',Tippedrightcount,' richt getippt. Bei', versuche, 'versuchen. Die Prozentuale chance auf 1-mal richtig getippt war' ,versuche/Tippedrightcount,'%')
    else:
        print('Sie haben kein einzigen richtig getippt. suchen sie sich einen Job, mit Glücksspiel wird es bei ihnen nichts wird....')
#©Tobikiss. https://github.com/Tobikisss/Lotto-german-
