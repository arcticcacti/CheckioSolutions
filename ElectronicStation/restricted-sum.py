# "Restricted sum" downloaded: Sun Jul 31 18:30:41 2016
def checkio(data):
    if not data:
        return 0
    else:
        return data[0] + checkio(data[1:])
