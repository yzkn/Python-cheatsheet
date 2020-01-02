### isinstance

| 関数                                | 結果    |
| ----------------------------------- | ------- |
| `isinstance(True, bool)`            | `True`  |
| ----------------------------------- | ------- |
| `isinstance(1, int)`                | `True`  |
| `isinstance(1.23, int)`             | `False` |
| `isinstance(1, float)`              | `False` |
| `isinstance(1.23, float)`           | `True`  |
| `isinstance(int('1'), int)`         | `True`  |
| `isinstance(float('1'), float)`     | `True`  |
| `isinstance(0b11, int)` 2 進数      | `True`  |
| `isinstance(0o11, int)` 8 進数      | `True`  |
| `isinstance(0x11, int)` 16 進数     | `True`  |
| ----------------------------------- | ------- |
| `isinstance('str', str)`            | `True`  |
| ----------------------------------- | ------- |
| `isinstance({0:0, 1:1, 2:2}, dict)` | `True`  |
| ----------------------------------- | ------- |
| `isinstance([0, 1, 2], list)`       | `True`  |
| ----------------------------------- | ------- |
| `isinstance({0, 1, 2}, set)`        | `True`  |
| ----------------------------------- | ------- |
| `isinstance((0, 1, 2), tuple)`      | `True`  |
