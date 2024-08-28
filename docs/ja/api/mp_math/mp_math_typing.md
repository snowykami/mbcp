---
title: mbcp.mp_math.mp_math_typing
---
### ***var*** `RealNumber = int | float`

- **タイプ**: `TypeAlias`

### ***var*** `Number = RealNumber | complex`

- **タイプ**: `TypeAlias`

### ***var*** `Var = SingleVar | ArrayVar`

- **タイプ**: `TypeAlias`

### ***var*** `OneSingleVarFunc = Callable[[SingleVar], SingleVar]`

- **タイプ**: `TypeAlias`

### ***var*** `OneArrayFunc = Callable[[ArrayVar], ArrayVar]`

- **タイプ**: `TypeAlias`

### ***var*** `OneVarFunc = OneSingleVarFunc | OneArrayFunc`

- **タイプ**: `TypeAlias`

### ***var*** `TwoSingleVarsFunc = Callable[[SingleVar, SingleVar], SingleVar]`

- **タイプ**: `TypeAlias`

### ***var*** `TwoArraysFunc = Callable[[ArrayVar, ArrayVar], ArrayVar]`

- **タイプ**: `TypeAlias`

### ***var*** `TwoVarsFunc = TwoSingleVarsFunc | TwoArraysFunc`

- **タイプ**: `TypeAlias`

### ***var*** `ThreeSingleVarsFunc = Callable[[SingleVar, SingleVar, SingleVar], SingleVar]`

- **タイプ**: `TypeAlias`

### ***var*** `ThreeArraysFunc = Callable[[ArrayVar, ArrayVar, ArrayVar], ArrayVar]`

- **タイプ**: `TypeAlias`

### ***var*** `ThreeVarsFunc = ThreeSingleVarsFunc | ThreeArraysFunc`

- **タイプ**: `TypeAlias`

### ***var*** `MultiSingleVarsFunc = Callable[..., SingleVar]`

- **タイプ**: `TypeAlias`

### ***var*** `MultiArraysFunc = Callable[..., ArrayVar]`

- **タイプ**: `TypeAlias`

### ***var*** `MultiVarsFunc = MultiSingleVarsFunc | MultiArraysFunc`

- **タイプ**: `TypeAlias`

