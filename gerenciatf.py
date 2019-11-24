import Tkinter
import threading
import subprocess

global testRuleAlertsVar, sshAcceptedAlertsVar, sshAuthFailAlertsVar, sshInvalidUserAlertsVar

containerName = "ubuntu"


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

alertsLabel.grid(row=0, column=1)
testRuleAlertsLabel.grid(row=1, column=1)
testRuleAlertsNum.grid(row=1, column=2)
sshAcceptedAlertsLabel.grid(row=2, column=1)
sshAcceptedAlertsNum.grid(row=2, column=2)
sshAuthFailAlertsLabel.grid(row=3, column=1)
sshAuthFailAlertsNum.grid(row=3, column=2)
sshInvalidUserAlertsLabel.grid(row=4, column=1)
sshInvalidUserAlertsNum.grid(row=4, column=2)


window.mainloop()
