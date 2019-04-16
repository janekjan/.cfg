#!/bin/sh

setxkbmap pl
# xscreensaver -no-splash &
udiskie --no-automount --no-notify --tray &
# xfce4-power-manager &
mate-power-manager &
nm-applet &
pa-applet &
redshift -l 52:21 &
feh --bg-fill /home/janek/pic/wallpaper/psych1.jpg &



