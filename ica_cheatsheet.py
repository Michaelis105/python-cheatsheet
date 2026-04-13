class MyClass:
    def __init__(self, a: int, b: str, c: bool):
        self.a, self.b, self.c = a, b, c
        #c = MyClass(3.14159, "hello", True)
    
    def strings(self): 
        return f"{self.a:.2f},{self.b.upper()}", self.b.strip(),
    
    def lists(self, l: list = [ 'a', 1, 1.0, True ]):
        l.append(3) # Add to end.
        l.insert(0, "new") # Add before index
        l.remove('a') # Remove first item equal - raise ValueError on DNE.
        l.pop(3) # Remove and return element at index, tail if undefined
        l.clear() # Deletes all elements, similar to `del list`
        l.index(1.0, start=0, end=1) # Return index first occurrence, start end range opt. Throws ValueError on not found
        l.count(True) # Return count of occurrence.
        l.sort(key=lambda x: -x, reverse=False) # Sort items asc in place.
        l.reverse() # Reverse in place.
        l.copy() # Shallow copy.
        [x for x in l if x % 2 == 0] # filter, transform on condition
        list(set(l)) # unique
        list(set(a) & set(b))   # intersection/common
        sorted(users, key=lambda u: (-u["score"], u["name"])) # same score → alphabetical by name
        return l[::-1], l[::2], l[0], l[-1], l[1:4], len(l), sum(l), min(l), max(l)
    
    def sets(self, s: set = { "a", 1, True }): # unordered collection, no duplicates.
        s.add("b") # Add element to set
        'a' in s, 'DNE' not in s, (s | s), (s & s), (s - s), (s ^ s)
    
    def dictionaries(self, d: dict = { "key": "value", "k1": True, "k2": 3 }): # Key-value pairs, key is unique
        d["foo"] = "bar"
        'key' in d, 'DNE' not in d
        d["DNE"], d.get('DNE', 'default') # Raise KeyError on DNE, Return None on DNE, or default
        del d["k2"], d.pop("k1", None) # Delete pair from dict, or return default
        list(d) # Return keys
        sorted(d) # Keys (sorted)
        
        {print(k, v) for k, v in d.copy().items()}  #d.keys(), d.values()
        {v: k for k, v in d.items()} # invert a dict 
        {k: v.upper() for k, v in d.items() if v["status"] == "active"} # filter a dict
        
        from collections import defaultdict
        by_dept = defaultdict(list) # group items without KeyError
        for emp in employees:
            by_dept[emp["dept"]].append(emp["name"])

        freq = defaultdict(int) # count occurrences
        for item in data:
            freq[item] += 1

    def custom_compare(self):
        from functools import cmp_to_key

        # use when logic can't fit in a simple key
        def compare(a, b):
            if a["priority"] != b["priority"]:
                return b["priority"] - a["priority"]  # high first
            if a["name"] != b["name"]:
                return -1 if a["name"] < b["name"] else 1
            return 0

        sorted(tasks, key=cmp_to_key(compare))

    def ica_pattern(self):
        # 1. group-by (most common ICA pattern)
        from collections import defaultdict
        groups = defaultdict(list)
        for item in data:
            groups[item["key"]].append(item)

        # 2. merge two dicts
        merged = {**dict1, **dict2}   # dict2 wins on conflict

        # 3. top-N by computed value
        sorted(items, key=lambda x: -x["val"])[:n]

        # 5. aggregate with running total
        totals = defaultdict(int)
        for txn in transactions:
            totals[txn["account"]] += txn["amount"]

        # 6. flatten nested list
        flat = [x for sub in nested for x in sub]

        # 7. deduplicate preserving order
        seen = set()
        deduped = [x for x in items
                if not (x in seen or seen.add(x))]
        
    def others(self):
        import json
        json.loads('{"name": "Alice", "age": 30}') # Returns a dictionary