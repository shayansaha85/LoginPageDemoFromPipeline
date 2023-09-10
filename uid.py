import datetime

def uid():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
    return formatted_datetime

filename = str(uid()) + ".txt"

content = str(uid())
file = open(filename, "w")
file.write(content)
file.close()
