####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Final Programmation orientée objet
###  Nom: Léo Migneault
###  No étudiant: 2032104
###  No Groupe: 00001
###  Description du fichier: Classe Enclos
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
import json


##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################
lsAnimaux = []

class Enclos:
    def __init__(self, pTypeEnclos = "", pTailleAuCarre = -1, pEnvironnement = ""):
        """
        Appel des attributs de la classe Enclos
        :param pTypeEnclos: Type de l'enclos (mammifère, oiseau ou poisson)
        :param pTailleAuCarre: Taille en mètres au carré de l'enclos
        :param pEnvironnement: Environnement de l'enclos (terrestre, aquatique ou hybride)
        """
        self.__TypeEnclos = pTypeEnclos
        self.__TailleAuCarre = pTailleAuCarre
        self.__Environnement = pEnvironnement

    def _getTypeEnclos(self):
        """
        Getter de l'attribut self.__TypeEnclos
        :return: self.__TypeEnclos
        """
        return self.__TypeEnclos

    def _setTypeEnclos(self, pTypeEnclos):
        """
        Setter de l'attribut self.__TypeEnclos
        :param pTypeEnclos: Paramètre d'entrée pTypeEnclos
        :return: none
        """
        if (str(pTypeEnclos).upper() == "MAMMIFÈRE" or str(pTypeEnclos).upper() == "OISEAU" or str(pTypeEnclos).upper()
        == "POISSON"):
            self.__TypeEnclos = str(pTypeEnclos).title()

    TypeEnclos = property(_getTypeEnclos, _setTypeEnclos)

    def _getTailleAuCarre(self):
        """
        Getter de l'attribut self.__TailleAuCarre
        :return: self.__TailleAuCarre
        """
        return self.__TailleAuCarre

    def _setTailleAuCarre(self, pTailleAuCarre):
        """
        Setter de l'attribut self.__TailleAuCarre
        :param pTailleAuCarre: Paramètre d'entrée pTailleAuCarre
        :return: none
        """
        if int(pTailleAuCarre) > 0 and int(pTailleAuCarre) < 50:
            self.__TailleAuCarre = pTailleAuCarre

    TailleAuCarre = property(_getTailleAuCarre, _setTailleAuCarre)

    def _getEnvironnement(self):
        """
        Getter de l'attribut self.__Environnement
        :return: self.__Environnement
        """
        return self.__Environnement

    def _setEnvironnement(self, pEnvironnement):
        """
        Setter de l'attribut self.__Environnement
        :param pEnvironnement: Paramètre d'entrée pEnvironnement
        :return: none
        """
        if ((str(pEnvironnement).upper() == "TERRESTRE" or str(pEnvironnement).upper() == "HYBRIDE") and
                (self.__TypeEnclos == "Mammifère" or self.__TypeEnclos == "Oiseau") or (str(pEnvironnement).upper() ==
                    "AQUATIQUE" or str(pEnvironnement).upper() == "HYBRIDE") and self.__TypeEnclos == "Poisson"):
            self.__Environnement = str(pEnvironnement).title()

    Environnement = property(_getEnvironnement, _setEnvironnement)

    def Serialiser(self, pJsonEnclos):
        """
        Pour sérialiser un objet de la classe Enclos()
        :param pJsonEnclos: Nom du fichier json en entrée
        :return: none
        """
        with open(pJsonEnclos, "w") as FichierJson:
            json.dump(self.__dict__, FichierJson)

    def Deserialiser(self, pJsonEnclos):
        """
        Pour désérialiser un objet de la classe Enclos()
        :param pJsonEnclos: Nom du fichier json en entrée
        :return: none
        """
        with open(pJsonEnclos, "r") as FichierJson:
            self.__dict__ = json.load(FichierJson)

    def __str__(self):
        chEnclos = "Type de l'enclos: {}\nTaille de l'enclos: {} m^2\nEnvironnement de l'enclos: {}".format(
            self.__TypeEnclos, str(self.__TailleAuCarre), self.__Environnement)
        return chEnclos
