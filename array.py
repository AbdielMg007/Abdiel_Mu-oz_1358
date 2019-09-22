class Array:
	    def __init__(self, n):
	        self.__data = []
	        for i in range(n):
	            self.__data.append(None)
	    
	    def to_string(self):
	        print(self.__data)
	        
	    def get_lenght(self):
	        return len(self.__data)
	    
	    def set_item(self, index, value):
	        if index>=0 and index <=len(self.__data):
	            self.__data[index]=value
	        else:
	            return "Fuera de rango"
	    
	    def get_item(self,index):
	        if index>=0 and index <=len(self.__data):
	            return self.__data[index]
	        else:
	            return "Fuera de rango"
	    
	    def clearing(self,value):
	        for i in range(len(self.__data)):
	            self.__data[i]=value
	    
	def main():
	    arreglo = Array(10)
	    arreglo.to_string()
	    print(f"El tamaño del arreglo es de {arreglo.get_lenght()}")
	    arreglo.set_item(1,10)
	    arreglo.to_string()
	    print(f"La posición 1 es = {arreglo.get_item(15)}")
	    arreglo.clearing(73)
	    arreglo.to_string()
	    
	main()

