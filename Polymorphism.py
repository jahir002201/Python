class Bird:
    def fly(self):
        return "Bird flies"

class Airplane:
    def fly(self):
        return "Airplane flies"

def make_it_fly(flyable):
    print(flyable.fly())

make_it_fly(Bird())     
make_it_fly(Airplane()) 
