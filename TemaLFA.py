from collections import deque

def citire_date():
    fin = open("automat.txt","r")

    #STARE INITIALA
    ns = int(fin.readline())

    #NR. STARI FINALE
    nr_final = int(fin.readline())

    final = []
    #CITIREA STARILOR FINALE
    for i in range(nr_final):
        stare = int(fin.readline())
        final.append(stare)

    nr_tranzitii = int(fin.readline())
    nr_noduri = int(fin.readline())

    A = [[0 for i in range(nr_noduri)] for i in range(nr_noduri)]
    i = 0
    while i != nr_tranzitii:
        data = fin.readline().split()
        A[int(data[0])][int(data[1])] = data[2:]
        i+=len(data[2:])

    fin.close()

    return A, ns, final, nr_noduri

def automat(cuvant, stare):
    coada = deque([])
    if len(cuvant) == 0 and stare in final:
        mesaj.append("CUVANTUL A FOST ACCEPTAT")


    elif len(cuvant) != 0:
        for i in range(nr_noduri):
            if A[stare][i] != 0:
                if cuvant[0] in A[stare][i]:
                    coada.append(i)

        while len(coada) != 0:
            stare_urm = coada.popleft()
            automat(cuvant[1:],stare_urm)

mesaj = ["CUVANTUL NU A FOST ACCEPTAT"]
A ,ns, final, nr_noduri = citire_date()
cuvant = input("Introduceti cuvantul: ")
automat(cuvant,ns)
print(mesaj[-1])


