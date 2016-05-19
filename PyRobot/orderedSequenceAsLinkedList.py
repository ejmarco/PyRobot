#!/usr/bin/python2.4
#

"""
Provides the OrderedSequenceAsLinkedList class.
"""


from orderedSequence import OrderedSequence
from linkedList import LinkedList
from cursor import Cursor
from iterator import Iterator
from visitor import Visitor

class OrderedSequenceAsLinkedList(OrderedSequence):
    """  Ordered sequence implemented using a linked list.
    """
    __slots__ = ['__list']
    def __init__(self):
        """ (OrderedSequenceAsLinkedList) -> None
             Constructs an ordered sequence.
        """
        super(OrderedSequenceAsLinkedList, self).__init__()
        self.__list = LinkedList()
        self.count = 0


    def insert(self, obj):
        """ (OrderedSequenceAsLinkedList, Object) -> None
             Inserts the given object at the end of this sequence.
        """
        self.__list.append(obj)
        self.count +=1
    
    def __getitem__(self, offset):
        """ (OrderedSequenceAsLinkedList, int) -> Object
             Returns the object in this sequence at the given offset.
        """
        counter = 0
        if offset < 0:
            raise IndexError()
        else:
            temp = self.__list.head
            while temp is not None:
                if counter is offset:
                    return temp.data
                counter += 1
                temp = temp.next
            if offset > counter:
                raise IndexError()        
    
    def purge(self):
        """ (OrderedSequenceAsLinkedList) -> None
             Purges this ordered sequence.
        """
        self.__list = LinkedList()
        self.count = 0

    def accept(self, visitor):
        """ (OrderedSequenceAsLinkedList, Visitor) -> None
        Makes the given visitor visit all the objects in this ordered sequence.
        """
        assert isinstance(visitor, Visitor)
        ptr = self.__list.head
        while ptr is not None:
            visitor.visit(ptr.data)
            if visitor.isDone:
                return
            ptr = ptr.next

    def __contains__(self, obj):
        """ (OrderedSequenceAsLinkedList, Object) -> bool
             Returns true if the given object instance is in this ordered sequence.
        """
        if self.__list.isEmpty is True:
            return False
        temp = self.__list.head
        while temp is not None:
            if temp.data is obj:
                return True
            temp = temp.next
        return False

    def find(self, arg):
        """ (OrderedSequenceAsLinkedList, Object) -> Object
             Finds an object in this ordered sequence that equals the given object.
        """
        if self.__list.isEmpty:
            return None
        temp = self.__list.head
        while temp is not None:
            if temp.data is arg:
                return temp.data
            temp = temp.next
        return None

    def withdraw(self, obj):
        """ (OrderedSequenceAsLinkedList, Object) -> None
             Withdraws the given object instance from this ordered sequence.
        """
        if self.__list.isEmpty is True:
            raise IndexError()
        else:
            self.__list.extract(obj)
            if self.count > 0:
                self.count -= 1

    def findPosition(self, obj):
        """ (OrderedSequenceAsLinkedList, Object) -> OrderedSequenceAsLinkedList.Cursor
             Finds the position of an object in this sequence that equals the given
             object and returns a cursor that refers to that object.
        """
        ptr = self.__list.head
        while ptr is not None:
            if ptr.data is obj:
                return self.Cursor(self,ptr)
            ptr = ptr.next
        return self.Cursor(None,None)

    class Cursor(Cursor):
        """
        A cursor that refers to an object in an ordered list.
        """
        __slots__ = ['__element']
        def __init__(self, lis, element):
            """ (OrderedSequenceAsLinkedList.Cursor, OrderedSequenceAsLinkedList, 
                LinkedList.Element) -> None
                Constructs a cursor that refers to the object in the given element
                of the given sequence.
           """
            super(OrderedSequenceAsLinkedList.Cursor, self).__init__(lis)
            self.__element = element

        def getData(self):
            """ (OrderedSequenceAsLinkedList.Cursor) -> Object
                 Returns the object to which this cursor refers.
            """
            if self.__element is not None:
                return self.__element.getData()
            else:
                raise IndexError()
        
        def insertAfter(self, obj):
            """ (OrderedSequenceAsLinkedList.Cursor, Object) -> None
                 Inserts the given object into the sequence after the
                 object to which this cursor refers.
            """
            if self.__element is None:
                raise IndexError
            self.__element.insertAfter(obj)
            self.__sequence.count += 1

        def insertBefore(self, obj):
            """ (OrderedSequenceAsLinkedList.Cursor, Object) -> None
                 Inserts the given object into the sequence before the
                 object to which this cursor refers.
            """
            if self.__element is None:
                raise IndexError
            self.__element.insertBefore(obj)
            self.__sequence.count += 1
        
        def withdraw(self):
            """ (OrderedSequenceAsLinkedList.Cursor) -> None
                 Withdraws from the sequence the object to which this cursor refers.
            """
            if self.__element is None:
                raise IndexError()
            self.__sequence._OrderedSequenceAsLinkedList__list.extract(self.__element.data)
            self.__sequence.count -= 1

    class Iterator(Iterator):
        """ Enumerates the items in an ordered sequence.
        """
        __slots__ = ['__element']
        def __init__(self, lis):
            """ (OrderedSequenceAsLinkedList.Iterator, OrderedSequenceAsLinkedList) -> None
                 Constructs an iterator for the given sequence.
            """
            super(OrderedSequenceAsLinkedList.Iterator, self).__init__(lis)
            self.__element = None

        def next(self):
            """ (OrderedSequenceAsLinkedList.Iterator) -> Object
                 Returns the next element.
            """
            if self.container.isEmpty:
                raise StopIteration()
            if self.__element is None:
                self.__element = self.container._OrderedSequenceAsLinkedList__list.head
            elif self.__element.next is None:
                self.__element = None
                raise StopIteration()
            else:
                self.__element = self.__element.next
            return self.__element.data

    def __iter__(self):
        """ (OrderedSequenceAsLinkedList) -> OrderedSequenceAsLinkedList.Iterator
             Returns an iterator for this ordered sequence.
        """
        return self.Iterator(self)

    def _compareTo(self, obj):
        """ (OrderedSequenceAsLinkedList, OrderedSequenceAsLinkedList) -> int
             Compares this ordered list with the given ordered sequence.
        """
        assert isinstance(self, obj.__class__)
        raise TypeError, 'Not Implemented'

    @staticmethod
    def main(*argv):
        "OrderedSequenceAsLinkedList test program."
        print OrderedSequenceAsLinkedList.main.__doc__
        lis = OrderedSequenceAsLinkedList()
        OrderedSequence.test(lis)
        return 0

if __name__ == "__main__":
    OrderedSequenceAsLinkedList.main()
