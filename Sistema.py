from abc import ABCMeta, abstractmethod


class Inmueble(metaclass=ABCMeta):
    """
    Clase base abstracta.

    El constructor requiere como argumento una instancia de la clase propietario.
    Todas las instancias de esta clase se crean con un código único que no se puede modificar.
    Los atributos estado y cochera están en el constructor y se crean por default para dar la posibilidad de mayor personalización al momento de instanciar el objeto.
.
    """



    unique_code_seq = 0

    posible_estado = ["en alquiler", "alquilado",
                      "en venta", "vendido", "en alquiler o venta"]


    def __init__(self, coveredArea, address, rooms, owner, estado="en venta", cochera=False):



        try:
            self._validadorDeinputs(coveredArea, address, rooms, owner, estado, cochera)
        except (TypeError, ValueError) as e:


            raise e

        else:
            self._unique_code = Inmueble.unique_code_seq + 1
            Inmueble.unique_code_seq = self._unique_code
            self._coveredArea = coveredArea
            self._address = address
            self._rooms = rooms
            self._owner = owner
            self._owner.añadirPropiedad(self)
            self._estado = estado
            self._cochera = cochera
            self._inquilino = ""
            self._costo = 0


    def _validadorDeinputs(self, coveredArea, address, rooms, owner, estado, cochera):
        """ Realiza controles de TypeError y ValueError sobre los argumentos del constructor de la clase base.

            Una funcion similar ( con distinto nombre ) se establece en cada clase hija para controlar los parametros pasados como argumentos,
            en dichas clases. Al utilizarla con Try/Except no neceista return alguno.

            Args: coveredArea, address, rooms, owner, estado, cochera

            """
        if not isinstance(coveredArea, (int, float)):
            raise TypeError('Error: covered_area debe ser int o float')
        if not isinstance(address, str):
            raise TypeError('Error: direccion debe ser str')
        if not isinstance(rooms, int):
            raise TypeError('Error: la cantidad de habitaciones debe ser enteros')
        if estado not in self.posible_estado:
            raise ValueError('Error: El estado no está habilitado')
        if not isinstance(owner, Propietario):
            raise TypeError('Error: Debe ser Propietario')
        if not isinstance(cochera, bool):
            raise TypeError("Error: El parametro cochera solo toma valores booleanos")

    def getCosto(self):
        return self._costo

    def setCosto(self, costo):
        if isinstance(costo, (int, float)) and costo >= 0:
            self._costo = costo
        else:
            raise TypeError("Error: error al momento de ingresar el costo")

    def getUniquecode(self):
        return self._unique_code

    def getCoveredArea(self):
        return self._coveredArea

    def setCoveredArea(self, area):
        if isinstance(area, (int, float)) and area > 0:
            self._coveredArea = area
        else:
            raise TypeError("Error: el area cubierta debe estar expresada en enteros o float.")

    def getAddress(self):
        return self._address

    def setAddress(self, address):
        if isinstance(address, str):
            self._address = address
        else:
            raise TypeError("Error: la direccion debe ser una cadena.")

    def getRooms(self):
        return self._rooms

    def setRooms(self, rooms):
        if isinstance(rooms, int) and rooms > 0:
            self._rooms = rooms
        else:
            raise TypeError("Error: las habitaciones estan mal expresadas.")

    def getOwner(self):
        return self._owner

    def setOwner(self, owner):
        if isinstance(owner, Propietario):
            self._owner = owner
        else:
            raise TypeError("Error: el dueño debe ser de la clase Propietario.")

    def getEstado(self):
        return self._estado

    def setEstado(self, estado):
        if isinstance(estado, str) and estado in self.posible_estado:
            self._estado = estado
        else:
            raise TypeError("Error: el estado debe ser una cadena y debe ser uno de los estados posibles.")

    def getCochera(self):
        return self._cochera

    def setCochera(self, cochera):
        if isinstance(cochera, bool):
            self._cochera = cochera
        else:
            raise TypeError("Error: el estado de la cochera debe ser True o False.")

    def getInquilino(self):
        return self._inquilino


    def modificarInquilino(self, nombre):
        """Permite asignar nombre al atributo de instancia inquilino.


           Toma como argumento un cadena y la asigna al atributo _inquilino.
           Esta funcion se deberia utilizar solo al momento del alquiler. Por lo tanto no tiene controles, ya que la funcion alquilarInmueble() tiene este control.
            Args:
                nombre (str)

            Returns:
                None
            """

        self._inquilino = nombre

    def detalleInmueble(self):
        """Genera una cadena con detalles del inmueble.

        Retorna una cadena formateada con detalles específicos del inmueble, incluyendo su código único,
        área cubierta, dirección, cantidad de habitaciones, propietario, estado,  la presencia o ausencia de cochera, si tiene inquilino y si posee costo.

        Returns:
            str: Una cadena que detalla la información del inmueble.
            """
        tipoInmueble = type(self).__name__
        cochera = "Con cochera" if self.getCochera() else "Sin cochera"
        detalles = (
            f'\n==========\n {tipoInmueble}\n Codigo de inmueble: {self.getUniquecode()} ,\n El inmueble tiene un área cubierta de : {self.getCoveredArea()},\n'
            f' Está en la dirección: {self.getAddress()},\n Tiene: {self.getRooms()} habitaciones,\n'
            f' Pertenece a: {self.getOwner().getFullname()},Dni:  {self.getOwner().getDni()},\n Estado: {self.getEstado()},\n {cochera}')


        if self.getInquilino():
            detalles += f'\n Inquilino: {self.getInquilino()}'

        if self.getCosto() > 0:
            detalles += f'\n Costo de la inidad: {self.getCosto()}'

        return detalles

    def __repr__(self):
        """Representación de cadena del objeto inmueble.

            Devuelve una cadena que representa de manera única el objeto inmueble. La cadena incluye el tipo de inmueble, el nombre completo
            y el DNI del propietario.

            Returns:
                str: Cadena que representa el objeto inmueble.
            """


        nombrePropietario = self.getOwner().getFullname()
        dniPropietario = self.getOwner().getDni()
        tipoInmueble = type(self).__name__
        return f"Clase {tipoInmueble}\n(Propietario: {nombrePropietario},\nDNI: {dniPropietario})"

    @abstractmethod
    def metodo_abstracto(self):
        """
                Método abstracto que debe ser implementado por las clases hijas.


        """
        pass


class Casa(Inmueble):
    """
    Clase que representa una casa.

    Esta clase hereda de la clase Inmueble y agrega características específicas de una casa, como el tamaño del patio (patioSurface).

    Args:
        coveredArea (float): Área cubierta de la casa.
        address (str): Dirección de la casa.
        rooms (int): Número de habitaciones en la casa.
        owner (Propietario): Propietario de la casa.
        estado (str, opcional): Estado de la casa. Puede ser "en venta", "alquilado", etc. Por defecto es "en venta".
        cochera (bool, opcional): Indica si la casa tiene cochera. Por defecto es False.
        patioSurface (float): Tamaño del patio de la casa.

    Attributes:
        patioSurface (float): Tamaño del patio de la casa.

    Methods:
        metodo_abstracto: Método abstracto que debe ser implementado por las clases hijas.
        detalleInmueble: devuelve una cadena.

    """
    def __init__(self, coveredArea, address, rooms, owner, patioSurface, estado="en venta", cochera=False):
        super().__init__(coveredArea, address, rooms, owner, estado, cochera)

        try:
            self._validadorDeinputsCasa(patioSurface)
        except TypeError as ty:
            raise ty
        else:
            self._patioSurface = patioSurface

    def _validadorDeinputsCasa(self, patioSurface):
        if not isinstance(patioSurface, (int, float)):
            raise TypeError('Error: patioSurface debe ser int o float')

    # Getter y Setters

    def getPatioSurface(self):
        return self._patioSurface

    def setPatioSurface(self, patio):
        if isinstance(patio, (int, float)):
            self._patioSurface = patio
        else:
            raise TypeError("Error: las medidas de superficie de patio deben ser enteros o flotantes.")

    def metodo_abstracto(self):
        pass

    def detalleInmueble(self):

        return super().detalleInmueble() + f',\n La casa tiene una superficie de patio de: {self.getPatioSurface()}.'


class Departamento(Inmueble):
    """
        Clase que representa un departamento.

        Esta clase hereda de la clase Inmueble y agrega características específicas de un departamento, como los gastos comunes (expenses) y el número de departamento (departmentNumber).

        Args:
            coveredArea (float): Área cubierta del departamento.
            address (str): Dirección del departamento.
            rooms (int): Número de habitaciones en el departamento.
            owner (Propietario): Propietario del departamento.
            expenses (float): Gastos comunes del departamento.
            departmentNumber (int): Número de departamento.
            cochera (bool, opcional): Indica si el departamento tiene cochera. Por defecto es False.
            estado (str, opcional): Estado del departamento. Puede ser "en venta", "alquilado", etc. Por defecto es "en venta".

        Methods:
            metodo_abstracto: Método abstracto que debe ser implementado por las clases hijas.
            detalleInmueble: devuelve una cadena.
        """


    def __init__(self, coveredArea, address, rooms, owner, expenses, departmentNumber, cochera=False,
                 estado='en venta'):
        super().__init__(coveredArea, address, rooms, owner, estado, cochera)

        try:
            self._validadorDeinputsDepto(expenses, departmentNumber)
        except TypeError as tys:
            raise tys
        else:
            self._expenses = expenses
            self._departmentNumber = departmentNumber

    def _validadorDeinputsDepto(self, expenses, departmentNumber):
        if not isinstance(expenses, (int, float)):
            raise TypeError('Error: expenses debe ser int o float')
        if not isinstance(departmentNumber, int):
            raise TypeError('Error: departmentNumber debe ser int')

    # Getters y Setters
    def setExpenses(self, expenses):
        if isinstance(expenses, (int, float)):
            self._expenses = expenses
        else:
            raise TypeError("Error: las medidas de superficie de patio deben ser enteros o flotantes.")

    def getExpenses(self):
        return self._expenses

    def getDepartmentNumber(self):
        return self._departmentNumber

    def setDepartamentNumber(self, numero):
        if isinstance(numero, int) and numero > 0:
            self._departmentNumber = numero
        else:
            raise TypeError("Error: error al ingresar el numero de Departamento.")

    def metodo_abstracto(self):
        pass

    def detalleInmueble(self):

        return (super().detalleInmueble() +
                f',\n El departamento tiene expensas por un monto igual a:  {self.getExpenses()},\n'
                f' y el numero de departamento es : {self.getDepartmentNumber()}')


class Propietario():
    """
        Clase que representa a un propietario de inmuebles.

        Args:
            fullname (str): Nombre completo del propietario.
            dni (int): Número de documento del propietario.

        Methods:
            describirPropiedad: Devuelve una cadena con la descripción de todas las propiedades del propietario.
            eliminarPropiedad: Devuelvo booleano si y puede eliminar ( si existe ) elemento de la lista de propiedades.
            añadirPropiedad: Devuelvo booleano.
        """

    def __init__(self, fullname, dni):

        try:
            self._validadorDeinputsPropietario(fullname, dni)
        except TypeError as tyq:
            raise tyq
        else:
            self._fullname = fullname
            self._dni = dni
            self._propiedades = []

    def _validadorDeinputsPropietario(self, fullname, dni):

        if not isinstance(fullname, str):
            raise TypeError('Error: el nombre debe ser un str')
        if not isinstance(dni, int):
            raise TypeError('Error: el dni debe ser un entero')

    # Getter y setters
    def getListaPropiedades(self):
        return self._propiedades


    def getFullname(self):
        return self._fullname

    def getDni(self):
        return self._dni

    def setFullname(self, nombre):
        if isinstance(nombre, str):
            self._fullname = nombre
        else:
            raise TypeError("Error: el nombre debe estar en cadena de texto.")

    def setDni(self, dni):
        if isinstance(dni, int):

            self._dni = dni
        else:
            raise TypeError("Error: el dni debe ser un entero.")

    def eliminarPropiedad(self, id):
        """
           Elimina una propiedad de la lista de propiedades del propietario.

           Args:
               id (int): Identificador único de la propiedad que se desea eliminar.

           Returns:
              bool: True si la propiedad se eliminó correctamente, False si no se encontró.

           Raises:
               TypeError: Si el id no es un entero.

        """

        if not isinstance(id, int):
            raise TypeError("Error: el id debe ser un entero.")

        else:
            for propiedad in self.getListaPropiedades():
                if propiedad.getUniquecode() == id:
                    self.getListaPropiedades().remove(propiedad)
                    return True
        return False

    def añadirPropiedad(self, *propiedades):
        """
            Añade una o más propiedades a la lista de propiedades del propietario.

            Esta funcion es importante porque permite al momento de crear un inmueble cualquiera que este sea asigando al propietario. Esto dentro del constructor
            de la clase inmueble.

            Args:
                *propiedades (Inmueble): Una o más instancias de la clase Inmueble que se agregarán a la lista de propiedades.

            Returns:
                bool: True si al menos una propiedad se añadió correctamente, False si ninguna se añadió.

            Raises:
                TypeError: Si algún elemento proporcionado no es una instancia de la clase Inmueble.
        """
        resultado = False
        for propiedad in propiedades:
            if not isinstance(propiedad, Inmueble):
                raise TypeError("Error: el elemento no es una instancia de la clase Inmueble.")
            else:
                if propiedad not in self.getListaPropiedades():
                    self.getListaPropiedades().append(propiedad)
                    resultado = True

        return resultado

    def describirPropiedad(self):
        """
            Genera una descripción detallada de todas las propiedades del propietario.

            Returns:
                str: Una cadena que contiene la descripción de todas las propiedades del propietario.
        """
        descripcion_propiedades = f"f\n==========\nEl propietario {self.getFullname()} posee : {str(len(self.getListaPropiedades()))} inmuebles \n"
        for propiedad in self.getListaPropiedades():
            descripcion_propiedades += propiedad.detalleInmueble() + "\n==========\n"
        if descripcion_propiedades:
            return descripcion_propiedades
        else:
            return f'El propietario {self.getFullname()} no posee propiedades a su nombre.'

    def __repr__(self):
        return f"Clase Propietario({self.getFullname()}, {self.getDni()})"


class Inmobiliaria():
    """
        Clase que representa una inmobiliaria.

        Atributos de clase:
            costoDeGestionAlquiler (float): Porcentaje de costo de gestión para alquileres.
            costoDeGestionventa (float): Porcentaje de costo de gestión para ventas.
            metroCuadrado (float): Precio por metro cuadrado.

        Methods:
            datallarInmueble: Devuelve una cadena con detalles de todos los inmuebles en cartera.
            listaPropietarios: Devuelve una cadena con la cantidad de propietarios y sus datos.
            añadirPropiedad: Añade una propiedad a la lista de propiedades de la inmobiliaria.
            eliminarPropiedad: Elimina una propiedad de la lista de propiedades.
            venderPropiedad: Vende una propiedad y transfiere la propiedad al nuevo propietario. Cambia el estado de la propiedad a "vendido"
            alquilarInmueble: Alquila un inmueble a un inquilino.
            ponerEnAlquiler: Cambia el estado de un inmueble a "en alquiler".
            calcularPrecio: Calcula el precio sugerido de un inmueble.
        """


    costoDeGestionAlquiler = 0.1
    costoDeGestionventa = 0.2
    metroCuadrado = 500



    def __init__(self):
        self._listaPropiedades = []
        self._ganancias = 0

    def getGanancias(self):
        return self._ganancias

    def setGanancias(self, costo):
        self._ganancias += costo

    def getlistaPropiedades(self):
        return self._listaPropiedades



    def datallarInmueble(self):

        propiedades_con_detalles = "Cantidad de inmuebles en cartera: " + str(
            len(self.getlistaPropiedades()))
        if self._listaPropiedades:

            for inmueble in self.getlistaPropiedades():
                # Concatena utilizando la funcion de la clase inmueble detalleInmueble
                propiedades_con_detalles += inmueble.detalleInmueble() + "\n==========\n"
            return propiedades_con_detalles
        else:
            return None  #"Sin propiedades"

    def listaPropietarios(self):
        """
           Genera una lista de propietarios de todas las propiedades gestionadas por la inmobiliaria.

           Returns:
               tuple: Una tupla que contiene una cadena descriptiva y una lista de propietarios.
                      La cadena indica la cantidad de inmuebles gestionados y la lista contiene las instancias de propietario correspondientes.

                      Si la inmobiliaria no tiene propiedades, devuelve la cadena 'Sin propiedades'.
        """
        if self.getlistaPropiedades():
            cadena = (f'La inmobiliria cuenta con {len(self.getlistaPropiedades())} inmuebles: ')
            lista = []
            for propiedad in self.getlistaPropiedades():
                lista.append(propiedad.getOwner())
            return cadena, lista
        return None


    def anañadirPropiedad(self, inmueble, costo):
        """
            Añade una propiedad al sistema de la inmobiliaria junto con su costo asociado ( este se aloja en el atributo _costo).

            Args:
                inmueble (Inmueble): Instancia de la clase Inmueble que se desea añadir al sistema.
                costo (int or float): Costo asociado al inmueble.

            Returns:
                bool: True o false

            Raises:
                TypeError: Se genera si el inmueble no es una instancia de la clase Inmueble o si el costo no es un entero o flotante.
            """
        if inmueble not in self.getlistaPropiedades():
            if not isinstance(inmueble, Inmueble):
                raise TypeError("Error: inmueble debe ser una instancia de la clase Inmueble.")
            if not isinstance(costo, (int, float)):
                raise TypeError("Error: El costo del inmueble debe estar expresado en enteros o floats.")

            inmueble.setCosto(costo)
            self.getlistaPropiedades().append(inmueble)
            return True  # Propiedad añadida correctamente
        else:
            return False  # La propiedad ya se encuentra en el sistema

    def eliminarPropiedad(self, id):
        if not isinstance(id, int):
            raise TypeError("Error: el id debe ser un entero.")

        propiedades_encontradas = []

        for propiedad in self.getlistaPropiedades():
            if propiedad.getUniquecode() == id:
                propiedades_encontradas.append(propiedad)

        if propiedades_encontradas:
            for propiedad in propiedades_encontradas:
                self.getlistaPropiedades().remove(propiedad)
            return True  # Propiedad eliminada con éxito
        else:
            return False  # No existen propiedades con ese ID

    def venderPropiedad(self, id, nuevo_propietario):
        """
            Vende una propiedad a un nuevo propietario.

            Esta función busca una propiedad por su ID, verifica que esté en venta, y luego realiza la transferencia de propiedad al nuevo propietario.
            También actualiza el estado de la propiedad a "vendido", cambia el costo de la propiedad (porque ya fue vendida)
            y registra las ganancias por la venta en la inmobiliaria.
            Args:
                id (int): Identificador único de la propiedad que se desea vender.
                nuevo_propietario (Propietario): Nuevo propietario al que se transferirá la propiedad.

            Returns:
                bool: True o false

        """
        if not isinstance(id, int):
            raise TypeError("Error: el id debe ser un entero.")

        if not isinstance(nuevo_propietario, Propietario):
            raise TypeError("Error: nuevo_propietario debe ser una instancia de la clase Propietario.")


        for propiedad in self.getlistaPropiedades():
            if propiedad.getUniquecode() == id:
                if propiedad.getEstado() == "en venta" or propiedad.getEstado() == "en alquiler o venta":

                    propietario = propiedad.getOwner()
                    # Elimina de la clase propietario la propiedad ( con la funcion eliminarPropiedad, deberia solo eliminar la propiedade de la lista )
                    # Es necesario que los objetos propietarios que se creen tengan el nombre de variable igual que el argumento fullname.
                    propietario.eliminarPropiedad(id)
                    propiedad.setOwner(nuevo_propietario)
                    # Al nuevo propietario ( previamente creado ) le asigna la propiedad vendida.
                    nuevo_propietario.añadirPropiedad(propiedad)
                    # Por ultimo remueve la propiedad de la lista. ( Esto podria modificarlo)
                    propiedad.setEstado("vendido")
                    gananciaVenta = propiedad.getCosto() * self.costoDeGestionventa
                    self.setGanancias(gananciaVenta)
                    propiedad.setCosto(0)
                    return True  # Propiedad vendida correctamente
                else:
                    return False  # La propiedad no está en venta
        return False  # Imposible la venta, la propiedad no está en el sistema

    def alquilarInmueble(self, id, inquilino):
        """
            Alquila un inmueble a un inquilino.

            Esta función busca un inmueble por su ID, verifica que esté disponible para alquiler (previamente se debe utilizar la funcion ponerEnAlquiler)
            , y luego asigna un inquilino al inmueble.
            También actualiza el estado de la propiedad a "alquilado" y registra las ganancias por el alquiler en la inmobiliaria.
            Args:
                id (int): Identificador único del inmueble que se desea alquilar.
                inquilino (str): Nombre del inquilino que se asignará al inmueble.

            Returns:
                bool: True o false.
        """

        if not isinstance(id, int) or id <= 0:
            raise TypeError("Error: el ID debe ser un entero mayor a 0.")

        if not isinstance(inquilino, str):
            raise TypeError("Error: el nombre del inquilino debe ser una cadena de texto.")

        for propiedad in self.getlistaPropiedades():
            if propiedad.getUniquecode() == id:
                if propiedad.getEstado() == "en alquiler" or propiedad.getEstado() == "en alquiler o venta":
                    propiedad.modificarInquilino(inquilino)
                    propiedad.setEstado("alquilado")
                    gananciaAlquiler = propiedad.getCosto() * self.costoDeGestionAlquiler
                    self.setGanancias(gananciaAlquiler)
                    return True  # La propiedad fue alquilada correctamente
                else:
                    return False  # La propiedad no está en alquiler

        return False  #La propiedad no esta en el sistema

    def ponerEnAlquiler(self, id):
        """
                    Pone en alquiler una propiedad.

                    Esta función busca un inmueble por su ID, verifica que no este previamente en alquiler
                    ,y luego asigna el nuevo estado.


                    Args:
                        id (int): Identificador único del inmueble que se desea poner en alquiler.


                    Returns:
                        bool: True o false.

                    Raises:
                        TypeError: si el id no es de tipo int.

                """
        if not isinstance(id, int):
            raise TypeError("Error: el id debe ser un entero.")
        for propiedad in self.getlistaPropiedades():
            if propiedad.getUniquecode() == id:
                if propiedad.getEstado() == "en alquiler":
                    return False
                else:
                    propiedad.setEstado("en alquiler")
                    return True  # La propiedad ha sido puesta en alquiler correctamente
        return False  # La propiedad no está en el sistema



    def ponerEnVenta(self, id):
        """
                    Pone en venta una propiedad.

                    Esta función busca un inmueble por su ID, verifica que no este previamente en venta
                    ,y luego asigna el nuevo estado.

                    Args:
                        id (int): Identificador único del inmueble que se desea poner en venta.

                    Returns:
                        bool: True o false.

                    Raises:
                        TypeError: si el id no es de tipo int.

                    """
        if not isinstance(id, int):
            raise TypeError("Error: el id debe ser un entero.")
        for propiedad in self.getlistaPropiedades():
            if propiedad.getUniquecode() == id:
                if propiedad.getEstado() == "en venta":
                    return False
                else:
                    propiedad.setEstado("en venta")
                    return True  # La propiedad ha sido puesta en venta correctamente
        return False  # La propiedad no está en el sistema

    # Calcularia el precio segun la inmobiliriaria, independientemente del precio que ponga el cliente.
    # La idea sera llegar a un intermedio entre ambos precios, si es que el cliente tiene un precio pretendido para la venta. Puede no tenerlo.
    def calcularPrecio(self, propiedad):
        """
                Calcula el precio sugerido de una propiedad en base a sus caracteristicas y su multiplicacion con los argeumentos de la clase Inmobiliaria.



                Args:
                    Inmueble (Inmueble): Identificador único del inmueble que se desea poner en venta.

                Returns:
                    float: resultado de la operacion.

                Raises:
                    TypeError: si el arguemtno inmueble no es de clase Inmueble.

                """

        precio = 0
        if isinstance(propiedad, Inmueble):

            precio += propiedad.getCoveredArea() * self.metroCuadrado
            if propiedad.getCochera():
                # Monto aleatorio asignado a tener o no cochera.
                precio += 500

            return f' Precio sugerido del inmueble, mas costos administrativos :{precio + (precio * self.costoDeGestionventa)}'
        else:
            return TypeError("Error: Ingrese un Objeto Clase Propiedad")

    def __repr__(self):

        clase = type(self).__name__
        return f"Clase {clase}"


class Salon(Inmueble):
    """
        Clase que representa un salón.

        Esta clase hereda de la clase Inmueble y agrega características específicas de un salón, como la capacidad.

        Args:
            coveredArea (float): Área cubierta del salón.
            address (str): Dirección del salón.
            owner (Propietario): Propietario del salón.
            capacidad (int): Capacidad del salón.Por defecto se crea en 0.
            estado (str, opcional): Estado del salón. Puede ser "en venta", "alquilado", etc. Por defecto es "en venta".
            cochera (bool, opcional): Indica si el salón tiene cochera. Por defecto es False.

        Methods:
            metodo_abstracto: Método abstracto que debe ser implementado por las clases hijas.
            detalleInmueble: devuelve una cadena.
        """
    def __init__(self, coveredArea, address, owner, capacidad=0, estado="en venta", cochera=False):
        super().__init__(coveredArea, address, 0, owner, estado, cochera)
        try:
            self._validadorDeSalon(capacidad)
        except TypeError as tyx:
            raise tyx
        else:

            self._capacidad = capacidad

    def _validadorDeSalon(self, capacidad):
        if not isinstance(capacidad, int):
            raise TypeError('Error: La capacidad del salón debe ser un número entero.')

        if capacidad < 0:
            raise ValueError('Error: La capacidad del salón no puede ser un número negativo.')

    def getCapacidad(self):
        return self._capacidad

    def setCapacidad(self, capacidad):
        if not isinstance(capacidad, int):
            raise TypeError('Error: La capacidad del salón debe ser un número entero.')
        if capacidad < 0:
            raise ValueError('Error: La capacidad del salón no puede ser un número negativo.')
        else:
            self._capacidad = capacidad

    def detalleInmueble(self):

        return super().detalleInmueble() + f'\n Capacidad del salón: {self.getCapacidad()}'

        return detalles

    def metodo_abstracto(self):
        pass


class Quinta(Inmueble):
    """
        Clase que representa una quinta.

        Esta clase hereda de la clase Inmueble y agrega características específicas de una quinta, como la presencia de pileta y quincho.

        Args:
            coveredArea (float): Área cubierta de la quinta.
            address (str): Dirección de la quinta.
            owner (Propietario): Propietario de la quinta.
            pileta (bool): Indica si la quinta tiene pileta. Por defecto en True.
            quincho (bool): Indica si la quinta tiene quincho. Por defecto en True.
            estado (str, opcional): Estado de la quinta. Puede ser "en venta", "alquilado", etc. Por defecto es "en venta".
            cochera (bool, opcional): Indica si la quinta tiene cochera. Por defecto es False.

        Methods:
            metodo_abstracto: Método abstracto que debe ser implementado por las clases hijas.
            detalleInmueble: devuelve una cadena.
        """
    def __init__(self, coveredArea, address, owner, pileta=True, quincho=True, estado="en venta", cochera=False):
        super().__init__(coveredArea, address, 0, owner, estado, cochera)
        try:
            self._validadorDeQuinta(pileta, quincho)
        except TypeError as tye:
            raise tye
        else:
            self._pileta = pileta
            self._quincho = quincho

    def _validadorDeQuinta(self, pileta, quincho):
        if not isinstance(pileta, bool) or not isinstance(quincho, bool):
            raise ValueError('Quincho y Pileta deben ser expresados en booleanos.')

    def getPileta(self):
        return self._pileta

    def getQuincho(self):
        return self._quincho

    def setPileta(self, pileta):
        if isinstance(pileta, bool):
            self._pileta = pileta
        else:
            raise TypeError("Error: Pileta debe ser un bool")

    def setQuincho(self, quincho):
        if isinstance(quincho, bool):
            self._quincho = quincho
        else:
            raise TypeError("Error: Quincho debe ser un bool")

    def detalleInmueble(self):
        pileta = "Con pileta" if self.getPileta() else "Sin pileta"
        quincho = "Con quincho" if self.getQuincho() else "Sin quincho"
        return super().detalleInmueble() + f',\n {pileta}, \n {quincho}.'

    def metodo_abstracto(self):
        pass
