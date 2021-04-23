from Personne import Personne
class Etudiant(Personne):#La classe Etudiant hérite de la classe Personne
    Filiere:str
    CNE:str
    def __init__(self,cin:str,prenom:str,ville:str,Filiere:str,CNE:str):
        super().__init__(cin,prenom,ville) #appel au constructeur de la classe mère
        self.Filiere=Filiere #instanciation des attributs de la classe Etudiant (Filière)
        self.CNE=CNE #instanciation des attributs de la classe Etudiant (CNE)
    #méthode 1:
    def __str__(self):
        return super().__str__()+'Filière : '+self.Filiere+' |  CNE : '+self.CNE
        #super() pour l'appel au constructeur de la classe mère
    """#méthode 2:
    def __str__(self):
        return Personne.__str__()+'Filière :'+self.Filiere+'  CNE :'+str(self.CNE) """
    
    def Details(self):
        print('Détails de l\'étudiant :\n')
        print(self.__str__())


