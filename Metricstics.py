from interface import IMetrics
import math
import random

class Metricstics(IMetrics):
    def __init__(self,data):
        try:
            self.random_numbers = []
            self.sorted_data_set = []
            self.session_data = {'data': self.data}
        except Exception as e:
            raise Exception(f"Error occurred while initializing METRICSTICS: {e}")

    def sort_data_set(self):
        self.sorted_data_set = sorted(self.random_numbers)

    def minimum(self):
        self.sort_data_set()
        return self.sorted_data_set[0]

    def maximum(self):
        self.sort_data_set()
        return self.sorted_data_set[-1]

    def mode(self):
        try:
            num_counts = {}
            for num in self.random_numbers:
                num_counts[num] = num_counts.get(num, 0) + 1
            max_freq = max(num_counts.values())
            all_mode = [key for key, value in num_counts.items() if value == max_freq]
            return all_mode
        except Exception as e:
            raise Exception(f"Error occurred while calculating mode: {e}")

    def median(self):
        try:
            self.sort_data_set()
            n = len(self.sorted_data_set)
            if n % 2 == 0:
                mid1 = self.sorted_data_set[n // 2 - 1]
                mid2 = self.sorted_data_set[n // 2]
                median = (mid1 + mid2) / 2
            else:
                median = self.sorted_data_set[n // 2]
            return round(median, 2)
        except Exception as e:
            raise Exception(f"Error occurred while calculating median: {e}")

    def mean(self):
        try:
            mean = sum(self.random_numbers) / len(self.random_numbers)
            return round(mean, 2)
        except ZeroDivisionError:
            raise Exception("Error: Cannot calculate mean for an empty dataset.")

    def mean_absolute_deviation(self):

        try:
            mean = self.mean()
            mad = sum(abs(num - mean) for num in self.random_numbers) / len(self.random_numbers)
            return round(mad, 2)
        except Exception as e:
            raise Exception(f"Error occurred while calculating MAD: {e}")

    def standard_deviation(self):
        try:
            mean = self.mean()
            variance = sum((num - mean) ** 2 for num in self.random_numbers) / len(self.random_numbers)
            standard_deviation = math.sqrt(variance)
            return round(standard_deviation, 2)
        except Exception as e:
            raise Exception(f"Error occurred while calculating standard deviation: {e}")

    #def load_from_random(self):
     #   for _ in range(1000):
      #      random_value = round(random.uniform(1, 1000), 2)
       #     self.random_numbers.append(random_value)
        #return ", ".join(map(str, self.random_numbers))

    def reset(self):
        self.random_numbers.clear()

    def get_generated_list(self):
        return self.random_numbers



