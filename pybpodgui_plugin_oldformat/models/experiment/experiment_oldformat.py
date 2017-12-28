# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os, json

class ExperimentOldFormat(object):
    """
    Save and Load actions for Experiment
    """
    
    def load(self, experiment_path, data):
        """
        Load experiment data from filesystem

        :ivar str experiment_path: Path of the experiment
        :ivar dict data: data object that contains all experiment info
        :return: Dictionary with loaded experiment info.
        :rtype: dict
        """
        settings_path = os.path.join(experiment_path, 'experiment-settings.json')
        with open(settings_path, 'r') as output_file:
            data = json.load(output_file)

            self.name = data['name']
            self.task = data.get('task', None)

            for path in self.__list_all_setups_in_folder(experiment_path):
                setup = self.create_setup()
                setup.load(path, {})

            self.path = experiment_path

        return data


    def __list_all_setups_in_folder(self, experiment_path):
        search_4_dirs_path = os.path.join(experiment_path, 'setups')
        if not os.path.exists(search_4_dirs_path):
            return []
        return sorted([os.path.join(search_4_dirs_path, d) for d in os.listdir(search_4_dirs_path) if
                       os.path.isdir(os.path.join(search_4_dirs_path, d))])
