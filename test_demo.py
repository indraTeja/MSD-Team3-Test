import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
from TC004_Nurse_Patient_CRUD import *
from TC010_press import *
from TC001_Hospital_CRUD import *
from TC003_NurseLogin import *
from TC011_Contact_us import *
from TC009_bed_availability import *
from TC002_Nurse_CRUD import *
from TC005_Nurse_Add_Bed import *

class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        print('set up')

    def runTest(self):
        print('run test')

# def suite():
#     # test_suite = unittest.TestSuite()
#
#
#     tc_1 = unittest.TestLoader().loadTestsFromTestCase(HomeTest_1)
#     # tc_2 = unittest.TestLoader().loadTestsFromTestCase(HomeTest_2)
#
#     # create a test suite combining search_text and home_page_test
#     test_suite = unittest.TestSuite([tc_1])
#
#     # test_suite.addTest(unittest.loader.findTestCases(tc1))
#     # test_suite.addTest(unittest.loader.findTestCases(tc2))
#
#     return test_suite
#
#
# mySuit = suite()
#
# runner = unittest.TextTestRunner()
# runner.run(mySuit)
#
# unittest.TextTestResult().run(mySuit)
