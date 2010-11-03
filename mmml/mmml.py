#!/usr/bin/env python

import gtk
import gtk.glade
import os
from string import Template

class GUI:
    def __init__(self):
        self.dlg = gtk.glade.XML("menudlg.glade")
        self.dlg.signal_autoconnect(self)
        self.template = Template(
        "[Desktop Entry]\n" +
        "Name=${name}\n" + 
        "Exec=${command}\n" +
        "Type=Application\n" +
        "Categories=${category}\n" +
        "Icon=${icon}\n" +
        "Path=${path}")

    def on_button_ok_clicked(self, widget):
        print "OK clicked!"
        # get data
        # valid?
        # open file
        f = open(os.path.expanduser('~') + '/.local/share/applications/testing.desktop', 'w')
        if f is not None:
            data = {}
            data['name'] = 'Testing'
            data['command'] = '/bin/sh'
            data['category'] = 'Office'
            data['icon'] = '/path/to/icon.png'
            data['path'] = '/bin'
            f.write(self.template.substitute(data))
            f.close()
        # Assuming everything is OK ;)
        gtk.main_quit()

        # else
        # display errors if not, set focus?

    def on_button_cancel_clicked(self, widget):
        gtk.main_quit()

if __name__ == "__main__":
    gui = GUI()
    gtk.main()
