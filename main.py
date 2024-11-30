from Fract import Fraction

def main():
    print("=== Demonstration of the Fraction class ===")
    try:
        # Création de fractions
        print("\n--- Creation of fractions ---")
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = Fraction(2, 3)
        f4 = Fraction(-5, -10)  # Devrait être réduit à 1/2
        print(f"Fraction 1: {f1}")  # 1/2
        print(f"Fraction 2: {f2}")  # 3/4
        print(f"Fraction 3: {f3}")  # 2/3
        print(f"Fraction 4 (reduced): {f4}")  # 1/2

        # Opérations mathématiques
        print("\n--- Mathematical operations ---")
        print(f"Addition: {f1} + {f2} = {f1 + f2}")  # 5/4
        print(f"Subtraction: {f1} - {f2} = {f1 - f2}")  # -1/4
        print(f"Multiplication: {f1} * {f3} = {f1 * f3}")  # 1/3
        print(f"Division: {f2} / {f3} = {f2 / f3}")  # 9/8

        # Comparaisons
        print("\n--- Comparisons ---")
        print(f"{f1} < {f2} = {f1 < f2}")  # True
        print(f"{f2} > {f3} = {f2 > f3}")  # True
        print(f"{f4} == {f1} = {f4 == f1}")  # True

        # Propriétés de fractions
        print("\n--- Fraction properties ---")
        print(f"{f1} is zero: {f1.is_zero()}")  # False
        print(f"{f4} is proper: {f4.is_proper()}")  # True
        print(f"{f3} is an integer: {f3.is_integer()}")  # False
        print(f"{f4} is a unit fraction: {f4.is_unit()}")  # True
        print(f"{f1} is adjacent to {f2}: {f1.is_adjacent_to(f2)}")  # False

        # Représentation sous forme de nombre mixte
        print("\n--- Mixed number representation ---")
        f5 = Fraction(7, 4)
        print(f"{f5} as mixed number: {f5.as_mixed_number()}")  # 1 3/4

        # Gestion des erreurs
        print("\n--- Handling errors ---")
        try:
            Fraction(1, 0)  # Devrait lever une ValueError
        except ValueError as e:
            print(f"Error creating fraction: {e}")

        try:
            f1 / Fraction(0, 1)  # Division par zéro
        except ZeroDivisionError as e:
            print(f"Error during division: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
