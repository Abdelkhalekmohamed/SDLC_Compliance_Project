import csv


def fix_csv_typo(file_path):
    corrected_rows = []

    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        corrected_rows.append(headers)

        for row in csv_reader:
            corrected_row = []
            for col in row:
                if 'used for security=False=False' in col:
                    print(f"Found typo in: {col}")
                corrected_row.append(col.replace('used for security=False=False', 'used for security=False'))
            corrected_rows.append(corrected_row)

    with open(file_path, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(corrected_rows)

    print(f"Typo corrected in {file_path}")


# Fix the typo in the compliance report CSV
fix_csv_typo('data/compliance_report.csv')
