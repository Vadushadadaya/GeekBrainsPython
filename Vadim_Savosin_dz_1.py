class Matrix:
    def __init__(self, matrix):
        self.matrix=matrix
    
    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])
    
    def __add__(self, other):
        numbers = []
        result = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                summ = self.matrix[i][j]+other.matrix[i][j]
                numbers.append(summ)
            result.append(numbers)
            numbers = []
        return Matrix(result)


m1 = Matrix([[1,2,3],[1,2,3],[1,2,3]])
m2 = Matrix([[3,2,1],[3,2,1],[3,2,1]])
summ = m1 + m2
print(summ)
print(m1)