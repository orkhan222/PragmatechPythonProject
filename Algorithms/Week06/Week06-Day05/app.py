# Bir dənə Restoran classı yaradın. 
# Bu classa init() metdou bu classın adını (restaurant_name) və mətbəx növü (cuisine_type) adlı iki atribitunu saxlamalıdır. 
# describe_restaurant() adlı bir metod yaradın hansı ki restoranın adını və mətbəxin növünü ekrana print etsin. 
# Restoranın açıq olmasını mesaj verən open_restaurant() adlı başqa bit metdi yaradın. Sonra restoran adlı obyekt yaradın bu class-dan və restotanın adını,
#  mətbəxinin növünü, restoran haqqında məlumatları və açıq olmasını çapa verin. 
# Bu Restoran classından daha iki obyek yaradın və describe_restaurant metodunu yeni yaratdığınız hər iki obyekt üçün tətbiq edin.

class Restoran:
    def __init__(self, restaurant_name, cuisine_type):
        self.x = restaurant_name
        self.y = cuisine_type

    def describe_restaurant(self):
        print (self.x ,self.y)
    

    def open_restaurant(self):
        print(f"{self.x}-7/24 aciqdi.")
        

adi= Restoran('Plaza','Median')


adi.describe_restaurant()
adi.open_restaurant


# User adlı yeni class yaradın. first_name, last_name və age atributları verin bu class-a. describe_user metdou yaradın user haqqında məlumatları çapa vermək üçün. 
# greet_user adlı başqa bir metod yaradın hansı ki userin ad və soyadına salam verən bir mesaj ekrana yazdırsın.
#  Bir neçə obyekt yaradın bu User class-ndan və hər birinin atribut və metodlarını istifadə edin.

class User:
    def __init__(self,login_attempts):
        self.x = login_attempts


    def increment_login_attempts(self):
        return self.x + 1

    def reset_login_attempts(self):
        return 0
   

a = User(0)
print(a.increment_login_attempts())

b = User(1)
print(b.increment_login_attempts())


c = User(2)

    # def __init__(self, first_name,last_name,age ):
    #     self.x = first_name
    #     self.y = last_name
    #     self.a = age

    
    # def describe_user(self):
    #     print(self.x ,self.y,self.a)

    # def greet_user(self):
    #     print(f"{self.x} {self.y} Xos geliniz.")



a=User('Orkhan','Mustafayev',19)
a.describe_user()
a.greet_user()
print(c.increment_login_attempts())
print(c.reset_login_attempts())


# login_attempts adlı bir atribut verin User classına. increment_ login_attempts adlı metod yaradın hansı ki hər dəfə işə düşəndə login_attempts 1 vahid artırır.
#  reset_login_attempts adlı bir metod yaradın hansı ki login_attemptsləri sıfırlayır. 
#  Sonra bir user obyekti yaradın bu class-dan və increment_ login_attemptsi bir neçə dəfə istifadə etdikdən sonra userin neçə dəfə cəhd etdiyini çapa verin. 
# Daha sonra cəhdlərin sayını sıfırlayın və yenidən cəhdlərin sayını çapa verin.





class User:
    def __init__(self,login_attempts):
        self.x = login_attempts


    def increment_login_attempts(self):
        return self.x + 1

    def reset_login_attempts(self):
        return 0
   

a = User(0)
print(a.increment_login_attempts())










