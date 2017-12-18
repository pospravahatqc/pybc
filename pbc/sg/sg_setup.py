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
    def __init__(self, ssh_client, clist, dlist, hlist, nlisst):
        print("Init Grid Setup")
        self._client = ssh_client
        self.clean(clist)
        self.download(dlist)
        self.add_node(nlisst)
        self.start_hub(hlist)

    def download(self, list):
        if self._client.check() == 'True':
            print('Download started...')
            # extrun ssh command
            self._client.executor(list)
            return 'True'
        else:
            print('No connection alive. Downloading stopped')
            return 'False'

    def start_hub(self, list):
        print('Starting hub...')
		# extrun ssh command
        self._client.executor(list)
        return 'True'

    def add_node(self, list):
        print('Adding node...')
		#extrun ssh command
        self._client.executor(list)
        return 'True'

    def clean(self, list):
        print('Cleanning machine...')
        self._client.executor(list)
