import csv

with open('Appendix B - Redacted Accessibility Survey Source Data.csv') as infile:
    results = csv.reader(infile)
    data = list(results)
    for line in data:
        if 'Unique' in line[0]:
            num_columns = len(line)
    num = 0
    for i in range(num_columns):
        with open('Data by Question/Summary of R1 Universities by Question_Question ' + str(num+1) + '.txt', 'w',
                  encoding='UTF-8') as outfile:
            for line in data:
                if 'Unique' in line[0]:
                    headers = line
                    print(headers[num], file=outfile)
                    print(file=outfile)
                if '(R1)' in line[1]:
                    if line[num] != '':
                        print(line[num], file=outfile)
        num += 1
