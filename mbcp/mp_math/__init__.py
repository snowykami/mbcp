# -*- coding: utf-8 -*-
"""
本包定义了一些常用的导入，可直接从`mbcp.mp_math`导入使用
导入的类有：
- [`AnyAngle`](./angle#class-anyangle)：任意角度
- [`CurveEquation`](./equation#class-curveequation)：曲线方程
- [`Line3`](./line#class-line3)：三维直线
- [`Plane3`](./plane#class-plane3)：三维平面
- [`Point3`](./point#class-point3)：三维点
- [`Segment3`](./segment#class-segment3)：三维线段
- [`Vector3`](./vector#class-vector3)：三维向量
"""
from .angle import AnyAngle
from .const import *
from .equation import CurveEquation
from .line import Line3
from .plane import Plane3
from .point import Point3
from .segment import Segment3
from .vector import Vector3
