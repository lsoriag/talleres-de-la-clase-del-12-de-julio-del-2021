


class Articulo:
    def __init__(self,cod,des,pre,sto):
        self.codigo=cod
        self.descripcion=des
        self.precio=pre
        self.stock=sto
        
class Cliente:
    def __init__(self,ced,nom,dir,tel):
        self.cedula=ced
        self.nombre=nom
        self.direccion=dir
        self.telefobo=tel

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
        return "Codigo: {} - Nombre: {} - Activo. {}".format(self.codigo, self.nombre, self.activo)

class Empleado(Persona):
    pass


class Venta:
    def __init__(self,fac,fec,cliente,tot,detalleVen):
        self.factura=fac
        self.fecha=fec
        self.cliente=cliente
        self.total=tot
        self.detalleVen=detalleVen

class VentaDet:
    def __init__(self,venta,producto,precio,cantidad):
        self.venta=venta
        self.producto=producto 
        self.precio=precio
        self.cantidad=cantidad

