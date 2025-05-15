def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

from collections import defaultdict, deque
import math



gears = defaultdict(list)

for _ in range(inp()):
    size, count = invr()
    gears[size].append(count)

unique_sizes = list(gears.keys())

log_speed = {size: -math.inf for size in unique_sizes}

start_size = unique_sizes[0]

#initial speed is 1 and log(1) = 0
log_speed[start_size] = 0

q = deque([(start_size, 0)])
visited = set()

while q:
    current_size, current_speed = q.popleft()
    state = (current_size, current_speed)
    if state in visited:
        continue

    visited.add(state)

    for neighbor_size in unique_sizes:
        if current_size != neighbor_size:
            for current_count in gears[current_size]:
                for neighbor_count in gears[neighbor_size]:
                    speed_change = math.log(current_count / neighbor_count)
                    new_speed = log_speed[current_size] + speed_change

                    if new_speed > log_speed[neighbor_size]:
                        log_speed[neighbor_size] = new_speed
                        if neighbor_size not in visited:
                            q.append(neighbor_size, new_speed)

ans = max(log_speed.values())

print(ans)

"""
6
19 364
21 1023
19 66
19 242
21 807
19 675
"""



