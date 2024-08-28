---
title: mbcp.mp_math.mp_math_typing
---
### ***var*** `RealNumber: TypeAlias = int | float`

### ***var*** `Number: TypeAlias = RealNumber | complex`

### ***var*** `SingleVar = TypeVar('SingleVar', bound=Number)`

### ***var*** `ArrayVar = TypeVar('ArrayVar', bound=Iterable[Number])`

### ***var*** `Var: TypeAlias = SingleVar | ArrayVar`

### ***var*** `OneSingleVarFunc: TypeAlias = Callable[[SingleVar], SingleVar]`

### ***var*** `OneArrayFunc: TypeAlias = Callable[[ArrayVar], ArrayVar]`

### ***var*** `OneVarFunc: TypeAlias = OneSingleVarFunc | OneArrayFunc`

### ***var*** `TwoSingleVarsFunc: TypeAlias = Callable[[SingleVar, SingleVar], SingleVar]`

### ***var*** `TwoArraysFunc: TypeAlias = Callable[[ArrayVar, ArrayVar], ArrayVar]`

### ***var*** `TwoVarsFunc: TypeAlias = TwoSingleVarsFunc | TwoArraysFunc`

### ***var*** `ThreeSingleVarsFunc: TypeAlias = Callable[[SingleVar, SingleVar, SingleVar], SingleVar]`

### ***var*** `ThreeArraysFunc: TypeAlias = Callable[[ArrayVar, ArrayVar, ArrayVar], ArrayVar]`

### ***var*** `ThreeVarsFunc: TypeAlias = ThreeSingleVarsFunc | ThreeArraysFunc`

### ***var*** `MultiSingleVarsFunc: TypeAlias = Callable[..., SingleVar]`

### ***var*** `MultiArraysFunc: TypeAlias = Callable[..., ArrayVar]`

### ***var*** `MultiVarsFunc: TypeAlias = MultiSingleVarsFunc | MultiArraysFunc`

