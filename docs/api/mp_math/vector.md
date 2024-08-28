---
title: mbcp.mp\nmath.vector
order: 1
icon: laptop-code
category: API
---

### ***class*** `Vector3`



### &emsp; ***def*** `__init__(self, x: float, y: float, z: float) -> None`

&emsp;3维向量

Args:

    x: x轴分量

    y: y轴分量

    z: z轴分量

<details>
<summary>源代码</summary>

```python
def __init__(self, x: float, y: float, z: float):
    """
        3维向量
        Args:
            x: x轴分量
            y: y轴分量
            z: z轴分量
        """
    self.x = x
    self.y = y
    self.z = z
```
</details>

### &emsp; ***def*** `approx(self, other: 'Vector3', epsilon: float) -> bool`

&emsp;判断两个向量是否近似相等。

Args:

    other:

    epsilon:



Returns:

    是否近似相等

<details>
<summary>源代码</summary>

```python
def approx(self, other: 'Vector3', epsilon: float=APPROX) -> bool:
    """
        判断两个向量是否近似相等。
        Args:
            other:
            epsilon:

        Returns:
            是否近似相等
        """
    return all([abs(self.x - other.x) < epsilon, abs(self.y - other.y) < epsilon, abs(self.z - other.z) < epsilon])
```
</details>

### &emsp; ***def*** `cal_angle(self, other: 'Vector3') -> 'AnyAngle'`

&emsp;计算两个向量之间的夹角。

Args:

    other: 另一个向量

Returns:

    夹角

<details>
<summary>源代码</summary>

```python
def cal_angle(self, other: 'Vector3') -> 'AnyAngle':
    """
        计算两个向量之间的夹角。
        Args:
            other: 另一个向量
        Returns:
            夹角
        """
    return AnyAngle(math.acos(self @ other / (self.length * other.length)), is_radian=True)
```
</details>

### &emsp; ***def*** `cross(self, other: 'Vector3') -> 'Vector3'`

&emsp;向量积 叉乘：v1 cross v2 -> v3



叉乘为0，则两向量平行。

其余结果的模为平行四边形的面积。



返回如下行列式的结果：



``i  j  k``



``x1 y1 z1``



``x2 y2 z2``



Args:

    other:

Returns:

    行列式的结果

<details>
<summary>源代码</summary>

```python
def cross(self, other: 'Vector3') -> 'Vector3':
    """
        向量积 叉乘：v1 cross v2 -> v3

        叉乘为0，则两向量平行。
        其余结果的模为平行四边形的面积。

        返回如下行列式的结果：

        ``i  j  k``

        ``x1 y1 z1``

        ``x2 y2 z2``

        Args:
            other:
        Returns:
            行列式的结果
        """
    return Vector3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
```
</details>

### &emsp; ***def*** `is_approx_parallel(self, other: 'Vector3', epsilon: float) -> bool`

&emsp;判断两个向量是否近似平行。

Args:

    other: 另一个向量

    epsilon: 允许的误差

Returns:

    是否近似平行

<details>
<summary>源代码</summary>

```python
def is_approx_parallel(self, other: 'Vector3', epsilon: float=APPROX) -> bool:
    """
        判断两个向量是否近似平行。
        Args:
            other: 另一个向量
            epsilon: 允许的误差
        Returns:
            是否近似平行
        """
    return self.cross(other).length < epsilon
```
</details>

### &emsp; ***def*** `is_parallel(self, other: 'Vector3') -> bool`

&emsp;判断两个向量是否平行。

Args:

    other: 另一个向量

Returns:

    是否平行

<details>
<summary>源代码</summary>

```python
def is_parallel(self, other: 'Vector3') -> bool:
    """
        判断两个向量是否平行。
        Args:
            other: 另一个向量
        Returns:
            是否平行
        """
    return self.cross(other).approx(zero_vector3)
```
</details>

### &emsp; ***def*** `normalize(self) -> None`

&emsp;将向量归一化。



自体归一化，不返回值。

<details>
<summary>源代码</summary>

```python
def normalize(self):
    """
        将向量归一化。

        自体归一化，不返回值。
        """
    length = self.length
    self.x /= length
    self.y /= length
    self.z /= length
```
</details>

### &emsp; ***@property***
### &emsp; ***def*** `np_array(self: Any) -> 'np.ndarray'`

&emsp;返回numpy数组

Returns:

<details>
<summary>源代码</summary>

```python
@property
def np_array(self) -> 'np.ndarray':
    """
        返回numpy数组
        Returns:
        """
    return np.array([self.x, self.y, self.z])
```
</details>

### &emsp; ***@property***
### &emsp; ***def*** `length(self: Any) -> float`

&emsp;向量的模。

Returns:

    模

<details>
<summary>源代码</summary>

```python
@property
def length(self) -> float:
    """
        向量的模。
        Returns:
            模
        """
    return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
```
</details>

### &emsp; ***@property***
### &emsp; ***def*** `unit(self: Any) -> 'Vector3'`

&emsp;获取该向量的单位向量。

Returns:

    单位向量

<details>
<summary>源代码</summary>

```python
@property
def unit(self) -> 'Vector3':
    """
        获取该向量的单位向量。
        Returns:
            单位向量
        """
    return self / self.length
```
</details>

### ***var*** `zero_vector3 = Vector3(0, 0, 0)`



### ***var*** `x_axis = Vector3(1, 0, 0)`



### ***var*** `y_axis = Vector3(0, 1, 0)`



### ***var*** `z_axis = Vector3(0, 0, 1)`



### ***var*** `length = self.length`



