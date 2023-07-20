import qrcode
ruta = "C:/Users/adanz/OneDrive/Escritorio/examen/"
nombre = input("Ingresa tu nombre ")
edad = int(input("Ingresa tu edad "))
if(edad>=18):
    informacion = nombre+" eres mayor de edad, tiene"+ str(edad)+" años"
else:
    informacion = nombre+" eres menor de edad, tiene "+str(edad)+" años"
img = qrcode.make(informacion)
f = open(ruta+"miQR.png", "wb")
img.save(f)
f.close()