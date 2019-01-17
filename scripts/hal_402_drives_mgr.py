#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from hal_402_mgr import Hal402Mgr
import time


def call_cleanup():
    # need to unload the userland component here?
    rospy.loginfo("%s: Stopping ..." % hal_402_drives_mgr.compname)
    rospy.loginfo("%s: Stopped" % hal_402_drives_mgr.compname)


if __name__ == '__main__':
    # Create and name node
    hal_402_drives_mgr = Hal402Mgr()
    rospy.on_shutdown(call_cleanup)
    # give some time to settle down until we are going to run
    # if we don't wait, drives can be not properly initialized and then
    # calling state transitions will give error 108's... Bad...
    time.sleep(10)
    try:
        hal_402_drives_mgr.run()
    except rospy.ROSInterruptException:
        rospy.loginfo("%s: ROSInterruptException" % hal_402_drives_mgr.compname)
