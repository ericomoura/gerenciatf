import Tkinter
import threading
import subprocess
import json
import time
import matplotlib.pyplot as plt
import matplotlib.animation as anim

global testRuleAlertsVar, sshAcceptedAlertsVar, sshAuthFailAlertsVar, sshInvalidUserAlertsVar
global alerts
alerts = []
containerName = "ubuntu"

def runAlertsThread():
    while True:
        bashCommand = "docker cp " + containerName + ":/var/ossec/logs/alerts/alerts.json ./alerts.json"
        subprocess.call(bashCommand.split(' '))
        alerts = []
        with open('./alerts.json', 'r') as alertsFile:
            fullFile = alertsFile.read()
            lines = fullFile.split('\n')
            for line in lines:
                if(line != ""):
                    alerts.append(json.loads(line))
        
        testRuleAlertsVar.set('0')
        sshAcceptedAlertsVar.set('0')
        sshAuthFailAlertsVar.set('0')
        sshInvalidUserAlertsVar.set('0')
        for alert in alerts:
            if(alert["rule"]["comment"] == "test rule"):
                testRuleAlertsVar.set(str(int(testRuleAlertsVar.get())+1))
            elif(alert["rule"]["comment"] == "First time user logged in."):
                sshAcceptedAlertsVar.set(str(int(sshAcceptedAlertsVar.get())+1))
            elif(alert["rule"]["comment"] == "SSHD authentication failed."):
                sshAuthFailAlertsVar.set(str(int(sshAuthFailAlertsVar.get())+1))
            elif(alert["rule"]["comment"] == "Attempt to login using a non-existent user"):
                sshInvalidUserAlertsVar.set(str(int(sshInvalidUserAlertsVar.get())+1))
               
        time.sleep(5)

def logEntryTestRule():
    bashCommand = "docker exec " + containerName + " /gerenciatf/logwriter.sh 1"
    subprocess.call(bashCommand.split(' '))
def logEntrySSHAccepted():
    bashCommand = "docker exec " + containerName + " /gerenciatf/logwriter.sh 2"
    subprocess.call(bashCommand.split(' '))
def logEntrySSHAuthFail():
    bashCommand = "docker exec " + containerName + " /gerenciatf/logwriter.sh 3"
    subprocess.call(bashCommand.split(' '))
def logEntrySSHInvalidUser():
    bashCommand = "docker exec " + containerName + " /gerenciatf/logwriter.sh 4"
    subprocess.call(bashCommand.split(' '))
def logEntryClearLog():
    bashCommand = "docker exec " + containerName + " /gerenciatf/logwriter.sh 999"
    subprocess.call(bashCommand.split(' '))
def logEntryClearAlerts():
    bashCommand = "docker exec " + containerName + " /gerenciatf/logwriter.sh 99"
    subprocess.call(bashCommand.split(' '))
    
def plotSSHChart(i):
    ax.clear()
    labels = ['Current', 'Allowed']
    currentSSHs = int(sshAuthFailAlertsVar.get())
    sizes = [currentSSHs, 10-currentSSHs]
    
    ax.set_title("SSH Authentication Failures")
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=True)
    ax.axis('equal')
    ax.legend()

bashCommand = "chmod +x ./logwriter.sh"
subprocess.call(bashCommand.split(' '))

#Window creation
window = Tkinter.Tk()
window.title("INF1015 - Erico e Felipe")

testRuleAlertsVar = Tkinter.StringVar()
testRuleAlertsVar.set('0')
sshAcceptedAlertsVar = Tkinter.StringVar()
sshAcceptedAlertsVar.set('0')
sshAuthFailAlertsVar = Tkinter.StringVar()
sshAuthFailAlertsVar.set('0')
sshInvalidUserAlertsVar = Tkinter.StringVar()
sshInvalidUserAlertsVar.set('0')

logButtonLabel = Tkinter.Label(window, text="GENERATE LOG ENTRY")
logButtonTestRule = Tkinter.Button(window, text="Test Rule", command=logEntryTestRule)
logButtonSSHAccepted = Tkinter.Button(window, text="SSH Accepted", command=logEntrySSHAccepted)
logButtonSSHAuthFail = Tkinter.Button(window, text="SSH Authentication Failed", command=logEntrySSHAuthFail)
logButtonSSHInvalidUser = Tkinter.Button(window, text="SSH Invalid User", command=logEntrySSHInvalidUser)
logButtonClearLog = Tkinter.Button(window, text="CLEAR LOG", command=logEntryClearLog)
logButtonClearAlerts = Tkinter.Button(window, text="CLEAR ALERTS", command=logEntryClearAlerts)

alertsLabel = Tkinter.Label(window, text="ALERTS INFO")
testRuleAlertsLabel = Tkinter.Label(window, text="Test rule alerts:")
testRuleAlertsNum = Tkinter.Label(window, textvariable=testRuleAlertsVar)
sshAcceptedAlertsLabel = Tkinter.Label(window, text="SSH Accepted alerts:")
sshAcceptedAlertsNum = Tkinter.Label(window, textvariable=sshAcceptedAlertsVar)
sshAuthFailAlertsLabel = Tkinter.Label(window, text="SSH Authentication Failed:")
sshAuthFailAlertsNum = Tkinter.Label(window, textvariable=sshAuthFailAlertsVar)
sshInvalidUserAlertsLabel = Tkinter.Label(window, text="SSH Invalid User:")
sshInvalidUserAlertsNum = Tkinter.Label(window, textvariable=sshInvalidUserAlertsVar)

logButtonLabel.grid(row=0, column=0)
logButtonTestRule.grid(row=1, column=0)
logButtonSSHAccepted.grid(row=2, column=0)
logButtonSSHAuthFail.grid(row=3, column=0)
logButtonSSHInvalidUser.grid(row=4, column=0)
logButtonClearLog.grid(row=5, column=0)
logButtonClearAlerts.grid(row=6, column=0)

alertsLabel.grid(row=0, column=1)
testRuleAlertsLabel.grid(row=1, column=1)
testRuleAlertsNum.grid(row=1, column=2)
sshAcceptedAlertsLabel.grid(row=2, column=1)
sshAcceptedAlertsNum.grid(row=2, column=2)
sshAuthFailAlertsLabel.grid(row=3, column=1)
sshAuthFailAlertsNum.grid(row=3, column=2)
sshInvalidUserAlertsLabel.grid(row=4, column=1)
sshInvalidUserAlertsNum.grid(row=4, column=2)

alertsThread = threading.Thread(target=runAlertsThread)
alertsThread.start()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ani = anim.FuncAnimation(fig, plotSSHChart, interval=1000)
fig.show()

window.mainloop()
