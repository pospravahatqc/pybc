import paramiko
ssh = paramiko.SSHClient()

class Ssh(object):

    instance = None
    #
    # def __new__(cls):
    #     if cls.instance is None:
    #         cls.instance = super(Ssh, cls).__new__()
    #     return cls.instance

    def __init__(self, host, user_name, password):
        print("Connecting to server by ssh...")
        self._host = host
        self._user_name = user_name
        self._password = password
        return self.instance

    def start(self): # ==> ssh
        print("Ssh client start...")
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            client.connect(str(self._host), 22, username=str(self._user_name), password=str(self._password))
            self._client = client
            return self
        except Exception as e:
            print(e)
            raise (e)
        # return False

    def check(self): # ==> boolean
        print('Check ssh client is active')
        return self._client.get_transport().is_active()

    def executor(self, list):
        channel = self._client.get_transport().open_session()
        # Check if connection is made previously
        if (channel):
            for cd in list:
                print("command started by executor: " + str(cd))
                stdin, stdout, stderr = self._client.exec_command(str(cd))
                while not stdout.channel.exit_status_ready():
                    # Print stdout data when available
                    if stdout.channel.recv_ready():
                         # Retrieve the first 1024 bytes
                         alldata = stdout.channel.recv(1024)
                    while stdout.channel.recv_ready():
                        # Retrieve the next 1024 bytes
                        alldata += stdout.channel.recv(1024)
                        # Print as string with utf8 encoding
                        print(str(alldata, "utf8"))
        else:
            print("Connection not opened.")


    def close(self): # close moved to executor
        self._client.close()
        print('Connection closed!')