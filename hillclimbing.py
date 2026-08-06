def objective_function(x):
    return -4 * (x - 5) ** 2 + 100




def hill_climb(start,step_size, max_iterations):
    
    current_state = start
    current_value = objective_function(current_state)

    for i in range(max_iterations):
        left = current_state - step_size
        right = current_state + step_size
        
        left_value = objective_function(left)
        right_value = objective_function(right)
        if left_value > current_value:
            current_state = left
            current_value = left_value
        elif right_value > current_value:
            current_state = right
            current_value = right_value
        else:
            break
    
    return current_state,current_value
start = float(input("Enter the starting point: "))
step_size = float(input("Enter the step size: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

optimal_state, optimal_value = hill_climb(start, step_size, max_iterations)
print(f"Optimal state: {optimal_state}, Optimal value: {optimal_value}")