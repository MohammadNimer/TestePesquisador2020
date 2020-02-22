import csv

with open('sms_senior.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["Full_Text"]} works in the {row["IsSpam"]} IsSpam, and was born in {row["Word_Count"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    
