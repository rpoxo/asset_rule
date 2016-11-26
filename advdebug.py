# ------------------------------------------------------------------------
# Project Reality debug module by rPoXo
#   wofdebug.py
#
# Description:
#
#   Provides various debug for wofspawner
#
# ------------------------------------------------------------------------

#import bf2 #suprisingly not needed
import host
import time
import os
import cPickle
import socket
import config as C
from datetime import datetime

global G_TIME_START  # global time, being set at start of round

G_TIME_START = 0
SOCK = None
FILENAME_DEBUG = 'debug_objmodv2.log'


# ------------------------------------------------------------------------
# UDP messages:
#   1 : string,
#   2 : position update,
#
#
#
#
#
#
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Init
# ------------------------------------------------------------------------
def init():
    global SOCK

    # create dgram udp socket
    try:
        SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        debugEcho('Created socket')
    except socket.error:
        debugEcho('Failed to create socket')

    setStartTime()
    setLogFilename()

# ------------------------------------------------------------------------
# setStartTime
# setting round start time
# ------------------------------------------------------------------------


def setStartTime():
    global G_TIME_START

    try:
        G_TIME_START = host.timer_getWallTime()
        debugEcho(
            'setStartTime(): successfully set start time at ' +
            str(G_TIME_START))
    except:
        debugEcho('setStartTime(): failed to reset start time')


def setLogFilename():
    global FILENAME_DEBUG

    debugEcho('setting filename')
    FILENAME_DEBUG = 'objmodv2_%s_%s_%s.log' % (
        datetime.now().hour, datetime.now().minute, datetime.now().second)
    debugEcho('filename set to %s' % (FILENAME_DEBUG))

# ------------------------------------------------------------------------
# sendMessageToAll
# send message to all ingame
# ------------------------------------------------------------------------


def sendMessageToAll(msg):
    try:
        host.rcon_invoke("game.sayAll \"" + str(msg) + "\"")
    except:
        host.rcon_invoke(
            "game.sayAll \"" +
            'sendMessageToAll(): failed to display message' +
            "\"")


# ------------------------------------------------------------------------
# echoMessage
# send message to server console
# ------------------------------------------------------------------------
def echoMessage(msg):
    try:
        host.rcon_invoke("echo \"" + str(msg) + "\"")
    except:
        host.rcon_invoke(
            "echo \"" +
            'sendMessageToAll(): failed to display message' +
            "\"")


# ------------------------------------------------------------------------
# time_now
# returning time spent from start
# ------------------------------------------------------------------------
def time_now():
    timenow = round((host.timer_getWallTime() - G_TIME_START), 5)
    return timenow


# ------------------------------------------------------------------------
# time_string_now
# returning formatted time string spent from start
# ------------------------------------------------------------------------
def time_string_now(length=8):
    timestring = str(time_now())
    while len(timestring) < length:
        timestring += '0'
    return timestring


def errorMessage():
    type_, value_, traceback_ = sys.exc_info()
    print 'Traceback:\n'
    print 'Type:   %s' % (type_)
    print 'Value:  %s' % (value_)
    print 'EXCEPTION: %s' % (str(sys.exc_info()[0]))
    print '\n...\n...\n...'
    errType = str(sys.exc_info()[0])
    errPart1 = 'EXCEPTION: ' + errType[errType.find('.') + 1:]
    errPart2 = str(sys.exc_info()[1])

    # \t is TAB
    trace = '\n\tTrace:'
    lastTrace = ''
    while sys.exc_info()[2] is not None:
        if sys.exc_traceback.tb_lineno == 0:
            sys.exc_info()[2] = sys.exc_traceback.tb_next
            continue

        lastTrace = str(sys.exc_traceback.tb_frame.f_code.co_filename) + \
            ' on line ' + str(sys.exc_traceback.tb_lineno)
        trace += '\n\t\t' + lastTrace
        sys.exc_info()[2] = sys.exc_traceback.tb_next

    print errPart1 + '\n\t' + errPart2 + trace + '\n'

# ------------------------------------------------------------------------
# debug
# simple func to create debug output
# ------------------------------------------------------------------------


def debugMessage(msg, senders=None):
    debugs = {
        'file': debugFile,  # debugging in files, set log path first
        'udp': debugUDP,  # UDP debug, sending
        'echo': debugEcho,  # printing debug to server console
        'ingame': debugIngame
    }
    if senders is None:
        for default_debug in C.DEBUGS_DEFAULT:
            debugs[default_debug](msg)
    else:
        for debug in senders:
            debugs[debug](msg)

# ------------------------------------------------------------------------
# debugPublic
# debug ingame
# ------------------------------------------------------------------------


def debugIngame(msg):
    sendMessageToAll(msg)


# ------------------------------------------------------------------------
# debugEcho
# debug in server console
# ------------------------------------------------------------------------
def debugEcho(msg):
    echoMessage(msg)


# ------------------------------------------------------------------------
# debugUDP
# debug to UDP server
# ------------------------------------------------------------------------
def debugUDP(msg, type=1):

    try:
        data = {
            'type': type,
            'msg': msg
        }
        message = cPickle.dumps(data)
        SOCK.sendto(message, (C.CLIENTHOST, C.CLIENTPORT))
    except:
        debugEcho('debugUDP(): failed to send debug message')


# ------------------------------------------------------------------------
# debugFile
# debug in file
# ------------------------------------------------------------------------
def debugFile(msg):

    try:
        # fileName = host.sgl_getModDirectory() + C.spawnerLogPath
        logFile = open(
            host.sgl_getModDirectory() +
            '/python/game/asset_rule/' +
            FILENAME_DEBUG,
            'a')
        logFile.write(str(msg) + '\n')
        logFile.close()
    except:
        pass

# ------------------------------------------------------------------------
# debugFile
# debug in file
# ------------------------------------------------------------------------


def updateMessageUDP(message):
    # message = cPickle.dumps(message)
    debugUDP(message, 2)
