#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import pisitools, shelltools, get

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("ar xf google-earth-stable_%s-r0_amd64.deb" % get.srcVERSION())
    shelltools.system("tar xvf data.tar.xz")
    shelltools.system("mv opt/google/earth/free/google-earth.desktop .")

def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/usr", "usr/bin")
    pisitools.insinto("/usr/share/applications", "google-earth.desktop")
    pisitools.dosym("ld-linux-x86-64.so.2", "/lib/ld-lsb-x86-64.so.3")
