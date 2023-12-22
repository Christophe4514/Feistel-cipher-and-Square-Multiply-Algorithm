def apply_permutation(key, permutation):
    permuted_key = [key[permutation[i]] for i in range(len(permutation))]
    return permuted_key

def generate_feistel_subkeys(key, permutation, left_shift_order, right_shift_order):
    # Étape 2 : Appliquer la permutation donnée
    permuted_key = apply_permutation(key, permutation)

    # Étape 3 : Diviser la clé en deux blocs de 4 bits
    k1 = permuted_key[:4]
    k2 = permuted_key[4:]

    # Étape 4 : Calculer k1 et k2
    k1_xor_k2 = [k1[i] ^ k2[i] for i in range(4)]
    k1_and_k2 = [k1[i] & k2[i] for i in range(4)]

    # Étape 5 : Appliquer les décalages
    k1_shifted = k1_xor_k2[left_shift_order:] + k1_xor_k2[:left_shift_order]
    k2_shifted = k1_and_k2[-right_shift_order:] + k1_and_k2[:-right_shift_order]

    # Étape 6 : Retourner les sous-clés générées
    return k1_shifted, k2_shifted

# Exemple d'utilisation
key = [1, 0, 1, 0, 0, 1, 1, 0]  # Clé de départ de longueur 8
permutation = [6, 5, 2, 7, 4, 1, 3, 0]  # Permutation personnalisée
left_shift_order = 2  # Ordre de décalage à gauche
right_shift_order = 1  # Ordre de décalage à droite

subkey1, subkey2 = generate_feistel_subkeys(key, permutation, left_shift_order, right_shift_order)
print("Sous-clé 1:", subkey1)
print("Sous-clé 2:", subkey2)

"""
    Dans cet exemple, l'utilisateur peut définir la permutation personnalisée en modifiant la liste permutation, l'ordre de décalage à gauche en modifiant left_shift_order et l'ordre de décalage à droite en modifiant right_shift_order. Les autres parties de l'algorithme restent les mêmes que dans l'implémentation précédente.

Notez que les valeurs des ordres de décalage doivent être des entiers positifs, et si nécessaire, vous pouvez ajouter des validations supplémentaires pour les entrées de l'utilisateur afin de garantir que les valeurs sont correctes.
    """