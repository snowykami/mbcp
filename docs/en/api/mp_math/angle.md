---
title: mbcp.mp_math.angle
---
### **class** `Angle`
### **class** `AnyAngle(Angle)`
### *method* `__init__(self, value: float, is_radian: bool = False)`



**Description**: 任意角度。

**Arguments**:
> - value: 角度或弧度值  
> - is_radian: 是否为弧度，默认为否  


<details>
<summary> <b>Source code</b> </summary>

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
### *method* `complementary(self) -> AnyAngle`



**Description**: 余角：两角的和为90°。

**Return**: 余角


<details>
<summary> <b>Source code</b> </summary>

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
### *method* `supplementary(self) -> AnyAngle`



**Description**: 补角：两角的和为180°。

**Return**: 补角


<details>
<summary> <b>Source code</b> </summary>

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
### *method* `degree(self) -> float`



**Description**: 角度。

**Return**: 弧度


<details>
<summary> <b>Source code</b> </summary>

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
### *method* `minimum_positive(self) -> AnyAngle`



**Description**: 最小正角。

**Return**: 最小正角度


<details>
<summary> <b>Source code</b> </summary>

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
### *method* `maximum_negative(self) -> AnyAngle`



**Description**: 最大负角。

**Return**: 最大负角度


<details>
<summary> <b>Source code</b> </summary>

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
### *method* `sin(self) -> float`



**Description**: 正弦值。

**Return**: 正弦值


<details>
<summary> <b>Source code</b> </summary>

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
### *method* `cos(self) -> float`



**Description**: 余弦值。

**Return**: 余弦值


<details>
<summary> <b>Source code</b> </summary>

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
### *method* `tan(self) -> float`



**Description**: 正切值。

**Return**: 正切值


<details>
<summary> <b>Source code</b> </summary>

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
### *method* `cot(self) -> float`



**Description**: 余切值。

**Return**: 余切值


<details>
<summary> <b>Source code</b> </summary>

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
### *method* `sec(self) -> float`



**Description**: 正割值。

**Return**: 正割值


<details>
<summary> <b>Source code</b> </summary>

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
### *method* `csc(self) -> float`



**Description**: 余割值。

**Return**: 余割值


<details>
<summary> <b>Source code</b> </summary>

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

### *method* `self + other: AnyAngle => AnyAngle`


<details>
<summary> <b>Source code</b> </summary>

```python
def __add__(self, other: 'AnyAngle') -> 'AnyAngle':
    return AnyAngle(self.radian + other.radian, is_radian=True)
```
</details>

### *method* `__eq__(self, other)`


<details>
<summary> <b>Source code</b> </summary>

```python
def __eq__(self, other):
    return approx(self.radian, other.radian)
```
</details>

### *method* `self - other: AnyAngle => AnyAngle`


<details>
<summary> <b>Source code</b> </summary>

```python
def __sub__(self, other: 'AnyAngle') -> 'AnyAngle':
    return AnyAngle(self.radian - other.radian, is_radian=True)
```
</details>

### *method* `self * other: float => AnyAngle`


<details>
<summary> <b>Source code</b> </summary>

```python
def __mul__(self, other: float) -> 'AnyAngle':
    return AnyAngle(self.radian * other, is_radian=True)
```
</details>

### `@overload`
### *method* `self / other: float => AnyAngle`


<details>
<summary> <b>Source code</b> </summary>

```python
@overload
def __truediv__(self, other: float) -> 'AnyAngle':
    ...
```
</details>

### `@overload`
### *method* `self / other: AnyAngle => float`


<details>
<summary> <b>Source code</b> </summary>

```python
@overload
def __truediv__(self, other: 'AnyAngle') -> float:
    ...
```
</details>

### *method* `self / other`


<details>
<summary> <b>Source code</b> </summary>

```python
def __truediv__(self, other):
    if isinstance(other, AnyAngle):
        return self.radian / other.radian
    return AnyAngle(self.radian / other, is_radian=True)
```
</details>

