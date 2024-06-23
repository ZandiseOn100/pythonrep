todo_list = {}

def add_task(task):
    todo_list[task._title] = {
        "title": task._title,
        "description": task._description,
        "status": task._status
        }
def remove_task(task):
    if task in todo_list:
        del todo_list[task] 
        
def update_task(title, description=None, status=None):
    if title in todo_list:
        if description in todo_list:
            todo_list["description"] = description
        if status in todo_list:
            todo_list["status"] = status    
def list_all_tasks():
        return todo_list   
def filter_tasks_by_status(status):
    return [task for task in todo_list.values() if task.status == status ]      