# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    #   use a stack
    #   if next token is an integer push it onto the stack
    #   if next token is an operator pop two integers and apply the operation
    #   then push the result back onto the stack
    #   at the end pop the final result and return it
    #
    # Instructions: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    stack = []
    for t in tokens:
        if t == "+":
            stack.append(stack.pop() + stack.pop())
        elif t == "*":
            stack.append(stack.pop() * stack.pop())
        elif t == "-":
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 - num2)
        elif t == "/":
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(int(num1 / num2))
        else:
            stack.append(int(t))
    return stack.pop()


def decode_string(s):
    # Outline:
    #   use a stack
    #   read characters from input string s and push them onto the stack until you reach a "]"
    #   then build a new string by popping from the stack until you reach a "["
    #   then pop the stack again to get k
    #   repeat the string you built k times and push it to the stack
    #   repeat these steps until you reach the end of the input string
    #   then build a new string by popping from the stack until it is empty then return the string
    #
    # Instructions: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    stack = []
    for c in s:
        encoded = ""
        while c == "]":
            nextstr = stack.pop()
            if nextstr  == "[":
                k = int(stack.pop())    # assuming k is a single digit
                c = k * encoded
            else:
                encoded = nextstr + encoded
        stack.append(c)

    result = ""
    while(stack != []):
        result = stack.pop() + result
    return result


def daily_temperatures(temps):
    # Outline:
    #   use a stack (when using list as a stack, push is stack.append(), pop is stack.pop(), peek is stack[-1])
    #   initialize list of waits as zeros
    #   loop over temps
    #   if stack is non-empty and current temperature is warmer than temperature at top of stack
    #   then pop temperature from stack, subtract its index from current index, and put this value in the list of waits
    #   repeat until (stack is non-empty and current temperature is warmer) is false
    #   next push current temp to stack and advance to next
    #   return list of waits
    #
    # Instructions: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    stack = []
    waits = [0] * len(temps)
    for i in range(0, len(temps)):
        while stack != [] and temps[stack[-1]] < temps[i]:
            j = stack.pop()
            waits[j] = i - j
        stack.append(i)
    return waits


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   use a queue
    #   use a counter to track number of islands
    #   create another grid to track location of visited 1s
    #   loop through 'grid'
    #   when you find an unvisited 1 add its location to the queue and increment island count
    #   go through queue:
    #       if location is a 1 and unvisited, mark it as visited and add adjacent locations to queue
    #       remove current location from queue and go to next in queue
    #   continue to next location in 'grid' and repeat above steps
    #   at the end, return the island count
    #
    # Instructions: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    queue = []
    visited = [[False]*len(i) for i in grid]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == "1" and not visited[i][j]):
                count += 1
                queue.append([i, j])
            while(queue != []):
                ii, jj = queue.pop(0)
                in_grid = ii >= 0 and ii < len(grid) and jj >= 0 and jj < len(grid[ii])
                if(in_grid and grid[ii][jj] == "1" and not visited[ii][jj]):
                    visited[ii][jj] = True
                    queue += [[ii + 1, jj], [ii - 1, jj], [ii, jj + 1], [ii, jj - 1]]
    return count


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
