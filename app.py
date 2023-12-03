import csv
import json

CSV_FILENAME = "test_data.csv"
OUTPUT_FILENAME = "output.json"


def convert_to_proper_types(value):
    """
    Converts the value that
    stored in str to the appropriate data type

    Example:
    "False" -> False (bool)
    "2314.23" -> 2314.23 (float)
    "252" -> 252 (int)
    """
    if value.isdigit():
        return int(value)
    # if you try to make the string a float number, you will get an error
    try:
        return float(value.replace(",", "."))
    except ValueError:
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        
    return value


def read_csv(file_path: str) -> (list, list):
    """
    This function parses the csv file and
    returns the head and body
    """
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file, delimiter=";")

        header = next(reader)
        data = [[convert_to_proper_types(cell) for cell in row] for row in reader]

    return header, data


def make_json(header: list, body: list) -> dict:
    """
    This function returns a dictionary based on our data (head, body)
    """
    json_data = {}
    
    for idx, row in enumerate(body, start=1):
        entry = {}
        for key, value in zip(header, row):
            entry[key.strip()] = value
        json_data[str(idx)] = entry
    
    return json_data


def main() -> None:
    header, body_data = read_csv(CSV_FILENAME)
    json_data = make_json(header, body_data)
    json_output = json.dumps(json_data, indent=2)

    with open(OUTPUT_FILENAME, "w", encoding="UTF-8") as output_file:
        output_file.write(json_output)
    print("Done!")

if __name__ == "__main__":
    main()
