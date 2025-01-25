#function to convert temperature from celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32
#function to convert temperature from fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
#function to convert temperature from celsius to kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273
#function to convert temperature from kelvin to celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273
#function to get input from user and display the converted temperature
def get_input_and_display():
    while(1):
        print("What conversion would you like to do?")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Quit")
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            celsius = float(input("Enter the temperature in Celsius: "))
            print("Temperature in Fahrenheit: ", celsius_to_fahrenheit(celsius))
            print()
        elif choice == 2:
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            print("Temperature in Celsius: ", fahrenheit_to_celsius(fahrenheit))
            print()
        elif choice == 3:
            celsius = float(input("Enter the temperature in Celsius: "))
            print("Temperature in Kelvin: ", celsius_to_kelvin(celsius))
            print()
        elif choice == 4:
            kelvin = float(input("Enter the temperature in Kelvin: "))
            print("Temperature in Celsius: ", kelvin_to_celsius(kelvin))
            print()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")
            print()
#main function
def main():
    get_input_and_display()
main()


