'''
Created on Jul 19, 2014
@author: Abhilash Shukla
Description: The language dictionary for English language
'''
class English():

    '''
    Gets data from LANG dictionary and sends back
    self    :    For getting "LANG" dictionary from the scope
    code    :    Error or Message code passed to get the relevant text from the language dictionaries
    '''
    def data(self, code):
        if code in self.LANG:
            return self.LANG[code]
        else:
            return False

    LANG = {

        #Message
        'msg_1' : "Thanks the filtered file has been successfully created.",

        #Errors
        'err_1' : "Sorry Processing Failed",
        'err_2' : "Sorry we couldn't generate the CSV successfully.",
        'err_3' : "OOPS! The file contains invalid data.",
        'err_4' : "OOPS! it seams that the file doesn't exist.",
        'err_5' : "OOPS! CSV File generation failed.",
        'err_6' : "OOPS! we guess CSV file isn't there, Please Check!."
    }