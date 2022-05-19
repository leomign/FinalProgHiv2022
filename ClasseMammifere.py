####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Final Programmation orientée objet
###  Nom: Léo Migneault
###  No étudiant: 2032104
###  No Groupe: 00001
###  Description du fichier: Classe Mammifere
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from ClasseAnimal import *


##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################
class Mammifere(Animal):
    def __init__(self, pAge = 0, pFaitInteressant = "", pNumeroAnimal = 0, pEnclos = Enclos(), pAlimentation = "",
                 pPosture = "", pCri = ""):
        """
        Appel des attributs de la classe Mammifere
        :param pAge: Âge du mammifère (entre 1 et 99 ans)
        :param pFaitInteressant: Fait intéressant sur le mammifère
        :param pNumeroAnimal: Nombre à 5 chiffres attribué au mammifère
        :param pEnclos: Objet instancié de la classe enclos
        :param pAlimentation: Alimentation du mammifère (carnivore, herbivore ou omnivore)
        :param pPosture: Posture du mammifère (bipède ou quadrupède)
        :param pCri: Cri du mammifère (entre 3 et 20 caractères)
        """
        Animal.__init__(self, pAge, pFaitInteressant, pNumeroAnimal, pEnclos)
        self.__Alimentation = pAlimentation
        self.__Posture = pPosture
        self.__Cri = pCri

    def _getAlimentation(self):
        """
        Getter de l'attribut self.__Alimentation
        :return: self.__Alimentation
        """
        return self.__Alimentation

    def _setAlimentation(self, pAlimentation):
        """
        Setter de l'attribut self.__Alimentation
        :param pAlimentation: Paramètre d'entrée pAlimentation
        :return: none
        """
        if (str(pAlimentation).upper() == "CARNIVORE" or str(pAlimentation).upper() == "HERBIVORE" or
                str(pAlimentation).upper() == "OMNIVORE"):
            self.__Alimentation = str(pAlimentation).title()

    Alimentation = property(_getAlimentation, _setAlimentation)

    def _getPosture(self):
        """
        Getter de l'attribut self.__Posture
        :return: self.__Posture
        """
        return self.__Posture

    def _setPosture(self, pPosture):
        """
        Setter de l'attribut self.__Posture
        :param pPosture: Paramètre d'entrée pPosture
        :return: none
        """
        if str(pPosture).upper() == "BIPÈDE" or str(pPosture).upper() == "QUADRUPÈDE":
            self.__Posture = str(pPosture).title()

    Posture = property(_getPosture, _setPosture)

    def _getCri(self):
        """
        Getter de l'attribut self.__Cri
        :return: self.__Cri
        """
        return self.__Cri

    def _setCri(self, pCri):
        """
        Setter de l'attribut self.__Cri
        :param pCri: Paramètre d'entrée pCri
        :return: none
        """
        if len(pCri) > 2 and len(pCri) < 21 and str(pCri).isalpha() == True:
            self.__Cri = str(pCri).title()

    Cri = property(_getCri, _setCri)

    def __str__(self):
        chMammifere = "{}\nNuméro de l'animal: {}\nÂge de l'animal: {}\nFait intéressant sur l'animal: {}\nRégime " \
                      "alimentaire: {}\nType de posture: {}\nType de cri: {}\nDonnées sur l'enclos:\n{}\n{}".format\
            ("*" * 30, str(self.NumeroAnimal), str(self.Age), self.FaitInteressant, self.__Alimentation,
             self.__Posture, self.__Cri, self.Enclos.__str__(), "*" * 30)
        return chMammifere
