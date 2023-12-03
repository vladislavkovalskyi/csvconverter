csv_filename = input("Enter the filename: ")
output_filename = input("Enter the OUTPUT filename: ")


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
        lines = file.readlines()

    header = lines[0].strip().split(";")
    data = [
        [convert_to_proper_types(cell) for cell in row.strip().split(";")]
        for row in lines[1:]
    ]

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


def normalize_json(json: str) -> str:
    data = ""
    for letter in json:
        if letter == "}":
            data += "}\n"
            continue
        data += letter
        
    return data.replace(" ", "").replace("'", "\"")



def main() -> None:
    header, body_data = read_csv(csv_filename)
    json_data = normalize_json(str(make_json(header, body_data)))

    print(json_data)
    with open(output_filename, "w", encoding="UTF-8") as output_file:
        output_file.write(json_data)
    print(f"Output written to {output_filename}")


if __name__ == "__main__":
    main()
