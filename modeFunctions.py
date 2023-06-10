def get_current_mode():
    modeFile = open("currentMode.txt", "r")
    cmode = modeFile.read()
    modeFile.close()

    return cmode


def push_new_mode(new_mode):
    modeFile = open("currentMode.txt", "w")
    modeFile.write(new_mode)
    modeFile.close()


