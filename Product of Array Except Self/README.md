# 238. Products of Array Except Self

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Topic](https://img.shields.io/badge/Topic-Array-blue)
![Status](https://img.shields.io/badge/Status-Solved-brightgreen)

---

## 📋 Problem Statement

Given an integer array `nums`, return an array `output` where `output[i]` is the product of all the elements of `nums` **except** `nums[i]`.

> Each product is **guaranteed** to fit in a **32-bit** integer.

---

## 💡 Examples

### Example 1

| Input | Output |
|-------|--------|
| `nums = [1, 2, 3, 4]` | `[24, 12, 8, 6]` |

### Example 2

| Input | Output |
|-------|--------|
| `nums = [-1, 1, 0, -3, 3]` | `[0, 0, 9, 0, 0]` |

---

## 🔧 Approach — Brute Force

For each index `i`, slice out `nums[i]` by combining the left and right parts of the array. Then multiply all remaining elements together and append the result to the output list.

### Steps

1. Loop through each index `i` in `nums`
2. Create a temporary list by joining `nums[:i]` and `nums[i+1:]` — this excludes `nums[i]`
3. Multiply all elements in the temporary list
4. Append the product to the output list

---

## 💻 Code

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            n = 1
            temp = nums[:i] + nums[i+1:]
            for j in temp:
                n = n * j
            output.append(n)

        return output
```

---

## 📊 Complexity Analysis

| | Complexity | Reason |
|---|---|---|
| ⏱️ Time | **O(n²)** | Outer loop runs `n` times, inner loop runs `n-1` times |
| 🗂️ Space | **O(n)** | Storing the output array of size `n` |

---

## ✅ Dry Run

For `nums = [1, 2, 3, 4]`:

| i | temp (nums without index i) | Product | output |
|---|---|---|---|
| 0 | `[2, 3, 4]` | 24 | `[24]` |
| 1 | `[1, 3, 4]` | 12 | `[24, 12]` |
| 2 | `[1, 2, 4]` | 8 | `[24, 12, 8]` |
| 3 | `[1, 2, 3]` | 6 | `[24, 12, 8, 6]` |

---

## 🚀 Optimized Approach (Follow-Up)

> Can you solve it in **O(n)** time **without** using division?

Use the **Prefix & Suffix Product** technique:

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
```

| | Brute Force | Optimized |
|---|---|---|
| Time | O(n²) | **O(n)** |
| Space | O(n) | **O(1)** *(output array excluded)* |
| Division used? | No | No |

---

## 🏷️ Tags

`Array` `Prefix Sum` `Medium` `NeetCode 150`