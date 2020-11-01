import random

class Table:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.content = []
        colours = {0:"Red", 1:"Green", 2:"Blue"}
        i = 1
        for row in range(rows):
            list_name = "row"+str(i)
            list_name = []
            for column in range(columns):
                colour = colours[random.randint(0, 2)]
                list_name.append(colour)
            i += 1
            self.content.append(list_name)

    def print_table(self):
        for i in range(self.rows):
            print(self.content[i])
    
    print("this")
    

while True:
    print("Incepe prin stabilirea numarului de randuri si coloane pentru tabel...")
    numar_randuri = int(input("\n\nCate randuri?\n"))
    numar_coloane = int(input("\n\nCate coloane?\n"))
    tabel = Table(numar_randuri, numar_coloane)
    print("\n\nAcesta este tabelul creat, completat automat in mod aleatoriu cu una dintre culorile Red, Green sau Blue\n")
    tabel.print_table()
    print("\nCare rand vrei sa-l vezi individual?")
    rand = int(input("\nRandul...")) - 1
    print(tabel.content[rand])
    print("\nCare coloana din randul {} vrei sa o vezi individual?".format(rand))
    coloana = int(input("\nCare coloana...")) - 1
    randul_selectat = tabel.content[rand]
    print(randul_selectat[coloana])
    raspuns = input("\nexit?")
    if raspuns == "yes":
        break
