#!/usr/bin/env python
# -*- coding:utf-8 -*-  

# author : younger shen
# email  : younger.x.shen@gmail.com


"""
    xsession.exception
    ~~~~~~~~~~~~~~~~

    xsession exceptions

    :copyright: (c) 2014 by younger shen
    :license: GPL, see LICENSE for more details
    :website: https://github.com/youngershen/xsession
"""
class KeyAlreadyExistsError(Exception):

    def __init__(self, key = None, message = None):
        """docstring for __init__("""
        self.key = key
        self.message = message


    def __unicode__(self):
        return  ""

    def __str__(self):

        return ""
