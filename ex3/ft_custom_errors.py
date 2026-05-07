class GardenError(OSError):
    def __init__(self, message = "Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message = "Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message = "Unknown water error"):
        super().__init__(message)

#Functions that raise the custom errors
def cause_plant_error():
    raise PlantError("The tomato plant is wilting!")

def cause_water_error():
    raise WaterError("Not enough water in the tank!")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        cause_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        cause_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        cause_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        cause_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")