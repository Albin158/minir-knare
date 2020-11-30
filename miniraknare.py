def multiplication():
    print ('\nRkäna med multiplikation')
    tal1 = float(input('Skriv ett tal: '))
    tal2 = float(input('Skriv ett annat tal: '))
    summa = tal1 * tal2
    print(f'Summan av {tal1} * {tal2} är {summa}\n')
    
run = 0
    
while run != 5:
    print('[1] Räkna med +')
    print('[2] Räkna med -')
    print('[3] Räkna med *')
    print('[4] Valfritt arbete, om du vill')
    print('[5] Avsluta')

    try:
        run = int(input('Gör ett val: '))
    except:
        print('Felaktig inmatning \n')

    if run == 1:
print('\nRäkna med addition')
try:
    tal1 = float(input('Skriv ett tal: '))
    tal2 = float(input('Skriv ett andra tal: '))
    summa = tal1 + tal2
    print(f'Summan av {tal1} + {tal2} är {summa}\n')
    except:
        print('Felaktig inmatning.\n')

