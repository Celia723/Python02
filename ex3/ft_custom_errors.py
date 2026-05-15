class GardenError(OSError):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


# Functions that raise the custom errors
def cause_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def cause_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        cause_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        cause_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        cause_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        cause_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
