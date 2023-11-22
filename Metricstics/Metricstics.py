from tkinter import messagebox
import math
import random

class Metricstics:
    def __init__(self, data=None):
        try:
            if data is not None:
                self.data = sorted(data)
            else:
                self.data = []
                self.load_from_random()
                self.sort_data_set()  # Sort the generated numbers
            self.session_data = {'data': self.data}
        except (TypeError, ValueError) as e:
            raise Exception(f"Error occurred while initializing Metricstics: {e}")

    def minimum(self):
        try:
            if not self.data:
                raise ValueError("Cannot calculate minimum for an empty dataset.")
            return min(self.data)
        except Exception as e:
            raise Exception(f"Error occurred while calculating minimum: {e}")

    def maximum(self):
        try:
            if not self.data:
                raise ValueError("Cannot calculate maximum for an empty dataset.")
            return max(self.data)
        except Exception as e:
            raise Exception(f"Error occurred while calculating maximum: {e}")

    def get_all_repeated_values(self):
        try:
            if not self.data:
                raise ValueError("Cannot find repeated values for an empty dataset.")

            num_counts = {}
            repeated_values = []

            for num in self.data:
                num_counts[num] = num_counts.get(num, 0) + 1

            for key, value in num_counts.items():
                if value > 1:
                    for i in range(value):
                        repeated_values.append(key)

            return repeated_values
        except Exception as e:
            raise Exception(f"Error occurred while getting repeated values: {e}")

    def mode(self):
        try:
            if not self.data:
                raise ValueError("Cannot calculate mode for an empty dataset.")

            num_counts = {}
            for num in self.data:
                num_counts[num] = num_counts.get(num, 0) + 1

            max_freq = max(num_counts.values())

            # Check if there are no repeated values
            if max_freq == 1:
                return 0

            all_mode = [key for key, value in num_counts.items() if value == max_freq]
            return all_mode
        except Exception as e:
            raise Exception(f"Error occurred while calculating mode: {e}")

    def median(self):
        try:
            if not self.data:
                raise ValueError("Cannot calculate median for an empty dataset.")

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
            if not self.data:
                raise ValueError("Cannot calculate mean for an empty dataset.")

            mean = sum(self.data) / len(self.data)
            return round(mean, 2)
        except ZeroDivisionError:
            raise Exception("Error: Cannot calculate mean for an empty dataset.")
        except Exception as e:
            raise Exception(f"Error occurred while calculating mean: {e}")

    def mean_absolute_deviation(self):
        try:
            if not self.data:
                raise ValueError("Cannot calculate mean absolute deviation for an empty dataset.")

            mean = self.mean()
            mad = sum(abs(num - mean) for num in self.data) / len(self.data)
            return round(mad, 2)
        except Exception as e:
            raise Exception(f"Error occurred while calculating mean_absolute_deviation: {e}")

    def standard_deviation(self):
        try:
            if not self.data:
                raise ValueError("Cannot calculate standard deviation for an empty dataset.")

            mean = self.mean()
            variance = sum((num - mean) ** 2 for num in self.data) / len(self.data)
            standard_deviation = math.sqrt(variance)
            return round(standard_deviation, 2)
        except Exception as e:
            raise Exception(f"Error occurred while calculating standard deviation: {e}")

    def load_from_random(self):
        try:
            self.data = [round(random.uniform(1, 1000), 2) for _ in range(1000)]
        except Exception as e:
            raise Exception(f"Error occurred while loading data from random: {e}")

    def reset(self):
        try:
            self.data.clear()
        except Exception as e:
            raise Exception(f"Error occurred while resetting data: {e}")

    def sort_data_set(self):
        try:
            self.data = sorted(self.data)
        except Exception as e:
            raise Exception(f"Error occurred while sorting data set: {e}")

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