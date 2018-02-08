 # !/usr/bin/python
# -*- coding: utf-8 -*-

import os, logging, json
from pybpodgui_api.exceptions.api_error import APIError

logger = logging.getLogger(__name__)

class ProjectOldFormat(object):

    def load(self, project_path):
        """
        Load project from a folder.

        :ivar str project_path: Full path of the project to load.
        """

        settings_path = os.path.join(project_path, 'project-settings.json')

        if not os.path.exists(settings_path):
            raise APIError("Project settings path not found: {0}".format(settings_path))

        with open(settings_path, 'r') as input_file:
            data = json.load(input_file)
            self.name = data['name']
            self.path = project_path

            logger.debug("==== LOAD TASKS ====")

            for infolder, path in self.__list_all_tasks_in_folder(project_path):
                task = self.create_task()
                task.load(path, {})

            logger.debug("==== LOAD BOARDS ====")

            # load boards
            for path in self.__list_all_boards_in_folder(project_path):
                board = self.create_board()
                board.load(path, {})

            logger.debug("==== LOAD SUBJECTS ====")

            # load experiments
            for path in self.__list_all_subjects_in_folder(project_path):
                subject = self.create_subject()
                subject.load(path, {})

            logger.debug("==== LOAD EXPERIMENTS ====")

            # load experiments
            for path in self.__list_all_experiments_in_folder(project_path):
                experiment = self.create_experiment()
                experiment.load(path, {})


            logger.debug("==== LOAD FINNISHED ====")


    ##########################################################################
    ####### AUXILIAR FUNCTIONS ###############################################
    ##########################################################################

    def __list_all_experiments_in_folder(self, project_path):
        search_4_dirs_path = os.path.join(project_path, 'experiments')
        if not os.path.exists(search_4_dirs_path): return []
        return sorted([os.path.join(search_4_dirs_path, d) for d in os.listdir(search_4_dirs_path) if
                       os.path.isdir(os.path.join(search_4_dirs_path, d))])

    def __list_all_subjects_in_folder(self, project_path):
        search_4_dirs_path = os.path.join(project_path, 'subjects')
        if not os.path.exists(search_4_dirs_path): return []
        return sorted([os.path.join(search_4_dirs_path, d) for d in os.listdir(search_4_dirs_path) if
                       os.path.isdir(os.path.join(search_4_dirs_path, d))])

    def __list_all_tasks_in_folder(self, project_path):
        path = os.path.join(project_path, 'tasks')
        if not os.path.exists(path): return []
        
        tasksfiles   =  [(False, os.path.join(path, d)) for d in os.listdir(path) if os.path.isfile(os.path.join(path,d)) and d.lower().endswith('.py')]
        tasksfiles   += [(True,  os.path.join(path, d, d+'.py')) for d in os.listdir(path) if os.path.isdir(os.path.join(path,d)) ]
        return sorted(tasksfiles)

    def __list_all_boards_in_folder(self, project_path):
        search_4_dirs_path = os.path.join(project_path, 'boards')
        if not os.path.exists(search_4_dirs_path): return []
        return sorted([os.path.join(search_4_dirs_path, d) for d in os.listdir(search_4_dirs_path) if
                       os.path.isdir(os.path.join(search_4_dirs_path, d))])