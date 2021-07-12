#Luis Fernando Soria
#Programacion orientada a objetos
#ejercicio ordenar 12-07-2021

class Ordenar:
    def _init_(self,lista):
        self.lista = lista
    
    def borbuja(self):
        for i in range(len(self.lista)):
            for j in range(i+1,len(self.lista)):
                if self.lista[i] < self.lista[j]:
                    aux = self.lista[i]
                    self.lista[i] = self.lista[j]
                    self.lista[j] = aux

    def insertar(self,valor):
        self.borbuja()
        auxlista=[]
        enc=False
        for pos, ele in enumerate(self.lista):
            if ele > valor:
                auxlista.append(self.lista[i])
                enc=True
                break
        if enc:
            for ele in range(pos):
                auxlista.append(valor)

            self.lista =self.lista[0:pos]+ auxlista + self.lista[pos:]
        else: self.lista.append(valor)
        return self.lista

    def insertar2(self,valor):
        self.borbuja()
        auxlista=[]
        enc=False
        for pos, ele in enumerate(self.lista):
            if ele > valor:
                auxlista.append(valor)
                enc=True
                break
        if enc: self.lista =self.lista[0:pos]+ auxlista + self.lista[pos:]
        else:
             self.lista.append(valor)
        return self.lista

ord1 = Ordenar(10,15,20,70,80)
#              0 ,1 ,2, 3, 4  
print(ord1.insertar(50))
#ord1.borbuja()
#print(ord1.lista)