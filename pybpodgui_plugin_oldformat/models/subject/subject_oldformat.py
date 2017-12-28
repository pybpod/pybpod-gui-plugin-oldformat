# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os, json

class SubjectOldFormat(object):


    ##########################################################################
    ####### FUNCTIONS ########################################################
    ##########################################################################

    
    def load(self, subject_path, data):
        """
        Load sebject data from filesystem

        :ivar str subject_path: Path of the subject
        :ivar dict data: data object that contains all subject info
        """
        settings_path = os.path.join(subject_path, 'subject-settings.json')
        with open(settings_path, 'r') as output_file:
            data = json.load(output_file)
            self.name = data['name']