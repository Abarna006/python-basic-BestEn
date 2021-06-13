#boot camp day2 (string practice)
print("30 days 30 hrs challenge")
print('30 days 30 hrs challenge')
#assigning strings to variable
Hrs = 'thirty'
print(Hrs)
#index using string
days = 'thirty days'
print(days[0])
#printing particular value from certain string
challenge = 'i will win'
print(challenge[7:10])
#printing length of the string
print(len(challenge))
#converting string to lower character
print(challenge.lower())
#string concatenation(joining two strings)
a = '30 days'
b = '30 hrs'
c = a+b
print(c)
#adding space during concatenation
a = '30 days'
b = '30 hrs'
c = a+ "" +b
print(c)
#case fold usage
text = 'thirty days and thirty hrs'
x = text.casefold()
print(x)
x = text.capitalize()
print(x)
x = text.isalpha()
print(x)
x = text.isalnum()
print(x)
