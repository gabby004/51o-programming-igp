from pathlib import Path
import overheads
import cash_on_hand
import profit_loss

# File paths for CSV files
overheads_fp = Path.cwd() / "csv_reports" / "Overheads.csv"
cash_on_hand_fp = Path.cwd() / "csv_reports" / "Cash_on_Hand.csv"
profit_loss_fp = Path.cwd() / "csv_reports" / "Profits_and_Loss.csv"


# Read data from CSV files
cash_on_hand_data = cash_on_hand.read_cash_on_hand_data(cash_on_hand_fp)
profit_loss_data = profit_loss.read_profit_loss_data(profit_loss_fp)

# Identify scenarios and overheads
overheads_output = overheads.identify_overheads(overheads_fp)
cash_on_hand_output = cash_on_hand.identify_scenario(cash_on_hand_data) 
profit_loss_output = profit_loss.identify_scenario(profit_loss_data) 

# Write the outputs to the summary report
with open("summary_report.txt", "w") as file:
    # overheads
    file.write(overheads_output)

    # cash on hand
    file.write(cash_on_hand_output)

    # profit and loss
    file.write(profit_loss_output)

print(overheads_output.strip('\n'))
print(cash_on_hand_output.strip('\n'))
print(profit_loss_output.strip('\n'))

print("\nSummary report generated successfully.")