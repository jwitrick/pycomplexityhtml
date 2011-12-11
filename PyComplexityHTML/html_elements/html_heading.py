'''
Created on Dec 11, 2011

@author: jwitrick
'''

class HTMLHeading(object):
    
    def __init__(self, input_str, header_level="3"):
        header_open = "<h%s>"%str(header_level)
        header_close = "</h%s>"%str(header_level)
        self.header = header_open+"%s"%input_str+header_close
        
    def __repr__(self):
        return self.header
        