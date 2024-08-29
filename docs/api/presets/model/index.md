---
title: mbcp.presets.model
---
### **class** `GeometricModels`
### `@staticmethod`
### *method* `sphere(radius: float, density: float)`



**说明**: 生成球体上的点集。

**返回**: List[Point3]: 球体上的点集。

**参数**:
> - radius:   
> - density:   


<details>
<summary> <b>源代码</b> </summary>

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

