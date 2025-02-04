# Keepmenu Installation

[Configuration](configure.md) - [Usage](usage.md)

## Requirements

1. Python 3.6+.
2. [Pykeepass][1] >= 4.0.0 and [pynput][2]. Install via pip or your
   distribution's package manager, if available.
3. Dmenu or Rofi. Rofi configuration/theming should be done via Rofi themes.
4. (optional) Pinentry. Make sure to set which flavor of pinentry command to use
   in the config file.
5. (optional) xdotool or ydotool (for Wayland). If you have a lot of Unicode
   characters or use a non-U.S.  English keyboard layout, xdotool is necessary
   to handle typing those characters.

#### Archlinux

`$ sudo pacman -S python-pip dmenu`

#### Fedora 34

`$ sudo dnf install python3-devel dmenu`

#### Ubuntu 21.10

Ensure Universe repository is enabled.

`$ sudo apt install python3-pip suckless-tools`

## Install (recommended)

`$ pip install --user keepmenu`

Add ~/.local/bin to $PATH

### Install (virtualenv)

    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install keepmenu

Link to the executable `venv/bin/keemenu` when assigning a keyboard shortcut.

### Install (virtualenv) from git

    $ git clone https://github.com/firecat53/keepmenu
    $ cd keepmenu
    $ make
    $ make run OR ./venv/bin/keepmenu
    
### Install (git)
  
    $ git clone https://github.com/firecat53/keepmenu
    $ cd keepmenu
    $ git checkout <branch> (if desired)
    $ pip install --user . OR
    $ pip install --user -e . (for editable install)

### Available in [Archlinux AUR][1]

[1]: https://aur.archlinux.org/packages/keepmenu-git "Archlinux AUR"
[2]: https://github.com/moses-palmer/pynput "pynput"
