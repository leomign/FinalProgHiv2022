####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Final Programmation orientée objet
###  Nom: Léo Migneault
###  No étudiant: 2032104
###  No Groupe: 00001
###  Description du fichier: Classe de DialogEnclos
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from EnclosDialog import *
from PyQt5 import QtWidgets, QtCore
from ClasseAnimal import *


##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################
lsEnclos = []

class DialogEnclos(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(DialogEnclos, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Ajouter un enclos")

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        """
        Cache les labels d'erreur lorsque le dialog est accédé et affiche la liste des enclos déjà instanciés
        """
        self.labelErreurTypeEnclos.setHidden(True)
        self.labelErreurTailleAuCarre.setHidden(True)
        self.labelErreurEnvironnement.setHidden(True)

        for obj in lsEnclos:
            self.textBrowserEnclos.append(str(obj))

    @QtCore.pyqtSlot()
    def on_pushButtonAjouter_clicked(self):
        """
        Instancie un objet de la classe Enclos à la liste lsEnclos
        """
        ExistePas = True
        E1 = Enclos()
        E1.TypeEnclos = self.comboBoxTypeEnclos.currentText()
        E1.Environnement = self.comboBoxEnvironnement.currentText()
        E1.TailleAuCarre = self.spinBoxTailleAuCarre.value()

        for obj in lsEnclos:
            if obj.TypeEnclos == E1.TypeEnclos:
                ExistePas = False

        if ExistePas == True:   # Vérifie si l'attribut TypeEnclos existe déjà dans la liste lsEnclos
            self.labelErreurTypeEnclos.setHidden(True)
        else:
            self.labelErreurTypeEnclos.setVisible(True)

        if E1.TailleAuCarre == self.spinBoxTailleAuCarre.value():   # Vérifie si l'attribut TailleAuCarre a été changé
            self.labelErreurTailleAuCarre.setHidden(True)
        else:
            self.labelErreurTailleAuCarre.setVisible(True)

        if E1.Environnement == self.comboBoxEnvironnement.currentText():    # Vérifie si l'attribut Environnement a été changé
            self.labelErreurEnvironnement.setHidden(True)
        else:
            self.labelErreurEnvironnement.setVisible(True)

        if E1.TailleAuCarre == self.spinBoxTailleAuCarre.value() and E1.Environnement == \
                self.comboBoxEnvironnement.currentText() and ExistePas == True:
            self.labelErreurTypeEnclos.setHidden(True)
            lsEnclos.append(E1)
            self.textBrowserEnclos.clear()
            for obj in lsEnclos:
                self.textBrowserEnclos.append(str(obj))
            self.comboBoxTypeEnclos.setCurrentIndex(0)
            self.comboBoxEnvironnement.setCurrentIndex(0)
            self.spinBoxTailleAuCarre.setValue(0)

    @QtCore.pyqtSlot()
    def on_pushButtonSerialiser_clicked(self):
        """
        Sérialise l'objet présent de la classe Enclos
        """
        E1 = Enclos()
        E1.TypeEnclos = self.comboBoxTypeEnclos.currentText()
        E1.Environnement = self.comboBoxEnvironnement.currentText()
        E1.TailleAuCarre = self.spinBoxTailleAuCarre.value()

        if E1.TailleAuCarre == self.spinBoxTailleAuCarre.value():   # Vérifie si l'attribut TailleAuCarre a été changé
            self.labelErreurTailleAuCarre.setHidden(True)
        else:
            self.labelErreurTailleAuCarre.setVisible(True)

        if E1.Environnement == self.comboBoxEnvironnement.currentText():    # Vérifie si l'attribut Environnement a été changé
            self.labelErreurEnvironnement.setHidden(True)
        else:
            self.labelErreurEnvironnement.setVisible(True)

        if E1.TailleAuCarre == self.spinBoxTailleAuCarre.value() and E1.Environnement == \
                self.comboBoxEnvironnement.currentText():
            E1.Serialiser("Serialisation.json")

    @QtCore.pyqtSlot()
    def on_pushButtonDeserialiser_clicked(self):
        """
        Désérialise l'objet présent de la classe Enclos
        """
        E1 = Enclos()
        E1.Deserialiser("Serialisation.json")
        self.textBrowserSerialiser.setText(str(E1))

    @QtCore.pyqtSlot()
    def on_pushButtonQuitter_clicked(self):
        """
        Ferme la fenêtre DialogEnclos
        """
        self.close()
