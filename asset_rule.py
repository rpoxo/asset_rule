#import bf2
#import host

#import game.realitycore as rcore
#import game.realitytimer as rtimer

import config as C
#import advdebug as D

global g_squad_monitor_enabled
global g_squad_timer_check

g_squad_monitor_enabled = False
g_squad_timer_check = None
g_squad_check_interval = 5

# ------------------------------------------------------------------------
# Init
# ------------------------------------------------------------------------
def init():
    #host.registerGameStatusHandler(onGameStatusChanged)
    pass

# ------------------------------------------------------------------------
# DeInit
# ------------------------------------------------------------------------
def deinit():
    global g_squad_monitor_enabled
    g_squad_monitor_enabled = False
    destroySquadCheckTimer()
    #host.unregisterGameStatusHandler(onGameStatusChanged)


# ------------------------------------------------------------------------
# onGameStatusChanged
# ------------------------------------------------------------------------
def onGameStatusChanged(status):
    global g_squad_monitor_enabled

    if status == bf2.GameStatus.Playing:
        # registering chatMessage handler
        #D.debugMessage('initializing asset rule')
        #host.registerHandler('ChatMessage', onChatMessage, 1)
        #host.registerHandler( 'EnterVehicle', onEnterVehicle )
        #host.registerHandler( 'ExitVehicle', onExitVehicle )
        #host.registerHandler( 'VehicleDestroyed', onVehicleDestroyed )
        
        #rcore.clearScreen( player )
        #rcore.blackScreen( player )
        g_squad_monitor_enabled = True
        setSquadCheckTimer()


def destroySquadCheckTimer():
    global g_squad_timer_check

    try:
        if g_squad_timer_check:
            g_squad_timer_check.destroy( )
            g_squad_timer_check = None
    except:
        pass


def setSquadCheckTimer():
    global g_squad_timer_check
    
    destroySquadCheckTimer( )

    if not g_squad_monitor_enabled:
        g_squad_timer_check = rtimer.Timer( check7Squads, g_squad_check_interval, 1, '' )
        g_squad_timer_check.setRecurring( g_squad_check_interval )

def check7Squads(data = ''):
    if not g_squad_monitor_enabled:
        return

    squads = host.rcon_invoke( "squadManager.listSquads " + str( team ) ).split( '\n' )
    #D.debugMessage(squads)
    for line in squads:
        line = line.replace( '\n', '' )
        line = line.replace( 'is public.', '' )
        words = line.split( ' ' )

        try:
            _id = words.pop( 0 )
            _id = int( _id.replace( 'id:', '' ) )
            if _id == 0:
                continue
        except:
            continue

        name = None
        if numPlayersOfSquad( team, _id ) > 0:
            try:
                name = ' '.join( words )
            except:
                pass

        g_squadNames[team][_id] = name

    