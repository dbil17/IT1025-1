# Define the Flower class
class Flower:
    def __init__(self, name):  # Constructor method to initialize an object with a name attribute
        self.name = name  # The 'name' attribute stores the name of the flower, set when the object is created.

    def grow(self):  # Method to simulate the flower growing
        print("The " + self.name + " is growing.")  # Output message indicating the flower is growing

    def bloom(self):  # Method to simulate the flower blooming
        print("The " + self.name + " is blooming.")  # Output message indicating the flower is blooming

# Main function to demonstrate object creation and method calls
def main():
    flower1 = Flower("Rose")  # Create a 'Flower' object named 'flower1' with the name 'Rose'
    flower1.grow()  # Call the 'grow' method on 'flower1'
    flower1.bloom()  # Call the 'bloom' method on 'flower1'
    
    flower2 = Flower("Daisy")  # Create a 'Flower' object named 'flower2' with the name 'Daisy'
    flower2.grow()  # Call the 'grow' method on 'flower2'
    flower2.bloom()  # Call the 'bloom' method on 'flower2'
    
    # Add a new flower to the example
    flower3 = Flower("Tulip")  # Create a 'Flower' object named 'flower3' with the name 'Tulip'
    flower3.grow()  # Call the 'grow' method on 'flower3'
    flower3.bloom()  # Call the 'bloom' method on 'flower3'

# Ensure that the main function runs only if this script is executed directly (not imported as a module)
if __name__ == "__main__":  # Checks if this file is being run directly
    main()  # Calls the main function to execute the code