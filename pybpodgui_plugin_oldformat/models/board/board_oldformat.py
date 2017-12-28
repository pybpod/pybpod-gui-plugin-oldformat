# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os, json

class BoardOldFormat(object):
    
    def load(self, board_path, data):
        """
        Load board data from filesystem

        :ivar str board_path: Path of the board
        :ivar dict data: data object that contains all board info
        """
        settings_path = os.path.join(board_path, 'board-settings.json')
        with open(settings_path, 'r') as output_file:
            data = json.load(output_file)
            
            self.name        = data['name']
            self.serial_port = data['serial_port']
            self._path       = board_path

            self.enabled_bncports       = data.get('enabled-bncports',      None)
            self.enabled_wiredports     = data.get('enabled-wiredports',    None)
            self.enabled_behaviorports  = data.get('enabled-behaviorports', None)