class vector:
    def __init__(self,dimension) :
        self.vec = []
        for i in range(dimension) :
            self.vec.append(0)
    def str(self) :
        output = ""
        for i in range(len(self.vec)) :
            output += str(self.vec[i]) + " "
        return output
    def length(self) :
        return len(self.vec)
    def set(self,pos,val) :
        assert( pos < self.length() )
        assert( 0 <= pos )
        try:
            int(val)
        except ValueError:
            assert(val==0)    
        self.vec[pos] = val
    def get(self,pos) :
        assert( pos < self.length() )
        assert( 0 <= pos )
        return self.vec[pos]
    def setArray(self,arr) :
        assert(len(arr) == self.length())
        for i in range(self.length()) :
            self.set(i,arr[i])
    def setVector(self,copyVec) :
        assert(copyVec.length() == self.length())
        for i in range(self.length()) :
            cv = copyVec.get(i)
            self.set(i,cv)
    def mulVector(self,mulVec) :
        assert(mulVec.length() == self.length())
        result = vector(self.length())
        for i in range(len(self.vec)) :
            result.set(i,self.get(i)*mulVec.get(i))
        return result
    def mulScalar(self,scalar) :
        result = vector(self.length())
        for i in range(len(self.vec)) :
            result.set(i,self.get(i)*scalar)
        return result
    def addScalar(self,scalar) :
        result = vector(self.length())
        for i in range(len(self.vec)) :
            result.set(i,self.get(i)+scalar)
        return result
    def subVector(self,subVec) :
        assert(subVec.length() == self.length())
        result = vector(self.length())
        for i in range(len(self.vec)) :
            result.set(i,self.get(i)-subVec.get(i))
        return result
    def subScalar(self,scalar) :
        result = vector(self.length())
        for i in range(len(self.vec)) :
            result.set(i,self.get(i)-scalar)
        return result
    def sumVector(self) :
        sum = 0
        for i in range(self.length()) :
            sum += self.get(i)
        return sum
    def dot(self,dotVec) :
        result = self.mulVector(dotVec)
        return result.sumVector()

class matrix:
    def __init__(self,dimX,dimY) :
        self.mat = []
        self.dimX = dimX
        self.dimY = dimY
        for i in range(dimX*dimY) :
            self.mat.append(0)
    def lengthX(self) :
        return self.dimX
    def lengthY(self) :
        return self.dimY
    def get(self,dX,dY) :
        assert( 0 <= dX )
        assert( 0 <= dY )
        pos = self.dimX * dY + dX
        assert(pos < self.dimX*self.dimY)
        return self.mat[pos]
    def set(self,dX,dY,val) :
        assert( 0 <= dX )
        assert( 0 <= dY )
        try:
            int(val)
        except ValueError:
            assert(val==0)
        pos = self.dimX * dY + dX
        assert(pos < self.dimX*self.dimY)
        self.mat[pos] = val
    def str(self) :
        output = ""
        for j in range(self.dimY) :
            for i in range(self.dimX) :
                output += str(self.get(i,j)) + " "
            output += "\n"
        return output
    def setArray(self,arr) :
        assert(len(arr) == self.dimX*self.dimY)
        for j in range(self.dimY) :
            for i in range(self.dimX) :
                pos = self.dimX * j + i
                self.set(i,j,arr[pos])            
    def setVectorX(self,dX,vec) :
        assert( dX < self.dimX )
        assert( vec.length() == self.lengthY() )
        for i in range(self.dimY) :
            v = vec.get(i)
            self.set(dX,i,v)
    def setVectorY(self,dY,vec) :
        assert( dY < self.dimY )
        assert( vec.length() == self.lengthX() )
        for i in range(self.dimX) :
            v = vec.get(i)
            self.set(i,dY,v)
    def getVectorX(self,dX) :
        assert( dX < self.dimX )
        vec = vector(self.dimY)
        for i in range(self.dimY) :
            a = self.get(dX,i)
            vec.set(i,a)
        return vec
    def getVectorY(self,dY) :
        assert( dY < self.dimY )
        vec = vector(self.dimX)
        for i in range(self.dimX) :
            a = self.get(i,dY)
            vec.set(i,a)
        return vec
    def mulVec(self,vec) :
        assert( vec.length() == self.dimX )
        result = vector(self.dimY)
        for j in range(self.dimY) :
            sumRes = 0
            for i in range(self.dimX) :
                sumRes += self.get(i,j) * vec.get(i)
            result.set(j,sumRes)
        return result
        
def test() :
    a = vector(3)
    a.setArray([1,2,3])
    b = vector(3)
    b.setArray([3,4,5])
    c = a.mulVector(b)
    print(c.str())
    print(c.sumVector())
    print(a.dot(b))

    m = matrix(2,3)
    m.setVectorX(0,a)
    m.setVectorX(1,a)
    print(m.str())
    z = m.getVectorX(1)
    print(z.str())

    v = vector(2)
    v.setArray([5,6])
    print(v.str())
    print(m.str())
    m.setVectorY(2,v)
    y = m.getVectorY(2)
    print(y.str())
    print(m.str())

    m2 = matrix(3,2)
    m2.setArray([1,-1,2,
                0,-3,1])

    v2 = vector(3)
    v2.setArray([2,1,0])

    print(m2.str())
    print(v2.str())

    v3 = m2.mulVec(v2)

    print(v3.str())

