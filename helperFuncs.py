import datetime
import csv

def check_agreement(rows):
    for row in rows:
        row['agree_3'] = 'yes' if row['cor_3'] == row['rater_3'] else 'no'
        row['agree_5'] = 'yes' if row['cor_5'] == row['rater_5'] else 'no'
    return rows

def write_csv(filename, header, rows):
    with open(filename, 'w', newline='') as csvfile:
        output_writer = csv.writer(csvfile)
        output_writer.writerow(header)
        for row in rows:
            output_writer.writerow([row['date'], row['rater_score'], row['cor_3'], 
                                    row['cor_5'], row['rater_3'], row['rater_5'], 
                                    row['id'], row['agree_3'], row['agree_5']])

def read_csv(filename):
    with open(filename, 'r', newline='') as csvfile:
        output = []
        input_reader = csv.reader(csvfile)
        next(input_reader)
        for row in input_reader:
            output.append({k:v for k, v in zip(['date', 'rater_score', 'cor_3', 'cor_5', 'rater_3', 'rater_5', 'id', 'agree_3', 'agree_5'], row)})
    return output

