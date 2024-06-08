Project Title: Real Estate Management System

Description:

This Python project is a real estate management system designed using Object-Oriented Programming (OOP) principles. It's implemented in PyCharm and aims to model various aspects of the real estate domain, including properties, owners, and a real estate agency.

Key Features:

Classes:

Inmueble (Property): Abstract base class representing any type of property.
Casa (House): Subclass of Inmueble with specific attributes like patio size.
Departamento (Apartment): Subclass of Inmueble with attributes like expenses and department number.
Salon (Hall): Subclass of Inmueble with a capacity attribute.
Quinta (Country House): Subclass of Inmueble with attributes like pool and barbecue area.
Propietario (Owner): Represents property owners.
Inmobiliaria (Real Estate Agency): Manages properties, owners, sales, and rentals.
Methods:

Getters and setters for all class attributes.
detalleInmueble(): Provides a detailed description of a property.
venderPropiedad(): Handles the sale of a property, including ownership transfer and commission calculation.
alquilarInmueble(): Manages the rental of a property, including tenant assignment and rent calculation.
calcularPrecio(): Calculates the suggested price of a property based on its characteristics.
Error Handling:

Extensive use of try-except blocks to handle potential errors like invalid input types or values.
Purpose:

This project serves as a foundation for a more comprehensive real estate management system. It demonstrates the use of OOP concepts like inheritance, abstraction, and encapsulation to model real-world entities and relationships.

How to Use (Basic Example):

Python
from inmueble import Casa, Propietario, Inmobiliaria

# Create an owner
owner = Propietario("John Doe", 12345678)

# Create a house
house = Casa(150.5, "123 Main Street", 3, owner, 50.0)

# Create a real estate agency
agency = Inmobiliaria()

# Add the house to the agency's portfolio
agency.anadirPropiedad(house, 250000)

# Get details of the house
print(house.detalleInmueble())
Usa el código con precaución.
play_circleeditcontent_copy
Installation:

Clone this repository.
Install the required dependencies: pip install -r requirements.txt (if you have a requirements file)
Future Enhancements:

Implement a user interface (GUI or web-based).
Add more property types and features.
Integrate with a database for persistent storage.
Implement search and filtering functionality.
Let me know if you'd like any modifications or additions to this README!




tune

share


more_vert


expand_content
add_circle


mic
send
Es posible que Gemini muestre información imprecisa, incl
