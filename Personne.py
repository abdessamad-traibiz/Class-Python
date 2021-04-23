from abc import ABC,abstractmethod #appel à la méthode abstract
class Personne(ABC):#déclaration de la classe Personne 
    cin:str #déclaration de l'objet (cin) de type string
    prenom:str #déclaration de l'objet (prenom) 
    ville:str #déclaration de l'objet (ville) 
    def __init__(self,cin:str,prenom:str,ville:str):  #Constructeur pour l'initialisation des attributs de la classe
        self.cin=cin #instanciation de l'attribut cin (self est obligatoire =Like (this))
        self.prenom=prenom
        self.ville=ville
    def __str__(self): #méthode d'affichage 
         return 'CIN : '+self.cin+' | Prénom : '+self.prenom+' | Ville : '+self.ville+' | ' 

    @abstractmethod
    def Details(self):
        pass
