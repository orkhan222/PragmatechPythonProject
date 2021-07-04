import random

istifadeci_1=input('Birinci oyuncu daxil etsin: ')
istifadeci_2=input('Ikinci oyuncu daxil etsin: ')


xal_1=0
xal_2=0
umumi_xal=1
i=0

while(i<5):
    number=random.randint(1,5)
    print('Reqemi tapin ')
    print('-----------------------')
    while(True):
        istifadeci_1_eded=int(input(f'{istifadeci_1} Her hansisa bir reqemi daxil edin: '))
        if istifadeci_1_eded == number:
            xal_1 += umumi_xal
        break

    while(True):
        istifadeci_2_eded=int(input(f'{istifadeci_2} Her hansisa bir reqemi daxil edin: '))
        if istifadeci_2_eded == number:
            xal_2 += umumi_xal

        break


print(istifadeci_1, "- Total",  xal_1, "xaliniz var")
print(istifadeci_2, "- Total",  xal_2, "xaliniz var")
if xal_1 > xal_2:
    print(istifadeci_1, "-- Siz udunuz---")
elif xal_1 < xal_2:
    print(istifadeci_2, "-- Siz ududunuz---")

else:
    print('Hec hec qaldiniz')