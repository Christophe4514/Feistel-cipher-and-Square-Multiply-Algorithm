def apply_permutation(block, permutation):
    permuted_block = [block[permutation[i]] for i in range(len(permutation))]
    return permuted_block

def feistel_encrypt(block, permutation, subkey1, subkey2):
    # Étape 2 : Appliquer la permutation π
    permuted_block = apply_permutation(block, permutation)

    # Étape 3 : Diviser le bloc en deux blocs de 4 bits
    G0 = permuted_block[:4]
    D0 = permuted_block[4:]

    # Étape 4 : Premier Round
    P = [2, 0, 1, 3]
    D1 = [G0[P[i]] ^ subkey1[i] for i in range(4)]
    G1 = [D0[i] ^ (G0[i] | subkey1[i]) for i in range(4)]

    # Étape 5 : Deuxième Round
    D2 = [G1[P[i]] ^ subkey2[i] for i in range(4)]
    G2 = [D1[i] ^ (G1[i] | subkey2[i]) for i in range(4)]

    # Étape 6 : Concaténer G2 et D2
    C = G2 + D2

    # Étape 7 : Appliquer l'inverse de la permutation π^(-1)
    inverse_permutation = [permutation.index(i) for i in range(len(permutation))]
    encrypted_block = apply_permutation(C, inverse_permutation)

    # Étape 8 : Retourner le texte chiffré
    return encrypted_block

# Exemple d'utilisation
block = [1, 0, 1, 0, 0, 1, 1, 0]  # Bloc de départ de longueur 8 bits
permutation = [4, 6, 0, 2, 7, 3, 1, 5]  # Permutation personnalisée
subkey1 = [1, 0, 1, 1]  # Sous-clé 1 de longueur 4 bits
subkey2 = [0, 1, 1, 0]  # Sous-clé 2 de longueur 4 bits

encrypted_block = feistel_encrypt(block, permutation, subkey1, subkey2)
print("Texte chiffré:", encrypted_block)