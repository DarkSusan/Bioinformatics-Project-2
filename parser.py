import csv

file = "CAZymes.csv"

def ecology_filter(input_file, features_header):
    with open(input_file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        header = next(reader)
        ecology_index = header.index("Ecology")
        aa_index = header.index(features_header)
        last_aa_index = len(header) - 1

        filtered_rows = []

        for row in reader:
            filtered_row = [row[ecology_index]] + row[aa_index:last_aa_index + 1]
            filtered_rows.append(filtered_row)

        filtered_rows.sort(key=lambda x: x[0])

    return filtered_rows, ["Ecology"] + header[aa_index:last_aa_index + 1]

def mycorrhizae_filter(filtered_rows, header, output_file):
    updated_rows = []

    for row in filtered_rows:
        if "mycorrhizae" in row[0].lower():
            row[0] = "mycorrhizae"
        else:
            row[0] = "non_mycorrhizae"
        updated_rows.append(row)

    updated_rows.sort(key=lambda x: x[0])

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)
        writer.writerows(updated_rows)

# Usage
filtered_rows, header = ecology_filter(file, "AA1")
mycorrhizae_filter(filtered_rows, header, f"filtered_{file.split(".")[0]}_mycorrhizae.csv")