# coding:utf8
__license__ = 'GPL 3'
__copyright__ = '2010, Hiroshi Miura <miurahr@linux.com>'
__docformat__ = 'restructuredtext en'

'''
Decode unicode text to an ASCII representation of the text for Japanese.
 Translate unicode string to ASCII roman string.

API is based on the python unidecode,
which is based on Ruby gem (http://rubyforge.org/projects/unidecode/) 
and  perl module Text::Unidecode
(http://search.cpan.org/~sburke/Text-Unidecode-0.04/). 

This functionality is owned by Kakasi Japanese processing engine.

Copyright (c) 2010 Hiroshi Miura
'''

import os, re
from unihandecode.unidecoder import Unidecoder
from unihandecode.unicodepoints import CODEPOINTS
from unihandecode.jacodepoints import CODEPOINTS as JACODES
from unihandecode.pykakasi import kakasi

class Jadecoder(Unidecoder):
    kakasi = None
    codepoints = {}

    def __init__(self):
        self.codepoints = CODEPOINTS
        self.codepoints.update(JACODES)
        self.kakasi = kakasi()

    def decode(self, text):
            result=self.kakasi.do(text)
            return re.sub('[^\x00-\x7f]', lambda x: self.replace_point(x.group()),result)

