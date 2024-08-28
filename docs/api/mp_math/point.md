---
title: mbcp.mp_math.point
---
### ***class*** `Point3`

- #### *def* `__init__(self, x: float, y: float, z: float)`


笛卡尔坐标系中的点。

参数:

x: x 坐标  

y: y 坐标  

z: z 坐标  


- #
<details>
<summary>源码</summary>

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

- #### *def* `approx(self, other: 'Point3', epsilon: float = APPROX)`


判断两个点是否近似相等。

参数:

other:   

epsilon:   


- #
<details>
<summary>源码</summary>

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

- #### *def* `__str__(self)`

- #
<details>
<summary>源码</summary>

```python
def __str__(self):
    return f'Point3({self.x}, {self.y}, {self.z})'
```
</details>

- #### `@overload`
- #### *def* `__add__(self, other: 'Vector3')`

- #
<details>
<summary>源码</summary>

```python
@overload
def __add__(self, other: 'Vector3') -> 'Point3':
    ...
```
</details>

- #### `@overload`
- #### *def* `__add__(self, other: 'Point3')`

- #
<details>
<summary>源码</summary>

```python
@overload
def __add__(self, other: 'Point3') -> 'Point3':
    ...
```
</details>

- #### *def* `__add__(self, other)`


P + V -> P
P + P -> P

参数:

other:   


- #
<details>
<summary>源码</summary>

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

- #### *def* `__eq__(self, other)`


判断两个点是否相等。

参数:

other:   


- #
<details>
<summary>源码</summary>

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

