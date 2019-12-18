from random import randint

programwahl=str(input('Wählen sie das, was das Programm machen soll.\n"Def" um die Lottozahlen und ihre Zahlen ziehen zu lassen.\n"Auto" um die Zahlen von selbst miteinadner vergleichen zu lassen und ihnen die Anzahl an richtig getippten aunzugeben.\n"Fullauto" um das Programm von selbst laufen zu lassen und ihnen die Prozentuale Gewinnchance mitzuteilen.\n"Regeln" um das Regelwerk des Programmes, sowie eine Einleitung zu bekommen.\n Bitte Eingeben: '))
#Programm um Lotto manuell zu spielen.
if programwahl=='Def':
    #Eingabe des Users an dem was er als Zahlen setzen will
    usr=[]
    z=1
    print('Welche Zahlen setzen sie (es dürfen NICHT 2-mal die Gleichen Zahlen gesetzt weren)?')
    for i in range (6):
        print('Ihre ' ,z,'. Zahl?(Bitte eingeben)')
        userzahlen=int(input())
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
        print('Ihre ' ,z,'. Zahl?(Bitte eingeben)')
        userzahlen=int(input())
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
        print('Ihre ' ,z,'. Zahl?(Bitte eingeben)')
        userzahlen=int(input())
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
        print('ihre Eingabe: ',usr,'\ndie Lotto-Zahlen: ',Lottozahlen,'\n\nSie haben ',Tippedrightcount,' richt getippt. Bei', versuche, 'Versuchen. Die prozentuale Chance auf 1-mal richtig gesetzt zu haben war' ,versuche/Tippedrightcount,'%')
    else:
        print('Sie haben kein einzigen richtig getippt. suchen sie sich einen Job, mit Glücksspiel wird es bei ihnen nichts wird....')
#Zusatz um den Spieler zu erklären wie er Spielt und wie die Regeln sind. Because, why not?
elif programwahl=='Regeln':
    print('Hier finden sie die Regeln, sowie eine Einführung in das Programm.')
    roe=str(input('Bitte Geben Sie entweder "Regeln" für die Regeln oder "Einführung" für eine Einführung ein: '))
    if roe=='Regeln':
        print('1. die Lottozahlen gehen nur von 1 bis 49. Wenn sie also Zahlen über 49 haben wird die Wahrscheinlichkeit mit dieser Zahl zu gewinnen gleich null.\n2. Bei der Abfrage nach ihren Zahlen auf welche sie Setzen möchten, dürfen sie nicht eine Zahl mehrfach verwenden da sonst im Programmmnenü Auto und Fullauto das Programm abstürtzt.\n3.drücken sie immer Enter um ihre eingabe zu bestätigen.')
        print('Bitte starten sie das Programm neu')
    elif roe=='Einführung':
        print('Willkommen in der Einführun im Programm. Hier erfahren Sie wie sie mein Programm benutzen.\n\n1. Einleitung:\nAm Anfang bietet das Programm ihnen die Möglichkeit eine seiner verschiedenen FUnktionen auszuwählen. Folgende Eingaben führen zu den Verschiedenen Funktionen:\n\n1. "Def" Def wird als eingabe für Default ausgeschrieben genommen. Hierbei ist es ihnen lediglich möglich Ihre eigenen Zahlen mit Zufallszahlen zu vergleichen. Es wird ihnen aber nicht gesagt ob sie eins richtig gesetzt haben.\n\n2. "Auto" wird ihnen als Auswahlmöglichkeit gegeben um wie in "Def" ihre eigenen Zahlen mit den Zufallszahlen zu vergleichen und gibt zusätzlich an wieviele sie richtig gesetzt haben.\n\n3. "Fullauto" wird ihnen angeboten damit sie ihre eigenen Zahlen in mehreren durchläufen automatisch die richtig Gesetzten anzugeben. Ebenfalls gibt es ihnen eine prozentuale Chance aus, welche anhand ihrer Eingabe berechnet wird.\n\n')  
        print('Bitte starten sie das Programm neu')
    else:
        print('Bitte neustarten und Eingabe ohne Fehler eingeben.')
else:
    print('Bitte neustarten und Eingabe ohne Fehler eingeben.')
#©Tobikiss. https://github.com/Tobikisss/Lotto-german-
