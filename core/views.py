from django.shortcuts import render
import string
from random import choice
from django.http import JsonResponse
import copy
import random


def home(request):
  return render(request,'core/home.html')


def generator(request):
    return render(request,'core/generator.html')

def password(request):
    if request.method == 'POST':
        length = int(request.POST.get('length'))
        uppercase = request.POST.get('uppercase')
        symbols = request.POST.get('symbols')
        numbers = request.POST.get('numbers')
        lowercase = request.POST.get('lowercase')
        chars = []
        if(lowercase):
            chars.extend(string.ascii_lowercase)
        if(uppercase):
            chars.extend(string.ascii_uppercase)
        if(symbols):
            chars.extend('!@#$%^&*')
        if(numbers):
            chars.extend('1234567890')
        generated_PASS = ''
        if(numbers or lowercase or symbols or uppercase):
            for x in range(length):
                generated_PASS += choice(chars)
        else:
            generated_PASS = 'zaznacz cos wrr'
        return JsonResponse({'password': generated_PASS})
    






def greibach(request):
    if request.method == 'POST':
        def usuwanie_regul_bezuzytecznych(zmienna1, zmienna2, zmienna3):
            """
                sprawdzenie które symbole się redukuja
            """
            symbole_red = []
            for i in (range(len(zmienna2))):
                for x in range(len(zmienna1[i])):
                    if zmienna2[i] not in zmienna1[i][x]:
                        symbole_red.append(zmienna2[i])
                        break

            """
                    sprawdzenie ktore symbole są produkowane
            """
            symbole_prod = [zmienna2[0]]
            while True:
                lista_pomocznicza = symbole_prod.copy()
                for i in range(0, len(symbole_prod)):
                    index = zmienna2.index(symbole_prod[i])
                    for x in range(len(zmienna1[index])):
                        for y in range(len(zmienna1[index][x])):
                            if zmienna1[index][x][y] in zmienna2 and zmienna1[index][x][y] not in symbole_prod:
                                symbole_prod.append(zmienna1[index][x][y])

                if lista_pomocznicza == symbole_prod:
                    break
            """
                sprawdzenie czy symbole sa uzyteczne oraz usuiecie symboli bezuzytecznych
            """
            for i in reversed(range(len(zmienna2))):
                if zmienna2[i] not in symbole_red:
                    symbole_prod.pop(i)

            for i in reversed(range(len(zmienna2))):
                if zmienna2[i] not in symbole_prod:
                    zmienna1.pop(i)
                    zmienna2.pop(i)
                    continue
                else:
                    for x in reversed(range(len(zmienna1[i]))):
                        for y in range(len(zmienna1[i][x])):
                            if zmienna1[i][x][y] not in symbole_prod and zmienna1[i][x][y] not in zmienna3:
                                zmienna1[i].pop(x)
                                break

        """
        wprowadzanie danych
        """
        terminalne = []
        reguly_prod = []
        symbole_pocz = []
        reguly = request.POST.get('regulyGreibach')
        stan = str("początek")
        reguly.strip()
        reguly = reguly.replace(",", " ")
        reguly = reguly.replace(";", " ; ")
        reguly = reguly.replace(">", " > ")
        reguly = reguly.split()
        zmienna_pomocnicza = -1
        for i in range(0, len(reguly)):
            match reguly[i]:
                case ";":
                    stan = ";"
                    zmienna_pomocnicza = zmienna_pomocnicza + 1
                case ">":
                    stan = ">"
                case _:
                    match stan:
                        case "początek":
                            terminalne.append(reguly[i])
                        case ";":
                            symbole_pocz.append(reguly[i])
                            reguly_prod.append([])
                        case ">":
                            reguly_prod[zmienna_pomocnicza].append(reguly[i])

        """
            usuwanie lambdy
        """
        usuwanie_regul_bezuzytecznych(reguly_prod, symbole_pocz, terminalne)

        for i in range(len(reguly_prod)):
            for x in range(len(reguly_prod[i])):
                if "^" in reguly_prod[i][x]:
                    for a in range(len(reguly_prod)):
                        for b in range(len(reguly_prod[a])):
                            if symbole_pocz[i] in reguly_prod[a][b]:
                                reguly_prod[a][b] = reguly_prod[a][b].replace(symbole_pocz[i], reguly_prod[i][x])
                                reguly_prod[i].pop(x)
        for i in range(0, len(reguly_prod)):
            for x in range(0, len(reguly_prod[i])):
                if "^" in reguly_prod[i][x]:
                    reguly_prod[i][x] = reguly_prod[i][x].replace("^", "")

        """
            lemat 2
        """

        for i in range(len(reguly_prod)):
            lista_pomocznicza = []
            for x in range(len((reguly_prod[i]))):
                if reguly_prod[i][x][0] == symbole_pocz[i]:
                    lista_pomocznicza.append("alfa")
                else:
                    lista_pomocznicza.append("beta")

            if "alfa" not in lista_pomocznicza:
                continue
            else:
                reguly_prod.append([])
                while True:
                    nowy_symbol = chr(random.randint(65, 90))
                    if nowy_symbol not in symbole_pocz:
                        break
                symbole_pocz.append(nowy_symbol)
                for x in reversed(range(len(lista_pomocznicza))):
                    if lista_pomocznicza[x] == "alfa":
                        reguly_prod[-1].append(reguly_prod[i][x][1:] + symbole_pocz[-1])
                        reguly_prod[-1].append(reguly_prod[i][x][1:])
                    else:
                        reguly_prod[i].append(reguly_prod[i][x]+symbole_pocz[-1])
                        reguly_prod[i].append(reguly_prod[i][x])
                    reguly_prod[i].pop(x)

        """
            pozostale przeksztalcenia
        """
        while True:
            lista_pomocznicza = copy.deepcopy(reguly_prod)

            for i in range(len(terminalne)):
                flag = "0"
                for x in range(len(reguly_prod)):
                    if len(reguly_prod[x]) == 1 and reguly_prod[x][0] == terminalne[i]:
                        flag = "1"
                if flag == "1":
                    continue
                while True:
                    nowy_symbol = chr(random.randint(65, 90))
                    if nowy_symbol not in symbole_pocz:
                        break
                symbole_pocz.append(nowy_symbol)
                reguly_prod.append([terminalne[i]])

            for i in range(len(reguly_prod)):
                for x in range(len(reguly_prod[i])):
                    for y in range(1, len(reguly_prod[i][x])):
                        if reguly_prod[i][x][y] in terminalne:
                            for z in range(len(reguly_prod)):
                                if len(reguly_prod[z]) == 1 and reguly_prod[z][0] == reguly_prod[i][x][y]:
                                    reguly_prod[i][x] = reguly_prod[i][x].replace(reguly_prod[i][x][y], symbole_pocz[z])

            for i in range(len(reguly_prod)):
                for x in reversed(range(len(reguly_prod[i]))):
                    if reguly_prod[i][x][0] != symbole_pocz[i] and reguly_prod[i][x][0] in symbole_pocz:
                        for y in range(len(symbole_pocz)):
                            if symbole_pocz[y] == reguly_prod[i][x][0]:
                                for z in range(len(reguly_prod[y])):
                                    reguly_prod[i].append(reguly_prod[y][z]+reguly_prod[i][x][1:])
                                reguly_prod[i].pop(x)

            if reguly_prod == lista_pomocznicza:
                break

        usuwanie_regul_bezuzytecznych(reguly_prod, symbole_pocz, terminalne)

        print(reguly_prod)
        print(symbole_pocz)

        wynikGr  = ""
        for i in range(len(symbole_pocz)):
            wynikGr += symbole_pocz[i] + " -> "
            for j in range(len(reguly_prod[i])):
                wynikGr += str(reguly_prod[i][j])
                if j != len(reguly_prod[i]) - 1:
                    wynikGr += " | "
            wynikGr += "\n"
        return JsonResponse({'wynikGreibach': wynikGr})
    return render(request,'core/greibach.html')

def chomsky(request):
    if request.method == 'POST':
        symbole_terminalne = []
        Reguły_produkcji = []
        oznaczenia_symboli = []
        reguly = request.POST.get('regulyChomsky')
        stan = str("początek")
        reguly.strip()
        reguly = reguly.replace(",", " ")
        reguly = reguly.replace(";", " ; ")
        reguly = reguly.replace(">", " > ")
        reguly = reguly.split()
        zmienna_pomocnicza = -1
        for i in range(0, len(reguly)):
            match reguly[i]:
                case ";":
                    stan = ";"
                    zmienna_pomocnicza = zmienna_pomocnicza + 1
                case ">":
                    stan = ">"
                case _:
                    match stan:
                        case "początek":
                            symbole_terminalne.append(reguly[i])
                        case ";":
                            oznaczenia_symboli.append(reguly[i])
                            Reguły_produkcji.append([])
                        case ">":
                            Reguły_produkcji[zmienna_pomocnicza].append(reguly[i])

        # Nie zmieniać
        symbole = []
        for i in range(0, len(Reguły_produkcji)):
            for x in range(0, len(Reguły_produkcji[i])):
                for a in range(0, len(Reguły_produkcji[i][x])):
                    if Reguły_produkcji[i][x][a] not in symbole:
                        symbole.append(Reguły_produkcji[i][x][a])

        """
        Skracanie długości produkcji do pordukowania
        1-2 symboli
        """
        for i in range(0, len(Reguły_produkcji)):
            for x in range(0, len(Reguły_produkcji[i])):
                if len(Reguły_produkcji[i][x]) == 1:
                    pass
                elif len(Reguły_produkcji[i][x]) == 2:
                    pass
                else:
                    while len(Reguły_produkcji[i][x]) > 2:
                        nowy_symbol_wejściowy = chr(random.randint(65, 91))
                        if nowy_symbol_wejściowy in oznaczenia_symboli:
                            nowy_symbol_wejściowy = chr(random.randint(65, 90))
                        else:

                            element = Reguły_produkcji[i][x][:-2] + nowy_symbol_wejściowy
                            lista_pomocnicza = [Reguły_produkcji[i][x][-2:]]
                            Reguły_produkcji.append(lista_pomocnicza)
                            Reguły_produkcji[i][x] = element
                        oznaczenia_symboli.append(nowy_symbol_wejściowy)

        """
        zamiana reguł produkcji produkujących 2 symbole w tym co najmniej 1 terminalny"
        """

        for i in range(0, len(symbole_terminalne)):
            zmienna_pomocnicza = 0
            for x in range(0, len(Reguły_produkcji)):
                if len(Reguły_produkcji[x]) == 1 and Reguły_produkcji[x][0] == symbole_terminalne[i]:
                    zmienna_pomocnicza = 1

            if zmienna_pomocnicza == 0:
                nowy_symbol_wejściowy = chr(random.randint(65, 90))
                if nowy_symbol_wejściowy in oznaczenia_symboli:
                    nowy_symbol_wejściowy = chr(random.randint(65, 90))
                else:
                    lista_pomocnicza = [symbole_terminalne[i]]
                    Reguły_produkcji.append(lista_pomocnicza)
                    oznaczenia_symboli.append(nowy_symbol_wejściowy)

        for i in range(0, len(Reguły_produkcji)):
            for x in range(0, len(Reguły_produkcji[i])):
                for a in range(0, len(Reguły_produkcji[i][x])):
                    if Reguły_produkcji[i][x][a] in symbole_terminalne and len(Reguły_produkcji[i][x]) != 1:
                        for z in range(0, len(symbole_terminalne)):
                            for b in range(0, len(Reguły_produkcji)):
                                for c in range(0, len(Reguły_produkcji[b])):
                                    if Reguły_produkcji[b][c] == symbole_terminalne[z] and len(
                                            Reguły_produkcji[b]) == 1:
                                        Reguły_produkcji[i][x] = Reguły_produkcji[i][x].replace(
                                            symbole_terminalne[z], oznaczenia_symboli[b])
                    else:
                        pass

        """
        zastosowanie lematu 1
        """
        for i in range(0, len(Reguły_produkcji)):
            for x in range(0, len(Reguły_produkcji[i])):
                for a in range(0, len(Reguły_produkcji[i][x])):
                    if len(Reguły_produkcji[i][x]) == 1:
                        for b in range(0, len(Reguły_produkcji)):
                            if Reguły_produkcji[i][x] == oznaczenia_symboli[b]:
                                Reguły_produkcji[i].pop(x)
                                x = x - 1
                                for c in range(0, len(Reguły_produkcji[b])):
                                    Reguły_produkcji[i].append(Reguły_produkcji[b][c])

        """
        usnięcie lambdy
        """
        # lambda tymczasowo oznaczona symbolem ^
        for i in range(0, len(Reguły_produkcji)):
            for x in reversed(range(0, len(Reguły_produkcji[i]))):
                if "^" in Reguły_produkcji[i][x]:
                    for a in range(0, len(Reguły_produkcji)):
                        for b in range(0, len(Reguły_produkcji[a])):
                            if oznaczenia_symboli[i] in Reguły_produkcji[a][b]:
                                Reguły_produkcji[a][b] = Reguły_produkcji[a][b].replace(oznaczenia_symboli[i],
                                                                                        Reguły_produkcji[i][x])
                                Reguły_produkcji[i].pop(x)
        for i in range(0, len(Reguły_produkcji)):
            for x in reversed(range(0, len(Reguły_produkcji[i]))):
                if "^" in Reguły_produkcji[i][x]:
                    Reguły_produkcji[i][x] = Reguły_produkcji[i][x].replace("^", "")

        """
        usuwanie syboli bezuzytecznych

        """
        symbole_bezużyteczne = []
        symbole_użyteczne = [oznaczenia_symboli[0]]
        for i in range(0, len(oznaczenia_symboli)):
            lista_pomocnicza = []
            for x in range(0, len(Reguły_produkcji[i])):
                if oznaczenia_symboli[i] in Reguły_produkcji[i][x]:
                    lista_pomocnicza.append("0")
                else:
                    lista_pomocnicza.append("1")
            if "1" not in lista_pomocnicza:
                symbole_bezużyteczne.append(oznaczenia_symboli[i])

        for i in range(0, len(symbole_użyteczne)):
            index = oznaczenia_symboli.index(symbole_użyteczne[i])
            for x in range(0, len(Reguły_produkcji[index])):
                for a in range(0, len(Reguły_produkcji[index][x])):
                    if Reguły_produkcji[index][x][a] in oznaczenia_symboli:
                        symbole_użyteczne.append(Reguły_produkcji[index][x][a])

        for i in range(0, len(symbole)):
            if symbole[i] not in symbole_użyteczne and symbole[i] not in symbole_terminalne and symbole[
                i] not in symbole_bezużyteczne:
                symbole_bezużyteczne.append(symbole[i])

        for i in range(0, len(symbole)):
            if symbole[i] not in symbole_użyteczne:
                symbole_bezużyteczne.append(symbole[i])

        for u in range(0, len(symbole_bezużyteczne)):
            i = 0
            x = 0
            while i < len(Reguły_produkcji):
                while x < len(Reguły_produkcji[i]):
                    if symbole_bezużyteczne[u] in Reguły_produkcji[i][x]:
                        Reguły_produkcji[i].pop(x)
                        x = x - 1
                    x = x + 1
                if symbole_bezużyteczne[u] == oznaczenia_symboli[i]:
                    Reguły_produkcji.pop(i)
                    oznaczenia_symboli.pop(i)
                    i = i - 1
                i = i + 1
        wynikChomsky = ""
        for i in range(0, len(Reguły_produkcji)):
            wynikChomsky += oznaczenia_symboli[i] + "->"
            for x in range(0, len(Reguły_produkcji[i]) - 1):
                wynikChomsky += Reguły_produkcji[i][x] + "|"
            wynikChomsky += (Reguły_produkcji[i][-1])
        
        return JsonResponse({'wynikChomsky': wynikChomsky})
    return render(request, 'core/chomsky.html')




