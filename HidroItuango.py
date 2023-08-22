NivelAgua =int(input("Cual es el nivel de agua: "))

#Evaluando multiples condiciones 
if NivelAgua > 0 and NivelAgua <=200:
    print(f"El nivel de agua es : {NivelAgua}, Esta muy bajo")
elif NivelAgua >200 and NivelAgua <= 400:
    print(f"El nivel de agua es : {NivelAgua}, Estamos operando con normalidad")
elif NivelAgua > 400:
    print(f"El nivel de agua es : {NivelAgua}, Inicie plan de evacuación")
else:
    print("Porfavor revise el sensor de agua, Nivel no valido")