import csv

with open('Appendix B - Redacted Accessibility Survey Source Data.csv') as infile:
    results = csv.reader(infile)
    data = list(results)
    institution_num_list = []
    for line in data:
        if 'Unique' in line[0]:
            headers = line
        if '(R1)' in line[1]:
            institution_num_list.append(line[0])
    list_num = 0
    for i in range(len(institution_num_list)):
        with open('Data by Institution/Summary of R1 Universities by Institution_Institution ID Number ' +
                  str(institution_num_list[list_num]) + '.txt', 'w', encoding='UTF-8') as outfile:

            num = 0
            for line in data:
                if 'Unique' in line[0]:
                        headers = line
                if line[0] == institution_num_list[list_num]:
                    for phrase in line:
                        if phrase != '':
                            print(headers[num], end=': ', file=outfile)
                            print('\n    ' + ''.join(phrase), file=outfile)
                            num += 1
                        elif phrase == '':
                            # print(headers[num] + ': ' + '\n    N/A', file=outfile)
                            num += 1
                    # print()
                    # print('--------------------')
                    # print()
        list_num += 1
