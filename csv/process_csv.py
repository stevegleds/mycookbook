# import numpy as np
""" Takes csv file and creates dictionary representation so that we can reference the columns as data fields.
This allows processing each row and filtering out extreme data that could be errors.
parse() is function to convert csv to disctionary
remove() is function to go through parsed file and produce output with bad values removed
"""
import csv


DATA_FILE = 'april2020_002.csv'  # this is source speed test data
OUTPUT_FILE = 'output2' + DATA_FILE   # this is the final file
print('Data file used is: ', DATA_FILE)
print('Output file used is:', OUTPUT_FILE)


def parse(raw_file, delimiter=','):
    """
    :param raw_file: probably csv file
    :param delimiter: specify delimiter
    :return: parsed data
    Parses a raw CSV file to a JSON-line object.
    """
    #  open csv file
    opened_file = open(raw_file)
    #  read csv file
    csv_data = csv.reader(
        opened_file,
        delimiter=delimiter)  # first delimiter is csv.reader variable name
    #  csv_data object is now an iterator meaning we can get each element one at a time
    #  build data structure to return parsed data
    parsed_data = []  # this list will store every row of data
    fields = csv_data.__next__(
    )  # this will be the column headers; we can use .next() because csv_data is an iterator
    for row in csv_data:
        if row[1] == "":  # there is no text in the field so no data to process
            pass
        else:
            parsed_data.append(dict(zip(fields, row)))
            # Creates a new dict item for each row with col header as key and stores in a list
        #  city_count += 1
    # close csv file
    opened_file.close()
    return parsed_data


def remove_extremes(data_file, output_file):

    with open(output_file, "w", newline='') as f:
        writer = csv.writer(f,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        writer.writerow([
            'Date', 'DL', 'UL', 'Ping',
            'TCPPing' 
        ])

        for item in data_file:
            if item['TCPPingTime'] != 'NULL' and int(item['TCPPingTime']) <= 4000 : 
                writer.writerow([
                    item['DateTimeStamp'], int(item['DownloadSpeed']) / 1000,
                    int(item['UploadSpeed']) / 1000, item['PingTime'], item['TCPPingTime']
                ])
    f.close()    
    return

def main():

    raw_data_file = parse(DATA_FILE)
    
    remove_extremes(raw_data_file, OUTPUT_FILE)

    


if __name__ == "__main__":
    main()
