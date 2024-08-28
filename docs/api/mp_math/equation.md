---
title: mbcp.mp\nmath.equation
order: 1
icon: laptop-code
category: API
---

### ***def*** `get_partial_derivative_func(func: MultiVarsFunc, var: int | tuple[int, ...], epsilon: Number) -> MultiVarsFunc`

求N元函数一阶偏导函数。这玩意不太稳定，慎用。

Args:

    func: 函数

    var: 变量位置，可为整数(一阶偏导)或整数元组(高阶偏导)

    epsilon: 偏移量

Returns:

    偏导函数

Raises:

    ValueError: 无效变量类型

<details>
<summary>源代码</summary>

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

### ***def*** `partial_derivative_func() -> Var`



<details>
<summary>源代码</summary>

```python
def partial_derivative_func(*args: Var) -> Var:
    args_list_plus = list(args)
    args_list_plus[var] += epsilon
    args_list_minus = list(args)
    args_list_minus[var] -= epsilon
    return (func(*args_list_plus) - func(*args_list_minus)) / (2 * epsilon)
```
</details>

### ***def*** `high_order_partial_derivative_func() -> Var`



<details>
<summary>源代码</summary>

```python
def high_order_partial_derivative_func(*args: Var) -> Var:
    result_func = func
    for v in var:
        result_func = get_partial_derivative_func(result_func, v, epsilon)
    return result_func(*args)
```
</details>

### ***class*** `CurveEquation`



### &emsp; ***def*** `__init__(self, x_func: OneVarFunc, y_func: OneVarFunc, z_func: OneVarFunc) -> None`

&emsp;曲线方程。

:param x_func:

:param y_func:

:param z_func:

<details>
<summary>源代码</summary>

```python
def __init__(self, x_func: OneVarFunc, y_func: OneVarFunc, z_func: OneVarFunc):
    """
        曲线方程。
        :param x_func:
        :param y_func:
        :param z_func:
        """
    self.x_func = x_func
    self.y_func = y_func
    self.z_func = z_func
```
</details>

### ***var*** `args_list_plus = list(args)`



### ***var*** `args_list_minus = list(args)`



### ***var*** `result_func = func`



### ***var*** `result_func = get_partial_derivative_func(result_func, v, epsilon)`



