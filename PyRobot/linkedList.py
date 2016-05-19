class LinkedList(object):
    """
    Linked list class.
    """
    __slots__ = ["__head","__tail"]
    class Element(object):
        """ Classe node """
        __slots = ["__data","__next","__list"]
        def __init__(self, lis, data, next):
            self.__list = lis
            self.__data = data
            self.__next = next
        def getData(self):
            return self.__data
        data = property(fget = lambda self: self.getData())
        def getNext(self):
            return self.__next
        next = property(fget = lambda self: self.getNext())
        def insertAfter(self, item): #insertar por la derecha
            self.__next = LinkedList.Element(self.__list, item, self.__next)
            if self.__list._LinkedList__tail is self:
                self.__list._LinkedList__tail = self.__next
        def insertBefore(self, item): #insertar por la izquierda
            element = LinkedList.Element(self.__list, item, self)
            if self is self.__list._LinkedList__head:
                self.__list._LinkedList__head = element
            else:
                temp = self.__list._LinkedList__head #objeto temporal para recorrer la lista
                while self is not temp.__next:
                    temp = temp.__next
                temp.insertAfter(item)                
        def extract(self): #elimina el nodo actual
            temp = None
            if self is self.__list._LinkedList__head:
                self.__list._LinkedList__head = self.__next
            else:
                temp = self.__list._LinkedList__head
                while self is not temp.__next:
                    temp = temp.__next
                temp.__next = self.__next
            if self is self.__list._LinkedList__tail:
                self.__list._LinkedList__tail = temp
    def __init__(self):
        """
        (LinkedList) --> None
        Constructs an empty linked list.
        """
        self.__head = None
        self.__tail = None
    def purge(self):
        self.__head = None
        self.__tail = None
    def getHead(self):  #coger el primer nodo
        return self.__head
    head = property(fget = lambda self: self.getHead())
    def getTail(self): #coger el ultimo nodo
        return self.__tail
    tail  = property(fget = lambda self: self.getTail())
    def getIsEmpty(self): #comprovar si la lista esta vacia
        if (self.__head or self.__tail) is None:
            return True
        else:
            return False
    isEmpty = property(fget = lambda self: self.getIsEmpty())
    def getFirst(self): #coger datos del primer nodo
        if self.getIsEmpty():
            raise IndexError, "Llista buida"
        else:
            return self.head.data
    first  = property(fget = lambda self: self.getFirst())
    def getLast(self): #coger datos del ultimo nodo
        if self.getIsEmpty():
            raise IndexError, "Llista buida"
        else:
            return self.tail.data
    last  = property(fget = lambda self: self.getLast())
    def prepend(self, item): #insertar nodo por el principio de la lista
        newitem = LinkedList.Element(self, item, None)
        if self.__head is None:
            self.__head = newitem
            self.__tail = newitem
        else:
            self.__head.insertBefore(item)
    def append(self, item): #insertar nodo por el final de la lista
        newitem = LinkedList.Element(self, item, None)
        if self.__head is None:
            self.__head = newitem
            self.__tail = newitem
        else:
            self.__tail.insertAfter(item)
    def __copy__(self): #copiar lista
        copy = LinkedList()
        temp = self.__head
        if self.__head is None:
            return copy
        else:
            copy.append(temp.data)
            while temp.next is not None:
                temp = temp.__next
                copy.append(temp.data)
            return copy
    def extract(self, item): #eliminar nodo de la lista
        if self.getIsEmpty():
            raise KeyError
        temp = self.getHead()
        if temp.getData() == item:
                temp.extract()
        else:
            while temp.getData() is not item:
                temp = temp.getNext()
                if temp.getData() == item:
                    temp.extract()
                    break
                if temp.getNext() is None:
                    raise KeyError
    def __str__(self): #convertir la lista en cadena de caracteres
        chain = "LinkedList {"
        temp = self.getHead()
        if temp is not None:
            while temp is not None:
                chain += str(temp.getData())
                if not temp.getNext() == None:
                    chain += ", "
                temp = temp.getNext()
        chain += "}"
        return chain
            
            
        
