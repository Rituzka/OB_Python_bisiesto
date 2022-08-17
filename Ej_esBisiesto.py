Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def isBisiesto(year):
    if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
        return("El año es bisiesto")
    else: return("El año no es bisiesto")

    
print(isBisiesto(1968))
El año es bisiesto
