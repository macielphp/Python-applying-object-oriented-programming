#Reduces redundancy of status management logic in various classes.
#Provides a single point for modifying how status is handled.
class Toggleable:
    def __init__(self): 
        self._active = False

    @property
    def active(self):
        return '✅' if self._active else '❌'
    
    def toggle_status(self):
        self._active = not self._active