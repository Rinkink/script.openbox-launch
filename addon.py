import logging, sys, subprocess

from distutils.spawn import find_executable

import xbmcaddon
import xbmcgui


addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
# addon_handle = int(sys.argv[1])

#TODO: Log to /var or kodi user temp dir, set log level in settings
logLevel = logging.getLevelName('DEBUG')
#logging.basicConfig(filename='/tmp/adon.log',level=logLevel)
logging.basicConfig(stream=sys.stdout,level=logLevel)

logging.debug(addonname + ' starting up.')

toRun = addon.getSetting('torun') # returns the string 'true' or 'false'
stopPlayback = True

# xbmcgui.Dialog().ok(addonname, line1, line2, line3)
# steam_bin=`which steam`
# steam_command = '-tenfoot -enableremotecontrol'

openboxCommand = find_executable('kodi-openbox-runprogram')
steamCommand = find_executable('steam')
logging.debug('openboxCommand:' + openboxCommand)
logging.debug('steamCommand:' + steamCommand)

openbox = '/usr/bin/kodi-openbox-runprogram'
steam = '/usr/games/steam'
steamArguments = [ '-tenfoot', '-enableremotecontrol']
#steamCommand = 'kodi-openbox-runprogram /usr/games/steam -tenfoot -enableremotecontrol'

all = [ openbox, steam ] + steamArguments

logging.debug('allArgs:')
logging.debug(all)

if stopPlayback :
    xbmc.Player().stop()

s = subprocess.Popen([ openbox, steam ] + steamArguments, shell=False)
s.communicate()
# xbmcplugin.endOfDirectory(pluginhandle)
xbmc.executebuiltin("ReplaceWindow(Programs,%s)" % ("plugin://"+addonID+"/"))


# xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# xbmcplugin.endOfDirectory(addon_handle)