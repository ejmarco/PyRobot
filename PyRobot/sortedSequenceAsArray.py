#!/usr/bin/python2.4
#

"""
Provides the SortedSequenceAsArray class.
"""


from sortedSequence import SortedSequence
from orderedSequenceAsArray import OrderedSequenceAsArray



class SortedSequenceAsArray(OrderedSequenceAsArray, SortedSequence):
    """
    A sorted sequence implemented using an array.
    """

    def __init__(self, size = 0):
        """
        (SortedSequenceAsArray [, int]) -> None
        Constructs a sorted sequence of the given size.
        """
        super(SortedSequenceAsArray, self).__init__(size)
        #self.__array = OrderedSequenceAsArray(size)

    def insert(self, obj):
        """
        (SortedSequenceAsArray, Object) -> None
        Inserts the given object into this sorted sequence.
        """
        if self.getIsFull():
            raise IndexError
        #contar la posicion en la que se insertara el objeto
        index = 0
        while obj < self._OrderedSequenceAsArray__array[index]:
            index += 1
        #reordenar el array para dejar un espacio libre e insertar el objeto
        aux = self.count
        while index<aux:
            self._OrderedSequenceAsArray__array[aux] = self._OrderedSequenceAsArray__array[aux-1]
            aux -= 1
        self._OrderedSequenceAsArray__array[index] = obj
        self.count+=1

        #el siguiente codigo pasa el joc pero no el auto-test de la clase
        #pos = self._OrderedSequenceAsArray__array[i-1]
        #cu = super(SortedSequenceAsArray, self).findPosition(pos)
        #super(SortedSequenceAsArray, self).Cursor.insertAfter(cu, obj)
        
    def findOffset(self, obj):
        """
        (SortedSequenceAsArray, Object) -> int
        Finds the offset in this sequence
        of the object that equals the given object.
        """
        """
        if super(SortedSequenceAsArray, self).__contains__(obj):
        #if self.__array.__contains__(obj):
            return super(SortedSequenceAsArray, self).findPosition(obj)
            #return self.__array.findPosition(obj)
        return -1"""
        #self.__contains__(obj)
        
        if obj in self:
            return super(SortedSequenceAsArray, self).findPosition(obj)
        return -1
    
    def findElement(self, obj):
        """
        (SortedSequenceAsArray, Object) -> Object
        Finds the object in this sequence that equals the given object.
        """
        #if super(SortedSequenceAsArray, self).__contains__(obj):
        #self.__contains__(obj)
        
        if obj in self:
            return obj
        else:
            return None
    
    class Cursor(OrderedSequenceAsArray.Cursor):
        """
        A cursor that refers to an object in a sorted sequence.
        """

        def __init__(self, seq, offset):
            """
            (SortedSequenceAsArray.Cursor, SortedSequenceAsArray, int) -> Object
            Constructs a cursor that refers to the object
            at the given offset in the given sequence.
            """
            super(SortedSequenceAsArray.Cursor, self).__init__(seq, offset)

        def insertAfter(self, obj):
            """
            (SortedSequenceAsArray.Cursor, Object) -> None
            Not allowed in sorted sequences.
            """
            raise TypeError

        def insertBefore(self, obj):
            """
            (SortedSequenceAsArray.Cursor, Object) -> None
            Not allowed in sorted sequences.
            """
            raise TypeError

    def findPosition(self, obj):
        """
        (SortedSequenceAsArray, Object) -> SortedSequenceAsArray.Cursor
        Finds the position of an object in this sorted sequence
        that equals the given object and returns a cursor
        that refers to that object.
        """
        return self.Cursor(self, self.findOffset(obj))

    def withdraw(self, obj):
        """
        (SortedSequenceAsArray, Object) -> None
        Withdraws the given object from this sorted sequence.
        """
        super(SortedSequenceAsArray, self).withdraw(obj)
        #self.__array.withdraw(obj)

    @staticmethod
    def main():
        "SortedSequenceAsArray test program."
        print SortedSequenceAsArray.main.__doc__
        slist = SortedSequenceAsArray(10)
        SortedSequence.test(slist)
        return 0

if __name__ == "__main__":
    SortedSequenceAsArray.main()
