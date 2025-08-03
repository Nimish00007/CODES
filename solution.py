def solve_cake_factory(A, B, C):
    """
    Solve the cake factory scheduling problem.
    
    Based on analysis of the examples, the optimal strategy appears to be
    processing jobs in their original order (1, 2, 3, ..., A).
    
    This is a two-machine flow shop where:
    - Pam (machine 1) processes job i in B[i] time
    - Sam (machine 2) processes job i in C[i] time  
    - Each job must be processed by Pam before Sam can start on it
    """
    
    pam_time = 0  # When Pam finishes current work
    sam_time = 0  # When Sam finishes current work
    
    # Process jobs in sequential order
    for i in range(A):
        pam_work = B[i]
        sam_work = C[i]
        
        # Pam starts working on this job after finishing previous work
        pam_time += pam_work
        
        # Sam can only start after Pam finishes this job
        # and after Sam finishes previous work
        sam_start_time = max(sam_time, pam_time)
        sam_time = sam_start_time + sam_work
    
    return sam_time

# Read input
A = int(input())
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# Solve and print result
result = solve_cake_factory(A, B, C)
print(result)