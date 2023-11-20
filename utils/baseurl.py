import os


def baseurl(pathlocation: str = None):
    app_path = os.path.split(__file__)[0]
    app_path = os.path.realpath(app_path + "/..")
    if pathlocation:
        app_path = os.path.join(app_path, pathlocation)
    return os.path.realpath(app_path)
