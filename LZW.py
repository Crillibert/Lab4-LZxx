
import sys
import struct

class LZW():
    def __init__(self, mensaje):
        self.mensaje


def codificacionLZW(nombre):
    string = ""
    n, Input = sys.argv[1:]
    resultados = []
    tablaMax = pow(2, int(n))
    lenTabla = 256
    tabla = {chr(i): i for i in range(lenTabla)}
    with open(nombre, 'r') as log:
        log.strip()
        dato = log.read()
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
    output = Input.split(".")
    outfile = open(output[0] + ".lzw", "wb")

    for m in resultados:
        outfile.write(struct.pack('>H', int(m)))

    outfile.close()