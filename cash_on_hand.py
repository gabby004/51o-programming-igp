from pathlib import Path
import csv

def read_cash_on_hand_data(file_path):
    """
    Reads the CSV file containing cash on hand data.
    Returns a list of tuples where each tuple contains the day and cash on hand difference.
    """
    cash_on_hand_data = []

    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        prev_cash_on_hand = None
        for row in reader:
            day = int(row[0])
            cash_on_hand = int(row[1])

            if prev_cash_on_hand is not None:
                cash_on_hand_diff = cash_on_hand - prev_cash_on_hand
                cash_on_hand_data.append((day, cash_on_hand_diff))

            prev_cash_on_hand = cash_on_hand

    return cash_on_hand_data

def identify_scenario(cash_on_hand_data):
    """
    Identifies the scenario based on the trend of cash on hand.
    Returns the scenario output.
    """
    increasing_trend = all(diff > 0 for _, diff in cash_on_hand_data)
    decreasing_trend = all(diff < 0 for _, diff in cash_on_hand_data)

    if increasing_trend:
        return scenario_1(cash_on_hand_data)
    elif decreasing_trend:
        return scenario_2(cash_on_hand_data)
    else:
        return scenario_3(cash_on_hand_data)

def scenario_1(cash_on_hand_data):
    """
    Scenario 1: Cash on hand is always increasing.
    Identifies the day and amount the highest increment occurs
    """
    max_increment_day, max_increment_amount = max(cash_on_hand_data, key=get_abs_second_element)
    output = "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
    output += f"[HIGHEST CASH SURPLUS] DAY: {max_increment_day}, AMOUNT: SGD{max_increment_amount}\n"
    return output

def scenario_2(cash_on_hand_data):
    """
    Scenario 2: Cash on hand is always decreasing.
    Identifies the day and amount the highest decrement occurs
    """
    min_decrement_day, min_decrement_amount = min(cash_on_hand_data,key=get_cash_on_hand_difference)
    output = "[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n"
    output += f"[HIGHEST CASH DEFICIT] DAY: {min_decrement_day}, AMOUNT: SGD{abs(min_decrement_amount)}\n"
    return output

def scenario_3(cash_on_hand_data):
    """
    Scenario 3: Cash on hand fluctuates.
    List down all the days and amount when deficit occurs and find out the top 3 highest deficit amount and the days it occurred.
    """
    deficits = sorted((day, diff) for day, diff in cash_on_hand_data if diff < 0)
    output = ""

    #List down all the days and amount when deficits occurs
    for day, deficit in deficits:
        output += f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD{abs(deficit)}\n"

    #Find out the top 3 highest deficit amount and the day it occurred
    top_3_deficits = sorted(deficits, key=get_abs_second_element, reverse=True)[:3]
    deficit_labels = ["[HIGHEST CASH DEFICIT]", "[2ND HIGHEST CASH DEFICIT]", "[3RD HIGHEST CASH DEFICIT]"]
    for i, (day, deficit) in enumerate(top_3_deficits, start=1):
        output += f"{deficit_labels[i - 1]} Day: {day}, AMOUNT: SGD{abs(deficit)}\n"

    return output

def get_abs_second_element(item):
    """
    Helper function to get the absolute value of the second element of a tuple.
    """
    return abs(item[1])

def get_cash_on_hand_difference(item):
    """
    Helper function to get the cash on hand difference.
    """
    return item[1]

# Main script
if __name__ == "__main__":
    file_path = Path.cwd() / "csv_reports" / "Cash_on_Hand.csv"
    cash_on_hand_data = read_cash_on_hand_data(file_path)
    scenario_output = identify_scenario(cash_on_hand_data)
    print(scenario_output)  # Print or write to a file as needed