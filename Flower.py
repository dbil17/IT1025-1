class Flower: 
#Blueprint for creating flower objects
    def __init__(self, name): 
#When a flower is created the name of it will be passed)
        self.name = name

    def grow(self): 
#means a flower is growing
        print("The " +self.name + " is growing.")

    def bloom(self): 
#will display a flower is blooming
        print("The " + self.name + " is blooming.")

def main():
    flower1 = Flower("Rose")
    flower1.grow()
    flower1.bloom()
    flower2 = Flower("Daisy")
    flower2.grow()
    flower2.bloom()
    flower3 = Flower("Tulip")
    flower3.grow()
    flower3.bloom()

#The code above creates a specific flower like Tulip by using the class Flower code before it. When the code is run the code will show that the flower grows and blooms.

if __name__ == "__main__":
  main()

#Makes sure the function runs when you run the code