from heapq import heappop, heappush
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
moves = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8], 6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}

def heuristic(state):
    return sum(abs(i // 3 - state[i] // 3) + abs(i % 3 - state[i] % 3) for i in range(1, 9) if state[i] != 0)

def solve_puzzle(initial_state):
    heap, visited = [(heuristic(initial_state), 0, initial_state, [])], set()
    while heap:
        _, cost, current_state, path = heappop(heap)
        if current_state == goal_state: return path
        if current_state in visited: continue
        visited.add(current_state)
        z = current_state.index(0)
        for move in moves[z]:
            new_state = list(current_state)
            new_state[z], new_state[move] = new_state[move], new_state[z]
            if tuple(new_state) not in visited:
                new_cost = cost + 1
                heappush(heap, (new_cost + heuristic(new_state), new_cost, tuple(new_state), path + [move]))
    return None

initial = (1, 2, 3, 4, 0, 5, 6, 7, 8)
solution = solve_puzzle(initial)
if solution:
    print("Solution steps:", solution)
    print("Number of steps:", len(solution))
else:
    print("No solution exists for the given initial state.")
