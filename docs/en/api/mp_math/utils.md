---
title: mbcp.mp_math.utils
---
### *func* `clamp() -> float`



**Description**: 区间限定函数

**Return**: 限制后的值

**Arguments**:
> - x: 待限定的值  
> - min_: 最小值  
> - max_: 最大值  


<details>
<summary> <b>Source code</b> </summary>

```python
def clamp(x: float, min_: float, max_: float) -> float:
    """
    区间限定函数
    Args:
        x: 待限定的值
        min_: 最小值
        max_: 最大值

    Returns:
        限制后的值
    """
    return max(min(x, max_), min_)
```
</details>

### *func* `approx(x: float = 0.0, y: float = APPROX) -> bool`



**Description**: 判断两个数是否近似相等。或包装一个实数，用于判断是否近似于0。

**Return**: 是否近似相等

**Arguments**:
> - x: 数1  
> - y: 数2  
> - epsilon: 误差  


<details>
<summary> <b>Source code</b> </summary>

```python
def approx(x: float, y: float=0.0, epsilon: float=APPROX) -> bool:
    """
    判断两个数是否近似相等。或包装一个实数，用于判断是否近似于0。
    Args:
        x: 数1
        y: 数2
        epsilon: 误差
    Returns:
        是否近似相等
    """
    return abs(x - y) < epsilon
```
</details>

### *func* `sign(x: float = False) -> str`



**Description**: 获取数的符号。

**Return**: 符号 + - ""

**Arguments**:
> - x: 数  
> - only_neg: 是否只返回负数的符号  


<details>
<summary> <b>Source code</b> </summary>

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

### *func* `sign_format(x: float = False) -> str`



**Description**: 格式化符号数
-1 -> -1
1 -> +1
0 -> ""

**Return**: 符号 + - ""

**Arguments**:
> - x: 数  
> - only_neg: 是否只返回负数的符号  


<details>
<summary> <b>Source code</b> </summary>

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

### **class** `Approx`
### *method* `__init__(self, value: RealNumber)`


<details>
<summary> <b>Source code</b> </summary>

```python
def __init__(self, value: RealNumber):
    self.value = value
```
</details>

### *method* `__eq__(self, other)`


<details>
<summary> <b>Source code</b> </summary>

```python
def __eq__(self, other):
    if isinstance(self.value, (float, int)):
        if isinstance(other, (float, int)):
            return abs(self.value - other) < APPROX
        else:
            self.raise_type_error(other)
    elif isinstance(self.value, Vector3):
        if isinstance(other, (Vector3, Point3, Plane3, Line3)):
            return all([approx(self.value.x, other.x), approx(self.value.y, other.y), approx(self.value.z, other.z)])
        else:
            self.raise_type_error(other)
```
</details>

### *method* `raise_type_error(self, other)`


<details>
<summary> <b>Source code</b> </summary>

```python
def raise_type_error(self, other):
    raise TypeError(f'Unsupported type: {type(self.value)} and {type(other)}')
```
</details>

### *method* `__ne__(self, other)`


<details>
<summary> <b>Source code</b> </summary>

```python
def __ne__(self, other):
    return not self.__eq__(other)
```
</details>

