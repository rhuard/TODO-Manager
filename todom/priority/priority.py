P_None = -1
P_Low = 0
P_Medium = 1
P_High = 2

priorities = {
        "Low" : P_Low,
        "LOW" : P_Low,
        "low" : P_Low,
        "l" : P_Low,
        "Medium" : P_Medium,
        "MEDIUM" : P_Medium,
        "medium" : P_Medium,
        "m" : P_Medium,
        "High" : P_High,
        "HIGH" : P_High,
        "high" : P_High,
        "h" : P_High,
        "None" : P_None,
        "NONE" : P_None,
        "none" : P_None
        }

p_names = {
        P_None : "None",
        P_High : "High",
        P_Medium : "Medium",
        P_Low : "Low"
        }

def PrintPriorityName(p):
    priority = p_names[P_None]
    if p in p_names:
        priority = p_names[p]

    return priority

def CheckPriority(p):
    priority = P_Low
    if p in priorities:
        priority = priorities[p]

    return priority

