def suma(a, b):
    """Calcula la suma de dos números."""
    return a + b

def resta(a, b):
    """Calcula la resta de dos números."""
    return a - b

def multiplicacion(a, b):
    """Calcula la multiplicación de dos números."""
    return a * b

def division(a, b):
    """Calcula la división de dos números, manejando la división por cero."""
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def obtener_mensaje_bienvenida(nombre="Usuario"):
    """Retorna un mensaje de bienvenida personalizado."""
    return f"¡Hola, {nombre}! Bienvenido a la aplicación."

if __name__ == "__main__":
    print(obtener_mensaje_bienvenida("DevOps Team"))
    
    a, b = 10, 5
    
    print(f"Resultado Suma ({a} + {b}): {suma(a, b)}")
    print(f"Resultado Resta ({a} - {b}): {resta(a, b)}")
    print(f"Resultado Multiplicación ({a} * {b}): {multiplicacion(a, b)}")
    print(f"Resultado División ({a} / {b}): {division(a, b)}")