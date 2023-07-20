# Importamos la libreria canvas del paquete reportlab
from reportlab.pdfgen import canvas
# abrimos el pdf
ruta = "C:/Users/adanz/OneDrive/Escritorio/examen/"
c = canvas.Canvas(ruta+'mypdf.pdf')
# Para titulos asignamos una fuente y el tamaño = 20
c.setFont('Helvetica', 20)
# Dibujamos texto: (X,Y,Texto)
c.drawString(25,800,"Crear PDF con Reportlab en Python!")
# Para parrafos normales cambiamos el tamaño a 12
c.setFont('Helvetica', 12)
# Dibujamos texto: (X,Y,Texto)
c.drawString(25,780,"Este es un ejemplo de parrafo en un PDF con la libreria reportlab y python!")
# Dibujamos una imagen (IMAGEN, X,Y, WIDTH, HEIGH)
#c.drawImage('image.jpg', 25, 480, 480, 270)
# Guardar
c.save()