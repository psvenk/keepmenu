"""Set global variables. Read the config file. Create default config file if one
doesn't exist.

"""
import configparser
import locale
import os
import shlex
from subprocess import call
import sys
from os.path import exists, expanduser

from keepmenu.menu import dmenu_err

# Setup logging for debugging. Usage: logger.info(...)
# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler('keepmenu.log', mode='w')
# formatter = logging.Formatter('%(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

AUTH_FILE = expanduser("~/.cache/.keepmenu-auth")
CONF_FILE = expanduser("~/.config/keepmenu/config.ini")
SERCRET_VALID_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

ENV = os.environ.copy()
ENV['LC_ALL'] = 'C'
ENC = locale.getpreferredencoding()
CACHE_PERIOD_DEFAULT_MIN = 360
CACHE_PERIOD_MIN = CACHE_PERIOD_DEFAULT_MIN
SEQUENCE = "{USERNAME}{TAB}{PASSWORD}{ENTER}"
MAX_LEN = 24
CONF = configparser.ConfigParser()

def reload_config():
    """Reload config file. Primarly for use with tests.

    """
    # pragma pylint: disable=global-statement
    global CACHE_PERIOD_MIN, \
        CACHE_PERIOD_DEFAULT_MIN, \
        CONF, \
        MAX_LEN, \
        ENV, \
        ENC, \
        SEQUENCE
    # pragma pylint: enable=global-variable-undefined
    CONF = configparser.ConfigParser()
    if not exists(CONF_FILE):
        try:
            os.mkdir(os.path.dirname(CONF_FILE))
        except OSError:
            pass
        with open(CONF_FILE, 'w') as conf_file:
            CONF.add_section('dmenu')
            CONF.set('dmenu', 'dmenu_command', 'dmenu')
            CONF.add_section('dmenu_passphrase')
            CONF.set('dmenu_passphrase', 'obscure', 'True')
            CONF.set('dmenu_passphrase', 'obscure_color', '#222222')
            CONF.add_section('database')
            CONF.set('database', 'database_1', '')
            CONF.set('database', 'keyfile_1', '')
            CONF.set('database', 'pw_cache_period_min', str(CACHE_PERIOD_DEFAULT_MIN))
            CONF.set('database', 'autotype_default', SEQUENCE)
            CONF.write(conf_file)
    try:
        CONF.read(CONF_FILE)
    except configparser.ParsingError as err:
        dmenu_err("Config file error: {}".format(err))
        sys.exit()
    if CONF.has_option('dmenu', 'dmenu_command'):
        command = shlex.split(CONF.get('dmenu', 'dmenu_command'))
    if "-l" in command:
        MAX_LEN = int(command[command.index("-l") + 1])
    else:
        MAX_LEN = 24
    if CONF.has_option("database", "pw_cache_period_min"):
        CACHE_PERIOD_MIN = int(CONF.get("database", "pw_cache_period_min"))
    else:
        CACHE_PERIOD_MIN = CACHE_PERIOD_DEFAULT_MIN
    if CONF.has_option('database', 'autotype_default'):
        SEQUENCE = CONF.get("database", "autotype_default")
    if CONF.has_option("database", "type_library"):
        if CONF.get("database", "type_library") == "xdotool":
            try:
                call(['xdotool', 'version'])
            except OSError:
                dmenu_err("Xdotool not installed.\n"
                          "Please install or remove that option from config.ini")
                sys.exit()
        elif CONF.get("database", "type_library") == "ydotool":
            try:
                call(['ydotool'])
            except OSError:
                dmenu_err("Ydotool not installed.\n"
                          "Please install or remove that option from config.ini")
                sys.exit()


reload_config()

# vim: set et ts=4 sw=4 :
