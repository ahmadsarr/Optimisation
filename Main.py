from time import time

from Modele import  Modele
from Node import Node
def exec():
    opti=Modele()
    print(" 1-Heuristique  Ordre croissant des prix des packs \nordre:{}  \nsolution :{}\nz={}\n\n".
          format(opti.ordeByPrix(),opti.heuristique(opti.ordeByPrix())[4],opti.heuristique(opti.ordeByPrix())[2]))

    print(" 2-Heuristique  Ordre croissant des prix des packs \nordre:{}  \nsolution :{}\nz={}\n\n".format(opti.orderByNombreHeure(),
          opti.heuristique(opti.orderByNombreHeure())[4],opti.heuristique(opti.orderByNombreHeure(False))[2]))

    print(" 3-Heuristique Ordre décroissant du nombre d’heures par packs \nordre:{}  \nsolution :{}\nz={}\n\n".format(opti.orderByRatioPrixSurNbHeure(),
          opti.heuristique(opti.orderByRatioPrixSurNbHeure(False))[4],opti.heuristique(opti.orderByRatioPrixSurNbHeure(False))[2]))

    print(" 4-Heuristique Ordre croissant du ratio (prix/nombre d’heures) \nordre:{}  \nsolution :{}\nz={}\n\n".format(opti.orderByRatioPrixSurNbHeure(),
          opti.heuristique(opti.orderByRatioPrixSurNbHeure(False))[4],opti.heuristique(opti.orderByRatioPrixSurNbHeure())[2]))

    print(" 5-La meilleur Heuristique  :{}\n\n".format(opti.bestHeuristique()[0]))
  #  input("entrez une touche pour continuer")
    s=opti.borneSUp()
    print("Q2-\nL’ordre initial{} \n la solution de la relaxation {} \nz={}\n\n".format(opti.orderByRatioPrixSurNbHeure(False),s[4],s[2]))
    deb=time()
    print("Debut parcours de noeud[bourne sup-sol relaxée]")
    s=opti.solve()
    print("Fin parcours")
    duree=time()-deb
    print("Q3-")
    print("La solution :{}\nl'objectif de la solution:{}\nz={}\n\n".format(s[0],s[2],s[1]))
    print("Le  nombre  de  nœuds  explorer  par  l’ordre  de  B&B :",Node.nbre)
    print("Temps d execution :%f"%duree)
    print("la solution  optimale{}\n Z:{}".format(s[0],s[1]))

if __name__=="__main__":
    exec()
