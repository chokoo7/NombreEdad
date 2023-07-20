from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
from datetime import date
from datetime import datetime
import qrcode 
#Dia actual
today = date.today()
#Fecha actual
now = datetime.now()
ruta = "C:/Users/adanz/OneDrive/Escritorio/examen/"
informacion = "Zamudio Ibarra Christofer Adan"
img = qrcode.make(informacion)
nombreImagen = ruta +"miQR.png"
f = open(nombreImagen, "wb")
img.save(f)
f.close()
#------FIN DE LA IMAGNE QR--------
c = canvas.Canvas(ruta+'PruebaPDF.pdf', pagesize=A5)

#TITULO
c.setFont('Helvetica-Bold', 13) #Tipo de letra y tamaño
c.drawString(90,550,"FARMACIAS DE SIMILARES SA DE CV ")
c.setFont('Helvetica', 8) 
c.drawString(97,538,"REGIMEN GENERAL DE LEY  PERSONAS MORALES ")
c.setFont('Helvetica', 8)
c.drawString(160,530,"DOMICILIO FISCAL")
c.setFont('Helvetica', 8)
c.drawString(100,520,"ALEMANIA No. 10 COL. INDEPENCIA ALCALDIA BENITO ")
c.setFont('Helvetica', 8)
c.drawString(100,510,"JUAREZ CP 03630 CIUDAD DE MEXICO, MEXICO RFC")
c.setFont('Helvetica', 8)
c.drawString(170,500,"FSI-970908-MIL5")
c.setFont('Helvetica', 8)
c.drawString(100,490,"DOMICILIO DEL ESTABLECIMIENTO, LUGAR  Y FECHA DE")
c.setFont('Helvetica', 8)
c.drawString(180,480,"EXPEDICION:")
c.setFont('Helvetica', 8)
c.drawString(150,470,"SUCURSAL: 452 PACHUCA 2")
c.setFont('Helvetica', 8)
c.drawString(100,460,"CLL. MORELOS 200, CENTRO. PACHUCA DE SOTO HIDALGO")
c.setFont('Helvetica', 8)
c.drawString(170,450,"MEXICO C.P. 42000")
c.setFont('Helvetica', 8)
c.drawString(150,440,"lunes, 17 jul. 2023 09:03:04 a.m")
c.setFont('Helvetica', 8)
c.drawString(80,430,"Caja: 1 CO Ticket: d62c8334-ba67-405e-a795-b57b63abd298")
c.setFont('Helvetica', 8)
c.drawString(80,420,"1547 CUBREBOCA TRIPLE PLI * BL   1 X      26.72     26.72")
c.setFont('Helvetica', 8)
c.drawString(80,410,"Codigos:  1")
c.setFont('Helvetica', 8)
c.drawString(80,400,"Pieazas a Entregar:  1")
c.setFont('Helvetica', 8)
c.drawString(80,390,"BL -  El Buen Lunes")
c.setFont('Helvetica', 8)
c.drawString(300,380,"Subtotal:                    26.72")
c.setFont('Helvetica-Bold', 11)
c.drawString(245,370,"Descuentos:           6.68")
c.setFont('Helvetica', 8)
c.drawString(290,360,"IVA AL 16 %:                    3.21")
c.setFont('Helvetica-Bold', 11)
c.drawString(170,350,"Total M.N:                                      23.25")
c.setFont('Helvetica', 8)
c.drawString(90,340,"(veintitres pesos 25/100 MN)")
c.setFont('Helvetica', 8)
c.drawString(200,330,"Pagos >> Efectivo:                        100.00")
c.setFont('Helvetica', 8)
c.drawString(250,320,"Cambio:                     76.75")
c.setFont('Helvetica', 8)
c.drawString(150,310,"Documento sin Efectos Fisicales")
c.setFont('Helvetica', 8)
c.drawString(90,300,"No se aceptan devoluciones en antibióticos, promociones.")
c.setFont('Helvetica', 8)
c.drawString(100,290,"cheques, transferencias y tickets facturados. Para pagos")
c.setFont('Helvetica', 8)
c.drawString(90,280,"con tarjeta la devolucion aplica el mismo día  y a la misma")
c.setFont('Helvetica', 8)
c.drawString(110,270,"tarjeta. En efectivo y CoDi dentro de los 4 días")
c.setFont('Helvetica', 8)
c.drawString(120,260,"posteriores y dentro del mismo mes calendario.")
c.setFont('Helvetica', 10)
c.drawString(70,250,"----------------------------------------------------------------------------------------------")
c.setFont('Helvetica', 8)
c.drawString(110,240,"Si requiere facture, favor de solicitar la al momento de efectuar")
c.setFont('Helvetica', 8)
c.drawString(170,230,"su compra en esta farmacia")
c.setFont('Helvetica', 8)
c.drawString(140,220,"Referencia de Facturación: 0045201367208")
c.setFont('Helvetica', 8)
c.drawString(180,210,"Facturación en línea")
c.setFont('Helvetica', 8)
c.drawString(170,200,"www.farmaciasdesimilares.com")
c.setFont('Helvetica', 8)
c.drawString(140,190,"Quejas y Sugerencias SIMITEL 800 911 6666")

h2 = 100
x2 = 100
y2 = h2 - 50
c.drawImage(nombreImagen,190,100,70,70)



'''c.setFont('Helvetica', 16) #Tipo de letra y tamaño
c.drawString(120,730,"Comprador: ")#Coordenadas y texto a mostrar
c.drawString(120,700,"Fecha: ")
c.setFont('Helvetica', 16)
c.drawString(230,730,"valor variable ")
c.drawString(180,700,str(now))
c.setFont('Helvetica-Bold', 20)

c.drawString(250,660,"Productos ")
h = 690
x = 100
y = h - 50
c.line(x,y, x + 380, y)

c.setFont('Helvetica-Bold', 16)
c.drawString(100,600,"Cantidad ")
c.drawString(200,600,"Nombre")
c.drawString(300,600,"PrecioUni ")
c.drawString(400,600,"Total ")

h2 = 640
x2 = 100
y2 = h2 - 50
c.line(x2,y2, x2 + 380, y2)
c.drawImage(nombreImagen,120,120,200,200)'''

c.save()