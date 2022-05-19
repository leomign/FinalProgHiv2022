####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Final Programmation orientée objet
###  Nom: Léo Migneault
###  No étudiant: 2032104
###  No Groupe: 00001
###  Description du fichier: Classe de DialogAnimal
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from ClasseMammifere import *
from ClasseOiseau import *
from ClassePoisson import *
from AnimalDialog import *
from PyQt5 import QtWidgets, QtCore
from classDialogEnclos import lsEnclos, lsAnimaux


##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################
class DialogAnimal(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(DialogAnimal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Ajouter un animal")

    def showEvent(self, a0: QtCore.QEvent) -> None:
        """
        Cache les labels d'erreur lorsque le dialog est accédé et affiche la liste des animaux déjà instanciés
        """
        self.labelErreurCri.setHidden(True)
        self.labelErreurNid.setHidden(True)
        self.labelErreurAge.setHidden(True)
        self.labelErreurEnclos.setHidden(True)

        for obj in lsAnimaux:
            self.textBrowserAnimal.append(str(obj))

    @QtCore.pyqtSlot()
    def on_pushButtonContinuer_clicked(self):
        """
        pushButton qui confirme les informations de la classe mère Animal et permet l'accès aux classes qui en héritent
        """
        EnclosExiste = False
        NumeroExiste = False
        A1 = Animal()

        A1.NumeroAnimal = self.lineEditNumeroAnimal.text()
        A1.FaitInteressant = self.textEditFaitInteressant.toPlainText()
        A1.Age = self.spinBoxAge.value()

        for elt in lsAnimaux:
            if elt.NumeroAnimal == A1.NumeroAnimal:
                NumeroExiste = True

        if A1.NumeroAnimal != self.lineEditNumeroAnimal.text():
            self.labelErreurNumeroAnimal.setText("Le numéro est invalide.")
        else:
            self.labelErreurNumeroAnimal.clear()

        if A1.Age != self.spinBoxAge.value():
            self.labelErreurAge.setVisible(True)
        else:
            self.labelErreurAge.setHidden(True)

        for obj in lsEnclos:
            if obj.TypeEnclos == self.comboBoxEnclos.currentText():
                EnclosExiste = True
        if EnclosExiste == True:

            self.labelErreurEnclos.setHidden(True)

            if A1.Age == self.spinBoxAge.value() and A1.NumeroAnimal == self.lineEditNumeroAnimal.text() and \
                    NumeroExiste == False:
                if self.comboBoxEnclos.currentIndex() == 0:
                    self.widgetMammifere.setEnabled(True)
                    self.AnimalTemp = Mammifere()

                elif self.comboBoxEnclos.currentIndex() == 1:
                    self.widgetOiseau.setEnabled(True)
                    self.AnimalTemp = Oiseau()

                elif self.comboBoxEnclos.currentIndex() == 2:
                    self.widgetPoisson.setEnabled(True)
                    self.AnimalTemp = Poisson()

                self.AnimalTemp.Age = A1.Age
                self.AnimalTemp.NumeroAnimal = A1.NumeroAnimal
                self.AnimalTemp.FaitInteressant = A1.FaitInteressant
                for obj in lsEnclos:
                    if obj.TypeEnclos == self.comboBoxEnclos.currentText():
                        self.AnimalTemp.Enclos = obj

                self.widgetAnimal.setDisabled(True)
                self.pushButtonAjouter.setEnabled(True)
                self.pushButtonSupprimer.setDisabled(True)

            elif A1.Age == self.spinBoxAge.value() and A1.NumeroAnimal == self.lineEditNumeroAnimal.text() and \
                    NumeroExiste == True:
                if self.comboBoxEnclos.currentIndex() == 0:
                    self.widgetMammifere.setEnabled(True)
                    self.AnimalTemp = Mammifere()

                elif self.comboBoxEnclos.currentIndex() == 1:
                    self.widgetOiseau.setEnabled(True)
                    self.AnimalTemp = Oiseau()

                elif self.comboBoxEnclos.currentIndex() == 2:
                    self.widgetPoisson.setEnabled(True)
                    self.AnimalTemp = Poisson()

                self.AnimalTemp.Age = A1.Age
                self.AnimalTemp.NumeroAnimal = A1.NumeroAnimal
                for obj in lsEnclos:
                    if obj.TypeEnclos == self.comboBoxEnclos.currentText():
                        self.AnimalTemp.Enclos = obj

                self.widgetAnimal.setDisabled(True)
                self.pushButtonModifier.setEnabled(True)

        else:
            self.labelErreurEnclos.setVisible(True)

    @QtCore.pyqtSlot()
    def on_pushButtonAjouter_clicked(self):
        """
        Rajoute les attributs de l'objet qui hérite de la classe mère et l'ajoute à la liste lsAnimaux ainsi qu'au
        textBrowserAnimal
        """
        if self.widgetMammifere.isEnabled():
            self.AnimalTemp.Alimentation = self.comboBoxAlimentation.currentText()
            self.AnimalTemp.Posture = self.comboBoxPosture.currentText()
            self.AnimalTemp.Cri = self.lineEditCri.text()

            if self.AnimalTemp.Cri == self.lineEditCri.text().title():
                lsAnimaux.append(self.AnimalTemp)
                self.textBrowserAnimal.clear()
                for obj in lsAnimaux:
                    self.textBrowserAnimal.append(str(obj))
                self.labelErreurCri.setHidden(True)
                self.widgetMammifere.setDisabled(True)
                self.pushButtonAjouter.setDisabled(True)
                self.pushButtonModifier.setDisabled(True)
                self.widgetAnimal.setEnabled(True)
                self.pushButtonSupprimer.setEnabled(True)
            else:
                self.labelErreurCri.setVisible(True)

        elif self.widgetOiseau.isEnabled():
            self.AnimalTemp.PeutVoler = self.comboBoxPeutVoler.currentText()
            self.AnimalTemp.VariationCouleurs = self.comboBoxVariationCouleurs.currentText()
            self.AnimalTemp.Vision = self.comboBoxVision.currentText()

            lsAnimaux.append(self.AnimalTemp)
            self.textBrowserAnimal.clear()
            for obj in lsAnimaux:
                self.textBrowserAnimal.append(str(obj))
            self.widgetOiseau.setDisabled(True)
            self.pushButtonAjouter.setDisabled(True)
            self.pushButtonModifier.setDisabled(True)
            self.widgetAnimal.setEnabled(True)
            self.pushButtonSupprimer.setEnabled(True)

        elif self.widgetPoisson.isEnabled():
            self.AnimalTemp.TypeEau = self.comboBoxTypeEau.currentText()
            self.AnimalTemp.Nid = self.lineEditNid.text()
            self.AnimalTemp.Camouflage = self.comboBoxCamouflage.currentText()

            if self.AnimalTemp.Nid == self.lineEditNid.text().title():
                lsAnimaux.append(self.AnimalTemp)
                self.textBrowserAnimal.clear()
                for obj in lsAnimaux:
                    self.textBrowserAnimal.append(str(obj))
                self.labelErreurNid.setHidden(True)
                self.widgetPoisson.setDisabled(True)
                self.pushButtonAjouter.setDisabled(True)
                self.pushButtonModifier.setDisabled(True)
                self.widgetAnimal.setEnabled(True)
                self.pushButtonSupprimer.setEnabled(True)
            else:
                self.labelErreurNid.setVisible(True)

    @QtCore.pyqtSlot()
    def on_pushButtonModifier_clicked(self):
        """
        Rajoute les attributs de l'objet qui hérite de la classe mère pour modifier l'objet de la liste lsAnimaux
        portant l'attribut NumeroAnimal correspondant et modifie le textBrowserAnimal en conséquence
        """
        if self.widgetMammifere.isEnabled():
            self.AnimalTemp.Alimentation = self.comboBoxAlimentation.currentText()
            self.AnimalTemp.Posture = self.comboBoxPosture.currentText()
            self.AnimalTemp.Cri = self.lineEditCri.text()

            if self.AnimalTemp.Cri == self.lineEditCri.text().title():
                for obj in lsAnimaux:
                    if obj.NumeroAnimal == self.AnimalTemp.NumeroAnimal:
                        lsAnimaux.remove(obj)
                lsAnimaux.append(self.AnimalTemp)
                self.textBrowserAnimal.clear()
                for obj in lsAnimaux:
                    self.textBrowserAnimal.append(str(obj))
                self.labelErreurCri.setHidden(True)
                self.widgetMammifere.setDisabled(True)
                self.pushButtonAjouter.setDisabled(True)
                self.pushButtonModifier.setDisabled(True)
                self.widgetAnimal.setEnabled(True)
            else:
                self.labelErreurCri.setVisible(True)

        elif self.widgetOiseau.isEnabled():
            self.AnimalTemp.PeutVoler = self.comboBoxPeutVoler.currentText()
            self.AnimalTemp.VariationCouleurs = self.comboBoxVariationCouleurs.currentText()
            self.AnimalTemp.Vision = self.comboBoxVision.currentText()

            lsAnimaux.append(self.AnimalTemp)
            for obj in lsAnimaux:
                if obj.NumeroAnimal == self.AnimalTemp.NumeroAnimal:
                    lsAnimaux.remove(obj)
            self.textBrowserAnimal.clear()
            for obj in lsAnimaux:
                self.textBrowserAnimal.append(str(obj))
            self.widgetOiseau.setDisabled(True)
            self.pushButtonAjouter.setDisabled(True)
            self.pushButtonModifier.setDisabled(True)
            self.widgetAnimal.setEnabled(True)

        elif self.widgetPoisson.isEnabled():
            self.AnimalTemp.TypeEau = self.comboBoxTypeEau.currentText()
            self.AnimalTemp.Nid = self.lineEditNid.text()
            self.AnimalTemp.Camouflage = self.comboBoxCamouflage.currentText()

            if self.AnimalTemp.Nid == self.lineEditNid.text().title():
                lsAnimaux.append(self.AnimalTemp)
                for obj in lsAnimaux:
                    if obj.NumeroAnimal == self.AnimalTemp.NumeroAnimal:
                        lsAnimaux.remove(obj)
                self.textBrowserAnimal.clear()
                for obj in lsAnimaux:
                    self.textBrowserAnimal.append(str(obj))
                self.labelErreurNid.setHidden(True)
                self.widgetPoisson.setDisabled(True)
                self.pushButtonAjouter.setDisabled(True)
                self.pushButtonModifier.setDisabled(True)
                self.widgetAnimal.setEnabled(True)
            else:
                self.labelErreurNid.setVisible(True)

    @QtCore.pyqtSlot()
    def on_pushButtonSupprimer_clicked(self):
        AnimalExiste = False
        for obj in lsAnimaux:
            if obj.NumeroAnimal == self.lineEditNumeroAnimal.text():
                AnimalASupprimer = obj
                AnimalExiste = True
                self.pushButtonModifier.setDisabled(True)
        if AnimalExiste == True:
            self.textBrowserAnimal.clear()
            lsAnimaux.remove(AnimalASupprimer)
            for obj in lsAnimaux:
                self.textBrowserAnimal.append(str(obj))

    @QtCore.pyqtSlot()
    def on_pushButtonQuitter_clicked(self):
        """
        Ferme la fenêtre DialogAnimal
        """
        self.close()
