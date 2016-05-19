#!/usr/bin/python2.4
#

"""
Provides the OrderedSequenceAsArray class.
"""

from orderedSequence import OrderedSequence
from container import Container
from searchableContainer import SearchableContainer
from Array import Array
from cursor import Cursor
from iterator import Iterator
from visitor import Visitor

class OrderedSequenceAsArray(OrderedSequence):
    """
    Ordered list implemented using an array.
    """
    __slots__ = ['__array']
    def __init__(self, size = 0):
        """
        (OrderedSequenceAsArray [, int]) -> None
        Constructs an ordered sequence of the given size.
        """
        super(OrderedSequenceAsArray, self).__init__()
        self.__array = Array(size)
        
    def insert(self, obj):
        """
        (OrderedSequenceAsArray, Object) -> None
        Inserts the given object at the end of this sequence.
        """
        if self.count == len(self.__array):
            raise IndexError, "Container Full"
        self.__array[self.count]=obj
        self.count += 1
        
    def purge(self):
        """
        (OrderedSequenceAsArray) -> None
        Purges this ordered sequence.
        """
        for i in range(self.count):
            self.__array[i] = None
        self.count = 0
        
        
    def getIsFull(self):
        """
        (OrderedSequenceAsArray) -> bool
        Returns true if this ordered sequence is full.
        """
        if len(self.__array) == 0:
            return True
        for i in range(len(self.__array)):
            if self.__array[i] is None:
                return False
        return True

    def getIsEmpty(self):
        if len(self.__array) == 0:
            return False
        for i in range(len(self.__array)):
            if self.__array[i] is not None:
                return False
        return True
    
    def accept(self, visitor):
        """
        (OrderedSequenceAsArray, Visitor) -> bool
        Makes the given visitor visit the objects in this ordered sequence.
        """
        assert isinstance(visitor, Visitor)
        for i in range(self.count):
            visitor.visit(self.__array[i])
            if visitor.isDone:
                return
        
    def __contains__(self, obj):
        """
        (OrderedSequenceAsArray, Object) -> bool
        Returns true if the given object instance is in this ordered sequence.
        """
        for i in range(self.count):
            if self.__array[i] == obj:
                return True
        return False
        
    def find(self, obj):
        """
        (OrderedSequenceAsArray, Object) -> Object
        Finds an object in this ordered sequence that equals the given object.
        """
        for i in range(self.count):
            if self.__array[i] is obj:
                return self.__array[i]
        return None

    def withdraw(self, obj):
        """
        (OrderedSequenceAsArray, Object) -> None
        Withdraws the given object instance from this ordered sequence.
        """
        found = False
        if self.count == 0:
            raise IndexError,'Container Empty'
        for i in range(self.count):
            if self.__array[i] == obj:
                self.__array[i] = self.__array[i+1]
                found = True
            elif found == True: #una vez encontrado el item se desplazan todos los siguientes una posicion
                self.__array[i] = self.__array[i+1]
        if found is False:
            raise KeyError()
        self.count -= 1

    def findPosition(self, obj):
        """
        (OrderedSequenceAsArray, Object) -> OrderedSequenceAsArray.Cursor
        Finds the position of an object in this sequence
        that equals the given object and returns a cursor
        that refers to that object.
        """

        i = 0
        while (i<self.count and self.__array[i] is not obj):
            i+=1
        #if i == self.count:
         #   raise KeyError
        return self.Cursor(self,i)
        

    def __getitem__(self, offset):
        """
        (OrderedSequenceAsArray, int) -> Object
        Returns the object in this sequence at the given._offset.
        """
        if offset < 0 or offset >= self.count:
            raise IndexError
        else:
            return self.__array[offset]
        

    class Cursor(Cursor):
        """
        A cursor that refers to an object in an ordered sequence.
        """
        __slots__ = ['__offset']
        def __init__(self, seq, offset):
            """
            (OrderedSequenceAsArray.Cursor, OrderedSequenceAsArray, int) -> None
            Constructs a cursor that refers to the object
            at the given.__offset of the given sequence.
            """
            super(OrderedSequenceAsArray.Cursor, self).__init__(seq)
            self.__offset = offset
            
        def getData(self):
            """
            (OrderedSequenceAsArray.Cursor) -> Object
            Returns the object to which this cursor refers.
            """
            if self.__offset > 0 and self.__offset <= self._Cursor__sequence.count:
                return self._Cursor__sequence._OrderedSequenceAsArray__array[self.__offset]
            else:
                raise IndexError()
            
        def insertAfter(self, obj):
            """
            (OrderedSequenceAsArray.Cursor, Object) -> None
            Inserts the given object into the sequence
            after the object to which this cursor refers.
            """
            if self.__offset < 0 or self.__offset >= self._Cursor__sequence.count:
                raise IndexError
            if self._Cursor__sequence.count == len(self._Cursor__sequence._OrderedSequenceAsArray__array):
                raise IndexError, "Container Full"
            insertPosition = self.__offset + 1
            i = self._Cursor__sequence.count
            while i > insertPosition:
                self._Cursor__sequence._OrderedSequenceAsArray__array[i] = self._Cursor__sequence._OrderedSequenceAsArray__array[i - 1]
                i -= 1
            self._Cursor__sequence._OrderedSequenceAsArray__array[insertPosition] = obj
            self._Cursor__sequence.count += 1

        def insertBefore(self, obj):
            """
            (OrderedSequenceAsArray.Cursor, Object) -> None
            Inserts the given object into the sequence
            before the object to which this cursor refers.
            """
            if self.__offset < 0 or self.__offset >= self._Cursor__sequence.count:
                raise IndexError
            if self._Cursor__sequence.count == len(self._Cursor__sequence._OrderedSequenceAsArray__array):
                raise IndexError, "Container Full"
            insertPosition = self.__offset
            i = self._Cursor__sequence.count
            while i > insertPosition:
                self._Cursor__sequence._OrderedSequenceAsArray__array[i] = self._Cursor__sequence._OrderedSequenceAsArray__array[i - 1]
                i -= 1
            self._Cursor__sequence._OrderedSequenceAsArray__array[insertPosition] = obj
            self._Cursor__sequence.count += 1
            self.__offset += 1

        def withdraw(self):
            """
            (OrderedSequenceAsArray.Cursor) -> None
            Withdraws from the sequence the object to which this cursor refers.
            """
            if self.__offset < 0 or self.__offset >= self._Cursor__sequence.count:
                raise IndexError
            found = False
            for i in range(self._Cursor__sequence.count):
                if self._Cursor__sequence._OrderedSequenceAsArray__array[i] == self._Cursor__sequence._OrderedSequenceAsArray__array[self.__offset]:
                    self._Cursor__sequence._OrderedSequenceAsArray__array[i] = self._Cursor__sequence._OrderedSequenceAsArray__array[i+1]
                    found = True
                elif found == True:
                    self._Cursor__sequence._OrderedSequenceAsArray__array[i] = self._Cursor__sequence._OrderedSequenceAsArray__array[i+1]
            if found is False:
                raise KeyError()

    class Iterator(Iterator):
        """
        Enumerates the items in an ordered sequence.
        """
        __slots__ = ['__position']
        def __init__(self, seq):
            """
            (OrderedSequenceAsArray.Iterator, OrderedSequenceAsArray) -> None
            Constructs an iterator for the given ordered sequence.
            """
            super(OrderedSequenceAsArray.Iterator, self).__init__(seq)
            self.__position = -1
            
        def next(self):
            """
            (OrderedSequenceAsArray.Iterator) -> Object
            Returns the next element.
            """
            self.__position += 1
            if self.__position == self.container.count:
                self.__position -= 1
                raise StopIteration()
            else:
                return self.container._OrderedSequenceAsArray__array[self.__position]

    def __iter__(self):
        """
        (OrderedSequenceAsArray) -> OrderedSequenceAsArray.Iterator
        Returns an iterator for this ordered sequence.
        """
        return self.Iterator(self)
        

    def _compareTo(self, obj):
        """
        (OrderedSequenceAsArray, OrderedSequenceAsArray) -> int

        Compares this ordered list with the given ordered list.
        """
        assert isinstance(self, obj.__class__)
        raise TypeError, 'Not Implemented'

    @staticmethod
    def main(*argv):
        "OrderedSequenceAsArray test program."
        print OrderedSequenceAsArray.main.__doc__
        oSeq = OrderedSequenceAsArray(10)
        OrderedSequence.test(oSeq)
        return 0

if __name__ == "__main__":
    OrderedSequenceAsArray.main(*sys.argv)

