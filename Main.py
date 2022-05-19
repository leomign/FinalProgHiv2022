####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Final Programmation orientée objet
###  Nom: Léo Migneault
###  No étudiant: 2032104
###  No Groupe: 00001
###  Description du fichier: Programme principal
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
import sys
from ZooMainWindow import *
from classDialogAnimal import *
from classDialogEnclos import *


##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################

class MainWdwQt(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWdwQt, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Menu")

    @QtCore.pyqtSlot()
    def on_pushButtonAnimal_clicked(self):
        """
        Ouvre le dialog DialogAnimal
        """
        self.pushButtonAnimal.setDisabled(True) # Rend le bouton Animal inactif pour empêcher l'ouverture de trop de fenêtres
        dialog = DialogAnimal()
        dialog.show()
        reply = dialog.exec_()
        self.pushButtonAnimal.setEnabled(True)  # Rend le bouton Animal actif à nouveau pour pouvoir interagir avec à nouveau

    @QtCore.pyqtSlot()
    def on_pushButtonEnclos_clicked(self):
        """
        Ouvre le dialog DialogEnclos
        """
        self.pushButtonEnclos.setDisabled(True) # Rend le bouton Enclos inactif pour empêcher l'ouverture de trop de fenêtres
        dialog = DialogEnclos()
        dialog.show()
        reply = dialog.exec_()
        self.pushButtonEnclos.setEnabled(True)  # Rend le bouton Enclos actif à nouveau pour pouvoir interagir avec à nouveau

    @QtCore.pyqtSlot()
    def on_pushButtonQuitter_clicked(self):
        """
        Ferme la fenêtre MainWdwQt
        """
        self.close()

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def Main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainWdwQt()
    form.show()
    app.exec()

#################################
###### PROGRAMME PRINCIPAL ######
#################################

if __name__ == "__main__":
    Main()
