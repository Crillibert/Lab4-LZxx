
import sys
import struct

class LZW():
    def __init__(self, mensaje):
        self.mensaje


def codificacionLZW(nombre):
    string = ""
    #Se establecen los datos que vamos a utilizar
    n = input("Bits: \n")
    resultados = []
    tablaMax = pow(2, int(n))
    lenTabla = 256
    #Se crea la tabla de valores ascii
    tabla = {chr(i): i for i in range(lenTabla)}
    #Se lee el archivo
    with open(nombre, 'r') as log:
        dato = log.read()
        dato.strip()
        #por cada simbolo se revisa si esta en la tabla ascii
        #y se va agregando al string que vamos revisando
        for simbolo in dato:
            simString = string + simbolo
            if simString in tabla:
                string = simString
            #Si no esta ese segmento se agrega a la lista
            else:
                resultados.append(tabla[string])
                if (len(tabla) <= tablaMax):
                    tabla[simString] = lenTabla
                    lenTabla += 1
                string = simbolo
    resultados.append(tabla[string])
    output = nombre.split(".")
    outfile = open(output[0] + ".lzw", "wb")
    bitsO = len(dato)*8
    mesFin = ""
    print("Mensaje codificado: \n")
    #Se colocan los datos en binario en el archivo de salida
    for m in resultados:
        outfile.write(struct.pack('>H', int(m)))
        mesFin = mesFin + str(bin(m)[2:])
    print(mesFin)
    print('\n')
    bitsC = len(mesFin)
    ratioDC = (1 - bitsC/bitsO)*100
    print("Ratio de compresion: ")
    print (str(ratioDC))

    outfile.close()

def decodificacionLZW(nombre):
    
    #Se establecen las variables
    archivo = open(nombre, 'rb')
    string = ""
    bytesDec = []
    n = input("Bits: \n")

    continuidad = True
    #Se leen dos bytes del archivo
    while continuidad:
        m = archivo.read(2)
        if len(m) != 2:
            break
        #convertimos los binario a decimal
        (dec, ) = struct.unpack('>H', m)
        #actualizamos la lista despues de convertir a decimal
        bytesDec.append(dec)

    tablaMax = pow(2, int(n))
    siguiente = 256
    lenTabla = 256

    mensajeDecod = ""
    tabla = {i:chr(i) for i in range(lenTabla)}
    #Revisamos el bit en el que estamos
    for codigoIdx, codigo in enumerate(bytesDec):
        if codigoIdx == 0:
            string = tabla[codigo]
            mensajeDecod = mensajeDecod+string

        else:
            #Si el codigo no existe en la tabla
            if codigo not in tabla:
                #El string nuevo se le suma el string viejo y su primer caracter
                stringNuvou = string + (string[0])

            else:
                #Solo se cambia el caracter del string al codigo encontrado
                stringNuvou = tabla[codigo]
            #Se adiciona al mensaje de salida lo encontrado
            mensajeDecod = mensajeDecod + stringNuvou
            #Si se sobrepasa la tabla es menor al maximo, se agrega el string encontrado
            if (len(tabla) <= tablaMax):
                tabla[siguiente] = string + (stringNuvou[0])
                siguiente += 1
            string = stringNuvou

        output = nombre.split(".")
        outfile = open(output[0] + "_Decodificado.txt", 'w')
        salida = ""
    for m in mensajeDecod:
        outfile.write(m)
        salida = salida + m
    print("Mensaje decodificado: \n")
    print(salida)
    outfile.close()