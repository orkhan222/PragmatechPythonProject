# Task04
def register():
    ad = input('Adnizi Daxil edin: ')
    while len(ad)< 3 < 11:
        print(f"Adniz 3 ve 11 arasi olmalidi:")
        ad = input('Adnizi Daxil edin: ')
    else:
        soyadin =input('Soyadinizi Daxil Edin: ')
        while len(soyadin)< 3 < 11:
            print(f"Soyaddininz 5 ve 15 arasi olmalidi:")
            soyadin = input('Soaynizi Daxil edin: ')
        else:
            dogum =input('Dogum Gunuz Daxil Edin: ')
            while len(dogum) !=4:
                print(f"Dogum Gunuz Daxil Edin: ")
                dogum = input('Dogum Gunuz Daxil Edin: ')
            else:
                email =input('Email Daxil Edin: ')
                while len(email)< 10< 22 or (("@gmail.com" not in email )):
                    if len(email)< 10 < 22:
                        print('Emaila daxil ol')
                    elif('@gmail.com' not in email):
                        print('Emaila  tezeden daxil olun')
                    print(f"Email Daxil Edin: ")
                    email = input('Email Daxil Edin: ')
                else:
                    password = input('Parol Daxil edin:  ')
                    password=password
    show= input('Regsiterin gostermesini isteysense yaz: ')


    if show.lower() == 'he':
        print(f"""ad: {ad}, soyad: {soyadin}, dogum: {2021-int(dogum)}, email: {email}""")

    else: 
        print(f"{ad} {soyadin}, good luck!")  

register()

# Task01
a=int(input('1-ci teref: '))
b=int(input('2-ci teref: '))
c=int(input('3-cu teref: '))

d=int(input('4-cu teref: '))
if a==b==c==d: 
    print(a**2)
else:
    print(sum(a))


# Task02
v=list(input('1-ci eded: '))
v=list(input('2-ci eded: '))
v=list(input('3-cu eded: '))
v=list(input('4-cu eded: '))

z = v[0]
for x in v:
    x > z
    z = x
print("en boyuk eded : ", x)

# Task05
m=0
list=[1,2,3,4,5,6,7,8,9]
[m := m + x for x in list]
print(m)

# Task06
list = [1 , 2 , 3 , 4 , 5]
i = list[0]
for x in list:
    if x < i:
        i = x
        
print('En kicik eded :', i)



# Task07
list =  ['abc', 'xyz', 'aba', '1221',]
a = 0
for x in list:
    if len(x) > 2 and  x[0] == x[-1]: 
        a += 1

print(a)

# Task03
meyveler = {'nar' , 'alma' , 'armud'}
j = input("meyve adi daxil edin :")
if j in meyveler:
    print('Duzdu')
else:
    print('Sehvdi')


# Task11
list = [1,2,3,4,5,6]
i = []
for x in list:
    if x % 2 == 1:
        i.append(x)
print(i)

# Task10
list =  ['abc', 'xyz', 'aba', '1221','4554']
o = 0
for x in list:
    if len(x) > 2 and  x[0] == x[-1]: 
        o += 1

print(o)