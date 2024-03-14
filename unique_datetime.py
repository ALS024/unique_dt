import re

def is_valid_datetime(datetime_str):
    # RegEx to match ISO 8601 
    pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}([+-]\d{2}:\d{2}|Z)$'
    return re.match(pattern, datetime_str) is not None

def read_datetime_values(input_file):
    with open(input_file, 'r') as f:
        return [line.strip() for line in f]

def write_unique_datetime_values(datetime_values, output_file):
    unique_datetime_values = set(datetime_values)
    with open(output_file, 'w') as f:
        for datetime_value in unique_datetime_values:
            f.write(datetime_value + '\n')

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    datetime_values = read_datetime_values(input_file)
    #print(datetime_values)
    #print(is_valid_datetime)
    valid_datetime_values = [dt for dt in datetime_values if is_valid_datetime(dt)]
    #print(valid_datetime_values)
    write_unique_datetime_values(valid_datetime_values, output_file)
    #print(write_unique_datetime_values)

if __name__ == "__main__":
    main()
