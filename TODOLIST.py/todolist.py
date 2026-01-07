print ('---------TODO LIST---------')
print ('1. Ajouter une tâcche')
print('2. Afficher les tâches')
print('3. Supprimer une tâche')
print('4. Quitter')

liste_taches = []
while True: # boucle infinie jusqu'a ce que l'utilisateur choisisse de quitter
    choix = input('Choisissez une option (1-4): ')
    
    if choix == '1':
        tache = input('Entrez la tâche à ajouter: ')
        liste_taches.append(tache)
        print(f'Tâche "{tache}" ajoutée.')  #confirmation d'ajout dela tache 
    
    elif choix == '2':
        print('Tâches:')
        for index, tache in enumerate(liste_taches, start=1): #enumerate pour afficher les taches avec leur numero ,,start=1 pour commencer la numerotation a 1
            print(f'{index}. {tache}')
    
    elif choix == '3':
        index_supprimer = int(input('Entrez le numéro de la tâche à supprimer: ')) - 1 #-1 permet de convertir le numero de tache en indice de liste
        if 0 <= index_supprimer < len(liste_taches): #verifie si l'indice est valide,, len() pour obtenir la taille de la liste
            tache_supprimee = liste_taches.pop(index_supprimer)  #pop() pour supprimer et renvoyer l'element a l'indice donne
            print(f'Tâche "{tache_supprimee}" supprimée.')
        else:
            print('Numéro de tâche invalide.')
    
    elif choix == '4':
        print('Quitter le programme.')
        break
    
    else:
        print('Option invalide. Veuillez choisir entre 1 et 4.')

print('---------fin du programme---------')