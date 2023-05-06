import gzip
import json
import numpy as np
import csv

np.set_printoptions(suppress=True)
filename = 'C:\\Users\\86173\\Desktop\\tf-binance-BTC_ETH-2022-07-21.gz'
csv_fp = open('output_data.csv', 'w', encoding='gb18030', newline='')
csv_writer = csv.writer(csv_fp)
csv_writer.writerow(('timestamp', 'std'))


def std1(list1):
    tempList = []
    for item1 in list1:
        tempList.append(item1[1])

    return np.std(tempList)


with gzip.open(filename, mode="rt") as f:
    first_line = json.loads(f.readlines()[0])
    startTime = (int(int(first_line[0]) / 1000) + 10) * 1000
    list = []

with gzip.open(filename, mode="rt") as f:
    for row in f:
        parsed = json.loads(row.rstrip("\n"))
        if startTime - int(parsed[0]) > 0:
            list.append([int(parsed[0]), float(parsed[2])])
            continue
        else:
            std = std1(list)
            csv_writer.writerow((startTime, std))
            startTime = startTime + 1000
            list.append([int(parsed[0]), float(parsed[2])])
            for item in list:
                if startTime - item[0] > 10000:
                    list.pop(0)
                else:
                    break


