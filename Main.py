from Metricstics import Metricstics
from interface import IRandom
import json


class SimpleRandom(IRandom):
    def __init__(self):
        self.seed_value = 12345678

    def generate(self):
        a = 1664525
        c = 1013904223
        m = 2 ** 32
        self.seed_value = (a * self.seed_value + c) % m
        return self.seed_value / m


def generate_test_data(random_generator, n=1000, low=0, high=1000):
    return [int(random_generator.generate() * (high - low) + low) for _ in range(n)]


def save_session(metrics, filename="session_data.json"):
    with open(filename, "w") as file:
        json.dump(metrics.session_data, file)
    print(f"Session data saved to {filename}")


def load_session(filename="session_data.json"):
    try:
        with open(filename, "r") as file:
            session_data = json.load(file)
            data = session_data
            print(data)
            metrics = Metricstics(data)
            print(f"Session data loaded from {filename}")
            return data
    except FileNotFoundError:
        print("Session data file not found.")
        return None
    except Exception as e:
        print(f"Error occurred while loading session data: {e}")
        return None


def menu(metrics):
    try:
        print("Select an Operation")
        print("1. Calculate Mean")
        print("2. Calculate Median")
        print("3. Calculate Mode")
        print("4. Calculate Standard Deviation")
        print("5. Calculate Mean Absolute deviation")
        print("6. Calculate Minimum")
        print("7. Calculate Maximum")
        print("8. Calculate All")

        choice = int(input())

        match choice:
            case 1:
                mean_value = metrics.mean()
                metrics.session_data['mean'] = mean_value
                print("Mean:", mean_value)
            case 2:
                median_value = metrics.median()
                metrics.session_data['median'] = median_value
                print("Median:", median_value)
            case 3:
                mode_value = metrics.mode()
                metrics.session_data['mode'] = mode_value
                print("Mode:", mode_value)
            case 4:
                std_deviation_value = metrics.standard_deviation()
                metrics.session_data['standard_deviation'] = std_deviation_value
                print("Standard Deviation:", std_deviation_value)
            case 5:
                mean_absolute_deviation_value = metrics.mean_absolute_deviation()
                metrics.session_data['mean_absolute_deviation'] = mean_absolute_deviation_value
                print("Mean_absolute_deviation:", mean_absolute_deviation_value)
            case 6:
                minimum_value = metrics.minimum()
                metrics.session_data['minimum'] = minimum_value
                print("Minimum:", minimum_value)
            case 7:
                maximum_value = metrics.maximum()
                metrics.session_data['maximum'] = maximum_value
                print("Minimum:", maximum_value)
            case 8:
                mean_value = metrics.mean()
                median_value = metrics.median()
                mode_value = metrics.mode()
                standard_deviation_value = metrics.standard_deviation()
                mean_absolute_deviation_value = metrics.mean_absolute_deviation()
                minimum_value = metrics.minimum()
                maximum_value = metrics.maximum()
                metrics.session_data['mean'] = mean_value
                metrics.session_data['median'] = median_value
                metrics.session_data['mode'] = mode_value
                metrics.session_data['standard_deviation'] = standard_deviation_value
                metrics.session_data['mean_absolute_deviation'] = mean_absolute_deviation_value
                metrics.session_data['minimum'] = minimum_value
                metrics.session_data['maximum'] = maximum_value
                print("Mean:", mean_value)
                print("Median:", median_value)
                print("Mode:", mode_value)
                print("Standard Deviation:", standard_deviation_value)
                print("Mean_absolute_deviation:", mean_absolute_deviation_value)
                print("Minimum:", minimum_value)
                print("Maximum:", maximum_value)
            case _:
                print("Wrong Input.")

    except Exception as e:
        print(f"Error occurred: {e}")

    try:
        print("Do you want to save this session data? (yes/no)")
        save_session_choice = input().lower()
        if save_session_choice == "yes":
            save_session(metrics)
    except Exception as e:
        print(f"Error occurred while saving session data: {e}")

def main():
    try:
        print("Do you want to load previous session data? (yes/no)")
        load_session_choice = input().lower()
        if load_session_choice == "yes":
            metrics_data = load_session()
            if (metrics_data is None):
                return
            metrics_data1 = metrics_data["data"]
            print(metrics_data)
            metrics = Metricstics(metrics_data1)
            menu(metrics)

        else:
            print("Please select how you want to input the data")
            print("1. Auto generate values")
            print("2. Input comma seperated data using command line")
            input_type = int(input())
            if (input_type == 1):
                random_generator = SimpleRandom()
                n = int(input("Enter the number of data values: "))
                test_data = generate_test_data(random_generator, n)
                print(test_data)
                metrics = Metricstics(test_data)
            elif (input_type == 2):
                input_list = [int(x) for x in input().split(',')]
                metrics = Metricstics(input_list)

            menu(metrics)

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()