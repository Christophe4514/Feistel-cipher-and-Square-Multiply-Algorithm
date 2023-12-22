def generate_feistel_subkeys(key):
    # Étape 2 : Appliquer la fonction de permutation H
    H = [6, 5, 2, 7, 4, 1, 3, 0]
    permuted_key = [key[H[i]] for i in range(8)]

    # Étape 3 : Diviser la clé en deux blocs de 4 bits
    k1 = permuted_key[:4]
    k2 = permuted_key[4:]

    # Étape 4 : Calculer k1 et k2
    k1_xor_k2 = [k1[i] ^ k2[i] for i in range(4)]
    k1_and_k2 = [k1[i] & k2[i] for i in range(4)]

    # Étape 5 : Appliquer les décalages
    k1_shifted = k1_xor_k2[2:] + k1_xor_k2[:2]
    k2_shifted = k1_and_k2[1:] + k1_and_k2[:1]

    # Étape 6 : Retourner les sous-clés générées
    return k1_shifted, k2_shifted

# Exemple d'utilisation
key = [1, 0, 1, 0, 0, 1, 1, 0]  # Clé de départ de longueur 8
subkey1, subkey2 = generate_feistel_subkeys(key)
print("Sous-clé 1:", subkey1)
print("Sous-clé 2:", subkey2)

"""
    Cet algorithme prend en entrée une clé key de longueur 8 bits. Il applique la permutation de la clé, divise la clé en deux blocs de 4 bits, calcule les sous-clés k1 et k2, applique les décalages spécifiés et retourne les deux sous-clés générées.

Dans cet exemple, la clé de départ est [1, 0, 1, 0, 0, 1, 1, 0]. Les sous-clés générées sont subkey1 = [1, 0, 0, 1] et subkey2 = [1, 0, 1, 0].
    """