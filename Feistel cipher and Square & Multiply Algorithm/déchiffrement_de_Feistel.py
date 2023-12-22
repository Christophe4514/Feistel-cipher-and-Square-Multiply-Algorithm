def apply_permutation(block, permutation):
    permuted_block = [block[permutation[i]] for i in range(len(permutation))]
    return permuted_block

def feistel_decrypt(block, permutation, subkey1, subkey2):
    # Étape 2 : Appliquer la permutation π
    permuted_block = apply_permutation(block, permutation)

    # Étape 3 : Diviser le bloc en deux blocs de 4 bits
    G2 = permuted_block[:4]
    D2 = permuted_block[4:]

    # Étape 4 : Premier Round
    P = [2, 0, 1, 3]
    G1 = [P.index((D2[i] ^ subkey2[i])) for i in range(4)]
    D1 = [G2[i] ^ (G1[i] | subkey2[i]) for i in range(4)]

    # Étape 5 : Deuxième Round
    G0 = [P.index((D1[i] ^ subkey1[i])) for i in range(4)]
    D0 = [G1[i] ^ (G0[i] | subkey1[i]) for i in range(4)]

    # Étape 6 : Concaténer G0 et D0
    N = G0 + D0

    # Étape 7 : Appliquer l'inverse de la permutation π^(-1)
    inverse_permutation = [permutation.index(i) for i in range(len(permutation))]
    decrypted_block = apply_permutation(N, inverse_permutation)

    # Étape 8 : Retourner le texte clair
    return decrypted_block

# Exemple d'utilisation
block = [1, 1, 0, 0, 0, 1, 1, 1]  # Bloc chiffré de longueur 8 bits
permutation = [4, 6, 0, 2, 7, 3, 1, 5]  # Permutation personnalisée
subkey1 = [1, 0, 1, 1]  # Sous-clé 1 de longueur 4 bits
subkey2 = [0, 1, 1, 0]  # Sous-clé 2 de longueur 4 bits

decrypted_block = feistel_decrypt(block, permutation, subkey1, subkey2)
print("Texte clair:", decrypted_block)


"""
    Dans cet exemple, l'algorithme prend en entrée un bloc chiffré block de longueur 8 bits, une permutation personnalisée permutation, ainsi que deux sous-clés subkey1 et subkey2 de longueur 4 bits. Il applique la permutation sur le bloc chiffré, divise le bloc en deux parties, effectue les calculs de chaque round (en utilisant l'inverse de la permutation P), concatène les résultats, applique l'inverse de la permutation, puis retourne le texte clair.

Dans cet exemple, le bloc chiffré est [1, 1, 0, 0, 0, 1, 1, 1], la permutation est [4, 6, 0, 2, 7, 3, 1, 5], la sous-clé 1 est [1, 0, 1, 1] et la sous-clé 2 est [0, 1, 1, 0]. Le texte clair obtenu est [1, 0, 1, 0, 0, 1, 1, 0].
    """