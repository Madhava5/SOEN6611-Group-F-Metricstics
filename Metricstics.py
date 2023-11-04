import math
import random

class Metricstics:
    def __init__(self):
        self.random_numbers = []
        self.sorted_data_set = []

    def sort_data_set(self):
        self.sorted_data_set = sorted(self.random_numbers)

    def minimum(self):
        self.sort_data_set()
        return self.sorted_data_set[0]

    def maximum(self):
        self.sort_data_set()
        return self.sorted_data_set[-1]

    def mode(self):
        num_counts = {}
        for num in self.random_numbers:
            num_counts[num] = num_counts.get(num, 0) + 1
        max_freq = max(num_counts.values())
        all_mode = [key for key, value in num_counts.items() if value == max_freq]
        return all_mode

    def median(self):
        self.sort_data_set()
        n = len(self.sorted_data_set)
        if n % 2 == 0:
            mid1 = self.sorted_data_set[n // 2 - 1]
            mid2 = self.sorted_data_set[n // 2]
            median = (mid1 + mid2) / 2
        else:
            median = self.sorted_data_set[n // 2]
        return round(median, 2)

    def arithmetic_mean(self):
        mean = sum(self.random_numbers) / len(self.random_numbers)
        return round(mean, 2)

    def mean_absolute_deviation(self):
        mean = self.arithmetic_mean()
        mad = sum(abs(num - mean) for num in self.random_numbers) / len(self.random_numbers)
        return round(mad, 2)

    def standard_deviation(self):
        mean = self.arithmetic_mean()
        variance = sum((num - mean) ** 2 for num in self.random_numbers) / len(self.random_numbers)
        standard_deviation = math.sqrt(variance)
        return round(standard_deviation, 2)

    def load_from_random(self):
        for _ in range(1000):
            random_value = round(random.uniform(1, 1000), 2)
            self.random_numbers.append(random_value)
        return ", ".join(map(str, self.random_numbers))

    def reset(self):
        self.random_numbers.clear()

    def get_generated_list(self):
        return self.random_numbers


if __name__ == "__main__":
    operations = Metricstics()

    # Load data from random numbers
    print("Generated Random Numbers: ", operations.load_from_random())

    # Calculate and display statistics
    print("Minimum:", operations.minimum())
    print("Maximum:", operations.maximum())
    print("Mode:", operations.mode())
    print("Median:", operations.median())
    print("Mean:", operations.arithmetic_mean())
    print("Mean Absolute Deviation:", operations.mean_absolute_deviation())
    print("Standard Deviation:", operations.standard_deviation())

    # Reset the data
    operations.reset()
    print("Data Reset. Generated List:", operations.get_generated_list())
