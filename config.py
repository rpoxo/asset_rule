# address and port for listening UDP server
SERVERHOST = 'localhost'  # Symbolic name meaning all available interfaces
SERVERPORT = 8888  # Arbitrary non-privileged port

# address and port for streaming client
CLIENTHOST = 'localhost'  # Symbolic name meaning all available interfaces
CLIENTPORT = 8888  # Arbitrary non-privileged port

# path to expor file
# keep in mind that if path does not exist - log file won't be created
LOGFILENAME = '/asset_rule.log'


# setting debug level, uncomment required debug
DEBUGS = [
    'file',  # debugging in files, set log path first
    'udp',  # UDP debug, sending
    'echo',  # printing debug to server console
    'ingame'  # printing debug ingame
]

DEBUGS_DEFAULT = [
    'file', # debugging in files, set log path first
    'udp', # UDP debug, sending
    'echo',  # printing debug to server console
    #'ingame' # printing debug ingame
]


SQUAD_NAMES = {
    1 : ['CAS', 'TRANS'],
    2 : ['TRANS']
    3 : ['TANK']
    }

ASSETS = {
    1 : [],
    2 : [],
    3 : []
    }