####################################
# QTILE CONFIG BY MAARTEN BRUYNINX #
####################################

# Imports
from typing import List  # noqa: F401
from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os


# Some quick settings
mod = "mod4"
terminal = "kitty -o background_opacity=0.95"
browser = "brave"

# Keybinds
keys = [
    # Rofi
    # Run
    Key([mod], 'space', lazy.spawn('rofi -show run -font "Caskaydia Cove Nerd Font 18"')),
    # Alt-tab like behavior
    Key([mod], 'Tab', lazy.spawn('rofi -show window -font "Caskaydia Cove Nerd Font 18" -theme running')),
    # Open Browser
    Key([mod], 'b', lazy.spawn('brave')),
    # Screenshot
    Key([mod, "shift"], "s", lazy.spawn('spectacle -rbc'), desc="open spectacle"),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Start terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    
    # Restart & Exit
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

# Groups
# I have 9 groups declared, but will autohide the ones not in use
group_names = [
    ("1", {'layout': 'Columns'}),
    ("2", {'layout': 'Columns'},),
    ("3", {'layout': 'Columns'}),
    ("4", {'layout': 'Columns'}),
    ("5", {'layout': 'Columns'}),
    ("6", {'layout': 'Columns'}),
    ("7", {'layout': 'Columns'}),
    ("8", {'layout': 'Columns'}),
    ("9", {'layout': 'Columns'})
]
groups = [Group(name, **kwargs) for name, kwargs in group_names]
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group 

# Colors

background_light = ["#3B4252", "#3B4252"]
background_dark = ["#2E3440", "#2E3440"]
foreground = ["#D8DEE9", "#D8DEE9"]

red = ["#BF616A", "#BF616A"]
green = ["#A3BE8C", "#A3BE8C"]
blue = ["#88c0d0", "#88c0d0"]
yellow = ["#EBCB8B", "#EBCB8B"]
orange = ["#D08770", "#D08770"]
purple = ["#B48EAD", "#B48EAD"]

colors = [["#2e3440", "#2e3440"],
          ["#4c566a", "#4c566a"],
#          ["#88c0d0", "#88c0d0"],
          ["#D8DEE9", "#D8DEE9"],
          ["#434c5e", "#434c5e"],
          ["#3b4252", "#3b4252"],
          ["#81a1c1", "#81a1c1"],
          ["#5E81AC", "#5E81AC"],
          ["#eceff4", "#eceff4"],
          ["#d8dee9", "#d8dee9"],
        ]


darks = [
    ["#2E3440", "#2E3440"],
    ["#3B4252", "#3B4252"],
    ["#434C5E", "#434C5E"],
    ["#4C566A", "#4C566A"],
]

accents =[
    ["#D08770", "#D08770"],
    ["#A3BE8C", "#A3BE8C"],
    ["#B48EAD", "#B48EAD"],
    ["#EBCB8B", "#EBCB8B"],
    ["#5E81AC", "#5E81AC"],
    ["#BF616A", "#BF616A"],
    ["#88c0d0", "#88c0d0"],
]


# Layout theme defines how to place windows in my layout (I only use one layout)
layout_theme = {
    "border_width": 2,
    "margin": 3,
    "border_focus": blue,
    "border_normal": "1D2330",
}
layouts = [
    layout.Columns(**layout_theme)
]

widget_defaults = dict(
    font="Caskaydia Cove Nerd Font",
    fontsize = 23,
    padding = 7,
    background= background_dark,
    foreground = foreground
)
extension_defaults = widget_defaults.copy()

# Incase we need spacing
dark_sep = widget.Sep(linewidth = 0, padding = 6, background = background_dark, foreground = background_dark)
light_sep = widget.Sep(linewidth = 0, padding = 6, background = background_light, foreground = background_light)

# List of widgets, to display on the bottom bar
widgets = [
    # Left side
    # Arch icon to open a terminal
    dark_sep,
    widget.Image(filename = "~/.config/qtile/arch.png",scale = "Trye", mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)}),
    dark_sep,
    # Group box
    dark_sep,
    widget.GroupBox(
        margin_y = 3,
        margin_x = 0,
        padding_y = 5,
        padding_x = 3,
        borderwidth = 3,
        disable_drag = True,
        block_highlight_text_color = colors[2],
        active = darks[3],
        inactive = colors[2],
        rounded = False,
        highlight_color = darks[0],
        highlight_method = "line",
        hide_unused = True,
        this_current_screen_border = colors[2],
        this_screen_border = colors [2],
        spacing = 20, fontsize = 25
    ),
    dark_sep,
    # Powerline-like arrow to right
    widget.TextBox(text = '\ue0b0', background = background_light, foreground = background_dark, padding = 0, fontsize = 43),
    # Middle side
    # Current window
    light_sep,
    widget.WindowName(background = background_light),
    light_sep,
    # Systemtray
    widget.Systray(background = background_light),
    light_sep,
    # Right side
    # Quick settings
    widget.TextBox(text = '\ue0b2', background = background_light, foreground = background_dark, padding = 0, fontsize = 43),
    dark_sep,
    # Updates
    widget.TextBox(text = "  ", padding = 0, foreground = accents[6]),
    widget.CheckUpdates(
        update_interval = 1800,
        distro = "Arch_checkupdates",
        display_format = " {updates}",
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e yay -Syyuu')},
        no_update_string = " 0",
        padding = 0,
        colour_have_updates = blue,
        colour_no_updates = blue,
    ),
    # Volume
    widget.TextBox(text = "    ", padding = 0, foreground = orange,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e alsamixer')},
    ),
    widget.Volume(foreground = orange),
    # Microphone
    widget.TextBox(text = "   ", padding = 0, foreground= orange,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e alsamixer')},
    ),
    widget.Volume(foreground = orange, channel = 'Capture'),
    # Battery
    widget.Battery(battery = 0 ,format='    {percent:2.0%} ', hide_threshold = 0.30, foreground = foreground, update_interval = 1),
    # Wifi
    widget.Net(foreground = red, interface = 'wlan0', format = '   NET {down} '),
    widget.Net(foreground = green, interface = 'wlan0', format = '  NET {up} '),
    # CPU
    widget.CPU(foreground = yellow, format = '  CPU {freq_current}GHz {load_percent}%'
            ,mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bashtop')}
    ),
    # GPU
    widget.NvidiaSensors(foreground = yellow, format = '   GPU {temp}°C', 
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e nvtop')}
    ),
    widget.Memory(foreground = yellow, measure_mem= 'G', format='   MEM{MemUsed: .0f}{mm} ', 
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bashtop')}
    ),
    # Clock
    widget.Clock(foreground = purple, format = "   %a %b %d    %H:%M "),
]

# need to re-create the group box or it won't work on 2 monitors
group_and_middle = [
        # Group box   
        dark_sep,
        widget.GroupBox(
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 3,
            borderwidth = 3,
            disable_drag = True,
            block_highlight_text_color = colors[2],
            active = darks[3],
            inactive = colors[2],
            rounded = False,
            highlight_color = darks[0],
            highlight_method = "line",
            hide_unused = True,
            this_current_screen_border = colors[2],
            this_screen_border = colors [2],
            spacing = 20, fontsize = 25
        ),
        widget.TextBox(text = '\ue0b0', background = background_light, foreground = background_dark, padding = 0, fontsize = 43),
        # Middle side
        # Current window
        light_sep,
        widget.WindowName(background = background_light),
        light_sep,
        # Systemtray
        widget.Systray(background = background_light),
        light_sep,
]

# Append the bar to the bottom of the screen

screens = [
    Screen(
        bottom=bar.Bar(widgets,50)
    ),
    Screen(
        bottom=bar.Bar(widgets[:4] + group_and_middle + widgets[11:],50)),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    Click([mod, 'shift'], "Button1", lazy.window.disable_floating()),
    Click([mod], "Button1", lazy.window.bring_to_front()) 
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], **layout_theme)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "LG3D"
