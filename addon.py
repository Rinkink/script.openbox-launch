import logging, sys, subprocess

from distutils.spawn import find_executable

import xbmcaddon
import xbmcgui

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
# addon_handle = int(sys.argv[1])

# Logging setup
#TODO: Log to /var or kodi user temp dir, set log level in settings
logLevel = logging.getLevelName('DEBUG')
fileLogger = logging.FileHandler('/tmp/adon.log')
fileLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logging.getLogger().addHandler(fileLogger)
stderrLogger=logging.StreamHandler()
stderrLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logging.getLogger().addHandler(stderrLogger)
logging.getLogger().setLevel(logLevel)

logging.debug(addonname + ' starting up.')

tempPath = xbmc.translatePath('special://temp')
logPath = xbmc.translatePath('special://logpath')
logging.debug('temp: [' + tempPath + ']')
logging.debug('logpath: [' + logPath + ']')

toRun = addon.getSetting('torun') # returns the string 'true' or 'false'
stopPlayback = True

openboxCommand = find_executable('kodi-openbox-runprogram')
steamCommand = find_executable('steam')
logging.debug('openboxCommand:' + openboxCommand)
logging.debug('steamCommand:' + steamCommand)

openbox = '/usr/bin/kodi-openbox-runprogram'
steam = '/usr/games/steam'
steamArguments = [ '-tenfoot', '-enableremotecontrol']

all = [ openbox, steam ] + steamArguments

logging.debug('allArgs:')
logging.debug(all)

if stopPlayback :
    xbmc.Player().stop()

logging.debug('Running command')

try:
	s = subprocess.Popen([ openbox, steam ] + steamArguments, shell=False)
	s.communicate()
except Exception as e:
	logging.error(e)
else:
	logging.debug('Replacing window')
	xbmc.executebuiltin("ReplaceWindow(Programs,%s)" % ("plugin://"+addonID+"/"))

logging.debug('Done?')
