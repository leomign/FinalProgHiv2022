####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Final Programmation orientée objet
###  Nom: Léo Migneault
###  No étudiant: 2032104
###  No Groupe: 00001
###  Description du fichier: Classe Poisson
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from ClasseAnimal import *


##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################
class Poisson(Animal):
    def __init__(self, pAge = 0, pFaitInteressant = "", pNumeroAnimal = 0, pEnclos = Enclos(), pTypeEau = "", pNid = ""
                 , pCamouflage = ""):
        """
        Appel des attributs de la classe Poisson
        :param pAge: Âge du poisson (entre 1 et 99 ans)
        :param pFaitInteressant: Fait intéressant sur le poisson
        :param pNumeroAnimal: Nombre à 5 chiffres attribué au poisson
        :param pEnclos: Objet instancié de la classe enclos
        :param pTypeEau: Type d'eau requis pour le poisson (douce ou salée)
        :param pNid: Type de nid dans lequel le poisson vit (entre 3 et 20 caractères)
        :param pCamouflage: Si le poisson a une bonne capacité de camouflage (oui ou non)
        """
        Animal.__init__(self, pAge, pFaitInteressant, pNumeroAnimal, pEnclos)
        self.__TypeEau = pTypeEau
        self.__Nid = pNid
        self.__Camouflage = pCamouflage

    def _getTypeEau(self):
        """
        Getter de l'attribut self.__TypeEau
        :return: self.__TypeEau
        """
        return self.__TypeEau

    def _setTypeEau(self, pTypeEau):
        """
        Setter de l'attribut self.__TypeEau
        :param pTypeEau: Paramètre d'entrée pTypeEau
        :return: none
        """
        if str(pTypeEau).upper() == "SALÉE" or str(pTypeEau).upper() == "DOUCE":
            self.__TypeEau = str(pTypeEau).title()

    TypeEau = property(_getTypeEau, _setTypeEau)

    def _getNid(self):
        """
        Getter de l'attribut self.__Nid
        :return: self.__Nid
        """
        return self.__Nid

    def _setNid(self, pNid):
        """
        Setter de l'attribut self.__Nid
        :param pNid: Paramètre d'entrée pNid
        :return: none
        """
        if len(pNid) > 2 and len(pNid) < 21 and str(pNid).isalpha() == True:
            self.__Nid = str(pNid).title()

    Nid = property(_getNid, _setNid)

    def _getCamouflage(self):
        """
        Getter de l'attribut self.__Camouflage
        :return: self.__Camouflage
        """
        return self.__Camouflage

    def _setCamouflage(self, pCamouflage):
        """
        Setter de l'attribut self.__Camouflage
        :param pCamouflage: Paramètre d'entrée pCamouflage
        :return: none
        """
        if str(pCamouflage).upper() == "OUI" or str(pCamouflage).upper() == "NON":
            self.__Camouflage = str(pCamouflage).title()

    Camouflage = property(_getCamouflage, _setCamouflage)

    def __str__(self):
        chPoisson = "{}\nNuméro de l'animal: {}\nÂge de l'animal: {}\nFait intéressant sur l'animal: {}\n" \
                    "Type d'eau: {}\nType de nid: {}\nPeut se camoufler: {}\nDonnées sur l'enclos:\n{}\n{}".format\
            ("*" * 30, str(self.NumeroAnimal), str(self.Age), self.FaitInteressant, self.__TypeEau, self.__Nid,
        self.__Camouflage, self.Enclos.__str__(), "*" * 30)
        return chPoisson
