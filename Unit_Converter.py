# Unit Converter - Complete Version
# Categories: Length, Temperature, Volume, Time

def length_conversion(value, from_unit, to_unit):
    # Base unit: meter
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "inch": 0.0254,
        "ft": 0.3048,
        "mile": 1609.34
    }
    return value * units[from_unit] / units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    # Convert from source to Celsius
    if from_unit == "C":
        c = value
    elif from_unit == "F":
        c = (value - 32) * 5 / 9
    elif from_unit == "K":
        c = value - 273.15
    # Convert Celsius to target
    if to_unit == "C":
        return c
    elif to_unit == "F":
        return c * 9 / 5 + 32
    elif to_unit == "K":
        return c + 273.15

def volume_conversion(value, from_unit, to_unit):
    # Base unit: liter
    units = {
        "L": 1,
        "mL": 0.001,
        "m3": 1000,
        "cm3": 0.001,
        "cc": 0.001
    }
    return value * units[from_unit] / units[to_unit]

def time_conversion(value, from_unit, to_unit):
    # Base unit: second
    units = {
        "ms": 0.001,
        "s": 1,
        "min": 60,
        "h": 3600,
        "day": 86400,
        "week": 604800,
        "year": 31536000
    }
    return value * units[from_unit] / units[to_unit]

def select_unit(units_dict):
    for i, unit in enumerate(units_dict.keys(), 1):
        print(f"{i}- {unit}")
    while True:
        try:
            choice = int(input("Select unit (number): "))
            if 1 <= choice <= len(units_dict):
                return list(units_dict.keys())[choice-1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

def main():
    print("🎉 Welcome to Unit Converter! 🎉\n")
    
    categories = {
        "1": ("Length", length_conversion, {"mm":0,"cm":0,"m":0,"km":0,"inch":0,"ft":0,"mile":0}),
        "2": ("Temperature", temperature_conversion, {"C":0,"F":0,"K":0}),
        "3": ("Volume", volume_conversion, {"L":0,"mL":0,"m3":0,"cm3":0,"cc":0}),
        "4": ("Time", time_conversion, {"ms":0,"s":0,"min":0,"h":0,"day":0,"week":0,"year":0})
    }

    while True:
        print("Categories:")
        for k, v in categories.items():
            print(f"{k}- {v[0]}")
        
        cat_choice = input("Select category (1-4): ")
        if cat_choice not in categories:
            print("Invalid category. Try again.\n")
            continue
        
        category_name, func, units_dict = categories[cat_choice]
        
        try:
            value = float(input("Enter the value to convert: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue
        
        print("\nAvailable units:")
        from_unit = select_unit(units_dict)
        to_unit = select_unit(units_dict)
        
        result = func(value, from_unit, to_unit)
        print(f"\n✅ {value} {from_unit} = {result} {to_unit}\n")
        
        again = input("Do you want to convert again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for using Unit Converter! Goodbye!")
            break

if __name__ == "__main__":
    main()
