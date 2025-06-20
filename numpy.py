import numpy as np
# Δημιουργία πίνακα 10x10 με τυχαίους πραγματικούς αριθμούς (float) από 0 έως 100
array_float = np.random.uniform(0, 100, (10, 10))
# Μετατροπή του πίνακα σε ακέραιους (int)
array_int = array_float.astype(int)

mean = np.mean(array_int) # μέσος όρος
median = np.median(array_int) # διάμεσος
std_dev = np.std(array_int) # τυπική απόκλιση

# Εκτυπώσεις
print("Πίνακας Πραγματικών:\n", array_float)
print("\nΠίνακας Ακεραίων:\n", array_int)
print(f"\nΜέσος Όρος: {mean}")
print(f"\nΔιάμεσος: {median}")
print(f"\nΤυπική Απόκλιση: {std_dev}")
#-------------------------------------------------------------------------------------------------------------

def multiply_lists(A, B):
    # Έλεγχος αν οι πίνακες μπορούν να πολλαπλασιαστούν
    if len(A[0]) != len(B):
        print("Διαστάσεις δεν ταιριάζουν.")
        return None

    # Δημιουργία κενού πίνακα για το αποτέλεσμα
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Πολλαπλασιασμός πινάκων
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


#-------------------------------------------------------------------------------------------------------------


# Δημιουργία πίνακα 100 στοιχείων από κανονική κατανομή με μέσο όρο 0 και τυπική απόκλιση 1
normal_array = np.random.normal(loc=0.0, scale=1.0, size=100)

print("Πίνακας από κανονική κατανομή:")
print(normal_array)
#-------------------------------------------------------------------------------------------------------------


# Δημιουργία πίνακα 5x5 με τυχαίους ακέραιους από 0 έως 99
array = np.random.randint(0, 100, (5, 5))

print("Αρχικός πίνακας:")
print(array)

# Εφαρμογή μάσκας για τα άρτια στοιχεία 
even_mask = (array % 2 == 0)

# Εφαρμογή μάσκας
even_only = np.where(even_mask, array, 0)

print("\nΠίνακας με μόνο τα άρτια στοιχεία:")
print(even_only)

#-------------------------------------------------------------------------------------------------------------



def main():
    # Ορισμός των πινάκων
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])

    B = np.array([[7, 8],
                  [9, 10],
                  [11, 12]])

    try:
        result = np.dot(A, B)
        print("Αποτέλεσμα πολλαπλασιασμού:\n", result)
    except ValueError:
     print("Σφάλμα: Δεν ταιριάζουν οι διαστάσεις των πινάκων.")

if __name__ == "__main__":
    main()

