import paramiko

class Ssh:
    def __init__(self, host, user_name, password):
        print("Connecting to server.")
        self._host = host
        self._user_name = user_name
        self._password = password

    def start(self):
        try:
            client = paramiko.SSHClient()  # 1 Started class . ssh -> client
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # ssh -> client
            client.connect(str(self._host), 22, username=str(self._user_name), password=str(self._password))  # ssh,connect
            return client
        except Exception as e:
            print(e)
            raise (e)
        # return False

    def executor(self, list):
        channel = self._client.get_transport().open_session()
        # Check if connection is made previously
        if (channel):
            for cd in list:
                print("command started: " + str(cd))
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
        self._client.close()
        print('Connection closed!')

# def close(self): # close moved to executor