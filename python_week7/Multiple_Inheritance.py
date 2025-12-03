class Flyer:
  def fly(self):
    print("Flying...")

class Swimmer:
  def swim(self):
    print("Swimming...")

class Duck(Flyer, Swimmer):
  pass

duck = Duck()
duck.fly()  # Output: Flying...
duck.swim()  # Output: Swimming...