def fibonacci_checker(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

def main():
    num = int(input("Digite um número para verificar se pertence a sequência de Fibonacci: "))
    if fibonacci_checker(num):
        print(f"{num} pertence a sequência de Fibonacci.")
    else:
        print(f"{num} não pertence a sequência de Fibonacci.")

if __name__ == "__main__":
    main()