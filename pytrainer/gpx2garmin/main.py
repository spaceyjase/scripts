#!/usr/bin/env python

from optparse import OptionParser
import os

class Main:
    def __init__(self, options):
        self.limit = options.limit
        self.device = options.device
        self.gpxfile = options.gpxfile
        self.tmpgpxfile = "/tmp/_gpx2garmin.gpx"

    def prepareGPX(self):
        # add a name to the gpx data in the <trk> stanza
        os.system('grep "<name>.*</name>" %s > /tmp/_gpx2garmin' % self.gpxfile)
        os.system('sed "/<trk>/r /tmp/_gpx2garmin" %s > %s' % (self.gpxfile, self.tmpgpxfile))
        
    def exportGPX(self):
        cmd = "gpsbabel -t -i gpx -f %s -o garmin " % self.tmpgpxfile
        if self.limit is not None:
            cmd = cmd + " -x simplify,count=%s" % self.limit
        cmd = cmd + " -F %s" % self.device
        os.system(cmd)

    def run(self):
        self.log = "Export of '%s' " % self.gpxfile
        try:
            self.prepareGPX()
            self.exportGPX()
            self.log = self.log + "successful!" 
        except:
            self.log = self.log + "failed!"
        return self.log

parser = OptionParser()
parser.add_option("-d", "--gpx2garmindevice", dest="device")
parser.add_option("-l", "--gpx2garminmaxpoints", dest="limit")
parser.add_option("-g", "--gpxfile", dest="gpxfile")
parser.add_option("-i", "--idrecord", dest="idrecord")
(options,args) =  parser.parse_args()

main = Main(options)
print main.run()
