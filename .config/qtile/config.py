
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
import os
import subprocess

try:
    from typing import List  # noqa: F401
except ImportError:
    pass

#CONSTANTS
BORDER_FOCUS = 'bd5b56'
BORDER_NORMAL = 'aaaaaa'
BAR_BACKGROUND = "#2E3440"
mod = "mod4"

# HOME = os.path.expanduser('~')
# WALLPAPER_DIR = os.path.expanduser('~/pic/wallpaper/psych1.jpg')

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),
    # Switch window focus to other pane(s) of stack
    Key([mod], "Tab", lazy.layout.next()),

    # Other windows controls
    Key([mod], "m", lazy.window.toggle_fullscreen()),
    # Key([mod], "n", lazy.window.toggle_minimize()),
    Key([mod], "v", lazy.window.toggle_floating()),
    Key([mod], "h", lazy.layout.shrink()),
    Key([mod], 'l', lazy.layout.grow()),
    
    # Swap panes of split stack
    # Key([mod, "shift"], "Tab", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod, "control"], "m", lazy.layout.toggle_split()),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout()),
    Key([mod, "control"], "c", lazy.window.kill()),

    Key([mod], "z", lazy.spawn("xscreensaver-command -lock")),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control", "shift"], "q", lazy.shutdown()),
    Key([mod, "control", "shift"], "a", lazy.spawn("sudo pm-hibernate")), #remember about setting permisssions in visudo or polkit
    Key([mod, "control", "shift"], "z", lazy.spawn("sudo pm-suspend-hybrid")),

    Key([mod], "r", lazy.spawn("rofi -combi-modi window,drun -show combi -modi combi")),
    Key([mod], "s", lazy.spawncmd()),
    Key([mod], "Return", lazy.spawn("terminator")),
]

# lazy.spawn("feh --bg-fill /home/janek/pic/wallpaper/psych1.jpg")

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.MonadTall(
        margin=5,
        border_focus=BORDER_FOCUS,
        border_normal=BORDER_NORMAL
    ),
    #Replace with Zoomy (keybinding for fullscreen)?
    layout.Max(
        
    ),
    # Replace Stack with Wmii?
    #layout.Stack(
    #    num_stacks=2,
    #    margin = 5,
    #    border_focus=BORDER_FOCUS,
    #    border_normal=BORDER_NORMAL
    #),
    #layout.Floating(
    #    border_focus=BORDER_FOCUS,
    #    border_normal=BORDER_NORMAL
    #)
    #layout.Tile()
]

widget_defaults = dict(
    font='mononoki',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                # widget.WindowName(),
                widget.WindowTabs(
                    selected = ('*','*'),
                    separator = '|'
                ),
                # widget.Cmus(),
                widget.HDDBusyGraph(),
                widget.CPUGraph(line_width=2),
                widget.Net(interface='wlp3s0'),
                widget.TextBox("| Janek", name="default"),
                widget.Systray(),
                widget.Clock(format='| %a, %d.%m.%y | %H:%M'),
                widget.CurrentLayoutIcon(),
                # widget.Wallpaper(
                #     directory='/home/janek/pic/wallpaper/',
                #     random_selection=True
                # )
            ],
            24,
            background=BAR_BACKGROUND,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], border_focus=BORDER_FOCUS, border_width=2, border_normal=BORDER_NORMAL)
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
