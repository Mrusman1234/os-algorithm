Available = [3, 3, 2]  
Max = [[7, 5, 3],      
       [3, 2, 2],
       [9, 0, 2],
       [2, 2, 2],
       [4, 3, 3]]
Allocation = [[0, 1, 0], 
              [2, 0, 0],
              [3, 0, 2],
              [2, 1, 1],
              [0, 0, 2]]
need = [[Max[i][j] - Allocation[i][j] for j in range(len(Max[0]))] for i in range(len(Max))]  

def safety_algorithm():
    work = Available[:]
    finish = [False] * len(Max)

    while True:
        safe_sequence = []
        for i in range(len(Max)):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(len(Max[0]))):
                work = [work[j] + Allocation[i][j] for j in range(len(Max[0]))]
                finish[i] = True
                safe_sequence.append(i)
                break
        if len(safe_sequence) == 0:
            if all(finish):
                print("System is in a safe state")
            else:
                print("System is in an unsafe state")
            break

def resource_request(process_index, request):
    global Available, Allocation, need
    
    if all(request[i] <= need[process_index][i] for i in range(len(request))):
        if all(request[i] <= Available[i] for i in range(len(request))):
            # Pretend to allocate resources
            for i in range(len(request)):
                Available[i] -= request[i]
                Allocation[process_index][i] += request[i]
                need[process_index][i] -= request[i]
            print("Resource allocated successfully")
        else:
            print("Process must wait, resources not available")
    else:
        print("Error: Process has exceeded its maximum claim")
safety_algorithm()
resource_request(1, [1, 0, 2])
print("Available resources:", Available)
print("Allocation matrix:", Allocation)
print("Need matrix:", need)
