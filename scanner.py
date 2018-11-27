import csv, io
from os import path

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

##Get CSV Filename
csvName = input('Enter CSV filename: ')
while True:
    try:
        csvText = io.open(path.join(d, csvName+'.csv')).readlines()
        csvFile = [row for row in csv.reader(csvText, delimiter=',', quotechar='"')]
        break
    except FileNotFoundError:
        csvName = input('File not found\n' + 'Enter CSV filename: ')

##Get columns from CSV
columns = csvFile[0]
columns = [str(i) + ' ' + column for i, column in enumerate(columns, 1)]
columnchoices = ', '.join(columns)

valid_cols = [i for i in range(1, len(columns)+1)]
valid_types = ['s', 'd', 'c']

search_input = input('Search for types or keywords? T/K: ')
while search_input.lower() != 't' and search_input.lower() != 'k':
    search_input = input('Invalid input\n' + 'Search for types or keywords? T/K: ')

##Show available columns enumerated
print('Available columns:', columnchoices)

if search_input.lower() == 't':
    ##Ask for column input and check validity
    columns_input = input('Pick column numbers: ').replace(' ', '')
    while True:
        try:
            column_nums = [int(column) for column in columns_input.split(',')]
            if len(column_nums) != len(set(column_nums)):
                raise AssertionError
            else:
                for column in column_nums:
                    if column not in valid_cols:
                        raise IndexError
            break
        except ValueError:
            columns_input = input('Incorrect input, expecting integers 1 or larger\n' + 'Pick column numbers: ').replace(' ', '')
        except AssertionError:
            columns_input = input('Incorrect input, duplicate columns chosen\n' + 'Pick column numbers: ').replace(' ', '')
        except IndexError:
            columns_input = input('One or more choices out of range\n' + 'Pick column numbers: ').replace(' ', '')

    ##Ask for type input and check validity
    types_input = input('Check for string, digit or currency? S/D/C per column: ').replace(' ', '')
    while True:
        try:
            types_to_check = [type_input for type_input in types_input.split(',')]
            if len(types_to_check) != len(column_nums):
                raise AssertionError
            else:
                for assertion in types_to_check:
                    if assertion not in valid_types:
                        raise ValueError
            break
        except ValueError:
            types_input = input('Error, wrong input, expecting either S, D or C\n' + 'Check for string, digit or currency? S/D/C per column: ').replace(' ', '')
        except AssertionError:
            types_input = input('Error, pick one type per column chosen\n' + 'Check for string, digit or currency? S/D/C per column: ').replace(' ', '')

    ##Check columns for corresponding type
    ## 's' checks isalpha()
    ## 'd' checks isdigit()
    ## 'c' replaces currency characters ($, .) and checks isdigit()
    for i in range(len(column_nums)):
        column = column_nums[i]
        columntype = types_to_check[i]
        for i in range(1, len(csvFile)):
            value = csvFile[i][column-1]
            if columntype.lower() == 's':
                if value.strip().isalpha() == False:
                    print('Error in text:',value+',','found in column:',column,'line:',i+1)
            elif columntype.lower() == 'd':
                if value.strip().isdigit() == False:
                    print('Error in digit:',value+',','found in column:',column,'line:',i+1)
            elif columntype.lower() == 'c':
                replaced_value = value.replace('$', '').replace('.', '').replace(',', '')
                if replaced_value.strip().isdigit() == False:
                    print('Error in currency:',value+',','found in column:',column,'line:',i+1)

elif search_input.lower() == 'k':
    ##Ask for column input and check validity
    column_num = input('Pick column number: ')
    col_numcheck = False

    while col_numcheck == False:
        try:
            column_num =  int(column_num)
            if column_num < 1 or column_num > len(columns):
                raise IndexError
            else: 
                col_numcheck = True
        except ValueError:
            column_num = input('Incorrect input, expecting integer 1 or larger\n' + 'Pick column number: ')
        except IndexError:
            column_num = input('Column chosen out of range\n' + 'Pick column number: ')        

    ##Ask for keywords to search for
    keywords_input = input('Enter keywords to check: ').replace(' ', '')
    keywords_to_check = [keyword.capitalize() for keyword in keywords_input.split(',')]

    for i in range(1, len(csvFile)):
        value = csvFile[i][column_num-1]
        if value not in keywords_to_check:
            print('Mismatch found:',value+',','in column:',column_num,'line:',i+1)

print('Scan Completed')




