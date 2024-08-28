---
title: mbcp.mp\nmath.segment
order: 1
icon: laptop-code
category: API
---

### ***class*** `Segment3`



### &emsp; ***def*** `__init__(self, p1: 'Point3', p2: 'Point3') -> None`

&emsp;三维空间中的线段。

:param p1:

:param p2:

<details>
<summary>源代码</summary>

```python
def __init__(self, p1: 'Point3', p2: 'Point3'):
    """
        三维空间中的线段。
        :param p1:
        :param p2:
        """
    self.p1 = p1
    self.p2 = p2
    '方向向量'
    self.direction = self.p2 - self.p1
    '长度'
    self.length = self.direction.length
    '中心点'
    self.midpoint = Point3((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2, (self.p1.z + self.p2.z) / 2)
```
</details>

