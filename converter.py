def convert_string_to_hex_and_ascii(input_string: str) -> dict:
    """
    Переводит строку в шестнадцатеричное представление и затем в ASCII.

    :param input_string: Исходная строка
    :return: Словарь с шестнадцатеричным и ASCII представлением
    """
    hex_representation = input_string.encode('utf-8').hex()
    ascii_representation = ''.join(chr(int(hex_representation[i:i+2], 16)) for i in range(0, len(hex_representation), 2))
    return {
        "hex": hex_representation,
        "ascii": ascii_representation
    }

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Перевести строку в шестнадцатеричное и ASCII представление")
        print("2. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            input_string = input("Введите строку: ")
            result = convert_string_to_hex_and_ascii(input_string)
            print(f"Шестнадцатеричное представление: {result['hex']}")
            print(f"ASCII представление: {result['ascii']}")

        elif choice == "2":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
