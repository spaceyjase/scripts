#!/usr/bin/env python

import gtk
import gtk.glade

class GUI:
    def __init__(self):
        self.dlg = gtk.glade.XML("menudlg.glade")
        self.dlg.signal_autoconnect(self)

    def on_button_ok_clicked(self, widget):
        print "OK clicked!"
        # Assuming everything is OK ;)
        gtk.main_quit()

    def on_button_cancel_clicked(self, widget):
        gtk.main_quit()

if __name__ == "__main__":
    gui = GUI()
    gtk.main()
