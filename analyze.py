from itertools import permutations

def calculate_time(order, B, C):
    """Calculate total completion time for a given order of jobs"""
    pam_time = 0
    sam_time = 0
    
    schedule = []
    for job_idx in order:
        pam_work = B[job_idx]
        sam_work = C[job_idx]
        
        # Pam starts working on this job
        pam_time += pam_work
        
        # Sam can only start after Pam finishes this job
        # and after Sam finishes previous job
        sam_start_time = max(sam_time, pam_time)
        sam_time = sam_start_time + sam_work
        
        schedule.append({
            'job': job_idx + 1,
            'pam_work': pam_work,
            'sam_work': sam_work,
            'pam_finish': pam_time,
            'sam_start': sam_start_time,
            'sam_finish': sam_time
        })
    
    return sam_time, schedule

# Example 1 data
B1 = [3, 2, 3, 4]  # jobs 1,2,3,4
C1 = [3, 2, 3, 4]
A1 = 4

print("Analyzing all possible orders for Example 1:")
print("Jobs: 1:[3,3], 2:[2,2], 3:[3,3], 4:[4,4]")
print()

min_time = float('inf')
best_order = None
best_schedule = None

# Try all possible permutations
for order in permutations(range(A1)):
    total_time, schedule = calculate_time(order, B1, C1)
    
    if total_time <= min_time:
        if total_time < min_time:
            print(f"New best found: Order {[x+1 for x in order]} -> Total time: {total_time}")
            min_time = total_time
            best_order = order
            best_schedule = schedule
        else:
            print(f"Tied best: Order {[x+1 for x in order]} -> Total time: {total_time}")

print(f"\nBest result: {min_time}")
print(f"Best order: {[x+1 for x in best_order]}")
print("\nDetailed schedule for best order:")
for step in best_schedule:
    print(f"Job {step['job']}: Pam works {step['pam_work']}min (finishes at {step['pam_finish']}), "
          f"Sam works {step['sam_work']}min (starts at {step['sam_start']}, finishes at {step['sam_finish']})")