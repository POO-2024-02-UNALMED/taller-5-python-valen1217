class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def _init_(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super()._init_(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    @staticmethod
    def cantidadPeces():
        return len(Pez._listado)

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Pez.salmones += 1
        return cls(nombre, edad, "oceano", genero, "rojo", 6)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Pez.bacalaos += 1
        return cls(nombre, edad, "oceano", genero, "gris", 6)

    def getColorEscamas(self):
        return self._colorEscamas
