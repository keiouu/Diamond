# coding=utf-8

import logging
import threading
import traceback


class Handler(object):
    """
    Handlers process metrics that are collected by Collectors.
    """
    def __init__(self, config=None):
        """
        Create a new instance of the Handler class
        """
        # Initialize Log
        self.log = logging.getLogger('diamond')
        # Initialize Data
        self.config = config
        # Initialize Lock
        self.lock = threading.Lock()

    def _process(self, metric):
        """
        Decorator for processing handlers with a lock, catching exceptions
        """
        try:
            try:
                self.lock.acquire()
                self.process(metric)
            except Exception:
                self.log.error(traceback.format_exc())
        finally:
            if self.lock.locked():
                self.lock.release()

    def process(self, metric):
        """
        Process a metric

        Should be overridden in subclasses
        """
        raise NotImplementedError

    def flush(self):
        """
        Flush metrics

        Optional: Should be overridden in subclasses
        """
        pass
