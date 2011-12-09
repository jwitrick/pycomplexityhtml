#!/usr/bin/env python

"""
Takes output from PyMetrics and outputs to html preview.

Currently takes the stdout output of PyMetrics but does not parse it.
HTMLFormatter simply wraps it with html <pre> tags.
"""
import sys

class HTMLFormatter(object):
    """Reformats the stdout output of PyMetrics"""
    html_str = """\
    <html>
    <head></head>
    <body>
        <h1>McCabe Code Complexity</h1>
        <pre>%(content)s</pre>
    </body>
    </html>
    """
    
    def format(self, metrics_str):
        lines = metrics_str.split("\n")
        header = [l for l in lines if l.startswith("==") and l.endswith("==")][0].replace("=", "").strip()
        val_dict = {"content":metrics_str}
        return self.html_str % val_dict

def main():
    """Process the input and output html"""
    args = sys.argv
    f = open(args[1], 'r')
    output = f.read()
    return HTMLFormatter().format(output)


if __name__ == '__main__':
    print main()
