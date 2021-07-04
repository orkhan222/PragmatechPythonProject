# # inheritance ve polimorfizmi tetbiq etmek ucun iki dene class yaradin, 
# # attribut ve metodlari inheritance numune getirin.


class Computer:
    def introduction(self):
        print("Computerin novleri:")

    def acer(self):
        print("Bezi computer novler meslen acer")

class HP(Computer):
    def acer(self):
        print("Acer hp-de yoxdu")

class Macbook(Computer):
    def acer(self):
        print("Acer Macbookdadi.")


value1 = Computer()
value2 = HP()
value3 = Macbook()

value1.introduction()
value1.acer()

value2.introduction()
value2.acer()


value3.introduction()
value3.acer()





# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'


print(Pizza(['cheese', 'tomatoes']))



import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


p = Pizza(4, ['mozzarella', 'tomatoes'])

p.area()
Pizza.circle_area(4)


class B:
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f'B ({self.a})'

    def __str__(self):
        return f'B with {self.a}'

    def __bytes__(self):
        return self.a.to_bytes(4, byteorder='big')

    def __format__(self, spec):
        if spec == 'f':
            return str(self.a)
        return str(self)

b = B(10)
print(repr(b))
print(str(b))
print(bytes(b))
print(format(b, 'f'))



class C:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __hash__(self):
        return hash(self.age)

    def __bool__(self):
        return self.age > 0

alice = C(15)
bob = C(30)
rel = 'younger' if alice < bob else 'older'
print(f'Alice is {rel} than Bob')
print(hash(alice))



class D:
    '''A class that contains a value and implements an access counter.
    The counter increments each time the value is changed.'''
    def __init__(self, val):
        super().__setattr__('counter', 0)
        super().__setattr__('value', val)

    def __setattr__(self, name, value):
        if name == 'value':
            super().__setattr__('counter', self.counter + 1)
        super().__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super().__setattr__('counter', self.counter + 1)
        super().__delattr__(name)

d = D(10)
print(d.value, d.counter)
d.value = 11
print(d.value, d.counter)




class Celsius:
    '''Descriptor for celsius value.'''
    def __init__(self, value=0.0):
        self.value = float(value)
    
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    '''Descriptor for farenheit value.'''
    def __get__(self, instance, owner):
        return (instance.celsius * 9 / 5) + 32.0

    def __set__(self, instance, value):
        instance.celsius = (value - 32) * 5 / 9


class Temperature:
    celsius = Celsius()
    fahrenheit = Fahrenheit()

e = Temperature()
e.celsius = 10
print(f'{e.celsius} ºC = {e.fahrenheit} ºF')
e.fahrenheit = 45
print(f'{e.celsius} ºC = {e.fahrenheit} ºF')




class FunctionalList:
    '''A class wrapping a list with some extra functional magic'''
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def head(self, n):
        return self.values[:n]

    def tail(self, n):
        return self.values[n:]

    def first(self):
        return self.values[0]

    def last(self):
        return self.values[-1]
 
a = FunctionalList([1, 2, 3, 4])
print(a.head(2))
print(a[0])



class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def __add__(self, other):
        total = self.balance
        if isinstance(other, Account):
            total += other.balance
        else:
            total += other
        return Account(total)

    def __radd__(self, other):
        total = self.balance + other
        return Account(total)

    def __iadd__(self, other):
        total = self.__add__(other)
        self.balance = total.balance
        return self

    def __str__(self):
        return f'Balance: {self.balance}' 

a = Account(5)
b = Account(10)
c = a + b
b += 10
a = 5 + b
print(a)
print(b)
print(c)



class H:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.fp = open(self.name)
        return self.fp

    def __exit__(self, exc, exc_value, traceback):
        print(f'Exception: {exc_value}')
        self.fp.close()
        self.fp = None


h = H('test.txt')
with h as v:
    print(v.read())






  