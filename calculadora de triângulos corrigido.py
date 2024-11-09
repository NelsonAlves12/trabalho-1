#autor: Alex Tavares
#data: 08.11.2024
#código: calculadora de triângulos

#Para garantir que o código funcione, é preciso que essas sentenças sejam respeitadas

#a + b > c
#a + c > b
#b + c > a



import math

def calcular_area_heron(a, b, c):
    """Calcula a área de um triângulo usando a fórmula de Heron.

    Args:
        a (float): Comprimento do lado a.
        b (float): Comprimento do lado b.
        c (float): Comprimento do lado c.

    Returns:
        float: Área do triângulo.

    Raises:
        ValueError: Se os lados não formarem um triângulo válido.
    """

    # Verifica se os lados formam um triângulo válido
    # A soma de quaisquer dois lados deve ser maior que o terceiro lado
    if a + b > c and a + c > b and b + c > a:
        # Se a condição for verdadeira, calculamos a área
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        raise ValueError("Os lados não formam um triângulo válido.")

def verificar_tipo_triangulo(a, b, c):
    """Verifica o tipo de triângulo.

    Args:
        a (float): Comprimento do lado a.
        b (float): Comprimento do lado b.
        c (float): Comprimento do lado c.

    Returns:
        str: Tipo do triângulo (equilátero, isósceles ou escaleno).
    """

    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or c == a:
        return "Isósceles"
    else:
        return "Escaleno"

# Entrada dos dados
while True:
    try:
        lado_a = float(input("Digite o valor do lado a: "))
        lado_b = float(input("Digite o valor do lado b: "))
        lado_c = float(input("Digite o valor do lado c: "))

        # Validação dos lados
        if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
            raise ValueError("Os lados do triângulo devem ser positivos.")

        # Cálculo da área e verificação do tipo
        area = calcular_area_heron(lado_a, lado_b, lado_c)
        tipo = verificar_tipo_triangulo(lado_a, lado_b, lado_c)

        print(f"A área do triângulo é: {area:.2f}")
        print(f"O triângulo é: {tipo}")
        break

    except ValueError as e:
        print(f"Erro: {e}")

