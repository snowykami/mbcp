---
title: mbcp.mp_math.mp_math_typing
---
### ***var*** `RealNumber = int | float`

- **Type**: `TypeAlias`

### ***var*** `Number = RealNumber | complex`

- **Type**: `TypeAlias`

### ***var*** `Var = SingleVar | ArrayVar`

- **Type**: `TypeAlias`

### ***var*** `OneSingleVarFunc = Callable[[SingleVar], SingleVar]`

- **Type**: `TypeAlias`

### ***var*** `OneArrayFunc = Callable[[ArrayVar], ArrayVar]`

- **Type**: `TypeAlias`

### ***var*** `OneVarFunc = OneSingleVarFunc | OneArrayFunc`

- **Type**: `TypeAlias`

### ***var*** `TwoSingleVarsFunc = Callable[[SingleVar, SingleVar], SingleVar]`

- **Type**: `TypeAlias`

### ***var*** `TwoArraysFunc = Callable[[ArrayVar, ArrayVar], ArrayVar]`

- **Type**: `TypeAlias`

### ***var*** `TwoVarsFunc = TwoSingleVarsFunc | TwoArraysFunc`

- **Type**: `TypeAlias`

### ***var*** `ThreeSingleVarsFunc = Callable[[SingleVar, SingleVar, SingleVar], SingleVar]`

- **Type**: `TypeAlias`

### ***var*** `ThreeArraysFunc = Callable[[ArrayVar, ArrayVar, ArrayVar], ArrayVar]`

- **Type**: `TypeAlias`

### ***var*** `ThreeVarsFunc = ThreeSingleVarsFunc | ThreeArraysFunc`

- **Type**: `TypeAlias`

### ***var*** `MultiSingleVarsFunc = Callable[..., SingleVar]`

- **Type**: `TypeAlias`

### ***var*** `MultiArraysFunc = Callable[..., ArrayVar]`

- **Type**: `TypeAlias`

### ***var*** `MultiVarsFunc = MultiSingleVarsFunc | MultiArraysFunc`

- **Type**: `TypeAlias`

