class MatrixImpN(object):
    """Creates a matrix ([[1,0],[0,1]])"""
    #####################
    # ###Magic Methods####
    #####################

    def __init__(self, matrix):
        self.width, self.height, self.matrix = self.checkMatrix(matrix)

    def __add__(self, other):
        self.checkBeforeAdding(other)
        old_matrices = zip(self.matrix, other.matrix)
        new_matrix = []
        for self_line, other_line in old_matrices:
            old_lines = zip(self_line, other_line)
            new_line = []
            for self_num, old_num in old_lines:
                new_line.append(self_num+old_num)
            new_matrix.append(new_line)
        com_matrix = MatrixImpN(new_matrix)
        return com_matrix

    def __mul__(self, other):
        self.checkBeforeMultiplying(other)
        new_matrix = []
        for self_line in self.matrix:
            new_line = []
            for idx in range(0, len(other.matrix[0])):
                other_line = [item[idx] for item in other.matrix]
                old_lines = zip(self_line, other_line)
                new_num = sum([self_num * other_num for self_num, other_num in old_lines])
                new_line.append(new_num)
            new_matrix.append(new_line)
        com_matrix = MatrixImpN(new_matrix)
        return com_matrix

    def __repr__(self):
        string = ""
        for row in self.matrix:
            string +=  "{}\n".format(row)
        return string

    #######################
    # ###custom commands####
    #######################
    @staticmethod
    def checkMatrix(matrix):
        checked = [[float(elem) for elem in row] for row in matrix]

        widths = [len(row) for row in matrix]
        width = widths[0]
        if all([width==w for w in widths]):
            return width,len(matrix),matrix
        else:
            raise Exception("Matrix not rectangle/square.")

    def checkBeforeAdding(self,other):
        if (self.height == other.height) and (self.width == other.width):
            pass
        else:
            raise Exception("Matrices not compatible for addition.")

    def checkBeforeMultiplying(self, other):
        if self.width == other.height:
            pass
        else:
            raise Exception("Matrices not compatible for multiplication.")

    @classmethod
    def identityMatrix(cls, length):
        """Creates a identity matrix (length)"""
        row = cls([[1]*length])
        return row.diagonal()

    def vector(self):
        """Makes a row vector out of column or row vector"""
        if self.height == 1:
            return self.matrix[0]
        elif self.width == 1:
            row = []
            for i in range(self.height):
                row.append(self.matrix[i][0])
            return row
        else:
            raise Exception("Matrix not vector")

    def diagonal(self):
        """Makes diagonal matrix out of a vector matrix [[1,2,3]] --> [[1,0,0],[0,2,0],[0,0,3]]"""
        a = self.vector()
        length = len(a)
        matrix = []
        for i in range(length):
            row = [0]*length
            row[i] = a[i]
            matrix.append(row)
        return self.__class__(matrix)


a = MatrixImpN.identityMatrix(3)
b = MatrixImpN([[1], [2], [3]])
b = b.diagonal()
print b
print a
