# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os

class SessionOldFormat(object):

    def load(self, session_path, data):
        """

        :param session_path:
        :param data:
        :return:
        """
        self.name = os.path.basename(session_path).replace('.txt', '')
        self.filepath = session_path