class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("No more room!")

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      pointer = self.top_item
      return pointer.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
  def get_size(self):
    return self.size
  
  def get_name(self):
    return self.name
  
  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks

stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks += [left_stack, middle_stack, right_stack]

#Set up the Game

num_disks = int(input("\nHow many disks do you want to play?\n"))
left_stack.limit = num_disks
middle_stack.limit = num_disks
right_stack.limit = num_disks

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))
  
for disk in range(num_disks, 0, -1):
  left_stack.push(disk)

num_optimal_moves = (2 ** num_disks) - 1

print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))

#Get User Input
def get_input():
  movements = {stack.get_name()[0]:stack.get_name() for stack in stacks}
  names_and_stacks = {stack.get_name():stack for stack in stacks}

  while True: 
    for letter, stack in movements.items():
      print("Enter " + letter + " for " + stack)
    
    user_input = input("")
    user_input = user_input.upper()

    if user_input in movements.keys():
      chosen_stack_name = movements.get(user_input)
      chosed_stack = names_and_stacks.get(chosen_stack_name)
      return chosed_stack

#Play the Game

num_user_moves = 0

while right_stack.has_space():
  for stack in stacks:
    stack.print_items()

  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    if from_stack.is_empty():
      print("\nThe stack you want to move from is empty?\n")
      for stack in stacks:
        stack.print_items()
      from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
        
    if to_stack.is_empty():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      #for stack in stacks:
        #stack.print_items()
    else:
      if to_stack.has_space() and from_stack.peek() < to_stack.peek():
        disk = from_stack.pop()
        to_stack.push(disk)
        num_user_moves += 1
        #for stack in stacks:
          #stack.print_items()
      else:
        print("\nInvalid move. Try again.")
    break
print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}\n".format(num_user_moves, num_optimal_moves))