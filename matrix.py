import tkinter as tk
import numpy as np
from tkinter import messagebox

# Déclaration des variables globales
matrice1_entry = []
matrice2_entry = []
resultat_entry = []
dimension = 0
mat_resultat = np.zeros((dimension, dimension), dtype=int)

def creer_matrice():
    global matrice1_entry, matrice2_entry, resultat_entry, dimension

    try:
        # Récupérer les dimensions des matrices
        dimension = int(dim_matrice.get())

        if dimension <= 1:
            raise ValueError("La dimension de la matrice doit être supérieure ou égal à deux")
        if dimension >= 10 :
            raise ValueError("Plus petit")

        # Supprimer les grilles existantes
        for widget in frame_matrice1.winfo_children():
            widget.destroy()
        for widget in frame_matrice2.winfo_children():
            widget.destroy()
        for widget in frame_resultat.winfo_children():
            widget.destroy()

        # Créer les grilles de saisie pour les matrices et le résultat
        matrice1_entry = []
        matrice2_entry = []
        resultat_entry = []

        for i in range(dimension):
            ligne1_entry = []
            ligne2_entry = []
            ligne_resultat = []
            for j in range(dimension):
                entry1 = tk.Entry(frame_matrice1, width=3)
                entry1.grid(row=i, column=j)
                ligne1_entry.append(entry1)

                entry2 = tk.Entry(frame_matrice2, width=3)
                entry2.grid(row=i, column=j)
                ligne2_entry.append(entry2)

                entry_resultat = tk.Entry(frame_resultat, width=5)
                entry_resultat.grid(row=i, column=j)
                ligne_resultat.append(entry_resultat)
            matrice1_entry.append(ligne1_entry)
            matrice2_entry.append(ligne2_entry)
            resultat_entry.append(ligne_resultat)
            
    except ValueError as e:
        afficher_erreur(str(e))

def additionner_matrice():
    global mat_resultat
    try:
        mat_resultat = np.zeros((dimension, dimension), dtype=int)
        for i in range(dimension):
            for j in range(dimension):
                valeur1 = int(matrice1_entry[i][j].get())
                valeur2 = int(matrice2_entry[i][j].get())
                mat_resultat[i, j] = valeur1 + valeur2
        afficher_resultat()
    except ValueError:
        afficher_erreur("Les coefficients des matrices doivent être des reels")

def multiplier_matrice():
    global mat_resultat
    try:
        mat_val1 = np.array([[int(entry.get()) for entry in row] for row in matrice1_entry])
        mat_val2 = np.array([[int(entry.get()) for entry in row] for row in matrice2_entry])
        mat_resultat = np.dot(mat_val1, mat_val2)
        afficher_resultat()
    except ValueError:
        afficher_erreur("Les coefficients des matrices doivent être des reels")

def reset_matrice():
    global matrice1_entry, matrice2_entry, resultat_entry
    for i in range(dimension):
        for j in range(dimension):
            matrice1_entry[i][j].delete(0, tk.END)
            matrice2_entry[i][j].delete(0, tk.END)
            resultat_entry[i][j].delete(0, tk.END)
            #taille.delete(0,tk.END)

def afficher_resultat():
    for i in range(dimension):
        for j in range(dimension):
            resultat_entry[i][j].delete(0, tk.END)
            resultat_entry[i][j].insert(0, str(mat_resultat[i, j]))

def afficher_erreur(message):
    messagebox.showerror("Erreur", message)

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calcul Matrice")


titre = tk.Label(fenetre, text = "Calcul Matrice", font =("Veradana", 20), bg ="sky blue", fg = "#154360").pack()

fenetre.geometry("300x200")
fenetre.config(bg = "sky blue")

# Frame pour la taille de la matrice
frame_dim = tk.Frame(fenetre)
frame_dim.pack()


label_dim = tk.Label(frame_dim, text="Dimension de la matrice:", bg = "sky blue")
label_dim.grid(row=0, column=0)

dim_matrice = tk.Entry(frame_dim, width=5)
dim_matrice.grid(row=0, column=1)

# Bouton pour créer les matrices
bouton_creer = tk.Button(frame_dim, text="Créer", bg ="#1F618D", fg ="white" ,command=creer_matrice)
bouton_creer.grid(row=0, column=2)

# Frames pour les matrices
frame_matrice1 = tk.Frame(fenetre)
frame_matrice1.pack(side=tk.LEFT, padx=10)

frame_matrice2 = tk.Frame(fenetre)
frame_matrice2.pack(side=tk.LEFT, padx=10)

frame_resultat = tk.Frame(fenetre)
frame_resultat.pack(side=tk.RIGHT, padx=30)

# Boutons pour les opérations
bouton_addition = tk.Button(fenetre, text="Additionner", bg ="#1F618D", fg = "white", width=10, height = 1, command=additionner_matrice)
bouton_addition.pack(side=tk.BOTTOM, padx=10, pady=10)

bouton_multiplication = tk.Button(fenetre, text="Multiplier", fg = "white", bg = "#1F618D" ,width = 10, height= 1,command=multiplier_matrice)
bouton_multiplication.pack(side=tk.BOTTOM, padx=10, pady=10)

bouton_reset = tk.Button(fenetre, text="Réinitialiser", bg = "#1F618D", fg ="white" ,width= 10, height= 1,command=reset_matrice)
bouton_reset.pack(side=tk.BOTTOM, padx=10, pady=10)

lab_resu = tk.Label(fenetre, text = "Résultat de ce côté", bg = "#2980B9", fg= "white")
lab_resu.place(x= "1700", y = "150")

menu_bar = tk.Menu(fenetre)

# menu
menu_fichier = tk.Menu(menu_bar, tearoff=0)
menu_fichier.add_command(label="Quitter", command=fenetre.quit)

menu_bar.add_cascade(label="Fichier", menu=menu_fichier)


fenetre.config(menu=menu_bar)



fenetre.mainloop()
