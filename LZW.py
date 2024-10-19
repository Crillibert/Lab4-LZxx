
import sys
import struct

class LZW():
    def __init__(self, mensaje):
        self.mensaje


def codificacionLZW(nombre):
    string = ""
    n = input("Bits: \n")
    resultados = []
    tablaMax = pow(2, int(n))
    lenTabla = 256
    tabla = {chr(i): i for i in range(lenTabla)}
    with open(nombre, 'r') as log:
        dato = log.read()
        dato.strip()
        
        for simbolo in dato:
            simString = string + simbolo
            if simString in tabla:
                string = simString
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
    

    for m in resultados:
        outfile.write(struct.pack('>H', int(m)))

    #bitlength = outfile.read()
    #bitsC = len(bitlength)
    #ratioDC = (1 - bitsC/bitsO)*100
    #print("Ratio de compresion: \n")
    #print (str(ratioDC))

    outfile.close()

def decodificacionLZW(nombre):
    

    archivo = open(nombre, 'rb')
    string = ""
    bytesDec = []
    n = input("Bits: \n")
    continuidad = True
    while continuidad:
        m = archivo.read(2)
        if len(m) != 2:
            break
        (dec, ) = struct.unpack('>H', m)
        bytesDec.append(dec)

    tablaMax = pow(2, int(n))
    siguiente = 256
    lenTabla = 256

    mensajeDecod = ""
    tabla = {i:chr(i) for i in range(lenTabla)}

    for codigoIdx, codigo in enumerate(bytesDec):
        if codigoIdx == 0:
            string = tabla[codigo]
            mensajeDecod = mensajeDecod+string

        else:
            if codigo not in tabla:
                stringNuvou = string + (string[0])

            else:
                stringNuvou = tabla[codigo]

            mensajeDecod = mensajeDecod + stringNuvou
            if (len(tabla) <= lenTabla):
                tabla[siguiente] = string + (stringNuvou[0])
                siguiente += 1
            string = stringNuvou

        output = nombre.split(".")
        outfile = open(output[0] + "_Decodificado.txt", 'w')

        for m in mensajeDecod:
            outfile.write(m)

        outfile.close()