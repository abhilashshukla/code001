'''
Created on: Jul 19, 2014
@author: Abhilash Shukla
Description: Project wide constants file for all global properties and objects.
'''
import time
class Constants:

    ACTIVE_LANGUAGE = "English"
    SECURITY_KEY = "fBU7Bngg{L?]#Prf{iX:!ALHq95N9s4)#4ra4a(W~]3ef{8+;<Y!ZdKhU?>bz87" #504-bit WPA Key
    ALLOWED_FILE_FORMAT = ( #List of all file formats allowed for process/upload modules
        'CSV'
    )
    DIRECTORY = { #List of all static directories
        'csv' : "storage/resources/csv/",
        'uploads' : "storage/uploads/"
    }
    FILES = { #List of all static files
        'CsvImportFileName' : "test_shares_data.csv"
    }

    '''
    Other Project Related Constants
    '''
    TOTAL_COMPANIES = 5 #Total companies for create a CSV list

    #Files
    CSV_FILE_PATH = DIRECTORY['csv'] + FILES['CsvImportFileName']

    #Creating filename with datetime now
    CSV_FILE_PUT_PATH = DIRECTORY['uploads'] + time.strftime("%d-%m-%Y") + '-' + time.strftime("%H%M%S") + '.csv'