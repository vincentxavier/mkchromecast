# This file is part of mkchromecast.

import subprocess
import time


def create_sink():
    sink_name = "Mkchromecast"

    create_sink = ["pactl", "load-module", "module-null-sink", "sink_name=" + sink_name]

    rename_sink = [
        "pacmd",
        "update-sink-proplist",
        sink_name,
        "device.description=" + sink_name,
    ]

    cs = subprocess.Popen(create_sink, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    csoutput, cserror = cs.communicate()

    time.sleep(1)

    rs = subprocess.Popen(rename_sink, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    rsoutput, rserror = rs.communicate()
    return


def remove_sink():
    remove_sink = ["pactl", "unload-module", "module-null-sink"]

    rms = subprocess.Popen(remove_sink, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    rmsoutput, rmserror = rms.communicate()
    return


def check_sink():
    try:
        check_sink = ["pacmd", "list-sinks"]
        chk = subprocess.Popen(
            check_sink, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        chkoutput, chkerror = chk.communicate()
    except FileNotFoundError:
        return None

    try:
        if "Mkchromecast" in chkoutput:
            return True
        else:
            return False
    except TypeError:
        if "Mkchromecast" in chkoutput.decode("utf-8"):
            return True
        else:
            return False
