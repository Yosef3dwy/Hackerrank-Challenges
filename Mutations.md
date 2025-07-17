# Mutate a String

You are given an immutable string, and you want to make changes to it.

**Example**

```python
>>> string = "abracadabra"
```

You can access an index by:

```python
>>> print(string[5])
a
```

What if you would like to assign a value?

```python
>>> string[5] = 'k'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

How would you approach this?

One solution is to convert the string to a list and then change the value.

```python
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print(string)
abrackdabra
```

Another approach is to slice the string and join it back.

```python
>>> string = string[:5] + "k" + string[6:]
>>> print(string)
abrackdabra
```

---

## Task

Read a given string, change the character at a given index and then print the modified string.

### Function Description

Complete the `mutate_string` function below.

```python
def mutate_string(string, position, character):
    # string: the string to change
    # position: the index to insert the character at
    # character: the character to insert
    # return the altered string
```

### Input Format

- The first line contains a string, `string`.
- The next line contains an integer `position` and a string `character`, separated by a space.

### Constraints

- `0 <= position < len(string)`
- `character` is a single character.

### Output Format

- Print the modified string.

### Sample Input

```
abracadabra
5 k
```

### Sample Output

```
abrackdabra
```

---

### Explanation

Replace the character at index `5` (0-based) with `'k'` gives `abrackdabra`.

