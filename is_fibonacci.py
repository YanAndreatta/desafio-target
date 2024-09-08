def is_fibonacci(n, a=0, b=1):
    if n == a:
        return True
    elif a > n:
        return False
    return is_fibonacci(n, b, a + b)

def fibonacci(value):
    if is_fibonacci(value):
        return f"{value} pertence à sequência de Fibonacci."
    else:
        return f"{value} não pertence à sequência de Fibonacci."

if __name__ == '__main__':
    num = int(input("Informe um número: "))
    print(fibonacci(num))

