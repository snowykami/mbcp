---
title: mbcp.mp\nmath.utils
order: 1
icon: laptop-code
category: API
---

### ***def*** `clamp(x: float, min_: float, max_: float) -> float`

区间截断函数。

Args:

    x:

    min_:

    max_:



Returns:

    限制后的值

<details>
<summary>源代码</summary>

```python
def clamp(x: float, min_: float, max_: float) -> float:
    """
    区间截断函数。
    Args:
        x:
        min_:
        max_:

    Returns:
        限制后的值
    """
    return max(min(x, max_), min_)
```
</details>

### ***def*** `approx(x: float, y: float, epsilon: float) -> bool`

判断两个数是否近似相等。或包装一个实数，用于判断是否近似于0。

Args:

    x:

    y:

    epsilon:



Returns:

    是否近似相等

<details>
<summary>源代码</summary>

```python
def approx(x: float, y: float=0.0, epsilon: float=APPROX) -> bool:
    """
    判断两个数是否近似相等。或包装一个实数，用于判断是否近似于0。
    Args:
        x:
        y:
        epsilon:

    Returns:
        是否近似相等
    """
    return abs(x - y) < epsilon
```
</details>

### ***def*** `sign(x: float, only_neg: bool) -> str`

获取数的符号。

Args:

    x: 数

    only_neg: 是否只返回负数的符号

Returns:

    符号 + - ""

<details>
<summary>源代码</summary>

```python
def sign(x: float, only_neg: bool=False) -> str:
    """获取数的符号。
    Args:
        x: 数
        only_neg: 是否只返回负数的符号
    Returns:
        符号 + - ""
    """
    if x > 0:
        return '+' if not only_neg else ''
    elif x < 0:
        return '-'
    else:
        return ''
```
</details>

### ***def*** `sign_format(x: float, only_neg: bool) -> str`

格式化符号数

-1 -> -1

1 -> +1

0 -> ""

Args:

    x: 数

    only_neg: 是否只返回负数的符号

Returns:

    符号 + - ""

<details>
<summary>源代码</summary>

```python
def sign_format(x: float, only_neg: bool=False) -> str:
    """格式化符号数
    -1 -> -1
    1 -> +1
    0 -> ""
    Args:
        x: 数
        only_neg: 是否只返回负数的符号
    Returns:
        符号 + - ""
    """
    if x > 0:
        return f'+{x}' if not only_neg else f'{x}'
    elif x < 0:
        return f'-{abs(x)}'
    else:
        return ''
```
</details>

### ***class*** `Approx`

用于近似比较对象



已实现对象 实数 Vector3 Point3 Plane3 Line3

### &emsp; ***def*** `__init__(self, value: RealNumber) -> None`

&emsp;

<details>
<summary>源代码</summary>

```python
def __init__(self, value: RealNumber):
    self.value = value
```
</details>

### &emsp; ***def*** `raise_type_error(self, other: Any) -> None`

&emsp;

<details>
<summary>源代码</summary>

```python
def raise_type_error(self, other):
    raise TypeError(f'Unsupported type: {type(self.value)} and {type(other)}')
```
</details>

