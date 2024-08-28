---
title: mbcp.mp\nmath.angle
order: 1
icon: laptop-code
category: API
---

### ***class*** `AnyAngle`



### &emsp; ***def*** `__init__(self, value: float, is_radian: bool) -> None`

&emsp;任意角度。

Args:

    value: 角度或弧度值

    is_radian: 是否为弧度，默认为否

<details>
<summary>源代码</summary>

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

### &emsp; ***@property***
### &emsp; ***def*** `complementary(self: Any) -> 'AnyAngle'`

&emsp;余角：两角的和为90°。

Returns:

    余角

<details>
<summary>源代码</summary>

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

### &emsp; ***@property***
### &emsp; ***def*** `supplementary(self: Any) -> 'AnyAngle'`

&emsp;补角：两角的和为180°。

Returns:

    补角

<details>
<summary>源代码</summary>

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

### &emsp; ***@property***
### &emsp; ***def*** `degree(self: Any) -> float`

&emsp;角度。

Returns:

    弧度

<details>
<summary>源代码</summary>

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

### &emsp; ***@property***
### &emsp; ***def*** `minimum_positive(self: Any) -> 'AnyAngle'`

&emsp;最小正角。

Returns:

    最小正角度

<details>
<summary>源代码</summary>

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

### &emsp; ***@property***
### &emsp; ***def*** `maximum_negative(self: Any) -> 'AnyAngle'`

&emsp;最大负角。

Returns:

    最大负角度

<details>
<summary>源代码</summary>

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

### &emsp; ***@property***
### &emsp; ***def*** `sin(self: Any) -> float`

&emsp;正弦值。

Returns:

    正弦值

<details>
<summary>源代码</summary>

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

### &emsp; ***@property***
### &emsp; ***def*** `cos(self: Any) -> float`

&emsp;余弦值。

Returns:

    余弦值

<details>
<summary>源代码</summary>

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

### &emsp; ***@property***
### &emsp; ***def*** `tan(self: Any) -> float`

&emsp;正切值。

Returns:

    正切值

<details>
<summary>源代码</summary>

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

### &emsp; ***@property***
### &emsp; ***def*** `cot(self: Any) -> float`

&emsp;余切值。

Returns:

    余切值

<details>
<summary>源代码</summary>

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

### &emsp; ***@property***
### &emsp; ***def*** `sec(self: Any) -> float`

&emsp;正割值。

Returns:

    正割值

<details>
<summary>源代码</summary>

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

### &emsp; ***@property***
### &emsp; ***def*** `csc(self: Any) -> float`

&emsp;余割值。

Returns:

    余割值

<details>
<summary>源代码</summary>

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

