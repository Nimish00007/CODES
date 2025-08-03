def solve_cake_factory(A, B, C):
    """
    Solve the cake factory scheduling problem using Johnson's algorithm.
    """
    # Separate jobs into two groups based on Johnson's rule
    group1 = []  # B[i] < C[i]
    group2 = []  # B[i] >= C[i]
    
    for i in range(A):
        if B[i] < C[i]:
            group1.append((B[i], C[i], i))
        else:
            group2.append((B[i], C[i], i))
    
    # Sort group1 by B[i] ascending (Pam's time)
    group1.sort(key=lambda x: x[0])
    
    # Sort group2 by C[i] descending (Sam's time)
    group2.sort(key=lambda x: x[1], reverse=True)
    
    # Combine the groups
    orders = group1 + group2
    
    # Calculate the completion time
    pam_time = 0  # When Pam finishes current work
    sam_time = 0  # When Sam finishes current work
    
    for pam_work, sam_work, _ in orders:
        # Pam starts working on this order after finishing previous work
        pam_time += pam_work
        
        # Sam can only start after Pam finishes this order
        # and after Sam finishes previous work
        sam_start_time = max(sam_time, pam_time)
        sam_time = sam_start_time + sam_work
    
    return sam_time

# Test with example 1
print("Example 1:")
A1 = 4
B1 = [3, 2, 3, 4]
C1 = [3, 2, 3, 4]
result1 = solve_cake_factory(A1, B1, C1)
print(f"Result: {result1}")
print(f"Expected: 13")
print()

# Test with example 2
print("Example 2:")
A2 = 3
B2 = [2, 3, 4, 5, 4]
C2 = [5, 4, 3, 2, 1]
result2 = solve_cake_factory(A2, B2, C2)
print(f"Result: {result2}")
print(f"Expected: 19")
print()

# Let's trace through example 1 to understand the scheduling
print("Tracing Example 1:")
group1 = []
group2 = []
for i in range(A1):
    if B1[i] < C1[i]:
        group1.append((B1[i], C1[i], i))
    else:
        group2.append((B1[i], C1[i], i))

print(f"Group 1 (B[i] < C[i]): {group1}")
print(f"Group 2 (B[i] >= C[i]): {group2}")

group1.sort(key=lambda x: x[0])
group2.sort(key=lambda x: x[1], reverse=True)
orders = group1 + group2

print(f"Final order: {orders}")

pam_time = 0
sam_time = 0
for i, (pam_work, sam_work, orig_idx) in enumerate(orders):
    pam_time += pam_work
    sam_start_time = max(sam_time, pam_time)
    sam_time = sam_start_time + sam_work
    print(f"Order {orig_idx+1}: Pam works {pam_work}, Sam works {sam_work}")
    print(f"  Pam finishes at: {pam_time}, Sam starts at: {sam_start_time}, Sam finishes at: {sam_time}")