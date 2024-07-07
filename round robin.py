class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def round_robin(processes, time_slice):
    total_processes = len(processes)
    current_time = 0
    quantum = time_slice
    remaining_processes = processes.copy()

    while remaining_processes:
        for process in remaining_processes[:]:
            if process.remaining_time <= quantum:
                current_time += process.remaining_time
                process.remaining_time = 0
                process.completion_time = current_time
                remaining_processes.remove(process)
            else:
                current_time += quantum
                process.remaining_time -= quantum

            for p in remaining_processes:
                if p.arrival_time <= current_time:
                    p.waiting_time += min(current_time, p.arrival_time + p.remaining_time) - current_time

    total_waiting_time = sum(process.waiting_time for process in processes)
    average_waiting_time = total_waiting_time / total_processes

    total_turnaround_time = sum(process.completion_time - process.arrival_time for process in processes)
    average_turnaround_time = total_turnaround_time / total_processes

    print("Process\t Arrival Time\t Burst Time\t Completion Time\t Turnaround Time\t Waiting Time")
    for process in processes:
        process.turnaround_time = process.completion_time - process.arrival_time
        print(f"{process.process_id}\t\t {process.arrival_time}\t\t {process.burst_time}\t\t {process.completion_time}\t\t\t {process.turnaround_time}\t\t\t {process.waiting_time}")

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")

def get_user_input():
    num_processes = int(input("Enter the number of processes: "))
    time_slice = int(input("Enter the time slice for Round Robin: "))
    processes = []

    for i in range(1, num_processes + 1):
        arrival_time = int(input(f"Enter arrival time for process {i}: "))
        burst_time = int(input(f"Enter burst time for process {i}: "))
        processes.append(Process(i, arrival_time, burst_time))

    return processes, time_slice

if __name__ == "__main__":
    processes, time_slice = get_user_input()
    round_robin(processes, time_slice)
