####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Final Programmation orientée objet
###  Nom: Léo Migneault
###  No étudiant: 2032104
###  No Groupe: 00001
###  Description du fichier: Classe Oiseau
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from ClasseAnimal import *


##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################
class Oiseau(Animal):
    def __init__(self, pAge = 0, pFaitInteressant = "", pNumeroAnimal = 0, pEnclos = Enclos(), pVariationCouleurs = "",
                 pPeutVoler = "", pVision = ""):
        """
        Appel des attributs de la classe Oiseau
        :param pAge: Âge de l'oiseau (entre 1 et 99 ans)
        :param pFaitInteressant: Fait intéressant sur l'oiseau
        :param pNumeroAnimal: Nombre à 5 chiffres attribué à l'oiseau
        :param pEnclos: Objet instancié de la classe enclos
        :param pVariationCouleurs: Variation des couleurs de l'oiseau (unicolore, bicolore ou multicolore)
        :param pPeutVoler: Si l'oiseau peut voler
        :param pVision: Type de vision de l'oiseau (normale, nocturne ou daltonienne)
        """
        Animal.__init__(self, pAge, pFaitInteressant, pNumeroAnimal, pEnclos)
        self.__VariationCouleurs = pVariationCouleurs
        self.__PeutVoler = pPeutVoler
        self.__Vision = pVision

    def _getVariationCouleurs(self):
        """
        Getter de l'attribut self.__VariationCouleurs
        :return: self.__VariationCouleurs
        """
        return self.__VariationCouleurs

    def _setVariationCouleurs(self, pVariationCouleurs):
        """
        Setter de l'attribut self.__VariationCouleurs
        :param pVariationCouleurs: Paramètre d'entrée pVariationCouleurs
        :return: none
        """
        if (str(pVariationCouleurs).upper() == "UNICOLORE" or str(pVariationCouleurs).upper() == "BICOLORE" or
                str(pVariationCouleurs).upper() == "MULTICOLORE"):
            self.__VariationCouleurs = str(pVariationCouleurs).title()

    VariationCouleurs = property(_getVariationCouleurs, _setVariationCouleurs)

    def _getPeutVoler(self):
        """
        Getter de l'attribut self.__PeutVoler
        :return: self.__PeutVoler
        """
        return self.__PeutVoler

    def _setPeutVoler(self, pPeutVoler):
        """
        Setter de l'attribut self.__PeutVoler
        :param pPeutVoler: Paramètre d'entrée pPeutVoler
        :return: none
        """
        if str(pPeutVoler).upper() == "OUI" or str(pPeutVoler).upper() == "NON":
            self.__PeutVoler = str(pPeutVoler).title()

    PeutVoler = property(_getPeutVoler, _setPeutVoler)

    def _getVision(self):
        """
        Getter de l'attribut self.__Vision
        :return: self.__Vision
        """
        return self.__Vision

    def _setVision(self, pVision):
        """
        Setter de l'attribut self.__Vision
        :param pVision: Paramètre d'entrée pVision
        :return: none
        """
        if (str(pVision).upper() == "NORMALE" or str(pVision).upper() == "AMÉLIORÉE" or
                str(pVision).upper() == "NOCTURNE"):
            self.__Vision = str(pVision).title()

    Vision = property(_getVision, _setVision)

    def __str__(self):
        chOiseau = "{}\nNuméro de l'animal: {}\nÂge de l'animal: {}\nFait intéressant sur l'animal: {}\nVariation " \
                   "des couleurs: {}\nL'oiseau peut voler: {}\nType de vision: {}\nDonnées sur l'enclos:\n{}\n{}"\
            .format("*" * 30, str(self.NumeroAnimal), str(self.Age), self.FaitInteressant, self.__VariationCouleurs,
             self.__PeutVoler, self.__Vision, self.Enclos.__str__(), "*" * 30)
        return chOiseau
