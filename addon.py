import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addon_handle = int(sys.argv[1])

toRun = addon.getSetting('torun') # returns the string 'true' or 'false'
stopPlayback = true


# my_addon.setSetting('my_setting', 'false')

# line1 = "Hello World!"
# line2 = "We can write anything we want here"
# line3 = "Using Python"
 
# xbmcgui.Dialog().ok(addonname, line1, line2, line3)

# steam_bin=`which steam`
# steam_command = '-tenfoot -enableremotecontrol'

s = subprocess.Popen(steamScript, shell=False)
s.communicate()

 if stopPlayback :
        xbmc.Player().stop()
    params = getFullPath(exePath, url, kiosk, userAgent)
    s = subprocess.Popen(params, shell=False)
    s.communicate()
    xbmcplugin.endOfDirectory(pluginhandle)
    xbmc.executebuiltin("ReplaceWindow(Programs,%s)" % ("plugin://"+addonID+"/"))


# xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# xbmcplugin.endOfDirectory(addon_handle)
