import os
import random
import uuid
from tkinter import messagebox

from Metricstics import Metricstics
from interface import IRandom
from datetime import datetime
import json


class RandomDataGenerator():

    def __init__(self, min_value=1, max_value=100):
        self.min_value = min_value
        self.max_value = max_value

    def generate_random_data(self, n):
        return [random.randint(self.min_value, self.max_value) for _ in range(n)]


def save_session(metrics, session_file="sessions.json"):
    session_name = input("Please enter a session name: ")

    # short_session_id = hashlib.sha256(str(uuid.uuid4()).encode('utf-8')).hexdigest()[:5]
    session_id = str(uuid.uuid4())[:5]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"session_data_{session_id}.json"

    # Save dataset to a file
    with open(filename, "w") as file:
        json.dump(metrics.session_data, file)

    # Save session information
    session_info = {
        'session_id': session_id,
        'session_name': session_name,
        'timestamp': timestamp,
        'file_location': filename
    }

    # Load existing sessions
    if os.path.exists(session_file):
        with open(session_file, "r") as file:
            sessions = json.load(file)
    else:
        sessions = []

    # Append new session and save
    sessions.append(session_info)
    with open(session_file, "w") as file:
        json.dump(sessions, file)

    # Inform the user about the saved session
    print(f"Session is saved! The new session ID is: {session_id}")


def load_session(session_file="sessions.json"):
    try:
        session_id = input("Please enter the session ID: ")
        with open(session_file, "r") as file:
            sessions = json.load(file)

        session_info = next((session for session in sessions if session['session_id'] == session_id), None)

        if session_info is None:
            print("No session found with the given ID.")
            return None

        with open(session_info['file_location'], "r") as file:
            session_data = json.load(file)
            metrics = Metricstics(session_data['data'])
            return metrics

    except FileNotFoundError:
        print("Session file not found.")
        return None
    except json.JSONDecodeError:
        print("Error reading the session file. The file might be corrupted.")
        return None
    except Exception as e:
        print(f"Error occurred while loading session data: {e}")
        return None


def menu(metrics):
    try:
        print("Select an Operation")
        print("1. Calculate Mean for the data")
        print("2. Calculate Median for the data")
        print("3. Calculate Mode for the data")
        print("4. Calculate Standard Deviation for the data")
        print("5. Calculate Mean Absolute deviation for the data")
        print("6. Calculate Minimum for the data")
        print("7. Calculate Maximum for the data")
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
    # global metrics
    try:
        print("Do you want to load previous session data? (yes/no)")
        load_session_choice = input().lower()
        if load_session_choice == "yes":
            metrics_data = load_session()
            if metrics_data:
                menu(metrics_data)


        else:
            print("Select how the data should be inputted")
            print("1. Auto generate values")
            print("2. Input comma separated values")
            input_type = int(input())
            if (input_type == 1):
                n = int(input("Enter the number of values needed: "))
                rand_data_generator = RandomDataGenerator(min_value=1, max_value=1000)
                random_data = rand_data_generator.generate_random_data(n)
                print(random_data)
                metrics = Metricstics(random_data)
            elif (input_type == 2):
                input_data = [int(x) for x in input("Enter the comma separated values").split(',')]
                metrics = Metricstics(input_data)

            menu(metrics)

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
