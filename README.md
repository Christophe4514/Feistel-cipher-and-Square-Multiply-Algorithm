# Feistel-cipher-and-Square-Multiply-Algorithm
Feistel cipher and Square &amp; Multiply Algorithm

# Installation 

    cloner le repository et lancer les différents fichiers specifiques.

* pas d'environnement virtuel à installer pour l'exécution des diffents programme.

# Chiffrement de Feistel 

    """
    L'algorithme prend en entrée un bloc block de départ de longueur 8 bits, une permutation personnalisée permutation, ainsi que deux sous-clés subkey1 et subkey2 de longueur 4 bits. Il applique la permutation sur le bloc, divise le bloc en deux parties, effectue les calculs de chaque round, concatène les résultats, applique l'inverse de la permutation, puis retourne le texte chiffré.

    Le bloc de départ est [1, 0, 1, 0, 0, 1, 1, 0], la permutation est [4, 6, 0, 2, 7, 3, 1, 5], la sous-clé 1 est [1, 0, 1, 1] et la sous-clé 2 est [0, 1, 1, 0]. Le texte chiffré obtenu est [1, 1, 0, 0, 0, 1, 1, 1].
    
    """

# Déchiffrement de Feistel 

    """
    L'algorithme prend en entrée un bloc chiffré block de longueur 8 bits, une permutation personnalisée permutation, ainsi que deux sous-clés subkey1 et subkey2 de longueur 4 bits. Il applique la permutation sur le bloc chiffré, divise le bloc en deux parties, effectue les calculs de chaque round (en utilisant l'inverse de la permutation P), concatène les résultats, applique l'inverse de la permutation, puis retourne le texte clair.

    Le bloc chiffré est [1, 1, 0, 0, 0, 1, 1, 1], la permutation est [4, 6, 0, 2, 7, 3, 1, 5], la sous-clé 1 est [1, 0, 1, 1] et la sous-clé 2 est [0, 1, 1, 0]. Le texte clair obtenu est [1, 0, 1, 0, 0, 1, 1, 0].
    
    """

# Génération de clés de Festeil 

    il ya deux algorithmes pour ceci: 


* 1) copy :

qui fait la permutation personalisée : 


    """
    L'utilisateur peut définir la permutation personnalisée en modifiant la liste permutation, l'ordre de décalage à gauche en modifiant left_shift_order et l'ordre de décalage à droite en modifiant right_shift_order. Les autres parties de l'algorithme restent les mêmes que dans l'implémentation précédente.

    Notez que les valeurs des ordres de décalage doivent être des entiers positifs, et si nécessaire, vous pouvez ajouter des validations supplémentaires pour les entrées de l'utilisateur afin de garantir que les valeurs sont correctes.
    """


* 2) géneration sans permutation personalisée : 

* 

    """
    Cet algorithme prend en entrée une clé key de longueur 8 bits. Il applique la permutation de la clé, divise la clé en deux blocs de 4 bits, calcule les sous-clés k1 et k2, applique les décalages spécifiés et retourne les deux sous-clés générées.

    Dans cet exemple, la clé de départ est [1, 0, 1, 0, 0, 1, 1, 0]. Les sous-clés générées sont subkey1 = [1, 0, 0, 1] et subkey2 = [1, 0, 1, 0].
    
    """


# Square & Multiply Algorithm

    
    """
    L'algorithme demande à l'utilisateur d'entrer les valeurs de x, b et n. Ensuite, il applique l'algorithme des carrés et des multiplications pour calculer x^b (mod n). Le résultat est affiché à la fin.

    L'algorithme des carrés et des multiplications est une méthode efficace pour calculer une exponentiation modulaire. Il repose sur le fait que toute représentation binaire de l'exposant peut être exprimée comme une combinaison de puissances de 2. L'algorithme effectue des carrés successifs et des multiplications supplémentaires en fonction des bits de l'exposant pour obtenir le résultat final. Cela réduit le nombre total de multiplications requises par rapport à une méthode naïve de multiplication répétée.
    """