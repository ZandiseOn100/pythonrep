class ToDoList:
    def __init__(self, title, description, status):
        self._title = title
        self._description = description
        self._status = status
        
    def get_title(self):
        return self._title    
    def set_title(self, title):
        self._title = title
    
    def get_description(self):
        return self._description
    def set_description(self, description):
        self._description = description
    
    def get_status(self):
        return self._status
    def set_description(self, status):
        self._status = status       
    
    def __str__(self):
        return f"'{self._title}' by {self._description} ({self._status})"  