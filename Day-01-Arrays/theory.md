# 📘 Day 01 – Arrays (Theory)

## 🔹 What is an Array?

An array is a data structure used to store **multiple values of the same type** in a **single variable**. The elements are stored in a **continuous memory block** and can be accessed using an index.

In Python, arrays are commonly represented using **lists**.

Example:

```python
arr = [10, 20, 30, 40]
```

---

## 🔹 Why Are Arrays Important?

Arrays are important because they:

* Store related data together
* Allow easy traversal using loops
* Act as the foundation for many other data structures
* Are heavily used in real-world applications like analytics, tracking, and monitoring systems

---

## 🔹 Array Traversal

Traversal means **visiting each element one by one**.

Most array problems are solved by:

* Initializing variables
* Looping through the array
* Updating values based on conditions

Example pattern:

```python
for element in arr:
    # process element
```

---

## 🔹 Finding Minimum and Maximum

To find minimum or maximum values:

* Assume the first element as both min and max
* Compare every element with stored values
* Update when a smaller or larger value is found

This avoids incorrect assumptions and works for all cases.

---

## 🔹 Time Complexity (TC)

Time complexity tells us **how the execution time grows** with input size.

For array traversal:

* One loop over n elements → **O(n)**

Even if we do multiple comparisons inside the same loop, the time complexity remains O(n).

---

## 🔹 Space Complexity (SC)

Space complexity tells us **how much extra memory** is used.

In Day 1 problems:

* We only used a few variables (min, max, sum)
* No extra arrays were created

So the space complexity is:

* **O(1)** (constant space)

---

## 🔹 Common Mistakes to Avoid

* Initializing min or max with 0 instead of first element
* Using multiple loops when one loop is enough
* Confusing time complexity with number of variables
* Relying too much on built-in functions

---

## 🔹 Key Insight from Day 1

> Most array problems are not hard — they just require **clear thinking and correct initialization**.

Mastering arrays makes future topics like strings, linked lists, and sliding window problems much easier.

---

## ✅ Summary

* Arrays store multiple values in one structure
* One loop can solve many problems efficiently
* Time complexity focuses on loops, not conditions
* Space complexity depends on extra memory used

Day 1 built the **foundation of logical thinking in DSA**.
