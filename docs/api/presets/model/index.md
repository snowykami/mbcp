---
title: mbcp.presets.model.\n\ninit\n\n
order: 1
icon: laptop-code
category: API
---

### ***def*** `sphere(radius: float, density: float) -> None`

生成球体上的点集。

Args:

    radius:

    density:

Returns:

    List[Point3]: 球体上的点集。

<details>
<summary>源代码</summary>

```python
@staticmethod
def sphere(radius: float, density: float):
    """
        生成球体上的点集。
        Args:
            radius:
            density:
        Returns:
            List[Point3]: 球体上的点集。
        """
    area = 4 * np.pi * radius ** 2
    num = int(area * density)
    phi_list = np.arccos([clamp(-1 + (2.0 * _ - 1.0) / num, -1, 1) for _ in range(num)])
    theta_list = np.sqrt(num * np.pi) * phi_list
    x_array = radius * np.sin(phi_list) * np.cos(theta_list)
    y_array = radius * np.sin(phi_list) * np.sin(theta_list)
    z_array = radius * np.cos(phi_list)
    return [Point3(x_array[i], y_array[i], z_array[i]) for i in range(num)]
```
</details>

### ***class*** `GeometricModels`



### &emsp; ***@staticmethod***
### &emsp; ***def*** `sphere(radius: float, density: float) -> None`

&emsp;生成球体上的点集。

Args:

    radius:

    density:

Returns:

    List[Point3]: 球体上的点集。

<details>
<summary>源代码</summary>

```python
@staticmethod
def sphere(radius: float, density: float):
    """
        生成球体上的点集。
        Args:
            radius:
            density:
        Returns:
            List[Point3]: 球体上的点集。
        """
    area = 4 * np.pi * radius ** 2
    num = int(area * density)
    phi_list = np.arccos([clamp(-1 + (2.0 * _ - 1.0) / num, -1, 1) for _ in range(num)])
    theta_list = np.sqrt(num * np.pi) * phi_list
    x_array = radius * np.sin(phi_list) * np.cos(theta_list)
    y_array = radius * np.sin(phi_list) * np.sin(theta_list)
    z_array = radius * np.cos(phi_list)
    return [Point3(x_array[i], y_array[i], z_array[i]) for i in range(num)]
```
</details>

### ***var*** `area = 4 * np.pi * radius ** 2`



### ***var*** `num = int(area * density)`



### ***var*** `phi_list = np.arccos([clamp(-1 + (2.0 * _ - 1.0) / num, -1, 1) for _ in range(num)])`



### ***var*** `theta_list = np.sqrt(num * np.pi) * phi_list`



### ***var*** `x_array = radius * np.sin(phi_list) * np.cos(theta_list)`



### ***var*** `y_array = radius * np.sin(phi_list) * np.sin(theta_list)`



### ***var*** `z_array = radius * np.cos(phi_list)`


