Product Printer Application Report
1. Introduction
This application is built using object-oriented programming principles, focusing on the Product and Printer classes to manage products and print their details in different formats. By leveraging inheritance and abstraction, the code provides a structured way to extend functionality without modifying existing code. Additionally, this design applies several of the SOLID principles—a set of guidelines to create robust, scalable, and maintainable software.

2. Code Analysis
Classes and Methods
Product Class
The Product class represents a product with two attributes:

name: Name of the product.
price: Price of the product.
It provides getter methods:

get_name: Returns the name of the product.
get_price: Returns the price of the product.
The Product class acts as a data container, with methods to access its properties.

Printer Abstract Class
The Printer class is an abstract base class (ABC) that enforces any subclass to implement the print_product method, which will define how product information should be printed.

TextProductPrinter Class
This subclass of Printer overrides the print_product method to print product information in plain text format, displaying the name and price in a user-friendly format:

python
Копировать код
Product: Smartphone, Price: 5000 MDL
JSONProductPrinter Class
Another subclass of Printer, JSONProductPrinter, implements the print_product method to display product information in JSON format:

json
Копировать код
{
    "name": "Smartphone",
    "price": 5000
}

3. Application of SOLID Principles
The code demonstrates several SOLID principles:

S - Single Responsibility Principle (SRP)
Each class in the code has a specific responsibility:

The Product class is responsible for holding product details.
The Printer class defines a blueprint for printing methods, while TextProductPrinter and JSONProductPrinter focus on specific output formats.
This separation of concerns adheres to SRP, as each class handles one aspect of functionality.

O - Open/Closed Principle (OCP)
The code is open for extension but closed for modification:

Adding a new printing format requires creating a new subclass of Printer without modifying existing code.
TextProductPrinter and JSONProductPrinter demonstrate this, as additional formats could be introduced simply by subclassing Printer and implementing the print_product method.
L - Liskov Substitution Principle (LSP)
The Printer class and its subclasses adhere to the LSP:

Any instance of Printer can be replaced by instances of TextProductPrinter or JSONProductPrinter without affecting the program’s correctness.
This is achieved by the shared method signature print_product enforced by the Printer abstract class.
I - Interface Segregation Principle (ISP)
While there is only one method in the Printer class, ISP is respected by keeping the interface focused. If additional methods were required (e.g., specialized formatting), they could be implemented in individual subclasses to keep the interface minimal and tailored.

D - Dependency Inversion Principle (DIP)
The code respects DIP by programming to an abstraction, not a concrete class. The Printer class provides an abstract interface, while the concrete implementations (TextProductPrinter, JSONProductPrinter) are created based on it. This allows for flexibility in choosing and extending printing methods.

4. Example Usage and Output
Code Execution Example
The main execution creates two Product objects and demonstrates both text and JSON printing:

python
Копировать код
if name == "main":
    product1 = Product("Smartphone", 5000)
    product2 = Product("Laptop", 15000)

    text_printer = TextProductPrinter()
    text_printer.print_product(product1)
    text_printer.print_product(product2)

    print("\n--- Now printing in JSON format ---\n")

    json_printer = JSONProductPrinter()
    json_printer.print_product(product1)
    json_printer.print_product(product2)
Output
This code produces:

plaintext
Копировать код
Product: Smartphone, Price: 5000 MDL
Product: Laptop, Price: 15000 MDL

--- Now printing in JSON format ---

{
    "name": "Smartphone",
    "price": 5000
}
{
    "name": "Laptop",
    "price": 15000
}
5. Conclusion
This application demonstrates a clean, maintainable codebase designed with SOLID principles. The use of abstraction and inheritance allows for easy extensibility, promoting a modular approach where new printing methods can be added without modifying existing code. This design fosters a scalable and flexible solution for managing and displaying product information in various formats.