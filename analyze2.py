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

# Example 2 data (corrected based on the image)
# It looks like A=3 but arrays have 5 elements, so let's try A=5
B2 = [2, 3, 4, 5, 4]  
C2 = [5, 4, 3, 2, 1]
A2 = 5  # Changed to 5 to match array length

print("Analyzing all possible orders for Example 2:")
print("Jobs: 1:[2,5], 2:[3,4], 3:[4,3], 4:[5,2], 5:[4,1]")
print()

if A2 <= 5:  # Only analyze if reasonable number of permutations
    min_time = float('inf')
    best_order = None
    best_schedule = None
    
    # Try all possible permutations
    count = 0
    for order in permutations(range(A2)):
        total_time, schedule = calculate_time(order, B2, C2)
        count += 1
        
        if total_time < min_time:
            print(f"New best found: Order {[x+1 for x in order]} -> Total time: {total_time}")
            min_time = total_time
            best_order = order
            best_schedule = schedule
    
    print(f"\nChecked {count} permutations")
    print(f"Best result: {min_time}")
    print(f"Best order: {[x+1 for x in best_order]}")
    print("\nDetailed schedule for best order:")
    for step in best_schedule:
        print(f"Job {step['job']}: Pam works {step['pam_work']}min (finishes at {step['pam_finish']}), "
              f"Sam works {step['sam_work']}min (starts at {step['sam_start']}, finishes at {step['sam_finish']})")
else:
    print("Too many permutations to check all")

# Let's also try with just first 3 jobs as stated in problem
print("\n" + "="*50)
print("Trying with just first 3 jobs (A=3):")
B2_short = [2, 3, 4]
C2_short = [5, 4, 3]
A2_short = 3

min_time = float('inf')
best_order = None
best_schedule = None

for order in permutations(range(A2_short)):
    total_time, schedule = calculate_time(order, B2_short, C2_short)
    
    if total_time < min_time:
        print(f"New best found: Order {[x+1 for x in order]} -> Total time: {total_time}")
        min_time = total_time
        best_order = order
        best_schedule = schedule

print(f"\nBest result for A=3: {min_time}")
print(f"Best order: {[x+1 for x in best_order]}")
print("\nDetailed schedule:")
for step in best_schedule:
    print(f"Job {step['job']}: Pam works {step['pam_work']}min (finishes at {step['pam_finish']}), "
          f"Sam works {step['sam_work']}min (starts at {step['sam_start']}, finishes at {step['sam_finish']})")