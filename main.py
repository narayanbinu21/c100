class Car (object):
    def __init__(self,model,color,speedlimit,company):
        self.color = color
        self.model = model
        self.speedlimit = speedlimit
        self.company = company
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelarate(self):
        print("accelerated")
    def change_gear(self,gear_type):
        print("gearchanged")
audi = Car("a6","white",40,"audi")
print(audi.change_gear())

