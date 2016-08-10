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
        "h" : P_High
        }

def CheckPriority(p):
    priority = P_Low
    if p in priorities:
        priority = priorities[p]

    return p
