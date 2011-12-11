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
        self.mccable = re.compile("McCabe Complexity .*")
        self.input_str = input_str
        self.html_str = HTMLFormatter.html_str
    
    def format_html(self):
        tables = self.find_McCabe_Blocks()
        output_html = ""
        for values in tables:
            output_html += values
        val_dict = {'content':output_html}
        return self.html_str % val_dict
    
    def find_McCabe_Blocks(self):
        blocks = self.input_str.split('===')
        tables = []
        for section in blocks:
            mccabe = section.split('McCabe Complexity ')          
            if len(mccabe) == 2:
                m = mccabe[1]
                lines = m.split('\n', 1)
                file_name = self._get_file_name_from_raw(lines[0])
                lines = lines[1].split('\n\n')
                table_items = []
                stats = lines[1].split('\n')
                for s in stats:
                    funct_stats = s.lstrip().replace('  ', ' ').replace('  ', ' ')
                    table_items.append(funct_stats)
                table = HTMLTable(table_items).__repr__()
                file_html = HTMLHeading("File: %s"%file_name).__repr__() + table
                
                tables.append(file_html)
        return tables

    def _get_file_name_from_raw(self, raw_file_name):
        file_info = raw_file_name.split('file ', 1)
        return file_info[1]

def main():
    """Process the input and output html"""
    args = sys.argv
    f = open(args[1], 'r')
    output = f.read()
    #return HTMLFormatter().format(output)
    return HTMLFormatter(output).format_html()


if __name__ == '__main__':
    print main()
