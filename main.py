
def lists():
    l = [ 'a', 1, 1.0, True ]
    l.append(3) # Add to end.
    l.insert(0, "beginning") # Add before index
    l.remove('a') # Remove first item equal - raise ValueError on DNE.
    l.pop(3) # Remove and return element at index, tail if undefined
    l.clear() # Deletes all elements, similar to `del list`
    l.index(1.0, start=0, end=1) # Return index first occurrence, start end range opt.
    l.count(True) # Return count of occurrence.
    l.sort(key=None, reverse=False) # Sort items asc in place.
    l.reverse() # Reverse in place.
    l.copy() # Shallow copy.

def stacks():
    st = [ 1, 2, 3]
    st.append(4)
    st.pop()

def sets():
    s = { "apple", 1, True }
    'apple' in s   
    'DNE' not in s


def dictionaries():
    d = { 
        "key": "value",
        "key1": True,
        "key2": 23
    }
    d["foo"] = "bar"
    d.get('DNE') # Return None on DNE.
    d["DNE"] # Raise KeyError on DNE.
    del d["key2"] # Delete pair from dict
    list(d) # Return keys
    sorted(d) # Keys (sorted)
    'key' in d
    'DNE' not in d

    for key, value in d.items():
        print(key, value)
    
def looping():
    for index, value in enumerate(['tic', 'tac', 'toe']):
        print(index, value)

    arr1 = ['name', 'quest', 'favorite color']
    arr2 = ['lancelot', 'the holy grail', 'blue']
    for value1, value2 in zip(arr1, arr2):
        print(value1, value2)

def main():
    pass

if __name__ == "__main__" :
    main()