import fractions

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
    

def mul_frac(frac1, frac2):
    frac = [frac1[0] * frac2[0], frac1[1]*frac2[1]]
    nwd = fractions.gcd(frac[0], frac[1])
    frac[0] = frac[0]/nwd
    frac[1] = frac[1]/nwd
    return frac

def div_frac(frac1, frac2):
    frac = [frac1[0] * frac2[1], frac1[1]*frac2[0]]
    nwd = fractions.gcd(frac[0], frac[1])
    frac[0] = frac[0]/nwd
    frac[1] = frac[1]/nwd
    return frac

def is_positive(frac):
    if frac[0] < 0 or frac[1] < 0:
        return False
    else:
        return True

def is_zero(frac):
    if frac[0] == 0:
        return True
    elif frac[1] == 0:
        print("Nie dzielimy przez 0!")
        return -1
    else:
        return False

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

def frac2float(frac):
    return float(frac[0])/float(frac[1])