

class Node:
    nbre=0
    def __init__(self,inf,sup,budget, data, value,name="root",z=0,time=0,nbNoeud=0):

        if len(data)==0 :
            self.node=None
        else:
            self.node=data[0]
            del data[0]
            self.data = data
            self.__class__.nbre += 1;
        self.budget=budget#budget restant
        self.value=value#les valeurs choisi pour chaque x
        self.z=z#le depense
        self.time=time#le temps total
        self.name=name
        self.nbNoeud=nbNoeud
        self.inf = inf
        self.sup = sup




    def gauche(self):
        if (self.node == None):
            return None#nous sommes a la fin
        nom,x=self.node#sinon recuperer les données courantes

        time, prix=x
        value = dict(self.value)
        value[nom] = 1
        if self.budget<prix:
            return None
        nbN = self.nbNoeud + 1
        inf = self.inf - prix
        sup = self.sup - prix
        return Node(inf,sup,self.budget-prix,list(self.data),value,
                    nom,
                    self.z+prix,
                    time+self.time,nbN)

    def droite(self):

        if (self.node==None):
            return None
        nom, x = self.node  # sinon recuperer les données courantes
        time, prix = x
        value=dict(self.value)
        value[nom] = 0
        if self.budget < prix:
            return None
        nbN = self.nbNoeud + 1

        return Node(self.inf,self.sup,self.budget, list(self.data),
                    value,nom,
                    self.z,
                    self.time,nbN)
    def __str__(self):
        return self.name
    def borne(self):
       return "Noeud :{} [{}-{}]".format(self.nbNoeud,self.inf,self.sup)
    def evaluate(self):
        return self.value,self.z,self.time





