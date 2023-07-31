glicose: float

glicose = input('Digite a medidade da glicose: ')

if float(glicose) <= 100:
    print('Classificação : normal')
else:
    if float(glicose) > 100 and float(glicose) <=140:
        print("Classificação : Elevado")
    else:
        print("Classificação : Diabetes")