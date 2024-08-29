---
title: mbcp.mp_math.point
---
### **class** `Point3`
### *method* `__init__(self, x: float, y: float, z: float)`



**Description**: 笛卡尔坐标系中的点。

**Arguments**:
> - x: x 坐标  
> - y: y 坐标  
> - z: z 坐标  


<details>
<summary> <b>Source code</b> </summary>

```python
def __init__(self, x: float, y: float, z: float):
    """
        笛卡尔坐标系中的点。
        Args:
            x: x 坐标
            y: y 坐标
            z: z 坐标
        """
    self.x = x
    self.y = y
    self.z = z
```
</details>

### *method* `approx(self, other: Point3, epsilon: float = APPROX) -> bool`



**Description**: 判断两个点是否近似相等。

**Arguments**:
> - other:   
> - epsilon:   

**Return**: 是否近似相等


<details>
<summary> <b>Source code</b> </summary>

```python
def approx(self, other: 'Point3', epsilon: float=APPROX) -> bool:
    """
        判断两个点是否近似相等。
        Args:
            other:
            epsilon:

        Returns:
            是否近似相等
        """
    return all([abs(self.x - other.x) < epsilon, abs(self.y - other.y) < epsilon, abs(self.z - other.z) < epsilon])
```
</details>

### `@overload`
### *method* `self + other: Vector3 => Point3`


<details>
<summary> <b>Source code</b> </summary>

```python
@overload
def __add__(self, other: 'Vector3') -> 'Point3':
    ...
```
</details>

### `@overload`
### *method* `self + other: Point3 => Point3`


<details>
<summary> <b>Source code</b> </summary>

```python
@overload
def __add__(self, other: 'Point3') -> 'Point3':
    ...
```
</details>

### *method* `self + other`



**Description**: P + V -> P
P + P -> P

**Arguments**:
> - other:   


<details>
<summary> <b>Source code</b> </summary>

```python
def __add__(self, other):
    """
        P + V -> P
        P + P -> P
        Args:
            other:
        Returns:
        """
    return Point3(self.x + other.x, self.y + other.y, self.z + other.z)
```
</details>

### *method* `__eq__(self, other)`



**Description**: 判断两个点是否相等。

**Arguments**:
> - other:   


<details>
<summary> <b>Source code</b> </summary>

```python
def __eq__(self, other):
    """
        判断两个点是否相等。
        Args:
            other:
        Returns:
        """
    return approx(self.x, other.x) and approx(self.y, other.y) and approx(self.z, other.z)
```
</details>

### *method* `self - other: Point3 => Vector3`



**Description**: P - P -> V

P - V -> P  已在 :class:`Vector3` 中实现

**Arguments**:
> - other:   


<details>
<summary> <b>Source code</b> </summary>

```python
def __sub__(self, other: 'Point3') -> 'Vector3':
    """
        P - P -> V

        P - V -> P  已在 :class:`Vector3` 中实现
        Args:
            other:
        Returns:

        """
    from .vector import Vector3
    return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
```
</details>

