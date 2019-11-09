import csv

with open('Appendix B - Redacted Accessibility Survey Source Data.csv') as infile:
    results = csv.reader(infile)
    data = list(results)
    for line in data:
        if 'Unique' in line[0]:
            headers = line
            num_columns = len(line)
    num = 0
    with open('Summary of R1 Universities.txt', 'w', encoding='UTF-8') as outfile:
        for i in range(num_columns):
            print(headers[num], file=outfile)
            print(file=outfile)
            for line in data:
                if '(R1)' in line[1]:
                    if line[num] != '':
                        print(line[num], file=outfile)

            print('\n\n', file=outfile)
            print('-------------------------------------', file=outfile)
            num += 1
