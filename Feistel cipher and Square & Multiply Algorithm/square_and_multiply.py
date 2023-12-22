def square_and_multiply(x, b, n):
    # Conversion de l'exposant b en une représentation binaire
    binary_exponent = bin(b)[2:]

    # Initialisation du résultat à 1
    result = 1

    # Parcours de la représentation binaire de droite à gauche
    for bit in binary_exponent[::-1]:
        # Étape du carré
        result = (result * result) % n

        # Si le bit est égal à 1, effectuer une multiplication supplémentaire
        if bit == '1':
            result = (result * x) % n

    return result

# Demande à l'utilisateur d'entrer les valeurs de x, b et n
x = int(input("Entrez la valeur de x : "))
b = int(input("Entrez la valeur de b : "))
n = int(input("Entrez la valeur de n : "))

# Appel de l'algorithme des carrés et des multiplications
result = square_and_multiply(x, b, n)

# Affichage du résultat
print("Résultat :", result)


"""
    Dans cet exemple, l'algorithme demande à l'utilisateur d'entrer les valeurs de x, b et n. Ensuite, il applique l'algorithme des carrés et des multiplications pour calculer x^b (mod n). Le résultat est affiché à la fin.

L'algorithme des carrés et des multiplications est une méthode efficace pour calculer une exponentiation modulaire. Il repose sur le fait que toute représentation binaire de l'exposant peut être exprimée comme une combinaison de puissances de 2. L'algorithme effectue des carrés successifs et des multiplications supplémentaires en fonction des bits de l'exposant pour obtenir le résultat final. Cela réduit le nombre total de multiplications requises par rapport à une méthode naïve de multiplication répétée.
    """