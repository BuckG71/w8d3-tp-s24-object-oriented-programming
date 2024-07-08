# Shape Class Hierarchy

This repository contains a Python program that demonstrates the use of inheritance and polymorphism through a hierarchy of shape classes. The program includes a base Shape class and derived classes for specific shapes such as Circle, Rectangle, and Triangle. Each shape class has its own attributes and methods for calculating the area and perimeter.

## Clone the Repository

To clone the repository, use the following command:

```sh
git clone <your-repo-url>
```

Replace <your-repo-url> with the actual URL of your GitHub repository.

## Setup Instructions

1. Navigate to the project directory:

    ```sh
    cd path/to/your/cloned/repo
    ```

2. Ensure you have Python installed. You can download Python from python.org.
3. (Optional) Create and activate a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
    ```

4.	Install any required dependencies. If you have any dependencies, list them in a requirements.txt file and run:

    ```sh
    pip install -r requirements.txt
    ```

## Running the Program

To run the program, use the following command:

```sh
python main.py
```

This will execute the main.py file, which contains the logic to create instances of various shapes and print their area and perimeter.

## Program Overview

### Classes:
• Shape: The base class for all shapes.  
• Circle: A class representing a circle, derived from Shape.
• Rectangle: A class representing a rectangle, derived from Shape.  
• Triangle: A class representing a triangle, derived from Shape.

### Functions:
• rand_color(): Returns a random color from a predefined list.  
• get_random(): Returns a random floating-point number between 1 and 10.  
• get_random_triangle_sides(): Generates three sides that form a valid triangle.  

### Main Program:
• Creates instances of Circle, Rectangle, and Triangle.  
• Prints the area and perimeter of each shape.  

## Example Output

The area of the purple circle is 78.54, and its perimeter is 31.42.  
The area of the yellow circle is 28.27, and its perimeter is 18.85.  
The area of the blue rectangle is 24.00, and its perimeter is 20.00.  
The area of the orange rectangle is 15.00, and its perimeter is 16.00.  
The area of the pink triangle is 6.00, and its perimeter is 12.00.  
The area of the chartreuse triangle is 10.00, and its perimeter is 14.00.  

Ensure that all shapes are correctly instantiated and have valid attributes and methods to avoid any errors during execution.  

## License

This project is licensed under the MIT License - see the LICENSE file for details.
