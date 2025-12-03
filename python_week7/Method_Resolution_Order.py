class A:
    def greet(self):
        return "Hello from class A"

class B(A):
    def greet(self):
        return "Hello from class B"

class C(A):
    def greet(self):
        return "Hello from class C"

class D(B, C):
    pass

# Creating an instance of class D
obj_d = D()
obj_c = C()
a = A()
print(obj_d.greet())  # Output: "Hello from class B"
print(obj_c.greet())
print(a.greet())