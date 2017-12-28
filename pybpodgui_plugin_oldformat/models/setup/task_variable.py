# !/usr/bin/python3
# -*- coding: utf-8 -*-

class TaskVariable(object):


    def load(self, setup_path, data):
        """
        Load variable data from filesystem

        :ivar str setup_path: Path of the setup
        :ivar dict data: data object that contains all setup info
        """
        self.name     = data['name']
        self.value    = data['value']
        self.datatype = data['datatype']
