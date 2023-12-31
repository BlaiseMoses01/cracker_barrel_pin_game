import sys
import time

class Node:
    def __init__(self, name, pin,  left=None, right=None , left_sibling=None, right_sibling=None):
        self.name = name
        self.left = left
        self.right = right
        self.left_sibling = left_sibling
        self.right_sibling = right_sibling
        self.pin=pin

    def set_name(self, name):
        self.name = name

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_left_sibling(self, left_sibling):
        self.left_sibling = left_sibling

    def set_right_sibling(self, right_sibling):
        self.right_sibling = right_sibling

    def set_pin(self, pin):
        self.pin = pin

    def get_name(self):
        return self.name

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_left_sibling(self):
        return self.left_sibling

    def get_right_sibling(self):
        return self.right_sibling

    def get_pin(self):
        return self.pin

    def has_left_sibling(self):
        if self.left_sibling is not None:
            return True
        return False

    def has_right_sibling(self):
        if self.right_sibling is not None:
            return True
        return False

    def has_left(self):
        if self.left is not None:
            return True
        return False

    def has_right(self):
        if self.right is not None:
            return True
        return False


def copy(node):
    c = Node(node.get_name(), node.get_pin(), node.get_left(), node.get_right(), node.get_left_sibling(), node.get_right_sibling())
    return c

def build_tree(size, empty, depth, head):

    linked = False
    is_empty = False

    if head.has_left_sibling():
        node = head.get_left_sibling()
        node = node.get_right()
        head.set_left(node)
        linked = True
    else:
        name = get_name(head.get_name(), "left")
        if name == empty:
            is_empty = True
        if is_empty:
            node = Node(name, True)
        else:
            node = Node(name, False)
        is_empty = False
        head.set_left(node)
        size = size - 1

    name = get_name(head.get_name(), "right")
    if name == empty:
        is_empty = True
    if is_empty:
        node = Node(name, True)
    else:
        node = Node(name, False)
    is_empty = False
    head.set_right(node)
    size = size - 1

    # set sibling relationship
    left = head.get_left()
    right = head.get_right()
    left.set_right_sibling(right)
    right.set_left_sibling(left)
    head.set_left(left)
    head.set_right(right)

    if depth == 1:
        return head

    # left recursive
    if not linked:
        head.set_left(build_tree(size , empty, depth-1, head.get_left()))
    # right recursive
    head.set_right(build_tree(size, empty, depth -1 , head.get_right()))
    return head


def get_rows(size):
    count = 0
    x = 0
    while count < size:
        for i in range (0, x+1):
            count += 1
        x += 1
    return x


def get_name(name, direction):
    x = int(name[0])
    y = int(name[1])
    ret = ""
    if direction == "left":
        ret = str(x+1) + str(y)
    else:
        ret = str(x+1)+str(y+1)
    return ret


def is_valid_move(a, b, c):
    if a.get_pin() is True and b.get_pin() is False and c.get_pin() is False:
        return str(a.get_name()) + "->" + str(b.get_name()) + "->" + str(c.get_name())
    elif a.get_pin() is False and b.get_pin() is False and c.get_pin() is True:
        return str(a.get_name()) + "->" + str(b.get_name()) + "->" + str(c.get_name())
    else:
        return "invalid"


def flip_pins(head, to_flip):

    for i in range(len(to_flip)):
      if to_flip[i] == head.get_name():
            head.set_pin(not head.get_pin())
            to_flip.pop(i)
            break
    
    if head.has_left():
       flip_pins(head.get_left(), to_flip)
    if head.has_right():
       flip_pins(head.get_right(), to_flip)
        
  
def make_move(head, move):
    
    to_flip = []
    c1 = str(move[0] + move[1])
    c2 = str(move[4] + move[5])
    c3 = str(move[8] + move[9])
    to_flip.append(c1)
    to_flip.append(c2)
    to_flip.append(c3)
    flip_pins(head, to_flip)
    return head


def get_possible_moves(head, possible_moves):

    if head.has_left() and head.get_left().has_left():
        left1 = head.get_left()
        left2 = left1.get_left()
        move = is_valid_move(head, left1, left2)
        if (move != "invalid") and (move not in possible_moves):
            possible_moves.append(move)

    if head.has_right() and head.get_right().has_right():
        right1 = head.get_right()
        right2 = right1.get_right()
        move = is_valid_move(head, right1, right2)
        if (move != "invalid") and (move not in possible_moves):
            possible_moves.append(move)

    if head.has_left_sibling() and head.get_left_sibling().has_left_sibling():
        ls1 = head.get_left_sibling()
        ls2 = ls1.get_left_sibling()
        move = is_valid_move(head, ls1, ls2)
        if (move != "invalid") and (move not in possible_moves):
            possible_moves.append(move)

    if head.has_left():
        get_possible_moves(head.get_left(), possible_moves)
    if head.has_right():
        get_possible_moves(head.get_right(), possible_moves)
    return possible_moves


def pin_count(head, count, seen):
    if not head.get_pin() and head.get_name() not in seen:
        count += 1
        seen.append(head.get_name())
    
    if head.has_left():
        count += pin_count(head.get_left(), 0, seen)
    if head.has_right():
        count += pin_count(head.get_right(), 0, seen)
    return count


def is_terminal(head):
    count = pin_count(head, 0, [])
    if count == 1:
        return True
    return False


def print_tree(head, seen):
    if not head.get_name() in seen:
        print(head.get_name())
        print(head.get_pin())
        seen.append(head.get_name())

    if head.has_left():
        print_tree(head.get_left(), seen)
    if head.has_right():
        print_tree(head.get_right(), seen)

        
def solve(head, trace, solutions):
    if is_terminal(head):
        print("solution found!")
        print(trace)
        solutions.append(trace.copy())
        return solutions
    

    moves = get_possible_moves(head,[])
    
    if not moves:
        return solutions
    else:
        for move in moves: 
            make_move(head, move)
            trace.append(move)
            solutions = solve(head, trace, solutions)
            make_move(head, move)
            trace.pop(len(trace)-1)
        return solutions




print("Welcome to the Peg Game Solver!")

mode = input("Enter '1' to solve a specific configuration or '2' to solve all configurations of a 15 peg board: ")
l = []
s = 15
if mode == '1':
    s = int(input("Enter board size: "))
    e = str(input("Enter the initial empty hole in the form 'xy' (ex:'00'): "))
    l.append(e)
else:
    l = ["00","10","11","20","21", "22", "30","31","32", "33","40","41","42","43","44"]
rows = get_rows(s)
for n in l:
    filename = n + ".txt"
    with open(filename, mode="wt") as f:
            f.write("Board with intial Hole as : "+n+"\n")
            target = False
            if n == "00":
                target = True
            h = Node("00", target)
            h = build_tree(s, n, rows-1, h)
            start = time.time()
            solutions = solve(h, [],[])
            end = time.time()
            f.write("   number of solutions: "+str(len(solutions)))
            f.write("   time to solve in seconds: "+str(end-start)+"\n")
            count1 = 0
            for solution in solutions: 
                count1 +=1
                f.write("   solution " + str(count1)+ ":\n")
                count2 = 0
                for move in solution:
                    count2+=1
                    f.write("       Move "+str(count2)+": "+move+"\n")
    f.close()
print("Goodbye!")

    






