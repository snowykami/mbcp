---
title: mbcp.mp_math.mp_math_typing
---
### ***var*** `RealNumber = int | float`

- **类型**: `TypeAlias`

### ***var*** `Number = RealNumber | complex`

- **类型**: `TypeAlias`

### ***var*** `Var = SingleVar | ArrayVar`

- **类型**: `TypeAlias`

### ***var*** `OneSingleVarFunc = Callable[[SingleVar], SingleVar]`

- **类型**: `TypeAlias`

### ***var*** `OneArrayFunc = Callable[[ArrayVar], ArrayVar]`

- **类型**: `TypeAlias`

### ***var*** `OneVarFunc = OneSingleVarFunc | OneArrayFunc`

- **类型**: `TypeAlias`

### ***var*** `TwoSingleVarsFunc = Callable[[SingleVar, SingleVar], SingleVar]`

- **类型**: `TypeAlias`

### ***var*** `TwoArraysFunc = Callable[[ArrayVar, ArrayVar], ArrayVar]`

- **类型**: `TypeAlias`

### ***var*** `TwoVarsFunc = TwoSingleVarsFunc | TwoArraysFunc`

- **类型**: `TypeAlias`

### ***var*** `ThreeSingleVarsFunc = Callable[[SingleVar, SingleVar, SingleVar], SingleVar]`

- **类型**: `TypeAlias`

### ***var*** `ThreeArraysFunc = Callable[[ArrayVar, ArrayVar, ArrayVar], ArrayVar]`

- **类型**: `TypeAlias`

### ***var*** `ThreeVarsFunc = ThreeSingleVarsFunc | ThreeArraysFunc`

- **类型**: `TypeAlias`

### ***var*** `MultiSingleVarsFunc = Callable[..., SingleVar]`

- **类型**: `TypeAlias`

### ***var*** `MultiArraysFunc = Callable[..., ArrayVar]`

- **类型**: `TypeAlias`

### ***var*** `MultiVarsFunc = MultiSingleVarsFunc | MultiArraysFunc`

- **类型**: `TypeAlias`

