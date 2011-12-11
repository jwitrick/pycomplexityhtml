#!/usr/bin/env python

"""
Takes output from PyMetrics and outputs to html preview.

Currently takes the stdout output of PyMetrics but does not parse it.
HTMLFormatter simply wraps it with html <pre> tags.
"""
import sys
import re
from html_elements.html_table import HTMLTable
from html_elements.html_heading import HTMLHeading

class HTMLFormatter(object):
    """Reformats the stdout output of PyMetrics"""
    html_str = """\
    <html>
    <head></head>
    <body>
        <h1>McCabe Code Complexity</h1>
        %(content)s
    </body>
    </html>
    """
    def __init__(self, input_str):
        self.input_str = input_str
        self.html_str = HTMLFormatter.html_str
        
    def _parse_input(self):
        blocks = self.input_str.split('===')
        tables = []
        for section in blocks:
            revelent_section = self.find_mcCabe_blocks(section)
            if revelent_section == "":
                continue
            tables.append(self.create_file_html(revelent_section))
        return tables
    
    def find_mcCabe_blocks(self, section):
        mccabe = section.split('McCabe Complexity ')
        mccabe_list = ""          
        if len(mccabe) == 2:
            mccabe_list = mccabe[1]
        return mccabe_list
    
    def create_file_html(self, file_info):
        lines = file_info.split('\n', 1)
        file_name = self._get_file_name_from_raw(lines[0])
        file_function_lines = self._get_file_function_lines(lines[1])
        funct_info = self._get_function_stats(file_function_lines[1])
        table_items = self._create_file_function_list(funct_info)
        file_html = self._get_file_html_info(file_name, table_items)
        return file_html
    
    def _get_file_name_from_raw(self, raw_file_name):
        file_info = raw_file_name.split('file ', 1)
        return file_info[1]
        
    def _get_file_function_lines(self, input_str):
        return input_str.split('\n\n')
    
    def _get_function_stats(self, input_str):
        return input_str.split('\n')
        
    def _create_file_function_list(self, funct_stats):
        table_items = []
        for s in funct_stats:
            funct_info = s.lstrip().replace('  ', ' ').replace('  ', ' ')
            table_items.append(funct_info)
        return table_items
        
    def _get_file_html_info(self, file_name, table_items):
        html_table = HTMLTable(table_items).__repr__()
        return HTMLHeading("File: %s"%file_name).__repr__() + html_table
        
    def format_html(self):
        tables = self._parse_input()
        output_html = ""
        for values in tables:
            output_html += values
        val_dict = {'content':output_html}
        return self.html_str % val_dict

    

def main():
    """Process the input and output html"""
    args = sys.argv
    f = open(args[1], 'r')
    output = f.read()
    #return HTMLFormatter().format(output)
    return HTMLFormatter(output).format_html()


if __name__ == '__main__':
    print main()
