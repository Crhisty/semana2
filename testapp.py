from app import suma, resta, multiplicacion, division, obtener_mensaje_bienvenida

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

def test_resta():
    assert resta(10, 5) == 5
    assert resta(5, 10) == -5

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(0, 10) == 0

def test_division():
    assert division(10, 2) == 5
    assert division(10, 0) == "Error: No se puede dividir por cero."

def test_mensaje_bienvenida():
    assert obtener_mensaje_bienvenida("Prueba") == "¡Hola, Prueba! Bienvenido a la aplicación."
    assert obtener_mensaje_bienvenida() == "¡Hola, Usuario! Bienvenido a la aplicación."

if __name__ == "__main__":
    test_suma()
    test_resta()
    test_multiplicacion()
    test_division()
    test_mensaje_bienvenida()
    print("¡Todas las pruebas pasaron correctamente!")
