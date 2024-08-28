---
title: mbcp.mp_math.segment
---
### ***class*** `Segment3`

### *def* `__init__(self, p1: 'Point3', p2: 'Point3')`


三维空间中的线段。
:param p1:
:param p2:



<details>
<summary>源碼</summary>

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

### *def* `__repr__(self)`


<details>
<summary>源碼</summary>

```python
def __repr__(self):
    return f'Segment3({self.p1}, {self.p2})'
```
</details>

### *def* `__str__(self)`


<details>
<summary>源碼</summary>

```python
def __str__(self):
    return f'Segment3({self.p1} -> {self.p2})'
```
</details>

