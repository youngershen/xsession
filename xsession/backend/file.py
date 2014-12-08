#!/usr/bin/env python
#-*- coding: utf-8 -*-

# author : younger shen
# email  : younger.x.shen@gmail.com

"""
    xsession.backend.file
    ~~~~~~~~~~~~~~~~

    file backend to xsession

    :copyright: (c) 2014 by younger shen
    :license: GPL, see LICENSE for more details
    :website: https://github.com/youngershen/xsession
"""

class FileBackend(object):

    def __init__(self, config):
        self.config = config

    def test(self):
        print "test from filebacnend"

