# -*- coding: utf-8 -*-
"""
    Logfile IP Error Handler
"""

class LogfileError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)        

    def __str__(self):
        return f"Error: {self.message}"