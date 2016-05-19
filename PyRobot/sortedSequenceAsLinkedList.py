#!/usr/bin/python2.4
#

"""
Provides the SortedSequenceAsLinkedList class.
"""


from sortedSequence import SortedSequence
from orderedSequenceAsLinkedList import OrderedSequenceAsLinkedList


class SortedSequenceAsLinkedList(OrderedSequenceAsLinkedList, SortedSequence):
    """
    A sorted sequence implemented using a linked list.
    """

    def __init__(self):
        """
        (SortedSequenceAsLinkedList) -> None
        Constructs a sorted list.
        """
        super(SortedSequenceAsLinkedList, self).__init__()
        #self.__list = OrderedSequenceAsLinkedList()

    def insert(self, obj):
        """
        (SortedSequenceAsLinkedList, Object) -> None
        Inserts the given object into this sorted list.
        """
        #self.__list.insert(obj)
        #self.__list.count +=1
        super(SortedSequenceAsLinkedList, self).insert(obj)


    def findElement(self, obj):
        """
        (SortedSequenceAsLinkedList, Object) -> LinkedList.Element
        Finds the list element that contains an object
        that equals the given object.
        """
        #self.__contains__(obj)
        if obj in self:
            return obj
        else:
            return None
        #super(SortedSequenceAsLinkedList, self).find(obj)

    class Cursor(OrderedSequenceAsLinkedList.Cursor):
        """
        A cursor that refers to an object in a sorted list.
        """
        __slots__ = ['__element']
        def __init__(self, seq, element):
            """
            (SortedSequenceAsLinkedList.Cursor, SortedSequenceAsLinkedList,
                LinkedList.Element) -> None
            Constructs a cursor that refers to the object
            in the given element of the given list.
            """
            super(SortedSequenceAsLinkedList.Cursor, self).__init__(seq, element)

        def insertAfter(self, obj):
            """
            (SortedSequenceAsLinkedList.Cursor, Object) -> None
            Not allowed in sorted lists.
            """
            raise TypeError

        def insertBefore(self, obj):
            """
            (SortedSequenceAsLinkedList.Cursor, Object) -> None
            Not allowed in sorted lists.
            """
            raise TypeError

    def findPosition(self, obj):
        """
        (SortedSequenceAsLinkedList, Object) -> SortedSequenceAsLinkedList.Cursor
        Finds the position of an object in this sorted list
        that equals the given object and returns a cursor
        that refers to that object.
        """
        return super(SortedSequenceAsLinkedList, self).findPosition(obj)
        
        """
        ptr = self._OrderedSequenceAsLinkedList__list.head
        while ptr is not None:
            if ptr.data is obj:
                return self.Cursor(self,ptr)
            ptr = ptr.next
        return self.Cursor(None,None)
        """
    def withdraw(self, obj):
        """
        (SortedSequenceAsArray, Object) -> None
        Withdraws the given object from this sorted sequence.
        """
        super(SortedSequenceAsLinkedList, self).withdraw(obj)

    
    @staticmethod
    def main():
        "SortedSequenceAsLinkedList test program."
        print SortedSequenceAsLinkedList.main.__doc__
        slist = SortedSequenceAsLinkedList()
        SortedSequence.test(slist)
        return 0

if __name__ == "__main__":
    SortedSequenceAsLinkedList.main()
