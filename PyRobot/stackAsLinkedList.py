from stack import Stack
from linkedList import LinkedList
from iterator import Iterator
from visitor import Visitor

class StackAsLinkedList(Stack):
        __slots__ = ['__list']
        def __init__(self):
                super(StackAsLinkedList, self).__init__()
                self.__list = LinkedList()
        def purge(self):
                self.__list.purge()
        def getTop(self):
                if self.__list.getIsEmpty():
                        raise IndexError("Empty")
                else:
                        return self.__list.getHead().getData()
        def push(self, obj):
                self.__list.prepend(obj)
                # el append de linkedlist ya hace las comprobaciones pertinentes
        def pop(self):
                item = self.__list.getFirst()
                self.__list.extract(self.__list.getFirst())
                return item
                # el extract de linkedlist ya hace las comprobaciones de lista vacia
        def accept(self, visitor):
                assert isinstance(visitor, Visitor)
                ptr = self.__list.head
                while ptr is not None:
                        visitor.visit(ptr.data)
                        if visitor.isDone:
                                return
                        ptr = ptr.next
        def getIsEmpty(self):
                return self.__list.getIsEmpty()
        class Iterator(Iterator):
                __slots__ = ['__position']
                def __init__(self, queue):
                        super(StackAsLinkedList.Iterator,self).__init__(stack)
                        self.__position = None
                def next(self):
                        if self.__position is None:
                                self.__position = self.container._StackAsLinkedList__list.head
                        else:
                                self.__position = self.__position.next
                        if self.__position is None:
                                raise StopIteration
                        return self.__position.data
        def __iter__(self):
                return self.Iterator(self)
        def _compareTo(self, obj):
                assert isinstance(self, obj.__class__)
                raise NotImplementedError
