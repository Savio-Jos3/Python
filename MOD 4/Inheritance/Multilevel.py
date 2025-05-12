class Grandparent:
    def wealth(self):
        print("Has land")

class Parent(Grandparent):
    def job(self):
        print("Works in IT")

class Child(Parent):
    def hobby(self):
        print("Plays guitar")

c = Child()
c.wealth()
c.job()
c.hobby()
