"""
UPDATE ME
//double **mread(FILE *fp, int *r, int *c)
//reads a matrix (in row-major order) from an open file
//ARGS:
//FILE *fp: pointer to a file containing an RxC Matrix
//int *r: pointer to int representing how many rows are in the matrix
//int *c: pointer to int representing how many columns are in the matrix 
/////////////////////////////////////////////////////////////////////////////////
"""
def mread(filename):
    matfile = open(filename, "r+")
    dimline = matfile.readline()
    dims = dimline.split(" ")
    rows = int(dims[0])
    cols = int(dims[1])
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    buffer = ""
    toke = ""

    for i in range(1, rows+1):
        buffer = matfile.readline()
        bufflist = buffer.split(" ")
        for j in range(1, cols+1):
            val = bufflist[j-1]
            doubleval = float(val)
            matrix[i-1][j-1] = doubleval
    matfile.close()
    return matrix


"""
UPDATE ME
//void mwrite(FILE *fp, int rA, int cA, double **A)
//writes the rAxcA matrix A to already open file
//ARGS:
//filename: pointer to a file to write a matrix to 
//rows: the number of rows to write
//cols: the number of comlumns to write 
//matrix: double array representing the matrix to be written 
/////////////////////////////////////////////////////////////////////
"""
def mwrite(filename, rows, cols, matrix):
    matfile = open(filename, "w")
    matfile.write(str(rows))
    matfile.write(" ")
    matfile.write(str(cols))
    for i in range(1, rows+1):
        matfile.write('\n')
        for j in range(1, cols+1):
            matfile.write(str(matrix[i-1][j-1]))
            matfile.write(" ")
    return

"""
UPDATE ME
//double **mmult(int rA, int cA, double **A, int rB, int cB, double **B)
//Return the product A*B as a new, dynamically allocated rA x cB matrix.
//ARGS:
//int rA, cA, rB, cB: the number of rows/columns in A and B
//double **A, B: double arrays representing the two matrices to be multiplied together
////////////////////////////////////////////////////////////////////////////////////////
"""
def mmult(rA, cA, matA, rB, cB, matB):
    matC = [[0 for x in range(cB)] for y in range(rA)]
    
    for i in range(1, rA+1):
        for j in range(1, cB+1):
            sum = 0
            for k in range(1, rB+1):
                sum = sum + matA[i-1][k-1] * matB[k-1][j-1]
            matC[i-1][j-1] = sum
    return matC


def main():
    matA = mread("newinput.txt")
    matB = mread("newinput.txt")
    matC = mmult(2, 2, matA, 2, 4, matB)
    mwrite("new.txt", 2, 4, matC)

main()