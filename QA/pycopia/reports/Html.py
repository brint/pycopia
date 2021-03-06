#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Report object that creats XHTML format reports.

"""

from pycopia import reports
from pycopia import timelib

def escape(s):
    s = s.replace("&", "&amp;") # Must be first
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    s = s.replace('"', "&quot;")
    return s


class XHTMLFormatter(reports.NullFormatter):
    MIMETYPE = "text/html"
    _MSGTYPESUB = {
        "PASSED":     '<span class="passed">PASSED</span>',
        "FAILED":     '<span class="failed">FAILED</span>',
        "EXPECTED_FAIL":  '<span class="expectedfail">EXPECTED FAIL</span>',
        "INCOMPLETE":    '<span class="incomplete">INCOMPLETE</span>',
        "ABORTED":    '<span class="aborted">ABORTED</span>',
        "INFO":       '<span class="info">INFO</span>',
        "DIAGNOSTIC": '<span class="diagnostic">DIAGNOSTIC</span>',
    }

    def initialize(self):
        return """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Test Results</title>
   <style type="text/css">
body {background: white; color: black;
    border: 0; padding: 0;
}
a:link {
    background-color: transparent;
}
a:visited   {
    background-color: transparent;
}
a:active    {
    background-color: transparent;
}
a:hover {
    background-color: transparent;
    text-decoration:underline;
}
img {
    border: 10px;
    padding: 0.25in;
}

pre {
    padding: 0;
    margin-left: 0.5in;
}

pre.analysis {
   color: #225500;
}

h1, h2, h3, h4, h5, h6 {
    font-family: Arial, sans-serif;
    color: #333;
    background: transparent;
    margin-bottom:0;
    padding:0;
}
h1 {
    font-size: 135%;
    padding: 0;
    padding-top: 10px;
    margin-bottom: 0;
}

h2 {
    font-size:  115%;
    text-decoration: underline;
    padding: 0;
    padding-bottom: 10px;
    margin-bottom: 0;
    margin-left: .5in;
}
h3, h4, h5 {
    font-size: 1.0em;
    margin-left: 0.75in;
}
p {
   margin: 0;
   padding: 0;
   margin-left: .5in;
   font-family: monospace;
}

p.note {
  color: #ff0000;
  padding: 5pt;
}

span.passed {
    color: green;
    font-weight: bold;
}
span.failed {
    color: red;
    font-weight: bold;
}
span.expectedfail {
    color: #dd0000;
    font-weight: normal;
}
span.incomplete {
    color: yellow;
}
span.aborted {
    color: yellow;
}
span.diagnostic {
    color: #F85AF8;
}

span.info {
    color: gray;
}

   </style>
  </head>
  <body>
"""

    def finalize(self):
        return "\n  </body>\n</html>\n"

    def page(self):
        return "<br><hr><br>\n"

    def title(self, title):
        s = ["<h1>"]
        s.append(escape(title))
        s.append("</h1>\n")
        return "".join(s)

    def heading(self, text, level=1):
        s = []
        s.append("\n<h%s>" % (level,))
        s.append(escape(text))
        s.append("</h%s>\n" % (level,))
        return "".join(s)

    def paragraph(self, text):
        return "<p>%s</p>\n" % (escape(text),)

    def message(self, msgtype, msg, level=1):
        if msgtype.find("TIME") >= 0:
            msg = timelib.localtimestamp(msg)
        msg = str(msg)
        msgtype = self._MSGTYPESUB.get(msgtype, msgtype)
        if msg.find("\n") > 0:
            return "<p>%s:</p>\n<pre>%s</pre>\n" % (msgtype, escape(msg))
        else:
            return '<p>%s: %s</p>\n' % (msgtype, escape(msg))

    def text(self, text):
        return "<pre>%s</pre>\n" % (text,)

    def analysis(self, text):
        return '<h3>Analysis</h3>\n<pre class="analysis">%s</pre>\n' % (text,)

    def url(self, text, url):
        return '<p>%s: <a href="%s">%s</a></p>\n' % (text, url, url)

    def summaryline(self, entry):
        sum = "<pre>%s\n</pre>\n" % (entry,)
        sum =  sum.replace("PASSED", self._MSGTYPESUB["PASSED"])
        sum =  sum.replace("FAILED", self._MSGTYPESUB["FAILED"])
        sum =  sum.replace("EXPECTED_FAIL", self._MSGTYPESUB["EXPECTED_FAIL"])
        return sum

    def section(self):
        return "<hr>\n"



if __name__ == "__main__":
    report = reports.get_report((None, "-", "text/html",))
    report.initialize()
    report.info("Some self test info.")
    report.passed("yippee!")
    report.add_analysis("Analyze this!")
    report.finalize()

# End of file
