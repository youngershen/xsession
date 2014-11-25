#!/usr/bin/env python
# -*- coding:utf-8 -*-  

# author : younger shen
# email  : younger.x.shen@gmail.com


"""
    xsession.manager
    ~~~~~~~~~~~~~~~~

    session entity to manage

    :copyright: (c) 2014 by younger shen
    :license: GPL, see LICENSE for more details
    :website: https://github.com/youngershen/xsession
"""

from session import Session

class Manager(object):
    """
       the purpose of manager is to manage all of the session,
       in you app there is should only one *Manage* instance

    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance__'):
            origin = super(Manager, cls)
            cls.__instance__ = origin.__new__(cls, *args, **kwargs)

        return cls.__instance__

    def __init__(self, config=None):
        """
            config is a dict object it contains the configuration of the manage need to know
            
            {
                'backend' : 'file|mysql|redis',
                'dir':'/var/www/html/temp',
                'expire' : '2014',
            }

            backend is for the store engine for session information
            expire is a time by hour for how long the session expires
        """
        self.config = config

    def init_backend(self):
        pass

    def init_file_backend(self):
        self.backend = __import__('backend.file').file.FileBackend()
        self.backend.test()
          



def main():
    a = Manager()
    a.init_file_backend()

if __name__ == '__main__':
    main()
