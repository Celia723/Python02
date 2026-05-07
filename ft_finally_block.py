class GardenError(OSError):
    def __init__(self, message = "Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message = "Unknown plant error"):
        super().__init__(message)

def water_plant(plant_name):
    if (plant_name == plant_name.capitalize()):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: {plant_name}")

def test_watering_system():
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    print("Opening watering system")
    plants = ["Tomato", "Lettuce", "Carrots"]
    try:
        for i in plants:
            water_plant(i)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")  

    print()
    print("Opening watering system")
    print("Testing invalid plants...")
    plants = ["Tomato", "lettuce", "Carrots"]
    try:
        for i in plants:
            water_plant(i)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    print()
    print("Cleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()