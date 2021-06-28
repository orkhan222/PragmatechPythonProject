from abc import ABC, abstractmethod


class Books(ABC):

    @abstractmethod
    def roman(self):
        pass


class Kitab(Books):

    # overriding abstract method
    def roman(self):
        print("Dedektiv kitab")


class Macəra (Books):

    def roman(self):
        print("Macəra kitabi")


class Elmi(Books):

    def roman(self):
        print("Elmi kitab")


class Dini(Books):

    def roman(self):
        print("Dini kitab")


R = Kitab()
R.roman()

K = Macəra()
K.roman()

R = Elmi()
R.roman()

K = Dini()
K.roman()

# Abstrakt dərslərdən nə vaxt istifadə edecik?

# -Kodu bir-birinə yaxın olan bir neçə sinif arasında bölüşmək üçün mücərrəd dərslərdən istifadə edirik.

# -Proyekte baslayandan ,evvel saytda bu hisseler olmalidi deyerek plan qururuq,
# abstrakt bu zaman hemin planlari unudanda bize xatirladir(remind).

# -Abstrakt siniflər, nümunə qura bilməyəcəyiniz siniflərdir. Yeni obyekt acmaq olmmur Abstrakt-dan.
# -Abstrakt sinifləri təyin etmək üçün abc modulundan istifadə edirik.





class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def display(self):
        return (self.name)

    def getAge(self):
        return (self.__age)

    def setAge(self, age):
        self.__age = age

    


person = Person('Dev', 30)

print(person.display())

person.setAge(35)
print(person.getAge())


# Tətbiqlər etibarlı şəkildə saxlanıla bilər.
# Kodun oxunaqlılığını artırır. Kodun bir hissəsindəki dəyişikliklər digərini narahat etməyəcəkdir.
# Kapsulasiya məlumatların qorunmasını təmin edir və təsadüfən məlumatların əldə edilməsinin qarşısını alır.