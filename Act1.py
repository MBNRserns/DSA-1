#OOPS- Object Oriented Programming Structure

#Focus on real life enteties to write code

#Object - Any real life entity represented in code
#for example student, cars, fruits\

#Class- blueprint of an object
#objects- instance of a class -> apple,banana,mango(objects)

class Fruit:
    #Properties of the fruit class
    def __init__(self, color, taste, shape, prefrence):
        self.color = color
        self.taste = taste
        self.shape = shape
        self.prefrence = prefrence

    #Getters
    def get_shape(self):
        print(self.shape)
    
    #Setter
    def set_shape(self,new_shape):
        self.shape = new_shape
        print(self.shape)

    #Function - user defined
    def showFruit(self):
        print("Hi I am a fruit with {} color {} shape and {} taste".format(self.color, self.shape, self.taste))

    #Function - user defined
    def user_input(self):
            self.preference= int(input("On a scale of 10, how much do you like the fruit?   "))
            print(self.preference)

#Objects 
#Once objrct is created, init func gets called itself
apple =Fruit("red","sweet","round","1")
#Object.func
apple.showFruit()
apple.get_shape()
apple.set_shape("oval")
apple.showFruit()
apple.user_input()
print()

orange=Fruit("orange","sour","cirlce","5")
orange.showFruit()
orange.get_shape()
orange.set_shape("oval")
orange.showFruit()
orange.user_input()
print()

banana=Fruit("yellow","sweet","crescent","6")
banana.showFruit()
banana.get_shape()
banana.set_shape("circle")
banana.showFruit()
banana.user_input()
print()



