from randGen import Generator
from helperFuncs import *
import matplotlib
import matplotlib.pyplot as plt

# Step 1
# -------------------------------
# begin by initializing and generating 10,000 rows.
# for more information on the Generator class, see randGen.py

date_range = (datetime.datetime(2005, 10, 1), datetime.datetime(2005, 10, 30))
rater_score = ['A', 'B', 'C', 'D', 'E']
answer_3 = ['Low', 'Average', 'High']
answer_5 = ['Bad', 'Okay', 'Intermediate', 'Great', 'Exceptional']

g = Generator(seed=None, date_tup=date_range, rater_score=rater_score, cor_3=answer_3, cor_5=answer_5, rater_3=answer_3, rater_5=answer_5)

random_rows = g.gen_n_rows(num=10000)

# Step 2
# ---------------------------------
# to check agreement utilize a small helper function (see helperFuncs.py)

random_rows = check_agreement(random_rows)

# Step 3
# ---------------------------------
# output the random rows to a csv file (again, see helperFuncs.py)

output_file = "random_data.csv"
header = ["Date", "Rater", "Correct Answer 3 Label", "Correct Answer 5 Label",
          "Rater Answer 3 Label", "Rater Answer 5 Label", "Task ID", 
          "3-Label Agreement", "5-Label Agreement"]

write_csv(output_file, header, random_rows)

# you can also read csv files
# random_rows = read_csv(output_file)

# for now let's use random_rows to make inferences on the data
# for each of these inferences you can visualise the output by uncommenting
# the marked line. output plots are already included for the random data
# defined in "plotted_random_data.csv".

# Step 4
# --------------------------------
# each of step 4's questions are accompanied by a brief code 
# snippet to find the solution to the question as well as a 
# simple visualization of the solution. each of these visualizations
# are meant to be run independent of one another, and sample plots from
# given sample data can be found in examples/


""" What is the agreement rate between the engineer and all the raters for each day? """
agreement_per_day = {}

# iterate through each item, count agreement and totals
# each day will have a 3ple containing [correct_3, correct_5, total]
for rows in random_rows:
    if rows['date'] not in agreement_per_day:
        agreement_per_day[rows['date']] = [0, 0, 0]

    if rows['agree_3'] == 'yes':
        agreement_per_day[rows['date']][0] += 1

    if rows['agree_5'] == 'yes':
        agreement_per_day[rows['date']][1] += 1

    agreement_per_day[rows['date']][2] += 1

# now convert to percentage [percent_3, percent_5, percent_combined]
agreement_per_day = {k:[v[0]/v[2], v[1]/v[2], (v[1]+v[0])/v[2]] for k, v in agreement_per_day.items()}

# print
#
# combined
#print({k:v[2] for k, v in agreement_per_day.items()})
#
# just 3
#print({k:v[0] for k, v in agreement_per_day.items()})
#
# just 5
#print({k:v[1] for k, v in agreement_per_day.items()})

# visualization
#
#x, y = zip(*sorted(agreement_per_day.items()))
#fig, ax = plt.subplots()
#ax.plot(x, y)
#plt.ylabel('percentage agreement')
#plt.xlabel('date')
#plt.title("Agreement rate between engineers and raters by date")
#ax.legend(['3-label','5-label','Combined'])
#plt.show()


""" Identify raters that have the highest agreement rates with the engineers """
agreement_per_rater = {}

# iterate through each item
# each rater will have a 3ple containing [correct_3, correct_5, total]
for rows in random_rows:
    if rows['rater_score'] not in agreement_per_rater:
        agreement_per_rater[rows['rater_score']] = [0, 0, 0]

    if rows['cor_3'] == rows['rater_3']:
        agreement_per_rater[rows['rater_score']][0] += 1

    if rows['cor_5'] == rows['rater_5']:
        agreement_per_rater[rows['rater_score']][1] += 1

    agreement_per_rater[rows['rater_score']][2] += 1

# now convert to percentage [percent_3, percent_5, percent_combined]
agreement_per_rater = {k:[v[0]/v[2], v[1]/v[2], (v[1]+v[0])/v[2]] for k, v in agreement_per_rater.items()}

# print
#
# combined
#print(sorted(agreement_per_rater.items(), key=lambda item: item[1][2], reverse=True))
#
# just 3
#print(sorted(agreement_per_rater.items(), key=lambda item: item[1][0], reverse=True))
#
# just 5
#print(sorted(agreement_per_rater.items(), key=lambda item: item[1][1], reverse=True))

# visualization
#
#x, y = zip(*sorted(agreement_per_rater.items()))
#fig, ax = plt.subplots()
#plt.ylabel('percentage agreement')
#plt.xlabel('rater')
#ax.plot(x, y)
#plt.title("Agreement rate between engineers and raters by rater")
#ax.legend(['3-label', '5-label', 'Combined'])
#plt.show()


""" Identify raters that have the lowest agreement rates with the engineers """

# this is just the reverse of the previous list

# print
#
# combined
#print(sorted(agreement_per_rater.items(), key=lambda item: item[1][2], reverse=False))
#
# just 3
#print(sorted(agreement_per_rater.items(), key=lambda item: item[1][0], reverse=False))
#
# just 5
#print(sorted(agreement_per_rater.items(), key=lambda item: item[1][1], reverse=False))

# visualization
#
#x, y = zip(*sorted(agreement_per_rater.items()))
#fig, ax = plt.subplots()
#plt.ylabel('percentage agreement')
#plt.xlabel('rater')
#ax.plot(x, y)
#ax.legend(['3-label', '5-label', 'Combined'])
#plt.show()

""" Identify raters that have completed the most Task IDs """
num_task_ids = {}
for row in random_rows:
    if row['rater_score'] not in num_task_ids:
        num_task_ids[row['rater_score']] = 0
    num_task_ids[row['rater_score']] += 1

# print
#
#print(sorted(num_task_ids.items(), key=lambda item: item[1]))

# visualization
#
#x, y = zip(*sorted(num_task_ids.items()))
#plt.bar(x, y)
#plt.ylabel("number of tasks completed")
#plt.xlabel("rater")
#plt.title("# of Task IDs completed by rater")
#plt.show()


""" Identify raters that have completed the least Task IDs """

# once again, just the inverse of the previous task

# print
#
#print(sorted(num_task_ids.items(), key=lambda item: item[1], reverse=True))

# visualization
#
#x, y = zip(*sorted(num_task_ids.items()))
#plt.bar(x, y)
#plt.ylabel("number of tasks completed")
#plt.xlabel("rater")
#plt.title("# of Task IDs completed by rater")
#plt.show()

""" What is the precision for each of the 3 labels? """

# create an array containing 'Label':[True Positive, False Positive, True Neg., False Neg.]
label_3 = {'Low': [0, 0, 0, 0], 'Average': [0, 0, 0, 0], 'High': [0, 0, 0, 0]}
for row in random_rows:
    for k, v in label_3.items():
        if k == row['rater_3']:
            if row['rater_3'] == row['cor_3']:
                # True Positive
                v[0] += 1
            else:
                # False Positive
                v[1] += 1
        else:
            if row['rater_3'] == row['cor_3']:
                # True Negative
                v[2] += 1
            else:
                if k == row['cor_3']:
                    # False Negative
                    v[3] += 1

# calculate precision = TP/(TP+FP)
label_3_prec = {k:v[0]/(v[0]+v[1]) for k, v in label_3.items()}

# print
#print(label_3_prec)

# visualization
#
#x, y = zip(*sorted(label_3_prec.items()))
#plt.bar(x, y)
#plt.ylabel("precision")
#plt.xlabel("label")
#plt.title("Label 3 Precision")
#plt.show()

""" What is the recall for each of the 3 labels? """

# calculate recall = TP/(TP+FN)
label_3_rec = {k:v[0]/(v[0]+v[3]) for k, v in label_3.items()}

# print
#print(label_3_rec)

# visualization
#
#x, y = zip(*sorted(label_3_prec.items()))
#plt.bar(x, y)
#plt.ylabel("recall")
#plt.xlabel("label")
#plt.title("Label 3 Recall")
#plt.show()

""" 
    To finish Step 4, I'd say the general result of these plots is about what I expected, while
    there is some deviation from random chance, the majority of the metrics agree that these
    raters are randomly choosing the labels regardless of what is shown to them (can't really be
    suprised there). If I were to attempt to improve these labels, I'd likely build 
    some type of quorum system, which only marks labels if a majority of the raters agree.
"""

# Step 5
# --------------------------------------------

""" Issue One: Are the raters working an even amount each day, or are they cramming
    their work into a single day """

""" Issue Two: Are the raters spending a reasonable amount of time on each input,
    or are they immediately labeling each data point """

""" Issue Three: Are the raters doing significantly better than randomly choosing labels? """

# Step 6
# --------------------------------------------

""" SQL Statement: 
    SELECT COUNT(*) FROM rater_date WHERE date="10-6-2005" AND agree_3="yes" GROUP BY rater_score
"""
