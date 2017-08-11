from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    shutil.rmtree("Gogland-%s/jre64" % Version)
    pisitools.insinto("/opt/gogland", "Gogland-%s/*" % Version)
    pisitools.dosym("/opt/gogland/bin/gogland.sh", "/usr/bin/gogland")
