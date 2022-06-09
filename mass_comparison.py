import pandas as pd
import re
df = pd.read_csv("/home/nathan/PycharmProjects/metabo/camera_output.csv")
df = df[df['adduct'].notna()]
saved_column = df.adduct

camera_mass_list = []
for row in saved_column:
    row = re.split(r" ",row)
    row = row[1]
    camera_mass_list.append(float(row))

df2 = pd.read_csv("/home/nathan/PycharmProjects/metabo/urine_metabolites_hmdb.csv")
saved_column_2 = df2.MONO_MASS

hmdb_mass_list = []
for row in saved_column_2:
    hmdb_mass_list.append(row)

match_list = []

for i in camera_mass_list:
    for count,j in enumerate(hmdb_mass_list):
        if abs(i - j) < 0.0001:
            print(i,"~=",j)
            print(count)
            input = df2.iloc[count, :]
            input = input.NAME
            if input not in match_list:
                match_list.append(input)

print(match_list)
with open(r'/home/nathan/Documents/CRTI/metabo/match_list_metabo', 'w') as fp:
    for item in match_list:
        fp.write("%s\n" % item)
    print('Done')

