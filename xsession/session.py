#!/usr/bin/env python
#-*- coding: utf-8 -*-

# author : younger shen
# email  : younger.x.shen@gmail.com

"""
    xsession.session
    ~~~~~~~~~~~~~~~~

    session entity to xsession

    :copyright: (c) 2014 by younger shen
    :license: GPL, see LICENSE for more details
    :website: https://github.com/youngershen/xsession
"""
from exception import KeyAlreadyExistsError    

class Session(object):

    def __init__(self):
        self.data = dict()


    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key, None)

    
    def pop(self, key):
        return self.data.popitem()

    def safe_set(self, key, value):
        if key in self.data.keys():
            raise KeyAlreadyExistsError(key)
        else:
            self.data[key] = value


    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()
     
    def clear(self):
        self.data.clear()

    def __unicode__(self):
        return str(self.data)

    def __str__(self):
        return self.__unicode__()

def main():
    raise KeyAlreadyExistsError('sf')
    print "test"


if __name__ == '__main__':
    try:
        main()
    except KeyAlreadyExistsError as e:
        print e
