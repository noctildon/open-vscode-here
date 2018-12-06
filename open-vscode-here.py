# -*- coding: utf-8 -*-

"""This module adds a menu item to the Caja right-click menu which allows to Open Visual Studio Code
   on the Selected Folder/Current Directory at predefined Geometry just through the right-clicking"""

#   open-vscode-here.py version 1.0.0
#
#   Edited by Wei-Chih, Huang <noctildon2@gmail.com> 2018
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.


from gi.repository import Caja, GObject, Gtk, GdkPixbuf
import urllib
import os
import subprocess
import locale
import gettext

APP_NAME = "caja-pyextensions"
LOCALE_PATH = "/usr/share/locale/"
ICONPATH = "/usr/share/icons/gnome/48x48/apps/terminal.png"
# internationalization
locale.setlocale(locale.LC_ALL, '')
gettext.bindtextdomain(APP_NAME, LOCALE_PATH)
gettext.textdomain(APP_NAME)
_ = gettext.gettext
# post internationalization code starts here


class OpenTerminalHere(GObject.GObject, Caja.MenuProvider):
    """Implements the 'Open VScode Here' extension to the caja right-click menu"""

    def __init__(self):
        """Caja crashes if a plugin doesn't implement the __init__ method"""
        try:
            factory = Gtk.IconFactory()
            pixbuf = GdkPixbuf.Pixbuf.new_from_file(ICONPATH)
            iconset = Gtk.IconSet.new_from_pixbuf(pixbuf)
            factory.add("terminal", iconset)
            factory.add_default()
        except:
            pass

    def run(self, menu, selected):
        """Runs the Open VScode Here on the given Directory"""
        uri_raw = selected.get_uri()
        if len(uri_raw) < 7:
            return
        curr_dir = urllib.unquote(uri_raw[7:])
        if os.path.isfile(curr_dir):
            curr_dir = os.path.dirname(curr_dir)

        bash_string = "code " + curr_dir.replace(' ', '\ ')

        subprocess.call(bash_string, shell=True)

    def get_file_items(self, window, sel_items):
        """Adds the 'Open VScode Here' menu item to the Caja right-click menu,
           connects its 'activate' signal to the 'run' method passing the selected Directory/File"""
        if len(sel_items) != 1 or sel_items[0].get_uri_scheme() != 'file':
            return
        item = Caja.MenuItem(name='CajaPython::vscode',
                             label=_('Open VScode Here'),
                             tip=_('Open the Visual Studio code on the Current/Selected Directory'),
                             icon='code')
        item.connect('activate', self.run, sel_items[0])
        return [item]

    def get_background_items(self, window, current_directory):
        """Adds the 'Open VScode Here' menu item to the Caja right-click menu,
           connects its 'activate' signal to the 'run' method passing the current Directory"""
        item = Caja.MenuItem(name='CajaPython::vscode',
                             label=_('Open VScode Here'),
                             tip=_('Open the Visual Studio code on the Current/Selected Directory'),
                             icon='code')
        item.connect('activate', self.run, current_directory)
        return [item]
