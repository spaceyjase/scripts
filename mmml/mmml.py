#!/usr/bin/env python

import gtk
import pygtk

class GUI:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("menudlg.gtk")
        builder.connect_signals({"on_window_destroy" : gtk.main_quit,
                                 "gtk_main_quit" : gtk.main_quit,
                                 "on_buttonOk_clicked" : self.on_ok_clicked,
                                 "on_buttonCancel_clicked" : self.on_cancel_clicked})
        self.window = builder.get_object("dialog1")
        self.window.show()

    def on_ok_clicked(self, widget):
        print "OK clicked!"

    def on_cancel_clicked(self, widget):
        gtk.main_quit()

if __name__ == "__main__":
    gui = GUI()
    gtk.main()
