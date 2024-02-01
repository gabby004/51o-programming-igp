from pathlib import Path
import csv

def read_profit_loss_data(file_path):
    """
    Reads the CSV file containing profit and loss data.
    Returns a list of tuples where each tuple contains the day and net profit difference.
    """
    profit_loss_data = []

    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        prev_net_profit = None
        for row in reader:
            day = int(row[0])
            net_profit = int(row[4])

            if prev_net_profit is not None:
                net_profit_diff = net_profit - prev_net_profit
                profit_loss_data.append((day, net_profit_diff))

            prev_net_profit = net_profit

    return profit_loss_data

def identify_scenario(profit_loss_data):
    """
    Identifies the scenario based on the trend of net profit.
    Returns the scenario output.
    """
    increasing_trend = all(diff > 0 for _, diff in profit_loss_data)
    decreasing_trend = all(diff < 0 for _, diff in profit_loss_data)

    if increasing_trend:
        return scenario_1(profit_loss_data)
    elif decreasing_trend:
        return scenario_2(profit_loss_data)
    else:
        return scenario_3(profit_loss_data)

def scenario_1(profit_loss_data):
    """
    Scenario 1: Net profit is always increasing.
    Identifies the day and amount the highest increment occurs
    """
    max_increment_day, max_increment_amount = max(profit_loss_data, key=get_abs_second_element)
    output = "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n"
    output += f"[HIGHEST NET PROFIT SURPLUS] DAY: {max_increment_day}, AMOUNT: SGD{max_increment_amount}\n"
    return output

def scenario_2(profit_loss_data):
    """
    Scenario 2: Net profit is always decreasing.
    Identifies the day and amount the highest decrement occurs
    """
    min_decrement_day, min_decrement_amount = min(profit_loss_data, key=get_net_profit_difference)
    output = "[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY\n"
    output += f"[HIGHEST PROFIT DEFICIT] DAY: {min_decrement_day}, AMOUNT: SGD{abs(min_decrement_amount)}\n"
    return output

def scenario_3(profit_loss_data):
    """
    Scenario 3: Net profit fluctuates.
    List down all the days and amount when deficit occurs and find out the top 3 highest deficit amount and the days it occurred.
    """
    deficits = sorted((day, diff) for day, diff in profit_loss_data if diff < 0)
    output = ""

    #List down all the days and amount when deficits occurs
    for day, deficit in deficits:
        output += f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{abs(deficit)}\n"

    #Find out the top 3 highest deficit amount and the day it occurred
    top_3_deficits = sorted(deficits, key=get_abs_second_element, reverse=True)[:3]
    deficit_labels = ["[HIGHEST NET PROFIT DEFICIT]", "[2ND HIGHEST NET PROFIT DEFICIT]", "[3RD HIGHEST NET PROFIT DEFICIT]"]
    for i, (day, deficit) in enumerate(top_3_deficits, start=1):
        output += f"{deficit_labels[i - 1]} DAY: {day}, AMOUNT: SGD{abs(deficit)}\n"

    return output

def get_abs_second_element(item):
    """
    Helper function to get the absolute value of the second element of a tuple.
    """
    return abs(item[1])

def get_net_profit_difference(item):
    """
    Helper function to get the net profit difference.
    """
    return item[1]

# Main script
if __name__ == "__main__":
    file_path = Path.cwd() / "csv_reports" / "Profits_and_Loss.csv"
    profit_loss_data = read_profit_loss_data(file_path)
    scenario_output = identify_scenario(profit_loss_data)
    print(scenario_output)  # Print or write to a file as needed