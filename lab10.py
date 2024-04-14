# class Fruit:
#     def __init__(self):
#         self._shape = ""



#     def canBePhone(self):
#         return "fruits can't be phones..."
    
# class Banana(Fruit):
#     def __init__(self, shape):
#         super().__init__(self,shape)

#     def canBePhone(self):
#         return "Bananas can be phones!"
    
# apple = Fruit('round')
# print(apple.canBePhone())

# banana = Banana('curved')
# print(banana.canBePhone())

################################################

# # Define class Fruit
# class Fruit():
#     def __init__(self, clr="", shp="", tst=""):
#         self._colour = clr
#         self._shape = shp
#         self._taste = tst

#     def setColour(self, value):
#         self._colour = value

#     def setShape(self, value):
#         self._shape = value

#     def setTaste(self, value):
#         self._taste = value

#     def descriptor(self):
#         return self._colour + ", " + self._shape + ", " + self._taste


# # Define class Banana
# class Banana(Fruit):
#     def __init__(self, clr="", shp="", tst=""):
#         super().__init__(clr, shp, tst)


# # Define class Apple
# class Apple(Fruit):
#     def __init__(self, clr="", shp="", tst="", type=""):
#         super().__init__(clr, shp, tst)
#         self._type = type

#     def setType(self, value):
#         self._type = value

#     def descriptor(self):
#         return super().descriptor() + ", " + self._type


# # Create some objects and test the methods
# afruit = Fruit("green", "round", "sweet")
# print("A fruit: ", afruit.descriptor())

# bn = Banana("yellow", "long", "soft and sweet")
# print("A banana: ", bn.descriptor())

# app1 = Apple("red", "round", "sweet and crunchy")
# print("An apple: ", app1.descriptor())
# app1.setType("Gala")
# print("A particular apple: ", app1.descriptor())

####################################################

class Automobile():
    def __init__(self, ndoors=0, clr=""):
        self._doors = ndoors
        self._colour = clr

    def printDoors(self):
        return "Number of doors is: " + str(self._doors)

    def printColour(self):
        return "Colour is: " + self._colour

    def display(self):
        return "Car is: " + str(self._doors) + " doors, " + self._colour

class SportsCar(Automobile):
    def __init__(self, ndoors=0, clr="", eng=0): #Should have same parameters, should be self first
        super().__init__(ndoors, clr)
        self._engine = eng

    def display(self):
        return super().display(), "with " + str(self._engine) + " hp"

