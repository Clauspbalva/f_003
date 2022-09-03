# **`multiply`**

Specification file for `multiply` function.

<br>

## 1. Requirements
---

### 1.1 ID
---
> f_003

<br>

### 1.2 Signature
---
> `n3 = multiply(n1, n2)`

<br>

### 1.3 Type and language
---
> Python function

<br>

### 1.4 Purpose
---
> Returns the multiplication of n1 and n2 
by successive addition

<br>

### 1.5 Inputs
---

| Input | Description | Type & Domain |
|---|---|---|
| `n1` | Integer number | *key:integer* <br> `int`
| `n2` | Integer number | *key:integer* <br> `int`

<br>

### 1.6 Outputs
---

| Output | Description | Type & Domain |
|---|---|---|
| `n3` | result of `n1` * `n2` made by successive additions | *key:integer* <br> `int`

## 1. Test cases
---
| Id | `n1` | `n2` | Output expected |
|---|---|---|---|
| 1 | `1.2` | `0` | None |
| 2 | `1` | `"12"` | None |
| 3 | `0` | `0` | 0 |
| 4 | `0` | `1` | 0 |
| 5 | `0` | `-1` | 0 |
| 6 | `-1` | `0` | 0 |
| 7 | `-2` | `-8` | 16 |

<br>

## 2. Algorithm
---

![Algorithm](f_003_algorithm.drawio.png)


