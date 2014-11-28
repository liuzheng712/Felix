"""
felix.py
In charge of listening and reponding to user speech
Executes all extensions to provide Felix's features
"""

class Felix(object):
    
    def __init__(self, extensionManager, speechManager, userInfo, IDENTIFIER="FELIX"):
        """
        Initializes the Felix class
        """
        self.extensionManager = extensionManager
        self.speechManager = speechManager
        self.IDENTIFIER = IDENTIFIER
        self.userInfo = userInfo
    
    def live(self):
        """
        Should run forever, after being called in main.py
        Listens and reponds to user speech
        Executes the appropriate extension for the input speech
        Prints any notifications
        """
        while True:
            ambientBase = None
            try: ambientBase = self.speechManager.listenForIdentifier(self.IDENTIFIER)
            except: continue
            if ambientBase:
                input = self.speechManager.listen(self.userInfo, ambientBase)
                self.extensionManager.execute(input, self.userInfo)