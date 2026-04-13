
class MyClass:
    def __init__(self, a: int, b: str, c: bool):
        self.a, self.b, self.c = a, b, c

    def __str__(self):
        return ", ".join([self.a, self.b, self.c])
    
    def __lt__(self, other):
        pass

def strings(): 
    pass
    # lower, upper, strip

def lists():
    l = [ 'a', 1, 1.0, True ]
    l.append(3) # Add to end.
    l.insert(0, "beginning") # Add before index
    l.remove('a') # Remove first item equal - raise ValueError on DNE.
    l.pop(3) # Remove and return element at index, tail if undefined
    l.clear() # Deletes all elements, similar to `del list`
    l.index(1.0, start=0, end=1) # Return index first occurrence, start end range opt. Throws ValueError on not found
    l.count(True) # Return count of occurrence.
    l.sort(key=lambda x: -x, reverse=False) # Sort items asc in place.
    l.reverse() # Reverse in place.
    l.copy() # Shallow copy.

    l[::-1]
    l[::2]
    l[0] # 1
    l[-1] # 5
    l[1:4] # [2, 3, 4])
    len(l)


def stacks():
    st = [ 1, 2, 3 ]
    st.append(4)
    st.pop()

def sets(): # unordered collection, no duplicates.
    s = { "apple", 1, True }
    s.add("banana") # Add element to set
    'apple' in s   
    'DNE' not in s
    (s | s), (s & s), (s - s), (s ^ s)


def dictionaries(): # Key-value pairs, key is unique
    d = { "key": "value", "k1": True, "k2": 23 }
    d["foo"] = "bar"
    'key' in d
    'DNE' not in d
    d.get('DNE') # Return None on DNE.
    d["DNE"] # Raise KeyError on DNE.
    del d["k2"] # Delete pair from dict
    list(d) # Return keys
    sorted(d) # Keys (sorted)
    
    for key, value in d.copy().items():
        print(key, value)
    
def looping():
    for index, value in enumerate(['tic', 'tac', 'toe']): # For sequences
        print(index, value)

    arr1 = ['name', 'quest', 'favorite color']
    arr2 = ['lancelot', 'the holy grail', 'blue']
    for value1, value2 in zip(arr1, arr2):
        print(value1, value2)

    for s in sorted(arr1):
        pass

def heapq(self):
        import heapq # min-heap by default
        nums = [5, 2, 9, 1, 5, 6]
        heapq.heapify(nums) # transforms list into a heap in-place
        heapq.heappush(nums, 0) # add an element to the heap
        heapq.heappop(nums) # remove and return the smallest element
    
def deque(self):
    from collections import deque
    d = deque([1, 2, 3])
    d.append(4) # add to the right end
    d.appendleft(0) # add to the left end
    d.pop() # remove from the right end
    d.popleft() # remove from the left end

def trees(self):
    # PREORDER: ROOT, LEFT, RIGHT = STACK PRINT, PRIGHT, PLEFT
    # 
    pass

def lambdas(self):
    sorted([5, 2, 9, 1, 5, 6], key=lambda x: -x) # Sort in descending order
    #sortedIntervals = sorted(intervals, key=lambda i: i[0]) # Sort intervals by start time

def bitwise():
    pass
    '''
    XOR
    0 ^ 0 = 0
    1 ^ 1 = 0
    1 ^ 0 = 1
    0 ^ 1 = 1
    '''

def exceptionHandling():
    try:
        x = 1 / 0
    except Exception as e:
        print(f"An error occurred: {e}")
        e.add_note("This is a note about the exception") # add additional information to the exception
        raise(e) # re-raise the exception after handling it
    #except:
        #print("An error occurred")
    finally:
        print("This will always execute")

if __name__ == "__main__" :
    bitwise()