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
        # get data
        entryName = self.dlg.get_widget("entryName")
        name = entryName.get_text()
        entryCommand = self.dlg.get_widget("entryCommand")
        listCategory = self.dlg.get_widget("comboboxCategory")
        entryIcon = self.dlg.get_widget("entryIcon")
        buttonPath = self.dlg.get_widget("filechooserbuttonPath")
        # valid?
        try:
            # open file
            desktop_path = os.path.expanduser('~') + '/.local/share/applications'
            if (os.path.exists(desktop_path)):
                f = open(desktop_path + '/' + name + '.desktop', 'w')
                print "Saving %s.desktop to %s" % (name, desktop_path)
                if f is not None:
                    data = {}
                    data['name'] = name 
                    data['command'] = entryCommand.get_text() 
                    data['category'] = listCategory.get_active_text()
                    data['icon'] = entryIcon.get_text()
                    data['path'] = buttonPath.get_filename() 
                    f.write(self.template.substitute(data))
                    f.close()
            else:
                print "'%s' does not exist; cannot save shortcut!" % desktop_path
        # else
        except IOError, e:
            print e
        except:
            print "Something bad happened... did you enter invalid data?"

        # Assuming everything is OK ;)
        gtk.main_quit()

    def on_button_cancel_clicked(self, widget):
        gtk.main_quit()
   
    def on_button_open_command_clicked(self, widget):
        dialog = gtk.FileChooserDialog(title="Browse command...",
                    buttons=(gtk.STOCK_CANCEL,
                             gtk.RESPONSE_CANCEL,
                             gtk.STOCK_OPEN,
                             gtk.RESPONSE_OK))
        if dialog.run() == gtk.RESPONSE_OK:
            command = self.dlg.get_widget("entryCommand")
            command.set_text(dialog.get_filename())
        dialog.destroy()

    def on_button_open_icon_clicked(self, widget):
        filter = gtk.FileFilter()
        filter.set_name("Images")
        filter.add_pattern("*.png")
        filter.add_pattern("*.xpm")
        filter.add_pattern("*.svg")
        filter.add_pattern("*.svg")
        filter.add_pattern("*.jpg")
        dialog = gtk.FileChooserDialog(title="Browse icon...",
                    buttons=(gtk.STOCK_CANCEL,
                             gtk.RESPONSE_CANCEL,
                             gtk.STOCK_OPEN,
                             gtk.RESPONSE_OK))
        dialog.add_filter(filter)
        if dialog.run() == gtk.RESPONSE_OK:
            icon = self.dlg.get_widget("entryIcon")
            icon.set_text(dialog.get_filename())
        dialog.destroy()

if __name__ == "__main__":
    gui = GUI()
    gtk.main()
