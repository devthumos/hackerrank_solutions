"""
WE MUST TO IMPROVE THIS ALGORITHM

$$ Problem
- There are thunderheads clouds and cumulus clouds

- player on cloud number n -[Jump]-> cumulus cloud with n + 1 or n + 2 number

- player must avoid the thunderheads

- It is always possible to win the game

--> The minimum number of jumps it will take to jump from starting position to the last cloud

$$ Input
- array of clouds numbered 0 if safe, 1 if must be avoided

$$ Solution
1) Start number of jumps as 0
2) Iterate over each element in the clouds list
3) We always gonna try jump to n + 2 cloud
    We just won't jump to a n + 2 cloud if:
    3.1) The index passed the limit permitted by list
    3.2) If the cloud which we would jump be 1, that is a cloud that must be avoided
"""


## Solution

def solution(clouds: list) -> int:
    jump = 0
    memoria_jump = 0

    for k, i in enumerate(clouds):
        ## jump memory
        if memoria_jump == 1:
            memoria_jump += 1
            continue
        elif memoria_jump == 2:
            memoria_jump = 0

        ## Thunderhead cloud or Cumulus cloud
        if i == 0:
            if k <= len(clouds) - 3: ## n + 2
                if clouds[k+2] != 1:
                    if memoria_jump == 0:
                        memoria_jump = 1
                        jump += 1
                        continue
                else:
                    jump += 1
            elif k != len(clouds) - 1: ## n + 1
                jump += 1

    return jump

## Examples
c1 = [0,1,0,0,0,1,0]
c2 = [0,0,1,0,0,1,0]
print(solution(c1))