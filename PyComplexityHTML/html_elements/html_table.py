'''
Created on Dec 11, 2011

@author: jwitrick
'''

class HTMLTable(object):

    def __init__(self, file_data):
        table_open = """\
        <table border=\"1\"\
        """
        table_close = """\
        </table>\
        """
        self.html_table = table_open
        self.html_table += self.createTableRowHeader()
        self.createHTMLTable(file_data)
        self.html_table += table_close
    
    def __repr__(self):
        return self.html_table
    
    def createHTMLTable(self, file_data):
        for funct in file_data:
            values = funct.split(' ')
            val_dict = {"score":values[0], "function":values[1]}
            self.html_table += self.createTableRow(val_dict)
        
    def createTableRowHeader(self):
        row_str = """<tr>\
            <th>McCabe Score:</th>\
            <th>Function Name:</th>\
            </tr>"""
        return row_str
        
    def createTableRow(self, val_dict):
        row_str = """\
            <tr>\
                <td>%(score)s</td>\
                <td>%(function)s</td>\
            </tr>"""
        return row_str % val_dict
    