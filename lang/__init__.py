'''
Created on Jul 19, 2014
@author: Abhilash Shukla
Description:Import appropriate language library as per settings
'''
from library.constants import Constants as cons
from lang_en import English

'''
Get relevant text as per the active language. NOTE: Language handling can also be managed dynamically, but not covered in this project scope
code    :    Error or Message code passed to get the relevant text from the language dictionaries
'''
def Lang(code):
    if cons.ACTIVE_LANGUAGE == "English":
        lang = English().data(code)

        if lang != False:
            return English().data(code)
        else:
            return ""