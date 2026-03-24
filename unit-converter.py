import sys

# Factors to convert each unit to meters (base unit)
CONVERSION_TO_METERS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "in": 0.0254,
    "ft": 0.3048
}

def get_float(prompt: str) -> float:
    """Helper to ensure valid float input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid numeric value.")
        except (KeyboardInterrupt, EOFError):
            print("\nOperation cancelled.")
            sys.exit(0)

def calculate_sq_ft():
    print("\n--- Square Foot Calculator ---")
    width = get_float("Enter the width: ")
    length = get_float("Enter the length: ")
    print(f"Result: {width * length:.2f} sq.ft")

def convert_units():
    print("\n--- Unit Converter ---")
    value = get_float("Enter the value: ")
    input_unit = input("Enter the input unit (mm, cm, m, in, ft): ").lower().strip()
    output_unit = input("Enter the output unit (mm, cm, m, in, ft): ").lower().strip()

    if input_unit not in CONVERSION_TO_METERS or output_unit not in CONVERSION_TO_METERS:
        print("Error: Invalid unit specified.")
        return

    # Convert to base unit (meters), then to output unit
    value_in_meters = value * CONVERSION_TO_METERS[input_unit]
    result = value_in_meters / CONVERSION_TO_METERS[output_unit]
    
    print(f"Result: {result:.4f} {output_unit}")

def main():
    print("=== Multi-Tool unit-converter ===")
    while True:
        print("\nOptions:")
        print("1. Unit Converter")
        print("2. Square Foot Calculator")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            convert_units()
        elif choice == '2':
            calculate_sq_ft()
        elif choice == '3':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nOperation cancelled.")
        sys.exit(0)
