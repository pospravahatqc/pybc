from abc import ABCMeta, abstractmethod

class BaseGrid:
    __metaclass__ = ABCMeta

    @abstractmethod
    def download(self, list):
        pass

    @abstractmethod
    def start_hub(self, list):
        pass

    @abstractmethod
    def add_node(self, list):
        pass

class GridSetup(BaseGrid): # inheritance of abstraction methods
    def __init__(self, ssh_client):
        self._client = ssh_client

    def download(self, list):
        print 'Download started...'
		# extrun ssh command
        self._client.executor(list)


    def start_hub(self, list):
        print 'Starting hub...'
		# extrun ssh command
        self._client.executor(list)


    def add_node(self, list):
        print 'Adding node...'
		#extrun ssh command
        self._client.executor(list)