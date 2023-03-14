"""
 wprowadzanie danych
"""
reguly_prod = []
symbole_pocz = []
reguly = str(input())
stan = ";"
reguly.strip()
reguly = reguly.replace(",", " ")
reguly = reguly.replace(";", " ; ")
reguly = reguly.replace(">", " > ")
reguly = reguly.split()
zmienna_pomocnicza = 0

for i in range(0, len(reguly)):
    match reguly[i]:
        case ";":
            stan = ";"
            zmienna_pomocnicza = zmienna_pomocnicza + 1
        case ">":
            stan = ">"
        case _:
            match stan:
                case ";":
                    symbole_pocz.append(reguly[i])
                    reguly_prod.append([])
                case ">":
                    reguly_prod[zmienna_pomocnicza].append(reguly[i])

"""
    utwożenie tabeli
"""
slowo = str(input())
tabela = []
for i in range(len(slowo)):
    tabela.append([])
    for x in range(len(slowo) - i):
        tabela[i].append([])


"""
    Wypełnienie pierwszego wiersza
"""
for i in range(len(tabela[0])):
    for x in range(len(reguly_prod)):
        for y in range(len(reguly_prod[x])):
            if slowo[i] == reguly_prod[x][y] and symbole_pocz[x] not in tabela[0][i]:
                tabela[0][i].append(symbole_pocz[x])

for i in range(1, len(tabela)):
    for x in range(len(tabela[i])):
        for a in range(i):
            for b in range(len(tabela[a][x])):
                for c in range(len(tabela[i - (a + 1)][x + a + 1])):
                    for y in range(len(reguly_prod)):
                        for z in range(len(reguly_prod[y])):
                            if (
                                tabela[a][x][b] + tabela[i - (a + 1)][x + (a + 1)][c]
                                == reguly_prod[y][z]
                            ):
                                if symbole_pocz[y] not in tabela[i][x]:
                                    tabela[i][x].append(symbole_pocz[y])


for i in range(len(tabela)):
    print(tabela[i])
