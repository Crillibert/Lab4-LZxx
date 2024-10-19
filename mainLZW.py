import LZW

nombre = input("Ingrese nombre del archivo txt a comprimir: \n")

LZW.codificacionLZW(nombre)

nombre = input("Ingrese nombre del archivo a descomprimir: \n")

LZW.decodificacionLZW(nombre)