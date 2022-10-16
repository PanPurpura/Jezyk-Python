# Cwiczenia nr. 2 - jezyk python
# Zadania 2.10 - 2.19 

# cw. 2.10
# Mamy dany napis wielowierszowy line. Podaæ sposób obliczenia liczby wyrazów w napisie.
# Przez wyraz rozumiemy ci¹g "czarnych" znaków,
# oddzielony od innych wyrazów bia³ymi znakami (spacja, tabulacja, newline).

def _2_10(line):   
    l = line.split()
    return len(l)

# cw. 2.11
# Podaæ sposób wyœwietlania napisu word tak,
# aby jego znaki by³y rozdzielone znakiem podkreœlenia.

def _2_11():
    word = "harbinger"
    new_ = ""
    for i in word:
        new_ = new_ + i + "_"
    print(new_)

# cw. 2.12
# Zbudowaæ napis stworzony z pierwszych znaków wyrazów z wiersza line.
# Zbudowaæ napis stworzony z ostatnich znaków wyrazów z wiersza line.

def _2_12(line):
    l = line.split()
    new_line_first = ""
    new_line_last = ""
    for i in l:
        new_line_first += i[0] 
        new_line_last += i[len(i)-1]
    print("Z pierwszych liter: {}".format(new_line_first))
    print("Z ostatnich liter: {}".format(new_line_last))

# cw. 2.13
# ZnaleŸæ ³¹czn¹ d³ugoœæ wyrazów w napisie line.
# Wskazówka: mo¿na skorzystaæ z funkcji sum().

def _2_13(line):
    l = line.split()
    sum = 0
    for i in l:
        sum += len(i)
    print("Laczna dlugosc wyrazow: {}".format(sum))

# cw. 2.14
# ZnaleŸæ: (a) najd³u¿szy wyraz,(b) d³ugoœæ najd³u¿szego wyrazu w napisie line.

def _2_14(line):
    l = line.split()
    count = 0
    new_line = ""
    for i in l:
        if(count < len(i)):
            count = len(i)
            new_line = i

    print("Najdluzszy wyraz: {}, jego dlugosc wynosi: {}".format(new_line, len(new_line)))

# cw. 2.15
# Na liœcie L znajduj¹ siê liczby ca³kowite dodatnie.
# Stworzyæ napis bêd¹cy ci¹giem cyfr kolejnych liczb z listy L.

def _2_15():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    li = []
    for i in l:
        li.append(str(i))
    line = "".join(li)
    print(line)

# cw. 2.16
# W tekœcie znajduj¹cym siê w zmiennej line zamieniæ ci¹g znaków "GvR" na "Guido van Rossum".

def _2_16():
    line = "GvR is a Dutch programmer best known as the creator of the Python. Everyone like GvR."
    line = line.replace("GvR", "Guido van Rossum")
    print(line)

# cw. 2.17
# Posortowaæ wyrazy z napisu line raz alfabetycznie, a raz pod wzglêdem d³ugoœci.
# Wskazówka: funkcja wbudowana sorted().

def _2_17(line):
    new_line = sorted(line.split(), key=str.lower)
    descendant = sorted(line.split(), key=str.lower, reverse=True)
    print("Alphabetically:\n{}".format(new_line))
    print("\nReverse:\n{}".format(descendant))

# cw. 2.18
# ZnaleŸæ liczbê cyfr zero w du¿ej liczbie ca³kowitej.
# Wskazówka: zamieniæ liczbê na napis.

def _2_18():
    number = 2064587065780246030043410
    line = str(number)
    count = 0
    for i in line:
        if(i == '0'):
            count += 1 
    print("Wystapienia cyfry 0: {}".format(count))

# cw. 2.19
# Na liœcie L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
# Chcemy zbudowaæ napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe bêd¹ mia³y blok dope³niony zerami,
# np. 007, 024. Wskazówka: str.zfill().

def _2_19():
    l = [385, 2, 5, 67, 7, 999, 135, 23, 61, 8, 111, 0, 12, 821, 780, 15]
    li = []
    for i in l:
        if(len(str(i)) < 3):
            li.append(str(i).zfill(3))
        else:
            li.append(str(i))
    line = "".join(li)
    print(line)

# Sprawdzenie dzialania poszczegolnych zadan poprzez odwolania do funkcji:

line = "neque   porro quisquam est qui dolorem    ipsum quia dolor sit amet consectetur      adipisci velit"
print("=== cw 2.10 ===")
print("Liczba wyrazow = {}".format(_2_10(line)))
print("\n=== cw 2.11 ===")
_2_11()
print("\n=== cw 2.12 ===")
_2_12(line)
print("\n=== cw 2.13 ===")
_2_13(line)
print("\n=== cw 2.14 ===")
_2_14(line)
print("\n=== cw 2.15 ===")
_2_15()
print("\n=== cw 2.16 ===")
_2_16()
print("\n=== cw 2.17 ===")
_2_17(line)
print("\n=== cw 2.18 ===")
_2_18()
print("\n=== cw 2.19 ===")
_2_19()
