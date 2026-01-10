# Initial list
list1 = [1, 2, 5, 3]

# --- Adding Elements ---

# .append(value): Add the value '5' to the end.
list1.append(5)
print(f"Append: {list1}")  # [1, 2, 5, 3, 5]

# .insert(index, value): Insert value '5' at index 1.
list1.insert(1, 5)
print(f"Insert: {list1}")  # [1, 5, 2, 5, 3, 5]

# .extend(iterable): Add multiple values from a list.
list1.extend([7, 8, 9])
print(f"Extend: {list1}")  # [1, 5, 2, 5, 3, 5, 7, 8, 9]

# --- Removing Elements ---

# .remove(value): Removes the FIRST occurrence of value '5'.
list1.remove(5)
print(f"Remove: {list1}")  # [1, 2, 5, 3, 5, 7, 8, 9]

# .pop([index]): Removes and returns the item at the last index (default).
removed_val = list1.pop() 
print(f"Pop (removed value: {removed_val}): {list1}")  # [1, 2, 5, 3, 5, 7, 8]

# .clear(): Removes all elements.
list1.clear()
print(f"Clear: {list1}")  # []

# --- Ordering and Copying ---

list2 = [1, 5, 7, 3, 7, 9]

# .sort(): Sorts the list IN PLACE by value.
list2.sort()
print(f"Sort: {list2}")  # [1, 3, 5, 7, 7, 9]

# [::-1]: Slicing creates a REVERSED COPY (new list) using index defaults and step -1.
a = list2[::-1]
print(f"Slicing [::-1] (New List): {a}") # [9, 7, 7, 5, 3, 1]

# .reverse(): Reverses the list IN PLACE.
list2.reverse()
print(f"Reverse (In Place): {list2}") # [9, 7, 7, 5, 3, 1]

# .copy() vs [::] (Both create shallow copies)
a2 = list2.copy()
a3 = list2[::]
print(f"Copy identity check (a2 is a3): {a2 is a3}") # False

# --- Querying ---

# .count(value): Counts occurrences of value '7'.
print(f"Count of value 7: {a2.count(7)}")  # 2

# .index(value): Finds the index of the FIRST occurrence of value '7'.
print(f"Index of value 7: {a2.index(7)}") # 1