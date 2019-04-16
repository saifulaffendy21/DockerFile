import os
import time

print "Deleting JIRA Software folder directory!"
os.system('rm -rf /var/atlassian')
os.system('rm -rf /opt/atlassian')
print "Done!\nDeleting JIRA Software from your system!"
