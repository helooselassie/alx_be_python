# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Ensure the exact pattern is used

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Function to get valid temperature input
def get_temperature_input():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        return temperature
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Main function to handle user interaction
def main():
    try:
        # Get the temperature from the user
        temperature = get_temperature_input()

        # Ask the user for the unit of the temperature
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Convert the temperature based on the unit
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        print(e)

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
