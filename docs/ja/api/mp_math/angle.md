---
title: mbcp.mp_math.angle
---
### ***class*** `Angle`

### ***class*** `AnyAngle`

### *def* `__init__(self, value: float, is_radian: bool = False)`


任意角度。

引数:

- value: 角度或弧度值  

- is_radian: 是否为弧度，默认为否  



<details>
<summary>ソースコード</summary>

```python
def __init__(self, value: float, is_radian: bool=False):
    """
        任意角度。
        Args:
            value: 角度或弧度值
            is_radian: 是否为弧度，默认为否
        """
    if is_radian:
        self.radian = value
    else:
        self.radian = value * PI / 180
```
</details>

### `@property`
### *def* `complementary(self) -> 'AnyAngle'`


余角：两角的和为90°。

戻り値:

- 余角



<details>
<summary>ソースコード</summary>

```python
@property
def complementary(self) -> 'AnyAngle':
    """
        余角：两角的和为90°。
        Returns:
            余角
        """
    return AnyAngle(PI / 2 - self.minimum_positive.radian, is_radian=True)
```
</details>

### `@property`
### *def* `supplementary(self) -> 'AnyAngle'`


补角：两角的和为180°。

戻り値:

- 补角



<details>
<summary>ソースコード</summary>

```python
@property
def supplementary(self) -> 'AnyAngle':
    """
        补角：两角的和为180°。
        Returns:
            补角
        """
    return AnyAngle(PI - self.minimum_positive.radian, is_radian=True)
```
</details>

### `@property`
### *def* `degree(self) -> float`


角度。

戻り値:

- 弧度



<details>
<summary>ソースコード</summary>

```python
@property
def degree(self) -> float:
    """
        角度。
        Returns:
            弧度
        """
    return self.radian * 180 / PI
```
</details>

### `@property`
### *def* `minimum_positive(self) -> 'AnyAngle'`


最小正角。

戻り値:

- 最小正角度



<details>
<summary>ソースコード</summary>

```python
@property
def minimum_positive(self) -> 'AnyAngle':
    """
        最小正角。
        Returns:
            最小正角度
        """
    return AnyAngle(self.radian % (2 * PI))
```
</details>

### `@property`
### *def* `maximum_negative(self) -> 'AnyAngle'`


最大负角。

戻り値:

- 最大负角度



<details>
<summary>ソースコード</summary>

```python
@property
def maximum_negative(self) -> 'AnyAngle':
    """
        最大负角。
        Returns:
            最大负角度
        """
    return AnyAngle(-self.radian % (2 * PI), is_radian=True)
```
</details>

### `@property`
### *def* `sin(self) -> float`


正弦值。

戻り値:

- 正弦值



<details>
<summary>ソースコード</summary>

```python
@property
def sin(self) -> float:
    """
        正弦值。
        Returns:
            正弦值
        """
    return math.sin(self.radian)
```
</details>

### `@property`
### *def* `cos(self) -> float`


余弦值。

戻り値:

- 余弦值



<details>
<summary>ソースコード</summary>

```python
@property
def cos(self) -> float:
    """
        余弦值。
        Returns:
            余弦值
        """
    return math.cos(self.radian)
```
</details>

### `@property`
### *def* `tan(self) -> float`


正切值。

戻り値:

- 正切值



<details>
<summary>ソースコード</summary>

```python
@property
def tan(self) -> float:
    """
        正切值。
        Returns:
            正切值
        """
    return math.tan(self.radian)
```
</details>

### `@property`
### *def* `cot(self) -> float`


余切值。

戻り値:

- 余切值



<details>
<summary>ソースコード</summary>

```python
@property
def cot(self) -> float:
    """
        余切值。
        Returns:
            余切值
        """
    return 1 / math.tan(self.radian)
```
</details>

### `@property`
### *def* `sec(self) -> float`


正割值。

戻り値:

- 正割值



<details>
<summary>ソースコード</summary>

```python
@property
def sec(self) -> float:
    """
        正割值。
        Returns:
            正割值
        """
    return 1 / math.cos(self.radian)
```
</details>

### `@property`
### *def* `csc(self) -> float`


余割值。

戻り値:

- 余割值



<details>
<summary>ソースコード</summary>

```python
@property
def csc(self) -> float:
    """
        余割值。
        Returns:
            余割值
        """
    return 1 / math.sin(self.radian)
```
</details>

### *def* `__add__(self, other: 'AnyAngle') -> 'AnyAngle'`


<details>
<summary>ソースコード</summary>

```python
def __add__(self, other: 'AnyAngle') -> 'AnyAngle':
    return AnyAngle(self.radian + other.radian, is_radian=True)
```
</details>

### *def* `__eq__(self, other)`


<details>
<summary>ソースコード</summary>

```python
def __eq__(self, other):
    return approx(self.radian, other.radian)
```
</details>

### *def* `__sub__(self, other: 'AnyAngle') -> 'AnyAngle'`


<details>
<summary>ソースコード</summary>

```python
def __sub__(self, other: 'AnyAngle') -> 'AnyAngle':
    return AnyAngle(self.radian - other.radian, is_radian=True)
```
</details>

### *def* `__mul__(self, other: float) -> 'AnyAngle'`


<details>
<summary>ソースコード</summary>

```python
def __mul__(self, other: float) -> 'AnyAngle':
    return AnyAngle(self.radian * other, is_radian=True)
```
</details>

### *def* `__repr__(self)`


<details>
<summary>ソースコード</summary>

```python
def __repr__(self):
    return f'AnyAngle({self.radian}, is_radian=True)'
```
</details>

### *def* `__str__(self)`


<details>
<summary>ソースコード</summary>

```python
def __str__(self):
    return f'AnyAngle({self.degree}° or {self.radian} rad)'
```
</details>

### `@overload`
### *def* `__truediv__(self, other: float) -> 'AnyAngle'`


<details>
<summary>ソースコード</summary>

```python
@overload
def __truediv__(self, other: float) -> 'AnyAngle':
    ...
```
</details>

### `@overload`
### *def* `__truediv__(self, other: 'AnyAngle') -> float`


<details>
<summary>ソースコード</summary>

```python
@overload
def __truediv__(self, other: 'AnyAngle') -> float:
    ...
```
</details>

### *def* `__truediv__(self, other)`


<details>
<summary>ソースコード</summary>

```python
def __truediv__(self, other):
    if isinstance(other, AnyAngle):
        return self.radian / other.radian
    return AnyAngle(self.radian / other, is_radian=True)
```
</details>

