import tkinter as tk
from tkinter import messagebox
from Metricstics import Metricstics
from GraphGenerator import GraphGenerator

class MetricsticsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Metricstics Calculator")

        # Create an instance of Metricstics without data
        self.Metricstics = Metricstics([])  # Pass an empty list initially

        # Input Frame
        input_frame = tk.Frame(root)
        input_frame.pack(padx=10, pady=10)

        tk.Label(input_frame, text="Input Numbers (comma-separated):", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
        self.input_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.input_entry.grid(row=0, column=1, columnspan=2, sticky="w")

        # Buttons
        generate_button = tk.Button(input_frame, text="Generate Random Numbers", command=self.generate_numbers,
                                    font=("Arial", 10), bg="green", fg="white")
        generate_button.grid(row=1, column=0, pady=10)

        calculate_button = tk.Button(input_frame, text="Calculate Statistics", command=self.calculate_statistics,
                                     font=("Arial", 10), bg="blue", fg="white")
        calculate_button.grid(row=1, column=1, pady=10)

        reset_button = tk.Button(input_frame, text="Reset Data", command=self.reset_data,
                                 font=("Arial", 10), bg="orange", fg="white")
        reset_button.grid(row=1, column=2, pady=10)

        # Output Frame
        output_frame = tk.Frame(root)
        output_frame.pack(padx=10, pady=10)

        tk.Label(output_frame, text="Statistics:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
        self.statistics_label = tk.Label(output_frame, text="", font=("Arial", 12), fg="blue")
        self.statistics_label.grid(row=0, column=1, columnspan=2, sticky="w")

        # Graphs Frame
        graphs_frame = tk.Frame(root)
        graphs_frame.pack(padx=10, pady=10)

        generate_graphs_button = tk.Button(graphs_frame, text="Generate Graphs", command=self.generate_all_graphs,
                                           font=("Arial", 12), bg="purple", fg="white")
        generate_graphs_button.pack()

    def generate_numbers(self):
        try:
            generated_numbers = self.Metricstics.load_from_random()
            self.Metricstics.sort_data_set()  # Sort the generated numbers
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, ", ".join(map(str, self.Metricstics.get_generated_list())))
            messagebox.showinfo("Success", "Numbers generated successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid comma-separated numbers.")

    def calculate_statistics(self):
        input_data = self.input_entry.get()
        try:
            # Convert input string to list of numbers
            numbers = [float(num.strip()) for num in input_data.split(",")]
            self.Metricstics = Metricstics(numbers)
            self.Metricstics.sort_data_set()  # Sort the data
            statistics_text = f"Minimum: {self.Metricstics.minimum()}\n" \
                              f"Maximum: {self.Metricstics.maximum()}\n" \
                              f"Mode: {self.Metricstics.mode()}\n" \
                              f"Median: {self.Metricstics.median()}\n" \
                              f"Mean: {self.Metricstics.mean()}\n" \
                              f"Mean Absolute Deviation: {self.Metricstics.mean_absolute_deviation()}\n" \
                              f"Standard Deviation: {self.Metricstics.standard_deviation()}"
            self.statistics_label.config(text=statistics_text)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid comma-separated numbers.")

    def reset_data(self):
        self.Metricstics.reset()
        self.input_entry.delete(0, tk.END)
        self.statistics_label.config(text="")

    def generate_all_graphs(self):
        try:
            statistics_values = [
                self.Metricstics.minimum(),
                self.Metricstics.maximum(),
                self.Metricstics.median(),
                self.Metricstics.mean(),
                self.Metricstics.mean_absolute_deviation(),
                self.Metricstics.standard_deviation()
            ]

            GraphGenerator.generate_bar_chart(statistics_values)
            GraphGenerator.generate_box_plot(statistics_values)
            GraphGenerator.generate_histogram(self.Metricstics.get_all_repeated_values())
            GraphGenerator.generate_dot_plot(statistics_values)
            GraphGenerator.generate_line_chart(statistics_values)
            GraphGenerator.generate_violin_plot(statistics_values)

        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MetricsticsGUI(root)
    root.mainloop()
