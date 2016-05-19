class DesTree(object):
    """Clase arbre de decisio"""
    __labels=['<tipus>','<catsize>','<domestic>','<tail>','<legs>','<fins>','<venomous>','<breathes>','<backbone>','<toothed>','<predator>','<aquatic>','<airborne>','<milk>','<eggs>','<feathers>','<hair>','<name>']
    __slots__=["__key","__childs"]

    def __init__(self, key=None):
        self.__key = key
        self.__childs = []
   
    def addChild(self, child):
        """afegeix un subabre child a la llista de fills del arbre actual"""
        for node in self.__childs:
            if child.getData() == node.getData():
                return None
        self.__childs.append(child)
			
    def getChilds(self):
        """Retorna la llista de fills"""
        return self.__childs
    
    def getData(self):
        """Retorna el valor del node"""
        return self.__key
    
    def getChild(self, data):
        """Reb dada y retorna el fill que conte la dada"""
        for node in self.__childs:
            if node.getData() == data:
                return node
        return None
    
    def Build(self,filename):
        """Obre un arxiu, llegeix cada linea y la guarda en una llista"""
        fileHandle = open(filename, "r")
        ll = fileHandle.readlines()
        fileList = []
        #if platform.system() == 'Windows':
         #   st = '\n'
        #else:
         #   st = '\r\n'
        for i in ll:
            fileList.append(i.rstrip("\n"))
        self.parser(fileList, 1, 0)
        
    def parser(self, fileList, lin, prof):
        """Omple l'arbre de desicio amb els valors de la llista obtinguts a build i filtra les etiquetes xml"""
        while (prof < len(self.__labels)) and (fileList[lin] == self.__labels[prof]):
            data = fileList[lin+1]
            subtree = DesTree(data)
            self.addChild(subtree)
            lin = self.getChild(data).parser(fileList, lin+2, prof+1)+1
        return lin
    def AddData(self,features):
        """Per afegir una llista d'atributs al arbre"""
        self.addDataRecursive(features, 0)
    def addDataRecursive(self, features, featurenum):
        """Funcio auxiliar de addData que introueix recursivament a la l'arbre els nous atributs de la llista"""
        if featurenum < len(features):
            node = DesTree(features[featurenum])
            self.addChild(node)
            self.getChild(features[featurenum]).addDataRecursive(features, featurenum+1)
            
    def GetDataClass(self, features):
        """Donada una llista d'atributs, recorre l'arbre i retorna el valor de la fulla corresponent"""
        notfound = 0
        leaf = self.getChilds()
        for prof in range(len(features)+1):
            for i in leaf:
                if notfound == len(leaf): #si no se ha encontrado en la hoja, paramos de iterar y devolvemos None
                    return None
                if prof is len(features): #si estamos en la profundidad maxima devolvemos el nombre del nodo
                    return i.getData()
                if str(i.getData()) == features[prof]: #si encontramos coincidencia de features continuamos desde ese nuevo nodo
                    leaf = i.getChilds()
                    notfound = 0
                    break
                notfound += 1
        return None        
        

