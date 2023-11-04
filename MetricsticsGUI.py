import tkinter as tk
from tkinter import messagebox
from Metricstics import Metricstics

class MetricsticsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Metricstics Calculator")

        self.Metricstics = Metricstics()

        # Input Frame
        input_frame = tk.Frame(root)
        input_frame.pack(padx=10, pady=10)

        tk.Label(input_frame, text="Genertaed Numbers:").grid(row=0, column=0, sticky="w")
        self.generated_numbers_label = tk.Label(input_frame, text="")
        self.generated_numbers_label.grid(row=0, column=1, columnspan=2, sticky="w")

        # Buttons
        generate_button = tk.Button(input_frame, text="Generate Numbers", command=self.generate_numbers)
        generate_button.grid(row=1, column=0, pady=10)

        calculate_button = tk.Button(input_frame, text="Calculate Statistics", command=self.calculate_statistics)
        calculate_button.grid(row=1, column=1, pady=10)

        reset_button = tk.Button(input_frame, text="Reset Data", command=self.reset_data)
        reset_button.grid(row=1, column=2, pady=10)

        # Output Frame
        output_frame = tk.Frame(root)
        output_frame.pack(padx=10, pady=10)

        tk.Label(output_frame, text="Statistics:").grid(row=0, column=0, sticky="w")
        self.statistics_label = tk.Label(output_frame, text="")
        self.statistics_label.grid(row=0, column=1, columnspan=2, sticky="w")

    def generate_numbers(self):
       try:
            generated_numbers = self.Metricstics.load_from_random()
            self.generated_numbers_label.config(text=generated_numbers)
            messagebox.showinfo("Success", "Numbers generated successfully!")
       except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter comma-separated numbers.")

    def calculate_statistics(self):
        if not self.Metricstics.get_generated_list():
            messagebox.showerror("Error", "Generate numbers first!")
        else:
            self.Metricstics.sort_data_set()
            statistics_text = f"Minimum: {self.Metricstics.minimum()}\n" \
                              f"Maximum: {self.Metricstics.maximum()}\n" \
                              f"Mode: {self.Metricstics.mode()}\n" \
                              f"Median: {self.Metricstics.median()}\n" \
                              f"Mean: {self.Metricstics.arithmetic_mean()}\n" \
                              f"Mean Absolute Deviation: {self.Metricstics.mean_absolute_deviation()}\n" \
                              f"Standard Deviation: {self.Metricstics.standard_deviation()}"
            self.statistics_label.config(text=statistics_text)

    def reset_data(self):
        self.Metricstics.reset()
        #self.input_entry.delete(0, 'end')
        self.statistics_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetricsticsGUI(root)
    root.mainloop()
