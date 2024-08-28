---
title: mbcp.mp_math.equation
---
### ***var*** `result_func = get_partial_derivative_func(result_func, v, epsilon)`

### *def* `get_partial_derivative_func(func: MultiVarsFunc = EPSILON)`


求N元函数一阶偏导函数。这玩意不太稳定，慎用。

参数:

func: 函数  

var: 变量位置，可为整数(一阶偏导)或整数元组(高阶偏导)  

epsilon: 偏移量  



<details>
<summary>源码</summary>

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

### *def* `partial_derivative_func()`


<details>
<summary>源码</summary>

```python
def partial_derivative_func(*args: Var) -> Var:
    args_list_plus = list(args)
    args_list_plus[var] += epsilon
    args_list_minus = list(args)
    args_list_minus[var] -= epsilon
    return (func(*args_list_plus) - func(*args_list_minus)) / (2 * epsilon)
```
</details>

### *def* `high_order_partial_derivative_func()`


<details>
<summary>源码</summary>

```python
def high_order_partial_derivative_func(*args: Var) -> Var:
    result_func = func
    for v in var:
        result_func = get_partial_derivative_func(result_func, v, epsilon)
    return result_func(*args)
```
</details>

### ***class*** `CurveEquation`

- #### *def* `__init__(self, x_func: OneVarFunc, y_func: OneVarFunc, z_func: OneVarFunc)`


曲线方程。

参数:

x_func: x函数  

y_func: y函数  

z_func: z函数  


- #
<details>
<summary>源码</summary>

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

- #### *def* `__call__(self)`


计算曲线上的点。

参数:

*t:   

参数:   


- #
<details>
<summary>源码</summary>

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

- #### *def* `__str__(self)`

- #
<details>
<summary>源码</summary>

```python
def __str__(self):
    return 'CurveEquation()'
```
</details>

