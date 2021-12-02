from pygame import *

CHANGE_STAGE = event.custom_type()
_events = {
    QUIT: [],
    KEYDOWN: [],
    KEYUP: [],
    VIDEORESIZE: [],
    JOYBUTTONDOWN: [],
    JOYBUTTONUP: [],
    CHANGE_STAGE: []
}

def init():
    global _events
    event.set_blocked(None)
    for k in _events:
        event.set_allowed(k)

def update():
    global _events
    for k in _events:
        _events[k] = event.get(k)

def isKeyDown(key_code):
    global _events
    for k in _events[KEYDOWN]:
        if k.code == key_code:
            return True
    return False

def check(ev_type):
    global _events
    if len(_events[ev_type]) > 0:
        return _events[ev_type][0]
    return False
