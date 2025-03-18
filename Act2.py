class Cars:
    def __init__(self,color,brand,speed,preference):
        self.color=color
        self.brand=brand
        self.speed=speed
        self.prefrence=preference

    def show_car(self):
        print("Hi I am a {} {} with a top speed of {}km/h".format(self.color,self.brand,self.speed))

c1=Cars("red","Mercedes","450","5")
c1.show_car()