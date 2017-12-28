# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os, glob, json


class SetupOldFormat(object):

    def load(self, setup_path, data):
        """
        Load setup data from filesystem

        :ivar str setup_path: Path of the setup
        :ivar dict data: data object that contains all setup info
        """
        settings_path = os.path.join(setup_path, 'setup-settings.json')
        self.path = setup_path

        with open(settings_path, 'r') as output_file:
            data = json.load(output_file)
            self.name  = data['name']
            self.board = data.get('board', None)
            for subject_name in data.get('subjects', []):
                self += self.project.find_subject(subject_name)

            self.board_task.load(setup_path, data)

        for filepath in self.__list_all_sessions_in_folder(setup_path):
            session = self.create_session()
            session.load(filepath, {})

        self._sessions = sorted(self.sessions, key=lambda x: x.started)

    def __list_all_sessions_in_folder(self, setup_path):
        search_4_files_path = os.path.join(setup_path, '*.txt')
        return sorted(glob.glob(search_4_files_path))
