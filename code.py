import subprocess
import json

bashCommand = "docker cp f9c0011705d3:/var/ossec/logs/alerts/alerts.json ./alerts.json"
logwriterCommand = "docker exec f9c0011705d3 /gerenciatf/logwriter.sh 1"


subprocess.call(logwriterCommand.split(' '))
subprocess.call(bashCommand.split(' '))

alerts = []
with open('./alerts.json', 'r') as alertsFile:
    fullFile = alertsFile.read()
    lines = fullFile.split('\n')
    for line in lines:
        if(line != ""):
            alerts.append(json.loads(line))

for alert in alerts:
    print(alert["decoder"])

