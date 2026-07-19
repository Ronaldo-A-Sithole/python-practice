name=input("Enter your name: ")
#print(name)

#int
a=int(input("Enter the velue of a:"))
b=int(input("Enter the value of b:"))
c=(a**2+b**2)**0.5
#print(c)

#Currency game 
#We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. How much do you have in US dollars? Let's find out! We will convert the amount of money you have in Colombian Pesos, Peruvian Soles, and Brazilian Reais to US dollars.
#The current exchange rates are as follows:
colombian_peso_rate = 0.00024
peruvian_sole_rate = 0.28
brazilian_real_rate = 0.20

a=float(input("What do you have left in pesos?" ))
b=float(input('What do you have left in soles?' ))
c=float(input("What do you have left in reais?" ))
d=float(a/colombian_peso_rate + b/peruvian_sole_rate + c/brazilian_real_rate)
print(d)
