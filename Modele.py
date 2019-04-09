from collections import  defaultdict
from operator import itemgetter
from time import  time

from Node import Node


class Modele:
    def __init__(self):
        self.data=defaultdict(lambda :[0,0])
        self.data["athletisme"]=[9,450]
        self.data["basket"]=[2,700]
        self.data["cyclisme"]=[3,350]
        self.data["football"]=[13,500]
        self.data["natation"]=[5,100]
        self.budget=1000
        self.zMax=self.borneSUp()
        self.initial=self.bestHeuristique()[1][0]

    def ordeByPrix(self,reverse=False):
        data = []
        for i, _ in sorted(self.data.items(), key=lambda v: v[1][1],reverse=reverse):
            data.append(i)
        return data
    def orderByNombreHeure(self,reverse=True):
        data = []
        for i, _ in sorted(self.data.items(), key=lambda v: v[1][0], reverse=reverse):
            data.append(i)
        return data
    def orderByRatioPrixSurNbHeure(self,reverse=True):
        data = []
        for i, _ in sorted(self.data.items(), key=lambda v: v[1][1]/v[1][0], reverse=reverse):
            data.append(i)
        return data
    def heuristique(self,data):
        z = self.budget
        i = 0
        bs = 0
        sport = []
        time = 0
        value = {k: 0 for k in data}
        while (z > 0 and i < len(data)):
            if (z >= self.data[data[i]][1]):
                z -= self.data[data[i]][1]
                bs += self.data[data[i]][1]
                sport.append(data[i])
                time += self.data[data[i]][0]
                value[data[i]]=1
            i += 1
        return sport, time, bs,len(sport),value

    def bestHeuristique(self):
         fontions={"Ordre croissant des prix des packs":self.heuristique(self.ordeByPrix())[2:4],
                   "Ordre décroissant du nombre d’heures par packs":self.heuristique(self.orderByNombreHeure())[2:4],
                   "Ordre décroissant du ratio (prix/nombre d’heures)":self.heuristique(self.orderByRatioPrixSurNbHeure())[2:4],
                   "Ordre croissant du ratio (prix/nombre d’heures)":self.heuristique(self.orderByRatioPrixSurNbHeure(False))[2:4]
                   }
         return sorted(fontions.items(),key=itemgetter(1),reverse=True)[0]
    def borneSUp(self):
        data=self.orderByRatioPrixSurNbHeure(False)
        value = {k: 1 for k in data}
        z = self.budget
        i = 0
        bs = 0
        sport = []
        time = 0
        while (z > 0 and i < len(data)):
            if (z >= self.data[data[i]][1]):
                z -= self.data[data[i]][1]
                bs += self.data[data[i]][1]
                sport.append(data[i])
                time += self.data[data[i]][0]
            else:
                bs +=z
                time += (z*self.data[data[i]][0])/self.data[data[i]][1]
                value[data[1]] = (z*self.data[data[i]][0])/self.data[data[i]][1]
                z=0
                sport.append(data[i])

            i += 1

        return sport, time, bs, len(sport),value

    def solve(self):
        keys=self.data.keys()

        value=list(self.data.values())
        datas = list(zip(keys, value))
        value = {k: 0 for k in keys}
        _, _, bs, *_ = self.borneSUp()
        root=Node(self.bestHeuristique()[1][0],self.borneSUp()[2],self.budget,datas,dict(value))
        l=[]
        _, _, bs, *_ = self.borneSUp()
        self.branchAndBoud(root,self.heuristique(self.ordeByPrix())[2],bs, l)
        #self.branchAndBoud(root,int(self.bestHeuristique()[1][0]),bs,l)
        sorted(l,key=itemgetter(1,2))
        return l[0]

    def branchAndBoud(self,node,inf,sup,l):
        g=node.gauche()
        d = node.droite()

        if(g==None and d==None):
            value,z,time=node.evaluate()
            if(z>=inf and z<sup ):
                l.append((value,z,time,node.nbNoeud))
            return
        if g!=None:
            self.branchAndBoud(g, inf, sup, l)
            print("G->",g.borne())
        if d!=None:
            self.branchAndBoud(d,inf,sup,l)
            print("D->{}".format(d.borne()))



