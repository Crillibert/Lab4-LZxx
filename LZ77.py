class LZ77:
    def __init__(self, window_size=20, buffer_size=15):
        self.window_size = window_size
        self.buffer_size = buffer_size

    def compress(self, data):
        i = 0
        compressed_data = []

        while i < len(data):
            match_length = 0
            match_distance = 0
            search_start = max(0, i - self.window_size)

            # Buscar la coincidencia más larga en el diccionario (window)
            for j in range(search_start, i):
                length = 0
                while (length < self.buffer_size and
                       i + length < len(data) and
                       data[j + length] == data[i + length]):
                    length += 1

                if length > match_length:
                    match_length = length
                    match_distance = i - j

            if i + match_length < len(data):
                next_char = data[i + match_length]
            else:
                next_char = ''

            compressed_data.append((match_distance, match_length, next_char))
            i += match_length + 1 if match_length > 0 else 1

        return compressed_data

    def decompress(self, compressed_data):
        decompressed_data = []

        for distance, length, next_char in compressed_data:
            if distance > 0:
                start = len(decompressed_data) - distance
                for _ in range(length):
                    decompressed_data.append(decompressed_data[start])
                    start += 1
            if next_char:
                decompressed_data.append(next_char)

        return ''.join(decompressed_data)

if(__name__ == "__main__"):
    # Ejemplo de uso
    lz77 = LZ77()
    data = "NuevaPruebaParaElIngeBustamanteDeEstructurasDos"

    compressed = lz77.compress(data)
    print("Comprimido:", compressed)

    decompressed = lz77.decompress(compressed)
    print("Descomprimido:", decompressed)

    with open("PRUEBA_LZ77.txt" , 'w') as file:
        file.write("Comprimido: ")
        for code in compressed:
            file.write(str(code[0]) + str(code[1]) + str(code[2]) + ", ")
        file.write("\n")
        file.write("Descomprimido: " + decompressed)
        


