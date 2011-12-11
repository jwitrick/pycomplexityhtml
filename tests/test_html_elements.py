'''
Created on Dec 11, 2011

@author: jwitrick
'''
import unittest
from PyComplexityHTML.html_elements.html_table import HTMLTable 

class TestHTMLElements(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_createTableRow(self):
        html_elements = HTMLTable([])
        val_dict = {"score":8, "function": "testFunction123"}
        table_row = html_elements.createTableRow(val_dict)
        expected = "<tr><td>8</td><td>testFunction123</td></tr>"
        self.assertEqual(expected, table_row.replace(' ', ''))

    def test_createTableRowHeader(self):
        html_elements = HTMLTable([])
        table_header = html_elements.createTableRowHeader()
        expected = "<tr><th>McCabe Score:</th><th>Function Name:</th></tr>"
        self.assertEqual(expected, table_header.replace('  ', ''))
        
    def test_createHTMLTable(self):
        input_data = []
        row_str = "9 testFunction123"
        input_data.append(row_str)
        html_elements = HTMLTable(input_data)
        html_table = html_elements.__repr__()
        expected = '<table border="1"<tr><th>McCabe Score:</th><th>Function Name:</th></tr><tr><td>9</td><td>testFunction123</td></tr></table>'
        self.assertEqual(expected, html_table.replace('  ', ''))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()