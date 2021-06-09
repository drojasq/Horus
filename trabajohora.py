
from datetime import datetime

def run():

    dt = datetime.now()
    print("{}-{}-{}".format(dt.year, dt.month, dt.day) +" " + "{}:{}:{}'".format(dt.hour, dt.minute, dt.second) )

if __name__ == "__main__":
    run()