#Clase erencia 12-07-2021

class Persona:
    _siguiente=0
    def __init__(self,nombre="Invitado",activo=True):
        #Persona._siguiente = Persona._siguiente+1
        self._codigo=self._siguiente()
        self._nombre=self.nombreMayuscula(nombre)
        self.activo=activo

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre (self,nom):
        self._nombre=nom
        
    @property
    def codigo(self):
        return self._codigo
    @nombre.setter
    def codigo (self,cod):
        self._codigo=cod

    def siguiente(self):
        Persona._siguiente=Persona._siguiente+1
        return Persona._siguiente

    def _nombreMayuscula(self,nomb):
        return nomb.upper()

    def mostrar_datos(self):
        return 
        
per1=Persona()
print(per1.mostrar_datos())

per2=Persona("Luis",False)
print(per2.nombre)    