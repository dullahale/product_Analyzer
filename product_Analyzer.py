import csv
from datetime import datetime


def readCSVFile(filepath):
    """
    This function takes a CSV file and returns a list of dictionaries.

    :param filepath: This is the path to the CSV file.

    :return: A list of dictionaries, where each dictionary represents a row of data.
    """
    with open(filepath, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]
        print(data)
    return data


def calculate_total_value(products):
    """
    This function takes list of products and calculates the total value for each of product
    based on its price and quantity.

    :param products: A list of dictionaries.

    :return: A modified list that contains the total value calculated.
    """
    for i in products:
        i['TotalValue'] = float(i['Price']) * int(i['Quantity'])
    return products


def calculate_days_since_last_recieved(products):
    """
    This function takes a list of products and calculate the last date the item was received

    :param products: The list of dictionaries.

    :return: A list of products with the additional information on when the last date the
            item was received.
    """
    today = datetime.now()
    for i in products:
        last_dateReceived = datetime.strptime(i["LastDateReceived"], '%Y-%m-%d')
        days_received = (today - last_dateReceived).days
        i["DaysReceived"] = days_received

    return products


def sort_data(data, column):
    """
    This function takes a list of dictionaries and sorts them based on the column .

    :param data: A list of dictionaries.

    :param column: A string representing the column in which the data will be stored.

    :return: A sorted list.
    """
    return sorted(data, key=lambda i: i[column], reverse=False)


def aggregate_total_quantity(data, quantity_column):
    """
    This function calculates the total quantity of products in a specified column.

    :param data: A list of dictionaries.

    :param quantity_column: A string that represents the column containing the quantity values.

    :return: The total quantity.
    """
    total_quantity = 0

    for i in data:

        product_ID = i.get("ProductId", "")
        quantity_value = i.get(quantity_column, "")

        if quantity_value and quantity_value.isdigit():
            quantity = int(quantity_value)
            total_quantity += quantity

        else:
            print(f"Invalid quantity value for ProductID {product_ID}")

    return total_quantity


def writeCSV(data, output_file):
    """
    This function writes data from list of dictionaries to a CSV file.

    :param data: A list of dictionaries, where each dictionary represents a row of data.

    :param output_file: This is the path to the CSV file where you write the data
    """
    if not data:
        print("No data to write !!!")
        return

    fieldnames = data[0].keys()
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


file_path = "Products.csv"

csv_data = readCSVFile(file_path)

# TODO: Uncomment from below and run the file


# # Calculate the total value
# data_with_total_value = calculate_total_value(csv_data)
#
# total_value_file = "Modified_with_total_value.csv"
#
# writeCSV(data_with_total_value, total_value_file)
# print(f"Total Value Calculation Complete. Results saved to {total_value_file}")
#
# # Calculate days since last received for each product
# data_with_last_date = calculate_days_since_last_recieved(csv_data)
#
# lastDate_value_file = "Modified_with_last_date.csv"
#
# writeCSV(data_with_last_date, lastDate_value_file)
# print(f"Last Date Calculation Complete. Results saved to {lastDate_value_file}")
#
# # Sort the data based on a column (replace 'ColumnName' with the actual column name)
# sorted_data = sort_data(csv_data, column='Quantity')
#
# sorted_data_file = "Sorted_file.csv"
#
# writeCSV(sorted_data, sorted_data_file)
# print(f"Sorting Complete. Results saved to {sorted_data_file}")
#
# # Aggregate total quantity (replace 'QuantityColumn' with the actual quantity column name)
# total_quantity = aggregate_total_quantity(csv_data, 'Quantity')
#
# aggregate_value_file = "Aggregate_value_file.csv"
#
# with open(aggregate_value_file, 'w') as csv_file:
#     csv_file.write(f"Total Quantity of products is {total_quantity}\n")
#
# print(f"Aggregation completed. Results saved to {aggregate_value_file}")
