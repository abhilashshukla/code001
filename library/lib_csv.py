'''
Created on Jul 19, 2014
@author: Abhilash Shukla
Description: This file will contain all reusable csv processing functionality
'''
import csv
from collections import OrderedDict, namedtuple
from lang import Lang

'''
Count number of columns in a CSV file
csv_file    :    Full qualified path of CSV file
'''
def GetColumnCount(csv_file):

    try:
        #Open a CSV File and get total number of columns
        with open(csv_file, 'rb') as csvfile:
            try:
                reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
                first_row = next(reader)
                return len(first_row)
            except Exception as e:
                print "{0} More Information: {1}".format(Lang('err_3'), e)
                return False
    except Exception as e:
        print "{0} More Information: {1}".format(Lang('err_4'), e)
        return False;

'''
Get data from CSV file
csv_file    :    Full qualified path of CSV file
'''
def GetData(csv_file):

    try:
        #Open a CSV File and get contents
        with open(csv_file, 'rb') as csvfile:
            try:
                reader = csv.reader(csvfile)

                #Create Ordered tuple
                DataTuple = namedtuple('FilteredData', ['price', 'year', 'month'])
                Odict = OrderedDict()

                #Read Company Names
                CompanyNames = next(reader)[2:]
                for name in CompanyNames:
                    Odict[name] = DataTuple(0, 'year', 'month')

                #Generate data row by row
                for row in reader:
                    year, month = row[:2]
                    for name, price in zip(CompanyNames, map(int, row[2:])):
                        if Odict[name].price < price:
                            Odict[name] = DataTuple(price, year, month)
                Data = [(name, data.year, data.month, data.price) for name, data in Odict.items()]
                return Data
            except Exception as e:
                return "{0} More Information: {1}".format(Lang('err_3'), e)
    except Exception as e:
        return "{0} More Information: {1}".format(Lang('err_4'), e)

'''
Export data to CSV file
csv_file    :    Full qualified path for CSV file destination
data_list   :    List of data returned via lib_csv.GetData
'''
def ExportData(csv_file, data_list):
    try:
        with open(csv_file, 'w') as f:
            #Write data to CSV file
            w = csv.writer(f)
            w.writerow(('Company Name', 'Year', 'Month', 'Price'))
            w.writerows([(name, year, month, price) for name, year, month, price in data_list])
            return True
    except Exception as e:
        return "{0} More Information: {1}".format(Lang('err_5'), e)