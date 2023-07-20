
import random

# Generating and printing a matrix size nlenght
def gen_matrix(nlength):

    matrix = []
    for n in range(nlength):
        row = [random.randint(0, 9) for n in range(nlength)]
        matrix.append(row)
    print(f'\n--- Generated a {nlength}x{nlength} matrix ---')
    for row in matrix:
        print(row)
    return matrix


# Adding rows and columns from the previous matrix and printing the totals by column and row.
def add_row_column(matrix):

    add_rows = [sum(row) for row in matrix]
    add_columns = [sum(column) for column in zip(*matrix)]

    print('\n--- 👇 Addition by row ---:')
    for item, added in enumerate(add_rows):
        print(f"- Total Row N.{item+1}: = {added}")

    print('\n--- 👇 Addition by Column ---:')
    for item, added in enumerate(add_columns):
        print(f"- Total Column N.{item+1}: = {added}")
    print('\n')

    return add_rows, add_columns


# Running the functions
def main():

    while True:
        # Exception handling
        try:
            # Asking a value
            nlength = int(input("\n--- Enter the desired size for the squared matrix : "))
            
            # handling invalid inputs
            if nlength <= 0 or type(nlength) not in [int] or nlength == '' or nlength == ' ' or nlength is None:
                raise ValueError("Number must be an integer greater than 0. Please, Try again.")
            break
        
        except (ValueError, TypeError) as e:
            print(f"\n⚠️  An error/exception occurred: {e}\n")
            return

    matrix = gen_matrix(nlength)
    add_row_column(matrix)

if __name__ == "__main__":
    
    main()




