
def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if (temp > 40):
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif (temp < 0):
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    tests = ["25", "abc", "100", "-50"]
    print()
    for data in tests:
        print(f"Input data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
        print()
    print("All tests completed- program didn't crash!")


if __name__ == "__main__":
    test_temperature()
