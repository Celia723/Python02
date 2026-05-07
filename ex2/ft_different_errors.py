def garden_operations(operation_number):

    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
         x = 1 / 0
    elif (operation_number == 2):
        open("/hola.txt")
    elif (operation_number == 3):
        y = 'a' + 4
    else:
        return
        
def test_error_types():

    tests = [0, 1, 2, 3, 4]
    print ("=== Garden Error Types Demo ===")
    for i in tests:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except  ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except  FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except  TypeError as e:
            print(f"Caught TypeError: {e}")
    print("All error types tested successfully!")

    # Extra: catching multiple types in one try
    print("\nDemonstrating multi-error catch...")
    try:
        garden_operations(0)
    except (ValueError, TypeError) as e:
        print(f"Caught one of multiple errors: {e}")


if __name__ == "__main__":
    test_error_types()