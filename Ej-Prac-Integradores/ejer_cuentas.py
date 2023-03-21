"""Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
- mostrar(): Muestra los datos de la persona.
- Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
"""
class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
        
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
        
    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        if edad < 0:
            print("La edad debe ser un número positivo")
        else:
            self._edad = edad
            
    def get_dni(self):
        return self._dni
    
    def set_dni(self, dni):
        if len(dni) != 8:
            print("El DNI debe tener 8 dígitos")
        else:
            self._dni = dni
            
    def mostrar(self):
        print("Nombre: ", self._nombre)
        print("Edad: ", self._edad)
        print("DNI: ", self._dni)
        
    def es_mayor_de_edad(self):
        if self._edad >= 18:
            return True
        else:
            return False

"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
- mostrar(): Muestra los datos de la cuenta.
- ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
- retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.
"""
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        self.__titular.mostrar()
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


"""
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase Cuenta creada anteriormente. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
- Un constructor.
- Los setters y getters para el nuevo atributo.
- En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad, 18 años, pero menor de 25 años y falso en caso contrario.
- Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.
"""
class CuentaJoven(Cuenta):
    
    def __init__(self, titular: Persona, cantidad: float = 0.0, bonificacion: float = 0.0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion
        
    def get_bonificacion(self):
        return self._bonificacion
    
    def set_bonificacion(self, bonificacion):
        self._bonificacion = bonificacion
        
    def es_titular_valido(self):
        edad = self.get_titular().get_edad()
        return edad >= 18 and edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero de una cuenta joven con titular no válido.")
    
    def mostrar(self):
        super().mostrar()
        print ("Cuenta Joven")
        print (" Bonificación: {}%".format(self._bonificacion))
        

persona1 = Persona("Paola", 30, "22448866F")
persona2 = Persona("Juan", 20, "12345678Z")

cuenta_comun = Cuenta(persona1, 1000.0)
cuenta_joven = CuentaJoven(persona2, 500.0, 5.0)

print ("imprimo cuenta comun: ")
cuenta_comun.mostrar()
print (" ")
print ("imprimo cuenta joven: ")
cuenta_joven.mostrar()


