def inverter_string(s):
    chars = list(s)
    inicio = 0
    fim = len(chars) - 1
    while inicio < fim:
        chars[inicio], chars[fim] = chars[fim], chars[inicio]
        inicio += 1
        fim -= 1
    return ''.join(chars)

def main():
    texto = input("insira uma string para inverter: ")
    texto_invertido = inverter_string(texto)
    print(f"string invertida: {texto_invertido}")

if __name__ == "__main__":
    main()