class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0             
def fcfs(processes):
    current_time = 0
    total_processes = len(processes)
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        
        process.waiting_time = current_time - process.arrival_time
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        current_time = process.completion_time

    total_waiting_time = sum(process.waiting_time for process in processes)
    average_waiting_time = total_waiting_time / total_processes

    total_turnaround_time = sum(process.turnaround_time for process in processes)
    average_turnaround_time = total_turnaround_time / total_processes

    print("Process\t Arrival Time\t Burst Time\t Waiting Time\t Turnaround Time")
    for process in processes:
        print(f"{process.process_id}\t\t {process.arrival_time}\t\t {process.burst_time}\t\t {process.waiting_time}\t\t {process.turnaround_time}")
    
    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")

def get_user_input():
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(1, num_processes + 1): 
        arrival_time = int(input(f"Enter arrival time for process {i}: "))
        burst_time = int(input(f"Enter burst time for process {i}: "))
        processes.append(Process(i, arrival_time, burst_time))

    return processes

if __name__ == "__main__":
    processes = get_user_input()
    fcfs(processes)

