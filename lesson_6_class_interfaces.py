class Animal:
    fur_color = "Orange"

    def speak(self):
        raise NotImplementedError

    def eat(self):
        raise NotImplementedError

    def chase(self):
        raise NotImplementedError

class HouseCat(Animal):
    def speak(self):
        print("Meeooowww")

cat = HouseCat()
cat.speak()