'''
Created on Jul 19, 2014
@author: Abhilash Shukla
Description: Main modules for this project
'''
from library.constants import Constants as cons
from lang import Lang
from library.lib_csv import GetColumnCount, GetData, ExportData

class Process():

    '''
    This will generate a CSV for filtered data having highest share pricing; company wise.
    '''
    def HighestSharePrice(self, filename=None):

        #CSV File Handling
        if filename == None:
            filename = cons.CSV_FILE_PATH

        #GetColumnCount access the CSV file if file doesn't exist then it will return "False"
        TotalCompanies = GetColumnCount(filename)
        if TotalCompanies != False:
            TotalCompanies = GetColumnCount(filename) - 2
        else:
            return Lang('err_6')

        #Restrict processing if there are ore companies as expected
        if TotalCompanies != cons.TOTAL_COMPANIES:
            return Lang('err_1')

        #Get Filtered Data
        data_list = GetData(filename)
        #Export data in csv file
        process_result = ExportData(cons.CSV_FILE_PUT_PATH, data_list)

        #Check if result of CSV export is true and handle the output accordingly
        if process_result == True:
            print Lang('msg_1')
            return True
        else:
            print Lang('err_2')
            return False

'''
To auto instantiate main modules
'''
Execute = Process().HighestSharePrice()