import matplotlib.pyplot as plt
import csv

ifile = open('output.csv', 'rb')
reader = csv.reader(ifile)
data = []
label = []

rownum = 0
for row in reader:
    label.append(row)
# Save header row.
    if rownum ==0:
        header = row
    else:
        colnum = 0
    for col in row:
        data.append(col)
        print('%-8s: %s' % (header[colnum], col))
        colnum += 1
    rownum += 1

plt.hist(data, label, (0,10000))
plt.show()

ifile.close()