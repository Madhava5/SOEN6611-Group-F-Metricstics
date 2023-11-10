from tkinter import messagebox

from interface import IMetrics
import math
import random


class Metricstics(IMetrics):
    # def __init__(self,data):
    #     try:
    #         self.random_numbers = []
    #         self.sorted_data_set = []
    #         self.session_data = {'data': self.data}
    #     except Exception as e:
    #         raise Exception(f"Error occurred while initializing METRICSTICS: {e}")

    # def sort_data_set(self):
    #     self.sorted_data_set = sorted(self.random_numbers)

    def __init__(self, data):
        try:
            self.data = sorted(data)
            self.session_data = {'data': self.data}
        except Exception as e:
            raise Exception(f"Error occurred while initializing Metricstics: {e}")

    def minimum(self):
        try:
            return min(self.data)
        except Exception as e:
            raise Exception(f"Error occurred while calculating minimum: {e}")

    def maximum(self):
        try:
            return max(self.data)
        except Exception as e:
            raise Exception(f"Error occurred while calculating maximum: {e}")

    def mode(self):
        try:
            num_counts = {}
            for num in self.data:
                num_counts[num] = num_counts.get(num, 0) + 1
            max_freq = max(num_counts.values())
            all_mode = [key for key, value in num_counts.items() if value == max_freq]
            return all_mode
        except Exception as e:
            raise Exception(f"Error occurred while calculating mode: {e}")

    def median(self):
        try:

            n = len(self.data)
            if n % 2 == 0:
                mid1 = self.data[n // 2 - 1]
                mid2 = self.data[n // 2]
                median = (mid1 + mid2) / 2
            else:
                median = self.data[n // 2]
            return round(median, 2)
        except Exception as e:
            raise Exception(f"Error occurred while calculating median: {e}")

    def mean(self):
        try:
            mean = sum(self.data) / len(self.data)
            return round(mean, 2)
        except ZeroDivisionError:
            raise Exception("Error: Cannot calculate mean for an empty dataset.")

    def mean_absolute_deviation(self):

        try:
            mean = self.mean()
            mad = sum(abs(num - mean) for num in self.data) / len(self.data)
            return round(mad, 2)
        except Exception as e:
            raise Exception(f"Error occurred while calculating mean_absolute_deviation: {e}")

    def standard_deviation(self):
        try:
            mean = self.mean()
            variance = sum((num - mean) ** 2 for num in self.data) / len(self.data)
            standard_deviation = math.sqrt(variance)
            return round(standard_deviation, 2)
        except Exception as e:
            raise Exception(f"Error occurred while calculating standard deviation: {e}")

    # def load_from_random(self):
    #   for _ in range(1000):
    #      random_value = round(random.uniform(1, 1000), 2)
    #     self.random_numbers.append(random_value)
    # return ", ".join(map(str, self.random_numbers))

    def reset(self):
        self.data.clear()

    def get_generated_list(self):
        return self.data

    def calculate_and_display(self, display, method):
        result = ""
        try:
            if method == "m":
                result = str(self.minimum())
            elif method == "M":
                result = str(self.maximum())
            elif method == "o":
                result = str(self.mode())
            elif method == "d":
                result = str(self.median())
            elif method == "μ":
                result = str(self.mean())
            elif method == "MAD":
                result = str(self.mean_absolute_deviation())
            elif method == "σ":
                result = str(float(self.standard_deviation()))

            display.config(text=result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calculate_all(self, all_displays):
        try:
            all_results = [
                self.minimum(),
                self.maximum(),
                self.mode(),
                self.median(),
                self.mean(),
                self.mean_absolute_deviation(),
                self.standard_deviation()
            ]

            for i, result in enumerate(all_results):
                all_displays[i].config(text=str(result))

        except Exception as e:
            messagebox.showerror("Error", str(e))
