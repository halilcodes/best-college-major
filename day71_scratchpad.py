import pandas as pd
import csv


a = [i for i in range(1,11)]

b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

with open("71-v2/csv_try.csv", "w") as df:
    writer = csv.writer(df)
    writer.writerow(["a_list", "b_list"])
    for i in range(len(a)):
        writer.writerow([a[i], b[i]])


with open("71-v2/csv_try_2.csv", "w") as df:
    writer = csv.writer(df)
    writer.writerow(["a_list", "b_list"])
    writer.writerows([a, b])


oldstring = "aaaabbbccc"
print(oldstring.replace("l", ""))