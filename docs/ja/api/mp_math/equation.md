---
title: mbcp.mp_math.equation
---
### *func* `get_partial_derivative_func(func: MultiVarsFunc = EPSILON) -> MultiVarsFunc`



**説明**: 求N元函数一阶偏导函数。这玩意不太稳定，慎用。

**戻り値**: 偏导函数

**引数**:
> - func: 函数  
> - var: 变量位置，可为整数(一阶偏导)或整数元组(高阶偏导)  
> - epsilon: 偏移量  

**例外**:
> - ValueError  无效变量类型


<details>
<summary> <b>ソースコード</b> </summary>

```python
def get_partial_derivative_func(func: MultiVarsFunc, var: int | tuple[int, ...], epsilon: Number=EPSILON) -> MultiVarsFunc:
    """
    求N元函数一阶偏导函数。这玩意不太稳定，慎用。
    Args:
        func: 函数
        var: 变量位置，可为整数(一阶偏导)或整数元组(高阶偏导)
        epsilon: 偏移量
    Returns:
        偏导函数
    Raises:
        ValueError: 无效变量类型
    """
    if isinstance(var, int):

        def partial_derivative_func(*args: Var) -> Var:
            args_list_plus = list(args)
            args_list_plus[var] += epsilon
            args_list_minus = list(args)
            args_list_minus[var] -= epsilon
            return (func(*args_list_plus) - func(*args_list_minus)) / (2 * epsilon)
        return partial_derivative_func
    elif isinstance(var, tuple):

        def high_order_partial_derivative_func(*args: Var) -> Var:
            result_func = func
            for v in var:
                result_func = get_partial_derivative_func(result_func, v, epsilon)
            return result_func(*args)
        return high_order_partial_derivative_func
    else:
        raise ValueError('Invalid var type')
```
</details>

### *func* `partial_derivative_func() -> Var`


<details>
<summary> <b>ソースコード</b> </summary>

```python
def partial_derivative_func(*args: Var) -> Var:
    args_list_plus = list(args)
    args_list_plus[var] += epsilon
    args_list_minus = list(args)
    args_list_minus[var] -= epsilon
    return (func(*args_list_plus) - func(*args_list_minus)) / (2 * epsilon)
```
</details>

### *func* `high_order_partial_derivative_func() -> Var`


<details>
<summary> <b>ソースコード</b> </summary>

```python
def high_order_partial_derivative_func(*args: Var) -> Var:
    result_func = func
    for v in var:
        result_func = get_partial_derivative_func(result_func, v, epsilon)
    return result_func(*args)
```
</details>

### **class** `CurveEquation`
### *method* `__init__(self, x_func: OneVarFunc, y_func: OneVarFunc, z_func: OneVarFunc)`



**説明**: 曲线方程。

**引数**:
> - x_func: x函数  
> - y_func: y函数  
> - z_func: z函数  


<details>
<summary> <b>ソースコード</b> </summary>

```python
def __init__(self, x_func: OneVarFunc, y_func: OneVarFunc, z_func: OneVarFunc):
    """
        曲线方程。
        Args:
            x_func: x函数
            y_func: y函数
            z_func: z函数
        """
    self.x_func = x_func
    self.y_func = y_func
    self.z_func = z_func
```
</details>

### *method* `__call__(self) -> Point3 | tuple[Point3, ...]`



**説明**: 计算曲线上的点。

**引数**:
> - *t:   
> - 参数:   


<details>
<summary> <b>ソースコード</b> </summary>

```python
def __call__(self, *t: Var) -> Point3 | tuple[Point3, ...]:
    """
        计算曲线上的点。
        Args:
            *t:
                参数
        Returns:

        """
    if len(t) == 1:
        return Point3(self.x_func(t[0]), self.y_func(t[0]), self.z_func(t[0]))
    else:
        return tuple([Point3(x, y, z) for x, y, z in zip(self.x_func(t), self.y_func(t), self.z_func(t))])
```
</details>

