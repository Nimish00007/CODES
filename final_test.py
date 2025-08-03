def solve_cake_factory(A, B, C):
    """
    Solve the cake factory scheduling problem using sequential order.
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

# Test with example 1
print("Example 1:")
A1 = 4
B1 = [3, 2, 3, 4]
C1 = [3, 2, 3, 4]
result1 = solve_cake_factory(A1, B1, C1)
print(f"Input: A={A1}, B={B1}, C={C1}")
print(f"Result: {result1}")
print(f"Expected: 13")
print(f"Match: {result1 == 13}")
print()

# Test with example 2 (using full arrays)
print("Example 2:")
A2 = 5
B2 = [2, 3, 4, 5, 4]
C2 = [5, 4, 3, 2, 1]
result2 = solve_cake_factory(A2, B2, C2)
print(f"Input: A={A2}, B={B2}, C={C2}")
print(f"Result: {result2}")
print(f"Expected: 19")
print(f"Match: {result2 == 19}")
print()

# Test with example 2 (using only first 3 elements as stated in problem)
print("Example 2 (first 3 only):")
A2_short = 3
B2_short = [2, 3, 4]
C2_short = [5, 4, 3]
result2_short = solve_cake_factory(A2_short, B2_short, C2_short)
print(f"Input: A={A2_short}, B={B2_short}, C={C2_short}")
print(f"Result: {result2_short}")
print(f"Expected: 19")
print(f"Match: {result2_short == 19}")

print("\nConclusion:")
print("The sequential order (1,2,3,...,A) works perfectly for example 2 with A=5.")
print("For example 1, no ordering gives exactly 13, but sequential gives 16.")
print("This suggests either an error in the expected output for example 1,")
print("or a different interpretation of the problem that I'm missing.")