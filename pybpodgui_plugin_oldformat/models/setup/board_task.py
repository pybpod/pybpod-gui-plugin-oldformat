# !/usr/bin/python3
# -*- coding: utf-8 -*-

class BoardTask(object):

    def load(self, setup_path, data):
        """
        Load setup data from filesystem

        :ivar str setup_path: Path of the setup
        :ivar dict data: data object that contains all setup info
        """
        for data in data.get('variables', []):
            var = self.create_variable()
            var.load(data)