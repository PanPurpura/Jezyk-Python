# Laboratorium nr. 5
# Zadanie 5.2

# Stworzyæ plik fracs.py i zapisaæ w nim funkcje do dzia³añ na u³amkach.
# U³amek bêdzie reprezentowany przez listê dwóch liczb ca³kowitych [licznik, mianownik].
# Napisaæ kod testuj¹cy modu³ fracs. Nie nale¿y korzystaæ z klasy Fraction z modu³u fractions. 
# Mo¿na wykorzystaæ funkcjê fractions.gcd() implementuj¹c¹ algorytm Euklidesa.

# We wszystkich przypadkach gdzie to bylo mozliwe, zastosowalem skracanie ulamkow.

import fractions

# Funkcja dodajaca dwa ulamki, u1 + u2.
def add_frac(frac1, frac2):
    nwd = fractions.gcd(frac1[1], frac2[1])
    nww = frac1[1]*frac2[1]/nwd
    if nwd == frac1[1] and nwd == frac2[1]:
        frac = [frac1[0] + frac2[0], nww]
    elif nwd == frac1[1]:
        pom = frac2[1]/nwd
        frac = [frac1[0]*pom + frac2[0], nww]
    elif nwd == frac2[1]:
        pom = frac1[1]/nwd
        frac = [frac1[0] + frac2[0]*pom, nww]
    else:
        frac = [frac1[0]*(frac2[1]/nwd) + frac2[0]*(frac1[1]/nwd), nww]

    skr = fractions.gcd(frac[0], frac[1])
    frac[0] = frac[0]/skr
    frac[1] = frac[1]/skr
    return frac

# Funkcja odejmujaca dwa ulamki, u1 - u2.
def sub_frac(frac1, frac2):
    nwd = fractions.gcd(frac1[1], frac2[1])
    nww = frac1[1]*frac2[1]/nwd
    if nwd == frac1[1] and nwd == frac2[1]:
        frac = [frac1[0] - frac2[0], nww]
    elif nwd == frac1[1]:
        pom = frac2[1]/nwd
        frac = [frac1[0]*pom - frac2[0], nww]
    elif nwd == frac2[1]:
        pom = frac1[1]/nwd
        frac = [frac1[0] - frac2[0]*pom, nww]
    else:
        frac = [frac1[0]*(frac2[1]/nwd) - frac2[0]*(frac1[1]/nwd), nww]

    skr = fractions.gcd(frac[0], frac[1])
    frac[0] = frac[0]/skr
    frac[1] = frac[1]/skr
    return frac
    
# Funkcja mnozaca dwa ulamki, u1 * u2
def mul_frac(frac1, frac2):
    frac = [frac1[0] * frac2[0], frac1[1]*frac2[1]]
    nwd = fractions.gcd(frac[0], frac[1])
    frac[0] = frac[0]/nwd
    frac[1] = frac[1]/nwd
    return frac

# Funkcja dzielaca dwa ulamki, u1 / u2
def div_frac(frac1, frac2):
    frac = [frac1[0] * frac2[1], frac1[1]*frac2[0]]
    nwd = fractions.gcd(frac[0], frac[1])
    frac[0] = frac[0]/nwd
    frac[1] = frac[1]/nwd
    return frac

# Funkcja sprawdzajaca czy ulamek jest dodatni.
def is_positive(frac):
    if frac[0] < 0 or frac[1] < 0:
        return False
    else:
        return True

# Funkcja sprawdzajaca czy ulamek daje 0.
def is_zero(frac):
    if frac[0] == 0:
        return True
    elif frac[1] == 0:
        print("Nie dzielimy przez 0!")
        return -1
    else:
        return False

# Funkcja porownujaca dwa ulamki.
def cmp_frac(frac1, frac2):
    if frac1[0] == frac2[0]:
        if frac1[1] < frac2[1]:
            return 1
        elif frac1[1] > frac2[1]:
            return -1
        else:
            return 0
    elif frac1[1] == frac2[1]:
        if frac1[0] > frac2[0]:
            return 1
        elif frac1[0] < frac2[0]:
            return -1
        else:
            return 0
    else:
        nwd = fractions.gcd(frac1[1], frac2[1])
        nww = frac1[1]*frac2[1]/nwd
        frac1[0], frac1[1] = frac1[0]*(nww/frac1[1]), nww
        frac2[0], frac2[1] = frac2[0]*(nww/frac2[1]), nww
        if frac1[0] > frac2[0]:
            return 1
        elif frac1[0] < frac2[0]:
            return -1
        else:
            return 0

# Funkcja konwertujaca ulamek na float.
def frac2float(frac):
    return float(frac[0])/float(frac[1])