---
title: mbcp.mp\nmath.point
order: 1
icon: laptop-code
category: API
---

### ***class*** `Point3`



### &emsp; ***def*** `__init__(self, x: float, y: float, z: float) -> None`

&emsp;笛卡尔坐标系中的点。

Args:

    x: x 坐标

    y: y 坐标

    z: z 坐标

<details>
<summary>源代码</summary>

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

### &emsp; ***def*** `approx(self, other: 'Point3', epsilon: float) -> bool`

&emsp;判断两个点是否近似相等。

Args:

    other:

    epsilon:



Returns:

    是否近似相等

<details>
<summary>源代码</summary>

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

