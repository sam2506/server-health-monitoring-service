import time
import requests
import configparser
from ggplot import *
from pandas import DataFrame

config = configparser.ConfigParser()
config.read('monitor.conf')

FILENAME = config['DEFAULT']['FILENAME']
TOTAL_TIME_IN_MINS = float(config['DEFAULT']['TOTAL_TIME_IN_MINS'])
TIME_INTERVAL_IN_MINS = float(config['DEFAULT']['TIME_INTERVAL_IN_MINS'])

# Endpoint of the server
URL = "http://localhost:3000/"

serverData = []

def getServerHealth():
    response = requests.get(url = URL)
    data = response.json()
    serverHealth = data['randomNumber'] 
    return serverHealth

# plot graph and save it in a file
def plotGraph(time):
    serverHealth = getServerHealth()
    serverData.append({'TIME in min': time,'ServerHealth': serverHealth})
    dataFrame = DataFrame(serverData)
    print(dataFrame)
    plot = ggplot(aes(x='TIME in min', y='ServerHealth'), data=dataFrame) + \
            geom_point(color='black') + \
            geom_line(alpha=0.25)
    plot.save(FILENAME)

# call plot graph function after every X minutes until total time finishes
currTime = 0
while True:
    if(currTime > TOTAL_TIME_IN_MINS):
        break
    plotGraph(currTime)
    currTime += TIME_INTERVAL_IN_MINS
    time.sleep(TIME_INTERVAL_IN_MINS * 60)