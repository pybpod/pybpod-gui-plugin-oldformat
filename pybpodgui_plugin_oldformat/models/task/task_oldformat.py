# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os

class TaskOldFormat(object):
    """
    Task I/O operations
    """

    def load(self, task_path, data):
        """
        Load variable data from filesystem

        :ivar str task_path: Path of the task
        :ivar dict data: data object that contains all task info
        """
        self.name = os.path.splitext(os.path.basename(task_path))[0]
        self.path = task_path