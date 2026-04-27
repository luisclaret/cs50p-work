def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction=fraction)
            print(gauge(percentage=percentage))
            break
        except ValueError:
            print("Error: Ingresa un formato válido (x/y)")
        except ZeroDivisionError:
            print("Error: No puedes dividir entre cero")


def convert(fraction):
    fraction_numbers = fraction.strip().split("/")
    try:
        x = int(fraction_numbers[0])
        y = int(fraction_numbers[1])
    except ValueError:
        raise ValueError("Error al convertir a entero!")
    except IndexError:
        raise ValueError("El string no es del tipo x/y")

    # Esta parte SÍ va afuera del try-except
    if y == 0:
        raise ZeroDivisionError("Error al dividir por cero!")
    if x > y or x < 0 or y < 0:
        raise ValueError("Valores inconsistentes")

    division = int((x / y) * 100)
    return division


def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
