import os
import datetime
import csv
import re
old_file = False  # Used to test if we are using an out of date file. This means we have forgotten to copy the new gmail export file mbox.
# Specify just the filenames. Process_sourcefile() will deal with paths and also check if the files are up to date.
input_filename = 'input.csv'
output_filename = 'output.csv'

def process_sourcefile(input_filename, old_file):
    input_file = os.path.join('', input_filename)
    input_modified_date = datetime.date.fromtimestamp(os.path.getmtime(input_file))
    print('today is:', datetime.date.today(), 'file is: ', input_modified_date )
    if datetime.date.today() != input_modified_date :
        old_file = True
    print("filename is: ", input_file, "modified on :", datetime.date.fromtimestamp(os.path.getmtime(input_file)))
    if old_file:
        print('Your file is old, are you sure you want to continue?')
        response = input('Enter Y to continue. Any other input will quit.')
        if response != 'Y':
            raise SystemExit

def update_output_file(input_filename, output_filename):
    # Using 'with open' because the source files can be very large and cause memory errors
    # Uses RE to identify patterns for emails such as 'To: email..'; 'To: <email ...'; 'RFC Recipient'
    emails = []
    with open(input_filename, 'r', encoding="utf-8") as fb:
        for line in fb:
            match = re.findall(r'To: [\w\.-]+@[\w\.-]+', line)
            for i in match:
                if 'steve' in i or 'pam' in i :
                    print(i, 'has been ignored')
                    pass
                else:
                    print('To: sample\t', i, 'will change to:', i[4:])
                    emails.append(i[4:])
        emails = list(set(emails))  # Removes duplicates
        emails.insert(0, 'email')  # Add title to first row for import
        emailsfile = open(output_filename, 'w', newline='')  # newline='' is to stop blank lines being inserted in csv file.
        wr = csv.writer(emailsfile, quoting=csv.QUOTE_ALL)
        for email in emails:
            wr.writerow([email])
        emailsfile.close()

process_sourcefile(input_filename, old_file)
update_output_file(input_filename, output_filename)



