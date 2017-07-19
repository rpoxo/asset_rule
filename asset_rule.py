import bf2
import host

import game.realitycore as rcore
import game.realitytimer as rtimer

import config as C
import advdebug as D

global g_squad_monitor_enabled
global g_squad_timer_check

g_squad_monitor_enabled = False
g_squad_timer_check = None
g_squad_check_interval = 5
g_limited_assets = {}

# ------------------------------------------------------------------------
# Init
# ------------------------------------------------------------------------
def init():
    host.registerGameStatusHandler(onGameStatusChanged)

# ------------------------------------------------------------------------
# DeInit
# ------------------------------------------------------------------------
def deinit():
    global g_squad_monitor_enabled

    g_squad_monitor_enabled = False
    destroySquadCheckTimer()
    host.unregisterGameStatusHandler(onGameStatusChanged)


# ------------------------------------------------------------------------
# onGameStatusChanged
# ------------------------------------------------------------------------
def onGameStatusChanged(status):
    global g_squad_monitor_enabled
    
    #if status == bf2.GameStatus.Playing:
    # registering chatMessage handler
    #host.registerHandler( 'ChatMessage', onChatMessage )
    #host.registerHandler( 'EnterVehicle', onEnterVehicle )
    #host.registerHandler( 'ExitVehicle', onExitVehicle )
    #host.registerHandler( 'VehicleDestroyed', onVehicleDestroyed )
    
    #rcore.clearScreen( player )
    #rcore.blackScreen( player )
    updateLimitedAssets()
    g_squad_monitor_enabled = True
    setSquadCheckTimer()
    #elif status == bf2.GameStatus.EndGame:
    #    g_squad_monitor_enabled = False
    #    destroySquadCheckTimer()
    

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
    D.debugMessage('setting timer, monitorEnabled(%s)' % (g_squad_monitor_enabled))
    
    if g_squad_monitor_enabled:
        D.debugMessage('setting timer, monitorEnabled(%s)' % (g_squad_monitor_enabled))
        g_squad_timer_check = rtimer.Timer( check7Squads, g_squad_check_interval, 1, '' )
        g_squad_timer_check.setRecurring( g_squad_check_interval )
        D.debugMessage('timer set')

def checkSquads( data ):
    if not g_squad_monitor_enabled:
        return
    
    squads_names = {}

    for team_check in range(1,3):
        D.debugMessage('checking squads in team %s' % (team_check))

        squads = host.rcon_invoke( "squadManager.listSquads " + str( team_check ) ).split( '\n' )
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

            #name = None
            #name = ' '.join( words )
            '''
            if rcore.numPlayersOfSquad( g_team_check, _id ) > 0:
                try:
                    name = ' '.join( words )
                except:
                    pass
            '''
            #D.debugMessage(words)
            name = words[0]
            
            
            if team_check not in squads_names.keys():
                squads_names[team_check] = {}

            squads_names[team_check][_id] = name

    #D.debugMessage(squads_names)

    for player in rcore.getPlayers():
        if player.isAIPlayer():
            continue
        checkPlayerInVehicleSquadName(player, squads_names)

def updateLimitedAssets():
    global g_limited_assets
    
    for vehicle_type in C.ASSETS.keys():
        for asset in C.ASSETS[vehicle_type]:
            if asset not in g_limited_assets.keys():
                g_limited_assets[asset] = vehicle_type
    

def checkPlayerInVehicleSquadName(player, squads_names):
    vehicleName = player.getVehicle().templateName
    squadId = player.getSquadId( )
    teamId = player.getTeam()

    if squadId > 9 or squadId == 0:
        return
    else:
        #D.debugMessage(squads_names)
        try:
            squadName = squads_names[teamId][squadId].upper()
        except:
            D.debugMessage('failed to set squad name for team %s squad %s' % (teamId, squadId))

    if vehicleName not in g_limited_assets.keys():
        return
    
    vehicle_type = g_limited_assets[vehicleName]
    if squadName not in C.SQUAD_NAMES[vehicle_type] or :
        D.debugMessage('blacking player %s riding %s in %s:%s' % (player.getName(), vehicleName, squadId, squadName))
        rcore.blackScreen( player )
        rcore.sendMessageToPlayer(player, 2021403, 0)
    elif squadName in C.SQUAD_NAMES[vehicle_type] and vehicleName.split('_')[1] in ['apc', 'ifv']:
        D.debugMessage('blacking player %s riding %s in %s:%s' % (player.getName(), vehicleName, squadId, squadName))
        rcore.blackScreen( player )
        rcore.sendMessageToPlayer(player, 2021403, 0)
    else:
        D.debugMessage('clearing player %s in %s:%s' % (player.getName(), squadId, squadName))
        rcore.clearScreen( player )
        










