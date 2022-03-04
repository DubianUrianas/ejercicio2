#*************************
#   manejo de listas
#*************************
from cgi import print_directory


def listas ():
    lista1 =[]
    lista2 =list()
    listasconelementos =[30,2000000,"Dubian Uriana", "Estudiante", True, ["magister", "Doctorado","Especializacion"] ]


    #print(listasconelementos)
    #utilizando el ciclo for
    for i in range(len(listasconelementos)):
        print(listasconelementos[i])

    print ("mostrando elementos con ciclo while")
    j=0
    while j< len(listasconelementos):
        print(listasconelementos[j])
        #j= j + 1
        j +=1

    listasconelementos[1]=listasconelementos[1]+200000

    print(listasconelementos[5][3])
    print(listasconelementos[-1][3])
    print(listasconelementos[0:3])#muestra las posicion desde la 0 hasta la 3
    print(listasconelementos[1:6:2])
    print(listasconelementos[0:6:2])

    listasconelementos.insert(2,["Sede Riohacha","Miguel soto"])
    print(listasconelementos)

    del (listasconelementos[2])
    print(listasconelementos)
    listasconelementos.remove("Docente")
    print(listasconelementos)
    
def main():
    listas()

if __name__== "__main__":
    main()