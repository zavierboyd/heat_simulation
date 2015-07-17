class MatrixImpN(object):

    ##########################
    ####automatic commands####
    ##########################

    def __init__(self,matrix):
        self.width,self.height,self.matrix = self.checkMatrix(matrix)

    def __add__(self,other):
        self.checkBeforeAdding(other)
        oldMatrixs = zip(self.matrix,other.matrix)
        newMatrix = []
        for sline,oline in oldMatrixs:
            oldLines = zip(sline,oline)
            newLine = []
            for snum,onum in oldLines:
                newLine.append(snum+onum)
            newMatrix.append(newLine)
        comMatrix=MatrixImpN(newMatrix)
        return comMatrix

    def __mul__(self,other):
        self.checkBeforeMultiplying(other)
        newMatrix=[]
        for sline in self.matrix:
            newLine=[]
            for idx in range(0,len(other.matrix[0])):
                oline = [item[idx] for item in other.matrix]
                oldLines=zip(sline,oline)
                newNum=sum([snum*onum for snum,onum in oldLines])
                newLine.append(newNum)
            newMatrix.append(newLine)
        comMatrix = MatrixImpN(newMatrix)
        return comMatrix

    def __repr__(self):
        string =""
        for l in self.matrix:
             string=string + "%s\n" %(l)
        return string

    #######################
    ####custom commands####
    #######################
    @staticmethod
    def checkMatrix(matrix):
        checked = [ [ float(elem) for elem in row] for row in matrix]

        widths = [ len(row) for row in matrix ]
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

    def checkBeforeMultiplying(self,other):
        if self.width == other.height:
            pass
        else:
            raise Exception("Matrices not compatible for multiplication.")
