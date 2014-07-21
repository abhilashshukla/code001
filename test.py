'''
Created on: Jul 19, 2014
@author: Abhilash Shukla
Description: Unit test case to test methods for CompanyShare Project
'''
import unittest
from library import lib_csv
from library.constants import Constants as cons

'''
Base class for Unit Testing
'''
class TestFunctions(unittest.TestCase):

    '''
    Test case for Highest Share Price module
    '''
    def test_HighestSharePrice(self):

        filename = cons.CSV_FILE_PATH
        TestOutput = lib_csv.GetData(filename)

        #Sample expected output from the demo CSV file processing
        ExpetedOutput = [('Company-A', '2000', 'Mar', 1000), ('Company-B', '2007', 'Mar', 986), ('Company-C', '1993', 'Jun', 995), ('Company-D', '2002', 'Apr', 999), ('Company-E', '2008', 'Oct', 997)]

        self.assertEqual(ExpetedOutput, TestOutput)

'''
To auto instantiate the unit tests
'''
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)