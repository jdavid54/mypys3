"""
@version: 0.96(2010-08-29)
http://easygui.sourceforge.net/index.html

@note: à propos d'EasyGui en français
traduction : f.laroche
http://laroche.lycee.free.fr

EasyGuiFr fournit une interface graphique simple d'usage pour l'utilisateur.
Elle ne nécessite aucune connaissance particulière du programmeur sur tkinter :
cadres, widgets,, appels ou fonction lambda. Toutes les interactions de la GUI
sont appelées par de simples fonctions qui retournent généralement une valeur élémentaire.

@note: Attention si vous utilisez EasyGuiFr avec IDLE
Vous pouvez rencontrer quelques probèmes de compatibilité avec IDLE : EasyGuiFr
est un module Tkinter qui utilise sa propre boucle de gestion d'événements de même que IDLE est
construit sur une base Tkinter avec sa propre boucle. Il se peut que les deux boucles
rentrent en conflit avec des résultats imprévisibles ; si tel est le cas utilisez
EasyGuiFr avec un autre EDI.

EasyGuiFr nécessite Tk version 8.0 ou plus.
"""

Version_EG = __doc__.split()[1]

__all__ = ['boite oui non'
    , 'boite continuer annuler'
    , 'boite_vrai_faux'      #boolbox'
    , 'boite_choix_numero'   #boite_numeros
    , 'boite_message'        #msgbox
    , 'boite_bouton'         #buttonbox'
    , 'saisie_entier'        #integerbox'
    , 'multsaisie_base'      #multenterbox
    , 'saisie_base'          #enterbox
    , 'boite_erreur_programme'  #exceptionbox'
    , 'boite_choix'          #choicebox
    , 'boite_code'           #codebox'
    , 'boite_texte'          #textbox'
    , 'repertoire_ouvre'     #diropenbox'
    , 'fichier_ouvre'        #fileopenbox'
    , 'fichier_sauve'        #filesavebox'
    , 'saisie_motdepasse'    #passwordbox'
    , 'multsaisie_motdepasse'#multpasswordbox'
    , 'multboite_choix'      #multchoicebox'
    , 'information'          #abouteasygui'
    , 'Version_EG'           #egversion'
    , 'Démonstration EG'     #egdemo'
    , 'EgStore'
    ]

import sys, os
import string
import pickle
import traceback


#--------------------------------------------------
# Vérifier la version de Python et faire le nécessaire
#--------------------------------------------------
"""
D'après la documentation de Python la variable sys.hexversion
contient le numéro de version encodé par un entier. Cet entier
augmente à chaque nouvelle version, y compris les versions non utilisables.
Par exemple, pour vérifier que l'interpréteur est au moins la version 1.5.2, utilisez :

if sys.hexversion >= 0x010502F0:
    # utiliser les méthodes modernes
    ...
else:
    # utiliser une implémentation différente ou prévenir l'utilisateur
    ...
"""

if sys.hexversion >= 0x020600F0:
    runningPython26 = True
else:
    runningPython26 = False

if sys.hexversion >= 0x030000F0:
    runningPython3 = True
else:
    runningPython3 = False
print(runningPython3)
try:
    from PIL import Image   as PILImage
    from PIL import ImageTk as PILImageTk
    PILisLoaded = True
except:
    PILisLoaded = False


if runningPython3:
    from tkinter import *
    import tkinter.filedialog as tk_FileDialog
    from io import StringIO
else:
    from Tkinter import *
    import tkFileDialog as tk_FileDialog
    from StringIO import StringIO

def write(*args):
    args = [str(arg) for arg in args]
    args = " ".join(args)
    sys.stdout.write(args)

def writeln(*args):
    write(*args)
    sys.stdout.write("\n")

say = writeln

if TkVersion < 8.0 :
    stars = "*"*75
    writeln("""\n\n\n""" + stars + """
Vous utilisez Tk version: """ + str(TkVersion) + """
Vous devez utiliser Tk version 8.0 ou plus pour utiliser EasyGuiFr.
Sortie du programme.
""" + stars + """\n\n\n""")
    sys.exit(0)

def dq(s):
    return '"%s"' % s

rootWindowPosition = "+300+200"

PROPORTIONAL_FONT_FAMILY = ("MS", "Sans", "Serif")
MONOSPACE_FONT_FAMILY    = ("Courier")

PROPORTIONAL_FONT_SIZE  = 10
MONOSPACE_FONT_SIZE     =  9  #a little smaller, because it it more legible at a smaller size
TEXT_ENTRY_FONT_SIZE    = 12  # a little larger makes it easier to see

#STANDARD_SELECTION_EVENTS = ["Return", "Button-1"]
STANDARD_SELECTION_EVENTS = ["Return", "Button-1", "space"]

# Initialisation à vide de diverses variables globales qui seront réinitialisées ultérieurement.
__boitechoixSelectionMultiple = None
__TextesWidget = None
__TexteBoutonReponse = None
__ResultatsBoiteChoix = None
__premierWidget = None
__saisie_baseText = None
__saisie_baseDefaultText=""
__multsaisie_baseText = ""
choixBoiteChoix = None
widgetBoiteChoix = None
widgetSaisie = None
fenetreBoite = None
msgErreurImage = (
    "\n\n---------------------------------------------\n"
    "Erreur: %s\n%s")

#-------------------------------------------------------------------
# Divers contrôles construits sur la base de la boite_bouton
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# boite_oui_non
#-----------------------------------------------------------------------
def boite_oui_non(msg="Veux tu continuer ?"
    , titre=" "
    , choix=("Oui", "Non")
    , image=None
    ):
    """
    Affiche une boite_message avec les choix "Oui" (par défaut) et "Non".
    La valeur revoyée est un nombre  : 0 pour Non, 1 pour Oui ou si le choix est annulé.
    Si le programmeur ne passe pas de message en argument, une demande générique est envoyée
    pour confirmation que l'utilisateur souhaite continuer.
    On peut donc l'utiliser comme suit :

        if boite_oui_non(): pass # continue
        else: sys.exit(0)  # sortie du programme

    @arg msg: le message à afficher.
    @arg titre: le titre de la fenêtre.
    @arg choix: une liste de choix à afficher.
    """
    return boite_vrai_faux(msg, titre, choix, image=image)

#-----------------------------------------------------------------------
# boite_continuer_annuler
#-----------------------------------------------------------------------
def boite_continuer_annuler(msg="Veux tu continuer ?"
    , titre=" "
    , choix=("Continuer", "Annuler")
    , image=None
    ):
    """
    Affiche une boite_message avec "Continuer" (défault -> 1) et "Annuler" (->0)
    Même fonctionnement que boite_oui_non
    Sans message argument foncctionne ainsi :
        if boite_continuer_annuler(): pass # continue
        else: sys.exit(0)  # quitter le programme
  """
    return boite_vrai_faux(msg, titre, choix, image=image)

#-----------------------------------------------------------------------
# boite_vrai_faux
#-----------------------------------------------------------------------
def boite_vrai_faux(msg="Veux tu continuer ?"
    , titre=" "
    , choix=("Vrai","Faux")
    , image=None
    ):
    """
    Affiche une boite_message avec "Vrai" (défault -> 1) et "Faux" (->0)
    Même fonctionnement que boite_oui_non
    Sans message argument foncctionne ainsi :
        if boite_vrai_faux(): pass # continue
        else: sys.exit(0)  # quitter le programme
    """

    reply = boite_bouton(msg=msg, choix=choix, titre=titre, image=image)
    if reply == choix[0]: return 1
    else: return 0

#-----------------------------------------------------------------------
# boite_choix_numero
#-----------------------------------------------------------------------
def boite_choix_numero(msg="Veux tu continuer ?"
    , titre=" "
    , choix=("Oui","Non")
    , image=None
    ):
    """
    Affiche une boîte avec les choix passés en paramètre ;
    renvoie le numéro du bouton cliqué (en démarrant à 0).
    """
    reply = boite_bouton(msg=msg, choix=choix, titre=titre, image=image)
    index = -1
    for choisi in choix:
        index = index + 1
        if reply == choisi: return index
    raise AssertionError(
        "Il y a un problème de logique dans le code d\'EasyGuiFr pour boite_choix_numero.")

#-----------------------------------------------------------------------
# boite_message
#-----------------------------------------------------------------------
def boite_message(msg="(Ton message est ici)", titre=" ", ok_button="OK",image=None,root=None):
    """
    Affiche une boite_message de base avec le seul bouton "OK"
    """
    if type(ok_button) != type("OK"):
        raise AssertionError("L\'argument 'ok_button' de la boite_message doit être une chaine de caractères.")

    return boite_bouton(msg=msg, titre=titre, choix=[ok_button], image=image,root=root)


#-------------------------------------------------------------------
# boite_bouton
#-------------------------------------------------------------------
def boite_bouton(msg="Sélectionnez ",titre=" "
    ,choix=("Bouton 1", "Bouton 2", "Bouton 3")
    , image=None
    , root=None
    ):
    """
    Affiche une boîte avec un message, un titre, une liste de boutons ;
    renvoie le texte du bouton choisi.
    """
    global fenetreBoite, __TexteBoutonReponse, __TextesWidget, buttonsFrame
    # Initialise __TexteBoutonReponse avec le premier choix.
    # C'est ce qui est renvoyé si la fenêtre est fermée avec le bouton du haut.
    __TexteBoutonReponse = choix[0]

    if root:
        root.withdraw()
        fenetreBoite = Toplevel(master=root)
        fenetreBoite.withdraw()
    else:
        fenetreBoite = Tk()
        fenetreBoite.withdraw()

    fenetreBoite.protocol('WM_DELETE_WINDOW', denyWindowManagerClose )
    fenetreBoite.title(titre)
    fenetreBoite.iconname('Dialog')
    fenetreBoite.geometry(rootWindowPosition)
    fenetreBoite.minsize(400, 100)

    # ------------- définit le messageFrame ---------------------------------
    messageFrame = Frame(master=fenetreBoite)
    messageFrame.pack(side=TOP, fill=BOTH)

    # ------------- definit l'imageFrame ---------------------------------
    tk_Image = None
    if image:
        imageFilename = os.path.normpath(image)
        junk,ext = os.path.splitext(imageFilename)

        if os.path.exists(imageFilename):
            if ext.lower() in [".gif", ".pgm", ".ppm"]:
                tk_Image = PhotoImage(master=fenetreBoite, file=imageFilename)
            else:
                if PILisLoaded:
                    try:
                        pil_Image = PILImage.open(imageFilename)
                        tk_Image = PILImageTk.PhotoImage(pil_Image, master=fenetreBoite)
                    except:
                        msg += msgErreurImage % (imageFilename,
                            "\nPython Imaging Library (PIL) ne peut convertir ce fichier en une image affichable."
                            "\n\nPIL report:\n" + formatage_message_erreur())

                else:  # PIL n'est pas chargé
                    msg += msgErreurImage % (imageFilename,
                    "\nImpossible d'ouvrir Python Imaging Library (PIL) pour afficher l'image.\n\n"
                    "Vous devez installer PIL\n"
                    "(http://www.pythonware.com/products/pil/)\n"
                    "pour afficher " + ext + " fichiers image.")

        else:
            msg += msgErreurImage % (imageFilename, "\nFichier Image pas trouvé.")

    if tk_Image:
        imageFrame = Frame(master=fenetreBoite)
        imageFrame.pack(side=TOP, fill=BOTH)
        label = Label(imageFrame,image=tk_Image)
        label.image = tk_Image # conserve la référence !
        label.pack(side=TOP, expand=YES, fill=X, padx='1m', pady='1m')

    # ------------- placement du cadre des boutons ---------------------------------
    buttonsFrame = Frame(master=fenetreBoite)
    buttonsFrame.pack(side=TOP, fill=BOTH)

    # -------------------- place les widgets dans les cadres -----------------------
    messageWidget = Message(messageFrame, text=msg, width=400)
    messageWidget.configure(font=(PROPORTIONAL_FONT_FAMILY,PROPORTIONAL_FONT_SIZE))
    messageWidget.pack(side=TOP, expand=YES, fill=X, padx='3m', pady='3m')

    __put_buttons_in_buttonframe(choix)

    # -------------- l'action commence -----------
    # met le focus sur le premier bouton
    __premierWidget.focus_force()

    fenetreBoite.deiconify()
    fenetreBoite.mainloop()
    fenetreBoite.destroy()
    if root: root.deiconify()
    return __TexteBoutonReponse


#-------------------------------------------------------------------
# saisie_entier
#-------------------------------------------------------------------
def saisie_entier(msg=""
    , titre=" "
    , defaut=""
    , borneinf=0      #lowerbound
    , bornesup=99     #upperbound=99
    , image = None
    , root  = None
    , **invalidKeywordArguments
    ):
    """
    Affiche une boite de saisie où l'utilisateur peut entrer un nombr entier ;
    la fonction a les arguments "defaut", "borneinf" et "bornesup" qui limitent
    la saisie.
    L'arg "defaut" peut valoir None.
    Si l'utilisateur n'entre pas les nombres corrects ou des chaines de caractères
    un message d'erreur est renvoyé et l'utilisatur recommence.
    L'entier saisi est renvoyé (pas le texte saisi). Si l'opération est annulée,
    None est renvoyé.
    """
    if "argLowerBound" in invalidKeywordArguments:
        raise AssertionError(
            "\nsaisie_entier no longer supports the 'argLowerBound' argument.\n"
            + "Use 'lowerbound' instead.\n\n")
    if "argUpperBound" in invalidKeywordArguments:
        raise AssertionError(
            "\nsaisie_entier no longer supports the 'argUpperBound' argument.\n"
            + "Use 'upperbound' instead.\n\n")

    if defaut != "":
        if type(defaut) != type(1):
            raise AssertionError(
                "La boite Saisie_Entier a reçu autre chose qu'un entier comme "
                + "defaut : " + dq(str(default)) , "Erreur")

    if type(borneinf) != type(1):
        raise AssertionError(
            "La boite SaisieEntier a reçu autre chose qu'un entier comme "
            + "limite inférieure pour " + dq(str(borneinf)) , "Erreur")

    if type(bornesup) != type(1):
        raise AssertionError(
            "La boite SaisieEntier a reçu autre chose qu'un entier comme "
            + "limite supérieure pour " + dq(str(bornesup)) , "Erreur")

    if msg == "":
        msg = ("Entre un entier compris entre " + str(borneinf)
            + " et " + str(bornesup))

    while 1:
        reply = saisie_base(msg, titre, str(defaut), image=image, root=root)
        if reply == None: return None

        try:
            reply = int(reply)
        except:
            boite_message("La valeur entrée n\'est pas un entier : " + str(reply)
                    , "Erreur")
            continue

        if reply < borneinf:
            boite_message ("La valeur entrée est trop petite (inférieure à "
                + str(borneinf) + ").", "Erreur")
            continue

        if reply > bornesup:
            boite_message ("La valeur entrée est trop grosse (supérieure à "
                + str(bornesup) + ").", "Erreur")
            continue

        # La réponse a passé toutes les vérifications,
        # c'est un entier compris entre les limites spécifiées.
        return reply

#-------------------------------------------------------------------
# multsaisie_base
#-------------------------------------------------------------------
def multsaisie_base(msg="Complètez les valeurs de chaque champ."
    , titre=" "
    , champs=()
    , valeurs=()
    ):
    """
    Affiche une boite avec plusieurs lignes de saisie.
    S'il y a moins de valeurs que de champs, la liste des valeurs est
    complétée avec des chaînes vides.
    S'il y a davantage de valeurs que de champs la liste des valeurs est tronquée.

    Retourne une liste avec les valeurs de chaque champ ou None  si l'utilisateur
    annule l'action.

    Ci-dessous un exemple qui montre comment la liste retournée peut être
    vérifiée avant d'être acceptée :
        ----------------------------------------------------------------------
        msg = "Entrez vos informations personnelles"
        titre = "Votre Adresse Personnelle"
        fieldNames = ["Nom","Prénom","Rue","Ville","Code Postal"]
        fieldValues = []  # laissés en blanc pour démarrer
        fieldValues = multsaisie_base(msg,titre, fieldNames)

        # assurez vous qu'aucun champ ne reste vide
        while 1:
            if fieldValues == None: break
            errmsg = ""
            for i in range(len(fieldNames)):
                if fieldValues[i].strip() == "":
                    errmsg += ('"%s" est un champ indispensable.\n\n' % fieldNames[i])
            if errmsg == "":
                break # pas de problèmes
            fieldValues = multsaisie_base(errmsg, titre, fieldNames, fieldValues)

        writeln("Votre réponse est : %s" % str(fieldValues))
        ----------------------------------------------------------------------

    @arg msg: le msg à afficher.
    @arg titre: le titre de la fenêtre.
    @arg champs: la liste des noms de champs.
    @arg valeurs:  la liste des valeurs des champs.
    """
    return __multfillablebox(msg,titre,champs,valeurs,None)


#-----------------------------------------------------------------------
# multsaisie_motdepasse
#-----------------------------------------------------------------------
def multsaisie_motdepasse(msg="Complètez les valeurs de chaque champ."
    , titre=" "
    , champs=tuple()
    , valeurs=tuple()
    ):
    r"""
    Même interface que multsaisie_base.  Mais dans multsaisie_motdepasse,
    le dernier champ doit être un mot de passe qui sera masqué par des astérisques.

    Ci-dessous un exemple qui montre comment la liste retournée peut être
    vérifiée avant d'être acceptée :
        msg = "Enter logon information"
        titre = "Demo of multsaisie_motdepasse"
        fieldNames = ["Server ID", "User ID", "Password"]
        fieldValues = []  # we start with blanks for the valeurs
        fieldValues = multsaisie_motdepasse(msg, titre, fieldNames)

        # make sure that none of the champs was left blank
        while 1:
            if fieldValues == None: break
            errmsg = ""
            for i in range(len(fieldNames)):
                if fieldValues[i].strip() == "":
                    errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
                if errmsg == "": break # no problems found
            fieldValues = multsaisie_motdepasse(errmsg, titre, fieldNames, fieldValues)

        writeln("Ta reponse est : %s" % str(fieldValues))
    """
    return __multfillablebox(msg,titre,champs,valeurs,"*")

def bindArrows(widget):
    widget.bind("<Down>", tabRight)
    widget.bind("<Up>"  , tabLeft)

    widget.bind("<Right>",tabRight)
    widget.bind("<Left>" , tabLeft)

def tabRight(event):
    fenetreBoite.event_generate("<Tab>")

def tabLeft(event):
    fenetreBoite.event_generate("<Shift-Tab>")

#-----------------------------------------------------------------------
# __multfillablebox
#-----------------------------------------------------------------------
def __multfillablebox(msg="Complètez les valeurs de chaque champ"
    , titre=" "
    , champs=()
    , valeurs=()
    , mask = None
    ):
    global fenetreBoite, __multsaisie_baseText, __multsaisie_baseDefaultText, cancelButton, widgetSaisie, okButton, finButton

    choices = ["Ok", "Annuler"]
    if len(champs) == 0: return None

    champs = list(champs[:])  # conversion éventuelle de tuples en listes
    valeurs = list(valeurs[:])  # conversion éventuelle de tuples en listes

    if   len(valeurs) == len(champs): pass
    elif len(valeurs) >  len(champs):
        champs = champs[0:len(valeurs)]
    else:
        while len(valeurs) < len(champs):
            valeurs.append("")

    fenetreBoite = Tk()

    fenetreBoite.protocol('WM_DELETE_WINDOW', denyWindowManagerClose )
    fenetreBoite.title(titre)
    fenetreBoite.iconname('Dialog')
    fenetreBoite.geometry(rootWindowPosition)
    fenetreBoite.bind("<Escape>", __multsaisie_baseCancel)

    # -------------------- positionnement du message dans fenetreBoite --------------------
    messageFrame = Frame(master=fenetreBoite)
    messageFrame.pack(side=TOP, fill=BOTH)

    #-------------------- le widget message ----------------------------
    messageWidget = Message(messageFrame, width="4.5i", text=msg)
    messageWidget.configure(font=(PROPORTIONAL_FONT_FAMILY,PROPORTIONAL_FONT_SIZE))
    messageWidget.pack(side=RIGHT, expand=1, fill=BOTH, padx='3m', pady='3m')

    global widgetSaisies
    widgetSaisies = []

    lastWidgetIndex = len(champs) - 1

    for widgetIndex in range(len(champs)):
        argFieldName  = champs[widgetIndex]
        argFieldValue = valeurs[widgetIndex]
        entryFrame = Frame(master=fenetreBoite)
        entryFrame.pack(side=TOP, fill=BOTH)

        # --------- widgetSaisie ----------------------------------------------
        labelWidget = Label(entryFrame, text=argFieldName)
        labelWidget.pack(side=LEFT)

        widgetSaisie = Entry(entryFrame, width=40,highlightthickness=2)
        widgetSaisies.append(widgetSaisie)
        widgetSaisie.configure(font=(PROPORTIONAL_FONT_FAMILY,TEXT_ENTRY_FONT_SIZE))
        widgetSaisie.pack(side=RIGHT, padx="3m")

        bindArrows(widgetSaisie)

        widgetSaisie.bind("<Return>", __multsaisie_baseGetText)
        widgetSaisie.bind("<Escape>", __multsaisie_baseCancel)

        # Pour le dernier widgetSaisie, s'il s'agit de multsaisie_motdepasse,
        # le contenu est affiché à l'aide d'un masque d'*
        if widgetIndex == lastWidgetIndex:
            if mask:
                widgetSaisies[widgetIndex].configure(show=mask)

        # saisie du texte dans le widgetSaisie
        widgetSaisies[widgetIndex].insert(0,argFieldValue)
        widgetIndex += 1

    # ------------------ ok button -------------------------------
    buttonsFrame = Frame(master=fenetreBoite)
    buttonsFrame.pack(side=BOTTOM, fill=BOTH)

    okButton = Button(buttonsFrame, takefocus=1, text="Ok")
    bindArrows(okButton)
    okButton.pack(expand=1, side=LEFT, padx='3m', pady='3m', ipadx='2m', ipady='1m')

    # liaison du commandButton avec le gestionnaire d'évènements
    commandButton  = okButton
    handler = __multsaisie_baseGetText
    for selectionEvent in STANDARD_SELECTION_EVENTS:
        commandButton.bind("<%s>" % selectionEvent, handler)

    # ------------------ bouton annuler -------------------------------
    cancelButton = Button(buttonsFrame, takefocus=1, text="Annuler")
    bindArrows(cancelButton)
    cancelButton.pack(expand=1, side=LEFT, padx='3m', pady='3m', ipadx='2m', ipady='1m')

    # liaison du commandButton avec le gestionnaire d'évènements
    commandButton  = cancelButton
    handler = __multsaisie_baseCancel
    for selectionEvent in STANDARD_SELECTION_EVENTS:
        commandButton.bind("<%s>" % selectionEvent, handler)

    # ------------------- on passe à l'action -----------------
    widgetSaisies[0].focus_force()  # met le focus sur le widgetSaisie
    fenetreBoite.mainloop()         # attente des événements

    # -------- on termine en détruisant la fenêtre ----------------------------------
    fenetreBoite.destroy()
    return __multsaisie_baseText

#-----------------------------------------------------------------------
# __multsaisie_baseGetText
#-----------------------------------------------------------------------
def __multsaisie_baseGetText(event):
    global __multsaisie_baseText

    __multsaisie_baseText = []
    for widgetSaisie in widgetSaisies:
        __multsaisie_baseText.append(widgetSaisie.get())
    fenetreBoite.quit()

def __multsaisie_baseCancel(event):
    global __multsaisie_baseText
    __multsaisie_baseText = None
    fenetreBoite.quit()

#-------------------------------------------------------------------
# saisie_base
#-------------------------------------------------------------------
def saisie_base(msg="Entrez un texte :"
    , titre=" "
    , defaut=""
    , nettoie=True
    , image=None
    , root=None
    ):
    """
    Affiche une boite de saisie de texte.
    Vous pouvez préciser des valeurs par défaut pour le texte lequel apparaîtra
    dans la ligne de saisie.
    La fonction renvoie le texte entré ou None si l'utilisateur a annulé.
    Par défaut, saisie_base nettoie le resultat en enlevant les blancs en début et
    en fin de saisie. Si vous ne voulez pas, mettez nettoie=False.
    """
    result = __fillablebox(msg, titre, defaut=defaut, mask=None,image=image,root=root)
    if result and nettoie:
        result = result.strip()
    return result

def saisie_motdepasse(msg="Entrez votre mot de passe :"
    , titre=" "
    , defaut=""
    , image=None
    , root=None
    ):
    """
    Affiche une boite où l'utilisateur peut rentrer un mot de passe.
    Le texte est masqué par des astériques, de sorte qu'on ne puisse le voir à l'écran.
    Renvoie le texte entré ou None si annulation.
    """
    return __fillablebox(msg, titre, defaut, mask="*",image=image,root=root)

def __fillablebox(msg
    , titre=""
    , defaut=""
    , mask=None
    , image=None
    , root=None
    ):
    """
    Affiche une boite de saisie de texte.
    Vous pouvez envoyer un texte par défaut qui apparaîtra automatiquement.
    Renvoie le texte entré ou None si annulation.
    """

    global fenetreBoite, __saisie_baseText, __saisie_baseDefaultText
    global cancelButton, widgetSaisie, okButton

    if titre == None: titre == ""
    if defaut == None: defaut = ""
    __saisie_baseDefaultText = defaut
    __saisie_baseText        = __saisie_baseDefaultText

    if root:
        root.withdraw()
        fenetreBoite = Toplevel(master=root)
        fenetreBoite.withdraw()
    else:
        fenetreBoite = Tk()
        fenetreBoite.withdraw()

    fenetreBoite.protocol('WM_DELETE_WINDOW', denyWindowManagerClose )
    fenetreBoite.title(titre)
    fenetreBoite.iconname('Dialog')
    fenetreBoite.geometry(rootWindowPosition)
    fenetreBoite.bind("<Escape>", __saisie_baseCancel)

    # ------------- mise en place du cadre ---------------------------------
    messageFrame = Frame(master=fenetreBoite)
    messageFrame.pack(side=TOP, fill=BOTH)

    # ------------- mise en place du cadre image (option) ------------------
    tk_Image = None
    if image:
        imageFilename = os.path.normpath(image)
        junk,ext = os.path.splitext(imageFilename)

        if os.path.exists(imageFilename):
            if ext.lower() in [".gif", ".pgm", ".ppm"]:
                tk_Image = PhotoImage(master=fenetreBoite, file=imageFilename)
            else:
                if PILisLoaded:
                    try:
                        pil_Image = PILImage.open(imageFilename)
                        tk_Image = PILImageTk.PhotoImage(pil_Image, master=fenetreBoite)
                    except:
                        msg += msgErreurImage % (imageFilename,
                            "\nPython Imaging Library (PIL) ne peut pas convertir ce fichier en une image affichable."
                            "\n\nPIL dit :\n" + formatage_message_erreur())

                else:  # PIL is not loaded
                    msg += msgErreurImage % (imageFilename,
                    "\n Impossible d'importer Python Imaging Library (PIL) pour afficher cette image.\n\n"
                    "Il faut installer PIL\n"
                    "(http://www.pythonware.com/products/pil/)\n"
                    "pour afficher " + ext + " fichiers d\'image.")

        else:
            msg += msgErreurImage % (imageFilename, "\nFichier image pas trouvé.")

    if tk_Image:
        imageFrame = Frame(master=fenetreBoite)
        imageFrame.pack(side=TOP, fill=BOTH)
        label = Label(imageFrame,image=tk_Image)
        label.image = tk_Image # garde la référence à l'image !
        label.pack(side=TOP, expand=YES, fill=X, padx='1m', pady='1m')

    # ------------- definit le cadre des boutons -------------------------------
#    buttonsFrame = Frame(master=fenetreBoite)
#    buttonsFrame.pack(side=TOP, fill=BOTH)


    # ------------- definit le cadre de saisie ---------------------------------
    entryFrame = Frame(master=fenetreBoite)
    entryFrame.pack(side=TOP, fill=BOTH)

    # ------------- definit le cadre des boutons -------------------------------
    buttonsFrame = Frame(master=fenetreBoite)
    buttonsFrame.pack(side=TOP, fill=BOTH)

    #-------------------- le widget message ----------------------------
    messageWidget = Message(messageFrame, width="4.5i", text=msg)
    messageWidget.configure(font=(PROPORTIONAL_FONT_FAMILY,PROPORTIONAL_FONT_SIZE))
    messageWidget.pack(side=RIGHT, expand=1, fill=BOTH, padx='3m', pady='3m')

    # ---------------- le widgetSaisie -----------------------------------------
    widgetSaisie = Entry(entryFrame, width=40)
    bindArrows(widgetSaisie)
    widgetSaisie.configure(font=(PROPORTIONAL_FONT_FAMILY,TEXT_ENTRY_FONT_SIZE))
    if mask:
        widgetSaisie.configure(show=mask)
    widgetSaisie.pack(side=LEFT, padx="3m")
    widgetSaisie.bind("<Return>", __saisie_baseGetText)
    widgetSaisie.bind("<Escape>", __saisie_baseCancel)
    # saisie du text dans le widgetSaisie
    widgetSaisie.insert(0,__saisie_baseDefaultText)

    # ------------------ bouton OK -------------------------------
    okButton = Button(buttonsFrame, takefocus=1, text="Ok")
    bindArrows(okButton)
    okButton.pack(expand=1, side=LEFT, padx='3m', pady='3m', ipadx='2m', ipady='1m')

    # liaison du commandButton avec le gestionnaire d'évènements
    commandButton  = okButton
    handler = __saisie_baseGetText
    for selectionEvent in STANDARD_SELECTION_EVENTS:
        commandButton.bind("<%s>" % selectionEvent, handler)

    # ------------------ bouton annuler -------------------------------
    cancelButton = Button(buttonsFrame, takefocus=1, text="Annuler")
    bindArrows(cancelButton)
    cancelButton.pack(expand=1, side=RIGHT, padx='3m', pady='3m', ipadx='2m', ipady='1m')

    # liaison du commandButton avec le gestionnaire d'évènements
    commandButton  = cancelButton
    handler = __saisie_baseCancel
    for selectionEvent in STANDARD_SELECTION_EVENTS:
        commandButton.bind("<%s>" % selectionEvent, handler)

    # ------------------- on passe à l'action -----------------
    widgetSaisie.focus_force()    # met le focus sur le widgetSaisie
    fenetreBoite.deiconify()
    fenetreBoite.mainloop()

    # -----------  après l'action ----------------------------------
    if root: root.deiconify()
    fenetreBoite.destroy()
    return __saisie_baseText


def __saisie_baseGetText(event):
    global __saisie_baseText

    __saisie_baseText = widgetSaisie.get()
    fenetreBoite.quit()

def __saisie_baseRestore(event):
    global widgetSaisie

    widgetSaisie.delete(0,len(widgetSaisie.get()))
    widgetSaisie.insert(0, __saisie_baseDefaultText)

def __saisie_baseCancel(event):
    global __saisie_baseText

    __saisie_baseText = None
    fenetreBoite.quit()

def denyWindowManagerClose():
    """
    Interdit au WindowManager de fermer la fenêtre
    """
    x = Tk()
    x.withdraw()
    x.bell()
    x.destroy()

#-------------------------------------------------------------------
# multboite_choix
#-------------------------------------------------------------------
def multboite_choix(msg="Faites autant de choix que vous voulez"
    , titre=" "
    , choix=()
    , **kwargs
    ):
    """
    Affiche une boite avec une liste de choix.
    On peut sélectionner plusieurs choix en cliquant sur chaque ligne.
    retourne la liste des choix, éventuellement vide ;
    retourne None si annulation.

    @arg msg : le msg à afficher.
    @arg titre : le titre de la fenêtre
    @arg choices : une liste de choix à afficher
    """
    if len(choix) == 0: choix = ["Erreur - aucun choix possible"]

    global __boitechoixSelectionMultiple
    __boitechoixSelectionMultiple = 1
    return __boite_choix(msg, titre, choix)


#-----------------------------------------------------------------------
# boite_choix
#-----------------------------------------------------------------------
def boite_choix(msg="Choisissez une possibilité"
    , titre=" "
    , choix=()
    ):
    """
    Affiche une boite avec une liste de choix.
    On ne peut sélectionner qu'un seul choix.
    Retourne le texte du choix fait, éventuellement vide ;
    retourne None si annulation.

    @arg msg : le msg à afficher.
    @arg titre : le titre de la fenêtre
    @arg choices : une liste de choix à afficher
    """

    if len(choix) == 0: choix = ["Erreur - aucun choix possible"]

    global __boitechoixSelectionMultiple
    __boitechoixSelectionMultiple = 0
    return __boite_choix(msg,titre,choix)


#-----------------------------------------------------------------------
# __boite_choix
#-----------------------------------------------------------------------
def __boite_choix(msg
    , titre
    , choix
    ):
    """
    Programme interne pour faire fonctionner boite_choix() et multboite_choix()
    """
    global fenetreBoite, __ResultatsBoiteChoix, widgetBoiteChoix, defaultText
    global widgetBoiteChoix, choixBoiteChoix
    #-------------------------------------------------------------------
    # Si choix est un tuple, on le convertit en liste pour pouvoir la trier.
    # Si choix est déjà une liste, on fait une nouvelle liste et on la trie,
    # ce qui ne change rien au choix initial.
    #-------------------------------------------------------------------
    choix = list(choix[:])
    if len(choix) == 0:
        choix = ["Erreur - aucun choix possible"]
    defaultButtons = ["Ok", "Annuler"]

    # vérifier que tous les choix sont des chaînes
    for index in range(len(choix)):
        choix[index] = str(choix[index])

    lines_to_show = min(len(choix), 20)
    if titre == None: titre = ""

    # Initialise la variable __ResultatsBoiteChoix
    # C'est la valeur qui sera renvoyée si l'utilisateur clique sur la fermeture de fenêtre
    __ResultatsBoiteChoix = None

    fenetreBoite = Tk()
    fenetreBoite.protocol('WM_DELETE_WINDOW', denyWindowManagerClose )
    screen_width  = fenetreBoite.winfo_screenwidth()
    screen_height = fenetreBoite.winfo_screenheight()
    root_width    = int((screen_width * 0.1))
    for k in range(len(choix)):
        long=len(choix[k])*PROPORTIONAL_FONT_SIZE
        if long > root_width: root_width=long
    root_height   = int((screen_height * 0.5))
    root_xpos     = int((screen_width * 0.1))
    root_ypos     = int((screen_height * 0.05))

    fenetreBoite.title(titre)
    fenetreBoite.iconname('Dialog')
    rootWindowPosition = "+0+0"
    fenetreBoite.geometry(rootWindowPosition)
    fenetreBoite.expand=NO
    fenetreBoite.minsize(root_width, root_height)
    rootWindowPosition = "+" + str(root_xpos) + "+" + str(root_ypos)
    fenetreBoite.geometry(rootWindowPosition)

    # ---------------- mise en place du cadre ----------------------------------
    message_and_buttonsFrame = Frame(master=fenetreBoite)
    message_and_buttonsFrame.pack(side=TOP, fill=X, expand=NO)

    messageFrame = Frame(message_and_buttonsFrame)
    messageFrame.pack(side=LEFT, fill=X, expand=YES)
    #messageFrame.pack(side=TOP, fill=X, expand=YES)

    buttonsFrame = Frame(message_and_buttonsFrame)
    buttonsFrame.pack(side=RIGHT, expand=NO, pady=0)
    #buttonsFrame.pack(side=TOP, expand=YES, pady=0)

    choiceboxFrame = Frame(master=fenetreBoite)
    choiceboxFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)

    # ----------------------- place les widgets dans le cadre ------------------

    messageWidget = Message(messageFrame, anchor=NW, text=msg, width=int(root_width * 0.9))
    messageWidget.configure(font=(PROPORTIONAL_FONT_FAMILY,PROPORTIONAL_FONT_SIZE))
    messageWidget.pack(side=LEFT, expand=YES, fill=BOTH, padx='1m', pady='1m')

    # --------  place le widget BoiteChoix dans le cadre choiceboxFrame -----------------------
    widgetBoiteChoix = Listbox(choiceboxFrame
        , height=lines_to_show
        , borderwidth="1m"
        , relief="flat"
        , bg="white"
        )

    if __boitechoixSelectionMultiple:
        widgetBoiteChoix.configure(selectmode=MULTIPLE)

    widgetBoiteChoix.configure(font=(PROPORTIONAL_FONT_FAMILY,PROPORTIONAL_FONT_SIZE))

    # ajoute une barre de défilement verticale
    rightScrollbar = Scrollbar(choiceboxFrame, orient=VERTICAL, command=widgetBoiteChoix.yview)
    widgetBoiteChoix.configure(yscrollcommand = rightScrollbar.set)

    # ajoute une barre de défilement horizontale
    bottomScrollbar = Scrollbar(choiceboxFrame, orient=HORIZONTAL, command=widgetBoiteChoix.xview)
    widgetBoiteChoix.configure(xscrollcommand = bottomScrollbar.set)

    # regroupe la Listbox and les barres de défilement.
    # Notez que le textArea doit être défini en premier mais être groupé en dernier,
    # si bien que la barre de défilement horizontale sera placée correctement.

    bottomScrollbar.pack(side=BOTTOM, fill = X)
    rightScrollbar.pack(side=RIGHT, fill = Y)

    widgetBoiteChoix.pack(side=LEFT, padx="1m", pady="1m", expand=YES, fill=BOTH)

    #---------------------------------------------------
    # Tri des choix, supprime les doublons
    # place les choix dans le widget BoiteChoix
    #---------------------------------------------------
    for index in range(len(choix)):
        choix[index] = str(choix[index])

    if runningPython3:
        choix.sort(key=str.lower)
    else:
        choix.sort( lambda x,y: cmp(x.lower(),y.lower())) # pas de différence minuscule-majuscule dans le tri

    lastInserted = None
    choixBoiteChoix = []
    for choisi in choix:
        if choisi == lastInserted: pass
        else:
            widgetBoiteChoix.insert(END, choisi)
            choixBoiteChoix.append(choisi)
            lastInserted = choisi

    fenetreBoite.bind('<Any-Key>', KeyboardListener)

    # place les boutons dans le cadre des boutons
    if len(choix) > 0:
        okButton = Button(buttonsFrame, takefocus=YES, text="Ok", height=1, width=6)
        bindArrows(okButton)
        okButton.pack(expand=NO, side=TOP,  padx='2m', pady='1m', ipady="1m", ipadx="2m")

    # liaison du commandButton avec le gestionnaire d'évènements
        commandButton  = okButton
        handler = __choiceboxGetChoice
        for selectionEvent in STANDARD_SELECTION_EVENTS:
            commandButton.bind("<%s>" % selectionEvent, handler)

    # liaison avec le clavier (Retour ou Double-click)
        widgetBoiteChoix.bind("<Return>", __choiceboxGetChoice)
        widgetBoiteChoix.bind("<Double-Button-1>", __choiceboxGetChoice)
    else:
        widgetBoiteChoix.bind("<Return>", __choiceboxCancel)
        widgetBoiteChoix.bind("<Double-Button-1>", __choiceboxCancel)

    cancelButton = Button(buttonsFrame, takefocus=YES, text="Annuler", height=1, width=6)
    bindArrows(cancelButton)
    cancelButton.pack(expand=NO, side=BOTTOM, padx='2m', pady='1m', ipady="1m", ipadx="2m")

    # liaison du commandButton avec le gestionnaire d'évènements
    commandButton  = cancelButton
    handler = __choiceboxCancel
    for selectionEvent in STANDARD_SELECTION_EVENTS:
        commandButton.bind("<%s>" % selectionEvent, handler)

    # ajout de boutons speciaux en cas de sélection multiple
    if len(choix) > 0 and __boitechoixSelectionMultiple:
        selectionButtonsFrame = Frame(messageFrame)
        selectionButtonsFrame.pack(side=RIGHT, fill=Y, expand=NO)

        selectAllButton = Button(selectionButtonsFrame, text="Tout Sél.", height=1, width=6)
        bindArrows(selectAllButton)

        selectAllButton.bind("<Button-1>",__choiceboxSelectAll)
        selectAllButton.pack(expand=NO, side=TOP,  padx='2m', pady='1m', ipady="1m", ipadx="2m")

        clearAllButton = Button(selectionButtonsFrame, text="Efface", height=1, width=6)
        bindArrows(clearAllButton)
        clearAllButton.bind("<Button-1>",__choiceboxClearAll)
        clearAllButton.pack(expand=NO, side=TOP,  padx='2m', pady='1m', ipady="1m", ipadx="2m")

    # -------------------- liaison avec le clavier (Esc) ----------------------------
    fenetreBoite.bind("<Escape>", __choiceboxCancel)

    # --------------------- l'action démarre -----------------------------------
    # met le focus sur le widget BoiteChoix et la sélection sur le premier item
    widgetBoiteChoix.select_set(0)
    widgetBoiteChoix.focus_force()

    # --- boucle principale -----
    fenetreBoite.mainloop()

    fenetreBoite.destroy()
    return __ResultatsBoiteChoix

def __choiceboxGetChoice(event):
    global fenetreBoite, __ResultatsBoiteChoix, widgetBoiteChoix

    if __boitechoixSelectionMultiple:
        __ResultatsBoiteChoix = [widgetBoiteChoix.get(index) for index in widgetBoiteChoix.curselection()]
    else:
        choice_index = widgetBoiteChoix.curselection()
        __ResultatsBoiteChoix = widgetBoiteChoix.get(choice_index)

    fenetreBoite.quit()

def __choiceboxSelectAll(event):
    global widgetBoiteChoix, choixBoiteChoix

    widgetBoiteChoix.selection_set(0, len(choixBoiteChoix)-1)

def __choiceboxClearAll(event):
    global widgetBoiteChoix, choixBoiteChoix

    widgetBoiteChoix.selection_clear(0, len(choixBoiteChoix)-1)

def __choiceboxCancel(event):
    global fenetreBoite, __ResultatsBoiteChoix

    __ResultatsBoiteChoix = None
    fenetreBoite.quit()

def KeyboardListener(event):
    global choixBoiteChoix, widgetBoiteChoix
    # Lecture de la dernière touche appuyée dans le choix de BoiteChoix
    key = event.keysym
    if len(key) <= 1:
        if key in string.printable:
            # Si la touche est dans la liste des touches acceptées,
            # avant d'effacer la liste de touches, on enregistre la sélection
            try:
                start_n = int(widgetBoiteChoix.curselection()[0])
            except IndexError:
                start_n = -1

            # effacer la sélection
            widgetBoiteChoix.selection_clear(0, 'end')

            # démarrer de la sélection précédente +1
            for n in range(start_n+1, len(choixBoiteChoix)):
                item = choixBoiteChoix[n]
                if item[0].lower() == key.lower():
                    widgetBoiteChoix.selection_set(first=n)
                    widgetBoiteChoix.see(n)
                    return
            else:
                # pas trouvé, on reprend au début
                for n in range(len(choixBoiteChoix)):
                    item = choixBoiteChoix[n]
                    if item[0].lower() == key.lower():
                        widgetBoiteChoix.selection_set(first = n)
                        widgetBoiteChoix.see(n)
                        return

                # toujours pas trouvé -- on regarde le prochain choix logique
                for n in range(len(choixBoiteChoix)):
                    item = choixBoiteChoix[n]
                    if item[0].lower() > key.lower():
                        if n > 0:
                            widgetBoiteChoix.selection_set(first = (n-1))
                        else:
                            widgetBoiteChoix.selection_set(first = 0)
                        widgetBoiteChoix.see(n)
                        return

                # encore rien (pas de choix plus grand que la touche)
                # on met la sélection au premier item de la liste
                lastIndex = len(choixBoiteChoix)-1
                widgetBoiteChoix.selection_set(first = lastIndex)
                widgetBoiteChoix.see(lastIndex)
                return

#-----------------------------------------------------------------------
# formatage_message_erreur
#-----------------------------------------------------------------------
def formatage_message_erreur():
    """
    Transcrit un message d'erreur (exception) en chaine utilisable pour affichage.
    """
    return "".join(traceback.format_exception(
           sys.exc_info()[0]
        ,  sys.exc_info()[1]
        ,  sys.exc_info()[2]
        ))

#-----------------------------------------------------------------------
# boite_erreur_programme
#-----------------------------------------------------------------------
def boite_erreur_programme(msg=None, titre=None):
    """
    Affiche une boîte avec un message d'erreur généré par Python (except)
    On peut éventuellement rajouter un titre ou un message.
    La dernière exception déclarée par l'interpréteur est utilisée.
    """
    if titre == None: titre = "Rapport d\'erreur"
    if msg == None:
        msg = "Une erreur (exception) est survenue dans le programme."

    boite_code(msg, titre, formatage_message_erreur())

#-------------------------------------------------------------------
# boite_code
#-------------------------------------------------------------------

def boite_code(msg=""
    , titre=" "
    , text=""
    ):
    """
    Affiche un texte dans une police à taille fixe sans retour à la ligne.
    Cette fonction est utilisable pour afficher du code ou un texte
    formaté avec des blancs (HTML par ex.).
    Le texte doit être une chaîne ou une liste de lignes.
    Le texte peut être modifié, le retour sera le texte modifié.
    """
    return boite_texte(msg, titre, text, codebox=1 )

#-------------------------------------------------------------------
# boite_texte
#-------------------------------------------------------------------
def boite_texte(msg=""
    , titre=" "
    , text=""
    , codebox=0
    ):
    """
    Affiche un texte dans une police proportionnelle avec retour automatique à la ligne.
    Cette fonction est utilisable pour afficher des textes standard.
    Le texte doit être une chaîne ou une liste de lignes.
    Le texte peut être modifié, le retour sera le texte modifié.
    """

    if msg == None: msg = ""
    if titre == None: titre = ""

    global fenetreBoite, __TexteBoutonReponse, __TextesWidget, buttonsFrame
    global rootWindowPosition
    choices = ["OK"]
    __TexteBoutonReponse = choices[0]

    fenetreBoite = Tk()

    fenetreBoite.protocol('WM_DELETE_WINDOW', denyWindowManagerClose )

    screen_width = fenetreBoite.winfo_screenwidth()
    screen_height = fenetreBoite.winfo_screenheight()
    root_width = int((screen_width * 0.8))
    root_height = int((screen_height * 0.5))
    root_xpos = int((screen_width * 0.1))
    root_ypos = int((screen_height * 0.05))

    fenetreBoite.title(titre)
    fenetreBoite.iconname('Dialog')
    rootWindowPosition = "+0+0"
    fenetreBoite.geometry(rootWindowPosition)
    fenetreBoite.expand=NO
    fenetreBoite.minsize(root_width, root_height)
    rootWindowPosition = "+" + str(root_xpos) + "+" + str(root_ypos)
    fenetreBoite.geometry(rootWindowPosition)

    mainframe = Frame(master=fenetreBoite)
    mainframe.pack(side=TOP, fill=BOTH, expand=YES)

    # ---------------- mise en place du cadre ----------------------------------
    # on place d'abord le cadre de la boite_texte de sorte à avoir la place nécessaire
    boite_texteFrame = Frame(mainframe, borderwidth=3)
    boite_texteFrame.pack(side=BOTTOM , fill=BOTH, expand=YES)

    message_and_buttonsFrame = Frame(mainframe)
    message_and_buttonsFrame.pack(side=TOP, fill=X, expand=NO)

    messageFrame = Frame(message_and_buttonsFrame)
    messageFrame.pack(side=LEFT, fill=X, expand=YES)

    buttonsFrame = Frame(message_and_buttonsFrame)
    buttonsFrame.pack(side=RIGHT, expand=NO)

    # ---------------- mise en place des widgets dans le cadre -----------------
    # place une zone de texte (textArea) dans le cadre supérieur
    if codebox:
        character_width = int((root_width * 0.6) / MONOSPACE_FONT_SIZE)
        textArea = Text(boite_texteFrame,height=25,width=character_width, padx="2m", pady="1m")
        textArea.configure(wrap=NONE)
        textArea.configure(font=(MONOSPACE_FONT_FAMILY, MONOSPACE_FONT_SIZE))

    else:
        character_width = int((root_width * 0.6) / PROPORTIONAL_FONT_SIZE)
        textArea = Text(boite_texteFrame, height=25, width=character_width, padx="2m", pady="1m")
        textArea.configure(wrap=WORD)
        textArea.configure(font=(PROPORTIONAL_FONT_FAMILY,PROPORTIONAL_FONT_SIZE))


    # liaison du clavier avec les barres de défilement
    mainframe.bind("<Next>" , textArea.yview_scroll( 1,PAGES))
    mainframe.bind("<Prior>", textArea.yview_scroll(-1,PAGES))

    mainframe.bind("<Right>", textArea.xview_scroll( 1,PAGES))
    mainframe.bind("<Left>" , textArea.xview_scroll(-1,PAGES))

    mainframe.bind("<Down>", textArea.yview_scroll( 1,UNITS))
    mainframe.bind("<Up>"  , textArea.yview_scroll(-1,UNITS))

    # ajoute une barre de défilement verticale
    rightScrollbar = Scrollbar(boite_texteFrame, orient=VERTICAL, command=textArea.yview)
    textArea.configure(yscrollcommand = rightScrollbar.set)

    # ajoute une barre de défilement horizontale
    bottomScrollbar = Scrollbar(boite_texteFrame, orient=HORIZONTAL, command=textArea.xview)
    textArea.configure(xscrollcommand = bottomScrollbar.set)

    # Regroupement de la zone de texte et des barres de défilement.
    # Bien que la zone de texte soit définie en premier, on la "pack" en dernier
    # pour que la barre horizontale soit correctement placée.

    # On n'a d'ailleurs besoin d'une barre horizontale que pour la boite_code
    # puisque pour la boite_texte les retours à la ligne se font automatiquement.
    if codebox:
        bottomScrollbar.pack(side=BOTTOM, fill=X)
    rightScrollbar.pack(side=RIGHT, fill=Y)
    textArea.pack(side=LEFT, fill=BOTH, expand=YES)

    # ---------- place un widget message dans son cadre ------------------------
    messageWidget = Message(messageFrame, anchor=NW, text=msg, width=int(root_width * 0.9))
    messageWidget.configure(font=(PROPORTIONAL_FONT_FAMILY,PROPORTIONAL_FONT_SIZE))
    messageWidget.pack(side=LEFT, expand=YES, fill=BOTH, padx='1m', pady='1m')

    #------------ place les boutons dans leur cadre ----------------------------
    okButton = Button(buttonsFrame, takefocus=YES, text="OK", height=1, width=6)
    okButton.pack(expand=NO, side=TOP,  padx='2m', pady='1m', ipady="1m", ipadx="2m")

    # liaison du commandButton avec le gestionnaire d'évènements
    commandButton  = okButton
    handler = __boite_texteOK
    for selectionEvent in ["Return","Button-1","Escape"]:
        commandButton.bind("<%s>" % selectionEvent, handler)

    # ----------------- l'action commence ----------------------------------------
    try:
        # chargement du texte dans la zone de texte
        if type(text) == type("abc"): pass
        else:
            try:
                text = "".join(text)  # conversion d'une liste en une unique chaîne
            except:
                boite_message("Erreur en essayant de convertir "+ str(type(text)) + " en texte dans la zone de texte")
                sys.exit(16)
        textArea.insert(END,text, "normal")

    except:
        boite_message("Ereur lors du chargement du texte.")
        sys.exit(16)

    try:
        okButton.focus_force()
    except:
        boite_message("Erreur en essayant d'activer le bouton Ok.")
        sys.exit(16)

    fenetreBoite.mainloop()

    # récupération du texte modifié et fermeture de la fenêtre
    areaText = textArea.get(0.0,END)
    fenetreBoite.destroy()
    return areaText # retourne __TexteBoutonReponse

#-------------------------------------------------------------------
# __boite_texteOK
#-------------------------------------------------------------------
def __boite_texteOK(event):
    global fenetreBoite
    fenetreBoite.quit()

#-------------------------------------------------------------------
# repertoire_ouvre
#-------------------------------------------------------------------
def repertoire_ouvre(msg=None
    , titre=None
    , default=None
    ):
    """
    Boite de dialogue destinée à choisir un répertoire.
    Si un message est spécifié il est ignoré.
    Retourne le nom d'un répertoire ou None si annulation.
    Si "default" précise un répertoire valide, la boite démarre sur ce répertoire,
    sinon c'est le répertoire courant.
    """
    titre=getFileDialogTitle(msg,titre)
    localRoot = Tk()
    localRoot.withdraw()
    if not default: default = None
    f = tk_FileDialog.askdirectory(
          parent=localRoot
        , title=titre
        , initialdir=default
        , initialfile=None
        )
    localRoot.destroy()
    if not f: return None
    return os.path.normpath(f)

#-------------------------------------------------------------------
# getFileDialogTitle
#-------------------------------------------------------------------
def getFileDialogTitle(msg
    , titre
    ):
    if msg and titre: return "%s - %s" % (titre,msg)
    if msg and not titre: return str(msg)
    if titre and not msg: return str(titre)
    return None # ni message ni titre

#-------------------------------------------------------------------
# La classe FileTypeObject est utilisée par fichier_ouvre.
#-------------------------------------------------------------------
class FileTypeObject:
    def __init__(self,filemask):
        if len(filemask) == 0:
            raise AssertionError('Type de Fichier est vide.')

        self.masks = []

        if type(filemask) == type("abc"):  # une chaîne
            self.initializeFromString(filemask)

        elif type(filemask) == type([]): # une liste
            if len(filemask) < 2:
                raise AssertionError('Masque de Fichier invalide.\n'
                +'La liste contient moins de 2 termes : "%s"' % filemask)
            else:
                self.name  = filemask[-1]
                self.masks = list(filemask[:-1] )
        else:
            raise AssertionError('Masque de Fichier invalide : "%s"' % filemask)

    def __eq__(self,other):
        if self.name == other.name: return True
        return False

    def add(self,other):
        for mask in other.masks:
            if mask in self.masks: pass
            else: self.masks.append(mask)

    def toTuple(self):
        return (self.name,tuple(self.masks))

    def isAll(self):
        if self.name == "Tous types": return True
        return False

    def initializeFromString(self, filemask):
        # enlève tout sauf l'extension du masque de fichier.
        self.ext = os.path.splitext(filemask)[1]
        if self.ext == "" : self.ext = ".*"
        if self.ext == ".": self.ext = ".*"
        self.name = self.getName()
        self.masks = ["*" + self.ext]

    def getName(self):
        e = self.ext
        if e == ".*"  : return "Tous types"
        if e == ".txt": return "fichiers Texte"
        if e == ".py" : return "fichiers Python"
        if e == ".pyc" : return "fichiers Python"
        if e == ".xls": return "fichiers Excel"
        if e.startswith("."):
            return e[1:].upper() + " fichiers"
        return e.upper() + " fichiers"


#-------------------------------------------------------------------
# fichier_ouvre
#-------------------------------------------------------------------
def fichier_ouvre(msg=None
    , titre=None
    , default="*"
    , filetypes=None
    ):
    """
    Boite de dialogue destinée à choisir un fichier.

    Info sur l'argument "default"
    ============================
        L'argument "default" précise un chemin qui (normalement)
        contient un ou plusieurs jokers.
        fichier_ouvre va afficher seulement les fichiers qui coincident avec le
        masque fourni.
        Si "default" est omis, "*" est utilisé (tous les fichiers du répertoire courant).

        Exemple WINDOWS 1 :
            ...default="c:/monrepertoire/*.py"
        ouvrira le répertoire c:\monrepertoire\ et affichera tous les fichiers Python.

        Exemple WINDOWS 2 :
            ...default="c:/monrepertoire/test*.py"
        ouvrira le répertoire c:\monrepertoire\ et affichera tous les fichiers
        Python dont le nom commence par test.

        Remarque: sous Windows, fichier_ouvre change automatiquement le séparateur
        de répertoire / (slash) de Python en sééparateur Windows : \ (antislash).

    Info sur l'argument "filetypes"
    ==============================
        S'il existe, il peut contenir une liste d'items,
        chaque item peut-être :
            - une chaîne contenant un masque comme "*.txt"
            - une liste de chaînes , où toutes les chaines contiennent un masque
                sauf la dernière (chacune commencera par "*.", comme "*.txt" pour
                les fichiers texte, "*.py" pour les fichiers Python, etc.) ;
                la dernière chaîne sera une description de fichier.
        Exemple :
            filetypes = ["*.css", ["*.htm", "*.html", "HTML files"]  ]

    Remarque
    =========
        Si la liste filetypes ne contient pas ("All files","*"), il sera ajouté.

        Si la liste filetypes ne contient pas de masque incluant l'extension de
        l'argument "default", il sera ajouté.
        Par exemple, si on a default="*abc.py" et qu'aucun filetypes n'est
        spécifié, alors *.py" sera ajouté.

    @rtype: chaîne ou None
    @retourne : le nom du fichier ou None si annulation.

    @arg msg: message à afficher.
    @arg titre: titre de la fenêtre
    @arg default: chemin du fichier avec jokers
    @arg filetypes: masques de fichiers comme "*.txt"
    """
    localRoot = Tk()
    localRoot.withdraw()

    initialbase, initialfile, initialdir, filetypes = fileboxSetup(default,filetypes)

    #------------------------------------------------------------
    # Paramètres de tk_FileDialog.askopenfilename :
    # si initialfile ne contient aucun joker, on n'a pas de fichier
    # initial. On n'en a alors pas besoin.
    # De même si initialbase est simplement "*", on n'a pas besoin
    #d'initialfile.
    #------------------------------------------------------------
    if (initialfile.find("*") < 0) and (initialfile.find("?") < 0):
        initialfile = None
    elif initialbase == "*":
        initialfile = None

    f = tk_FileDialog.askopenfilename(parent=localRoot
        , title=getFileDialogTitle(msg,titre)
        , initialdir=initialdir
        , initialfile=initialfile
        , filetypes=filetypes
        )

    localRoot.destroy()

    if not f: return None
    return os.path.normpath(f)


#-------------------------------------------------------------------
# fichier_sauve
#-------------------------------------------------------------------
def fichier_sauve(msg=None
    , titre=None
    , default=""
    , filetypes=None
    ):
    """
    Boite de dialogue destinée à saisir le nom de sauvegarde d'un fichier.

    Retourne un nom de fichier ou None si annulation.
    "default" peut contenir un nom de fichier (le nom initial du fichier
    à enregistrer), ou vide ou contenir un masque incluant des jokers.
    "filetypes" fonctionne comme dans fichier_ouvre.
    """

    localRoot = Tk()
    localRoot.withdraw()

    initialbase, initialfile, initialdir, filetypes = fileboxSetup(default,filetypes)

    f = tk_FileDialog.asksaveasfilename(parent=localRoot
        , title=getFileDialogTitle(msg,titre)
        , initialfile=initialfile
        , initialdir=initialdir
        , filetypes=filetypes
        )
    localRoot.destroy()
    if not f: return None
    return os.path.normpath(f)

#-------------------------------------------------------------------
#
# fileboxSetup
#
#-------------------------------------------------------------------
def fileboxSetup(default,filetypes):

    if not default: default = os.path.join(".","*")
    initialdir, initialfile = os.path.split(default)
    if not initialdir : initialdir  = "."
    if not initialfile: initialfile = "*"
    initialbase, initialext = os.path.splitext(initialfile)
    initialFileTypeObject = FileTypeObject(initialfile)

    allFileTypeObject = FileTypeObject("*")
    ALL_filetypes_was_specified = False

    if not filetypes: filetypes= []
    filetypeObjects = []

    for filemask in filetypes:
        fto = FileTypeObject(filemask)

        if fto.isAll():
            ALL_filetypes_was_specified = True # important

        if fto == initialFileTypeObject:
            initialFileTypeObject.add(fto)
        else:
            filetypeObjects.append(fto)

    #------------------------------------------------------------------
    # S'assurer que la liste des filetypes inclut le type ALL FILES.
    #------------------------------------------------------------------
    if ALL_filetypes_was_specified:
        pass
    elif allFileTypeObject == initialFileTypeObject:
        pass
    else:
        filetypeObjects.insert(0,allFileTypeObject)
    #------------------------------------------------------------------
    # S'assurer que la liste inclut initialFileTypeObject
    # de sorte que ce soit l'option par défault.
    # Modification de comportement entre Python version 2.5 et 2.6
    #------------------------------------------------------------------
    if len(filetypeObjects) == 0:
        filetypeObjects.append(initialFileTypeObject)

    if initialFileTypeObject in (filetypeObjects[0], filetypeObjects[-1]):
        pass
    else:
        if runningPython26:
            filetypeObjects.append(initialFileTypeObject)
        else:
            filetypeObjects.insert(0,initialFileTypeObject)

    filetypes = [fto.toTuple() for fto in filetypeObjects]

    return initialbase, initialfile, initialdir, filetypes

#-------------------------------------------------------------------
# Routines de base
#-------------------------------------------------------------------
# Ces routines sont utilisées dans plusieurs fonctions du module EasyGuiFr.

def __buttonEvent(event):
    """
    Transmet un événement généré par le clic d'un bouton.
    """
    global  fenetreBoite, __TextesWidget, __TexteBoutonReponse
    __TexteBoutonReponse = __TextesWidget[event.widget]
    fenetreBoite.quit() # quitte la boucle principale

def __put_buttons_in_buttonframe(choices):
    """
    Place les boutons dans le cadre ad-hoc
    """
    global __TextesWidget, __premierWidget, buttonsFrame

    __premierWidget = None
    __TextesWidget = {}

    i = 0

    for buttonText in choices:
        tempButton = Button(buttonsFrame, takefocus=1, text=buttonText)
        bindArrows(tempButton)
        tempButton.pack(expand=YES, side=LEFT, padx='1m', pady='1m', ipadx='2m', ipady='1m')

        # garder la trace du texte associé à ce widget
        __TextesWidget[tempButton] = buttonText

        # Garder la trace du premier widget pour mettre le focus dessus
        if i == 0:
            __premierWidget = tempButton
            i = 1

        # liaison du commandButton avec le gestionnaire d'évènements
        commandButton  = tempButton
        handler = __buttonEvent
        for selectionEvent in STANDARD_SELECTION_EVENTS:
            commandButton.bind("<%s>" % selectionEvent, handler)

#-----------------------------------------------------------------------
#
#     classe EgStore
#
#-----------------------------------------------------------------------
class EgStore:
    r"""
    Cette classe permet un stockage persistant des données d'une application
    basée sur EasyGuiFr.

# Exemple A
#-----------------------------------------------------------------------
# define a class named Settings as a subclass of EgStore
#-----------------------------------------------------------------------
class Settings(EgStore):
::
    def __init__(self, filename):  # filename is required
        #-------------------------------------------------
        # Specify default/initial valeurs for variables that
        # this particular application wants to remember.
        #-------------------------------------------------
        self.userId = ""
        self.targetServer = ""

        #-------------------------------------------------
        # For subclasses of EgStore, these must be
        # the last two statements in  __init__
        #-------------------------------------------------
        self.filename = filename  # this is required
        self.restore()            # restore valeurs from the storage file if possible



# Example B
#-----------------------------------------------------------------------
# create settings, a persistent Settings object
#-----------------------------------------------------------------------
settingsFile = "myApp_settings.txt"
settings = Settings(settingsFile)

user    = "obama_barak"
server  = "whitehouse1"
settings.userId = user
settings.targetServer = server
settings.store()    # persist the settings

# run code that gets a new value for userId, and persist the settings
user    = "biden_joe"
settings.userId = user
settings.store()


# Example C
#-----------------------------------------------------------------------
# recover the Settings instance, change an attribute, and store it again.
#-----------------------------------------------------------------------
settings = Settings(settingsFile)
settings.userId = "vanrossum_g"
settings.store()

"""
    def __init__(self, filename):  # obtaining filename is required
        self.filename = None
        raise NotImplementedError()

    def restore(self):
        """
        Set the valeurs of whatever attributes are recoverable
        from the pickle file.

        Populate the attributes (the __dict__) of the EgStore object
        from     the attributes (the __dict__) of the pickled object.

        If the pickled object has attributes that have been initialized
        in the EgStore object, then those attributes of the EgStore object
        will be replaced by the valeurs of the corresponding attributes
        in the pickled object.

        If the pickled object is missing some attributes that have
        been initialized in the EgStore object, then those attributes
        of the EgStore object will retain the valeurs that they were
        initialized with.

        If the pickled object has some attributes that were not
        initialized in the EgStore object, then those attributes
        will be ignored.

        IN SUMMARY:

        After the recover() operation, the EgStore object will have all,
        and only, the attributes that it had when it was initialized.

        Where possible, those attributes will have valeurs recovered
        from the pickled object.
        """
        if not os.path.exists(self.filename): return self
        if not os.path.isfile(self.filename): return self

        try:
            f = open(self.filename,"rb")
            unpickledObject = pickle.load(f)
            f.close()

            for key in list(self.__dict__.keys()):
                default = self.__dict__[key]
                self.__dict__[key] = unpickledObject.__dict__.get(key,default)
        except:
            pass

        return self

    def store(self):
        """
        Save the attributes of the EgStore object to a pickle file.
        Note that if the directory for the pickle file does not already exist,
        the store operation will fail.
        """
        f = open(self.filename, "wb")
        pickle.dump(self, f)
        f.close()


    def kill(self):
        """
        Delete my persistent file (i.e. pickle file), if it exists.
        """
        if os.path.isfile(self.filename):
            os.remove(self.filename)
        return

    def __str__(self):
        """
        return my contents as a string in an easy-to-read format.
        """
        # find the length of the longest attribute name
        longest_key_length = 0
        keys = []
        for key in self.__dict__.keys():
            keys.append(key)
            longest_key_length = max(longest_key_length, len(key))

        keys.sort()  # sort the attribute names
        lines = []
        for key in keys:
            value = self.__dict__[key]
            key = key.ljust(longest_key_length)
            lines.append("%s : %s\n" % (key,repr(value))  )
        return "".join(lines)  # return a string showing the attributes

#-----------------------------------------------------------------------
#
# test/demo easyguifr
#
#-----------------------------------------------------------------------
def egdemo():
    """
    Lance la démo d'EasyGuiFr.
    """
    # efface la console
    writeln("\n" * 100)

    intro_message = ("Sélectionner le type de boîte en démo\n"
    + "\n * Python version " + sys.version
    + "\n * EasyGuiFr version " + Version_EG
    + "\n * Tk version " + str(TkVersion)
    )

    while 1: # boucle permanente
        choices = [
            "boite_message",
            "boite_bouton -- boite avec boutons",
            "boite_bouton(image)-- une boite_bouton avec image",
            "boite_choix",
            "multboite_choix",
            "boite_texte",
            "boite oui non",
            "boite continuer annuler",
            "saisie_base",
            "saisie_base(image) -- saisie_base sous une image",
            "boite_erreur_programme",
            "boite_code",
            "saisie_entier",
            "boite_vrai_faux",
            "boite_choix_numero",
            "fichier_sauve",
            "fichier_ouvre",
            "saisie_motdepasse",
            "multsaisie_base",
            "multsaisie_motdepasse",
            "repertoire_ouvre",
            "information",
            "aide"
            ]
        choice = boite_choix(msg=intro_message
            , titre="EasyGuiFr " + Version_EG
            , choix=choices)

        if not choice: return

        reply = choice.split()

        if   reply[0] == "boite_message":
            reply = boite_message("Petit message", "C'est un titre long")
            writeln("Votre reponse est : %s" % repr(reply))

        elif reply[0] == "information":
            reply = information()

        elif reply[0] == "aide":
            _demo_help()

        elif reply[0] == "boite_bouton":
            reply = boite_bouton()
            writeln("Votre reponse est : %s" % repr(reply))

            titre = "Démo de boite_bouton avec beaucoup de boutons !"
            msg = "Cette boite_bouton montre ce qui se passe si on a trop de boutons."
            reply = boite_bouton(msg=msg, titre=titre, choix=choices)
            writeln("Votre reponse est : %s" % repr(reply))

        elif reply[0] == "boite_bouton(image)":
            _demo_boite_bouton_avec_image()

        elif reply[0] == "boite_vrai_faux":
            reply = boite_vrai_faux()
            writeln("Votre reponse est : %s" % repr(reply))

        elif reply[0] == "saisie_base":
            image = "python_and_check_logo.gif"
            message = "Entre le nom de ton/ta meilleur(e) ami(e)."\
                      "\n(Le résultat va être nettoyé des blancs inutiles.)"
            reply = saisie_base(message, "Love !", "   Marie-Renée Leblanc    ")
            writeln("Ta reponse est : %s" % repr(reply))

            message = "Entre le nom de ton/ta meilleur(e) ami(e)."\
                      "\n(Le résultat NE va PAS être nettoyé des blancs inutiles.)"
            reply = saisie_base(message, "Love!", "     Sagamore Noonan     ",nettoie=False)
            writeln("Ta reponse est : %s" % repr(reply))

        elif reply[0] == "saisie_base(image)":
            image = "python_and_check_logo.gif"
            message = "Quelle sorte de serpent avons-nous là ?"
            reply = saisie_base(message, "Quiz",image=image)
            writeln("Ta reponse est : %s" % repr(reply))

        elif reply[0] == "boite_erreur_programme":
            try:
                thisWillCauseADivideByZeroException = 1/0
            except:
                boite_erreur_programme()

        elif reply[0] == "saisie_entier":
            reply = saisie_entier(
                "Entre un nombre entre 3 et 333",
                "Démo: saisie_entier AVEC une valeur par défaut",222, 3, 333)
            writeln("Ta reponse est : %s" % repr(reply))

            reply = saisie_entier(
                "Entre un nombre entre -10 et +10",
                "Démo: saisie_entier SANS valeur par défaut"
                )
            writeln("Ta reponse est : %s" % repr(reply))

        elif reply[0] == "repertoire_ouvre" : _demo_repertoire_ouvre()
        elif reply[0] == "fichier_ouvre": _demo_fichier_ouvre()
        elif reply[0] == "fichier_sauve": _demo_fichier_sauve()

        elif reply[0] == "boite_choix_numero":
            titre = reply[0]
            msg   =  "Démo de " + reply[0]
            choices = ["Choix 1", "Choix 2", "Choix 3", "Choix 4"]
            reply = boite_choix_numero(msg, titre, choices)
            writeln("Ta reponse est : %s" % repr(reply))

        elif reply[0] == "saisie_motdepasse":
            reply = saisie_motdepasse("Démo de boite_motdepasse SANS valeur par défaut"
                + "\n\nEntre ton mot de passe secret", "Member Logon")
            writeln("Ta reponse est : %s" % str(reply))

            reply = saisie_motdepasse("Démo de boite_motdepasse AVEC valeur par défaut"
                + "\n\nEntre ton mot de passe secret", "Member Logon", "alfie")
            writeln("Ta reponse est : %s" % str(reply))

        elif reply[0] == "multsaisie_base":
            msg = "Entre tes informations personnelles"
            titre = "Adresse"
            fieldNames = ["Nom","Prénom","Rue","Ville","Code Postal"]
            fieldValues = []  # on démarre avec des champs vides
            fieldValues = multsaisie_base(msg,titre, fieldNames)

            # s'assurer qu'aucun champ ne reste vide
            while 1:
                if fieldValues == None: break
                errmsg = ""
                for i in range(len(fieldNames)):
                    if fieldValues[i].strip() == "":
                        errmsg = errmsg + ('"%s" est indispensable.\n\n' % fieldNames[i])
                if errmsg == "": break # pas de problemes
                fieldValues = multsaisie_base(errmsg, titre, fieldNames, fieldValues)

                writeln("Ta reponse est : %s" % str(fieldValues))

        elif reply[0] == "multsaisie_motdepasse":
            msg = "Entrez les informations"
            titre = "Démo de multsaisie_motdepasse"
            fieldNames = ["Identification Serveur", "Identifiant Utilisateur", "Mot de Passe"]
            fieldValues = []  # on démarre avec des champs vides
            fieldValues = multsaisie_motdepasse(msg,titre, fieldNames)

            # s'assurer qu'aucun champ ne reste vide
            while 1:
                if fieldValues == None: break
                errmsg = ""
                for i in range(len(fieldNames)):
                    if fieldValues[i].strip() == "":
                        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
                if errmsg == "": break # pas de problemes
                fieldValues = multsaisie_motdepasse(errmsg, titre, fieldNames, fieldValues)

            writeln("Ta reponse est : %s" % str(fieldValues))

        elif reply[0] == "boite" and reply[1] == "oui":
            titre = "Démo de boite oui non"
            msg = "Es tu prêt à sauter du 10ème étage ?"
            reply = boite_oui_non(msg, titre)
            writeln("Ta reponse est : %s" % repr(reply))
            if reply:
                boite_message("Personne ne saute du 10ème étage !", "Bof !")

        elif reply[0] == "boite" and reply[1] == "continuer":
            titre = "Démo de boite continuer annuler"
            msg = "Si tu as encore faim tu auras une autre glace..."
            reply = boite_continuer_annuler(msg,titre)
            writeln("Ta reponse est : %s" % repr(reply))

        elif reply[0] == "boite_choix":
            titre = "Demo de boite_choix"
            longchoice = "TCeci est un exemple de très longue option que tu peux choisir ou pas."
            listChoices = ["nnn", "ddd", "eee", "fff", "aaa", longchoice
                    , "aaa", "bbb", "ccc", "ggg", "hhh", "iii", "jjj", "kkk", "lll", "mmm"
                    ,"nnn", "ooo", "ppp", "qqq", "rrr", "sss", "ttt", "uuu", "vvv"]

            msg = "Choisis une option. " + ("Une séquence de texte ! "*3) + "\n Une ligne de texte séparée ?"*6
            reply = boite_choix(msg=msg, choix=listChoices)
            writeln("Ta reponse est : %s" % repr(reply))

            msg = "Choisis une option."
            reply = boite_choix(msg=msg, titre=titre, choix=listChoices)
            writeln("Ta reponse est : %s" % repr(reply))

            msg = "Choisis une option."
            reply = boite_choix(msg="La liste de choix est vide !", choix=[])
            writeln("Ta reponse est : %s" % repr(reply))

        elif reply[0] == "multboite_choix":
            listChoices = ["aaa", "bbb", "ccc", "ggg", "hhh", "iii", "jjj", "kkk"
                , "LLL", "mmm" , "nnn", "ooo", "ppp", "qqq"
                , "rrr", "sss", "ttt", "uuu", "vvv"]

            msg = "Choisis autant d\'options que tu veux."
            reply = multboite_choix(msg,"Demo of multboite_choix", listChoices)
            writeln("Ta reponse est : %s" % repr(reply))

        elif reply[0] == "boite_texte": _demo_boite_texte(reply[0])
        elif reply[0] == "boite_code": _demo_boite_code(reply[0])

        else:
            boite_message("Choix\n\n" + choice + "\n\nn\'est pas reconnu", "Erreur dans le Programme")
            return

def _demo_boite_texte(reply):
    text_snippet = ((\
"""
C'etait le temps des cerises et du muguet. Tu sentais le sous-bois et la lavande mais
une tenace odeur de champignons envahit brutalement la foret...
L'homme des bois se tenait devant nous, droit comme un if, la hache a la main...
Subitement il l'abattit sur sa tete que je garde maintenant precieusement dans mon sac a dos...
L'homme est parti je ne sais ou mais il en manquait quelques morceaux que mes dents avaient arraches !
""" \
*5)+"\n\n")*10
    titre = "Démo de boite_texte"
    msg = "Voici un exemple de texte. " * 16
    reply = boite_texte(msg, titre, text_snippet)
    writeln("Votre reponse est : %s" % str(reply))

def _demo_boite_code(reply):
    code_snippet = ("dafsdfa dasflkj pp[oadsij asdfp;ij asdfpjkop asdfpok asdfpok asdfpok"*3) +"\n"+\
"""# voici un code Python débile...
for machinTruc in maListeDeBetises:
    fais quelquechose avec(machinTruc)
    fais quelquechose()
    fais quelquechose()
    if autrechose(machinTruc):
        faisQuelquechoseDePlusInteressant()

"""*16
    msg = "Voici un exemple de code. " * 16
    reply = boite_code(msg, "Exemple de Code", code_snippet)
    writeln("Votre reponse est : %s" % repr(reply))


def _demo_boite_bouton_avec_image():

    msg   = "Aimez vous cette image ?\n"
    choices = ["Oui","Non","Sans opinion"]

    for image in [
        "python_and_check_logo.gif"
        ,"python_and_check_logo.jpg"
        ,"python_and_check_logo.png"
        ,"zzzzz.gif"]:

        reply=boite_bouton(msg + image,image=image,choix=choices)
        writeln("Votre reponse est : %s" % repr(reply))


def _demo_help():
    savedStdout = sys.stdout    # save the sys.stdout file object
    sys.stdout = capturedOutput = StringIO()
    help("EasyGui")
    sys.stdout = savedStdout   # restore the sys.stdout file object
    boite_code("Aide EasyGui",text=capturedOutput.getvalue())

def _demo_fichier_sauve():
    filename = "monNouveauFichier.txt"
    titre = "Sauve Fichier"
    msg ="Sauve ficher comme:"

    f = fichier_sauve(msg,titre,default=filename)
    writeln("Vous avez choisi de sauver le fichier : %s" % f)

def _demo_repertoire_ouvre():
    titre = "Démo de repertoire_ouvre"
    msg = "Choisissez le répertoire à ouvrir."
    d = repertoire_ouvre(msg, titre)
    writeln("Vous avez choisi le répertoire : %s" % d)

def _demo_fichier_ouvre():
    msg  = "fichiers Python"
    titre = "Ouvrir fichiers"
    default="*.py"
    f = fichier_ouvre(msg,titre,default=default)
    writeln("Vous avez choisi d\'ouvrir le fichier : %s" % f)

    default="./*.gif"
    filetypes = ["*.jpg",["*.zip","*.tgs","*.gz", "fichiers archive"],["*.htm", "*.html","fichiers HTML"]]
    f = fichier_ouvre(msg,titre,default=default,filetypes=filetypes)
    writeln("Vous avez choisi d\'ouvrir le fichier : %s" % f)

def _dummy():
    pass

EASYGUI_ABOUT_INFORMATION = '''
========================================================================
0.96(2010-08-29)
========================================================================
Cette version gère quelques difficultés liées à la version de Python

BUG FIXES
------------------------------------------------------
 *  Certaines utilisations de Python 2.x- ressemblant à des exceptions faisaient
    apparaître une exception dans Python 3.x.

 *  Dans certaines circonstances, PIL était incapable d'afficher autre chose que
    des images gif.
    Il semble que cela était du à une syntaxe dépendant de la version de PIL utilisée.
    Remarque : http://www.pythonware.com/products/pil/ dit que PIL n'est pas
    encore supporté par Python 3.x.

Changement de LICENSE
------------------------------------------------------
EasyGuifr est sous le régime de ce qu\'on appelle
"modified BSD license" (ou encore "revised BSD", "new BSD", "3-clause BSD").
Cette license est GPL-compatible mais moins restrictive que GPL.
Les version précédentes étaient sous Creative Commons Attribution License 2.0.

'''

def information():
    """
    Affiche quelques informations sur EasyGui
    """
    boite_code("informations EasyGui\n"+Version_EG,"EasyGui",EASYGUI_ABOUT_INFORMATION)
    return None

if __name__ == '__main__':
    if True:
        egdemo()
    else:
        # test de la fenêtre principale
        root = Tk()
        msg = """Ceci est un test de la fenêtre principale Tk() où sera placée une boite_message.
                C'est un essai instructif.\n\n"""
        messageWidget = Message(root, text=msg, width=1000)
        messageWidget.pack(side=TOP, expand=YES, fill=X, padx='3m', pady='3m')
        messageWidget = Message(root, text=msg, width=1000)
        messageWidget.pack(side=TOP, expand=YES, fill=X, padx='3m', pady='3m')


        boite_message("test de passage à fenetreBoite", root=root)
        boite_message("second test de passage à fenetreBoite", root=root)

        reply = saisie_base("Saisissez quelque chose au clavier", root=root)
        writeln("Vous avez écrit :", reply)

        reply = saisie_base("Saisissez autre chose au clavier", root=root)
        writeln("Vous avez écrit :", reply)
        root.destroy()

"""
@note:
INFORMATION de LICENSE
EasyGuiFr version 0.96.01

Copyright (c) 2010, Stephen Raymond Ferg
2014, Frédéric Laroche
Tous droits réservés.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
       this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright notice,
       this list of conditions and the following disclaimer in the documentation and/or
       other materials provided with the distribution.

    3. The name of the author may not be used to endorse or promote products derived
       from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

@note:
ABOUT THE EASYGUI LICENSE

This license is what is generally known as the "modified BSD license",
aka "revised BSD", "new BSD", "3-clause BSD".
See http://www.opensource.org/licenses/bsd-license.php

This license is GPL-compatible.
See http://en.wikipedia.org/wiki/License_compatibility
See http://www.gnu.org/licenses/license-list.html#GPLCompatibleLicenses

The BSD License is less restrictive than GPL.
It allows software released under the license to be incorporated into proprietary products.
Works based on the software may be released under a proprietary license or as closed source software.
http://en.wikipedia.org/wiki/BSD_licenses#3-clause_license_.28.22New_BSD_License.22.29

"""