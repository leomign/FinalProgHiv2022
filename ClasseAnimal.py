####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Final Programmation orientée objet
###  Nom: Léo Migneault
###  No étudiant: 2032104
###  No Groupe: 00001
###  Description du fichier: Classe Animal
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from ClasseEnclos import *


##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################
class Animal:
    def __init__(self, pAge = -1, pFaitInteressant = "", pNumeroAnimal = -1, pEnclos = Enclos()):
        """
        Appel des attributs de la classe Animal
        :param pAge: Âge de l'animal (entre 1 et 99 ans)
        :param pFaitInteressant: Fait intéressant à propos de l'animal
        :param pNumeroAnimal: Nombre à 5 chiffres attribué à l'animal
        :param pEnclos: Objet instancié de la classe Enclos
        """
        self.__Age = pAge
        self.FaitInteressant = pFaitInteressant
        self.__NumeroAnimal = pNumeroAnimal
        self.Enclos = pEnclos

    def _getAge(self):
        """
        Getter de l'attribut self.__Age
        :return: self.__Age
        """
        return self.__Age

    def _setAge(self, pAge):
        """
        Setter de l'attribut self.__Age
        :param pAge: Paramètre d'entrée pAge
        :return: none
        """
        if int(pAge) > 0 and int(pAge) < 100:
            self.__Age = pAge

    Age = property(_getAge, _setAge)

    def _getNumeroAnimal(self):
        """
        Getter de l'attribut self.__NumeroAnimal
        :return: self.__NumeroAnimal
        """
        return self.__NumeroAnimal

    def _setNumeroAnimal(self, pNumeroAnimal):
        """
        Setter de l'attribut self.__NumeroAnimal
        :param pNumeroAnimal: Paramètre d'entrée pNumeroAnimal
        :return: none
        """
        if len(pNumeroAnimal) == 5 and str(pNumeroAnimal).isnumeric() == True:
            self.__NumeroAnimal = pNumeroAnimal

    NumeroAnimal = property(_getNumeroAnimal, _setNumeroAnimal)

    def __str__(self):
        chAnimal = "{}\nNuméro de l'animal: {}\nÂge de l'animal: {}\nFait intéressant sur l'animal: {}\nDonnées sur " \
                   "l'enclos: {}\n{}".format("*" * 30, str(self.__NumeroAnimal), str(self.__Age), self.FaitInteressant,
                                             self.Enclos.__str__(), "*" * 30)
        return chAnimal
