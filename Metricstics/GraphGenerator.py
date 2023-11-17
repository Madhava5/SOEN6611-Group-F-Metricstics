# GraphGenerator.py

import matplotlib.pyplot as plt
import seaborn as sns

class GraphGenerator:
    @staticmethod
    def generate_bar_chart(statistics_values):
        plt.bar(["Minimum", "Maximum", "Median", "Mean", "MAD", "Standard Deviation"], statistics_values)
        plt.xlabel("Statistics")
        plt.ylabel("Values")
        plt.title("Bar Chart")
        plt.show()

    @staticmethod
    def generate_box_plot(statistics_values):
        sns.boxplot(data=statistics_values)
        plt.title("Box Plot")
        plt.show()

    @staticmethod
    def generate_histogram(statistics_values):
        plt.hist(statistics_values, bins=10, edgecolor='black')
        plt.xlabel("Values")
        plt.ylabel("Frequency")
        plt.title("Histogram")
        plt.show()

    @staticmethod
    def generate_dot_plot(statistics_values):
        sns.stripplot(x=list(range(len(statistics_values))), y=statistics_values, jitter=True, size=8)
        plt.title("Dot Plot")
        plt.xlabel("Index")
        plt.ylabel("Values")
        plt.show()

    @staticmethod
    def generate_line_chart(statistics_values):
        plt.plot(list(range(len(statistics_values))), statistics_values, marker='o')
        plt.xlabel("Index")
        plt.ylabel("Values")
        plt.title("Line Chart")
        plt.show()

    @staticmethod
    def generate_violin_plot(statistics_values):
        sns.violinplot(data=statistics_values)
        plt.title("Violin Plot")
        plt.show()