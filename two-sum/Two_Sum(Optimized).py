# This is Optimized Solution and Only valid for Exactly One Solution.(Means no repetation of solutions and Numbers.)

def twosumsolution(values,target):
    emptyhash = {}
    if len(values) == 0:
        print("list is empty.")
    elif len(values)==1:
        return values
    elif len(values)>=2:
        for i , n in enumerate(values):
            minus = target - n
            if minus in emptyhash:
                print([emptyhash[minus],i])
            else:
                emptyhash[n] = i
                
list_values = [3,-1,0,-10,12]
target_value = -10

twosumsolution(list_values,target_value)
        