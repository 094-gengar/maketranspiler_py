# maketranspiler_py

## Usage

- 手元で使うときは、`secret_information.py`にAPI-keyを`SECRET_API_KEY`という変数名で定義してください

```py
>>> import maketranspiler as mt
>>> transpiler = mt.transpiler_class("Python")
>>> transpiler.transpile_code("「Hello, world!」と表示する")
"print('Hello, world!')"
>>>
```

```py
>>> import maketranspiler as mt
>>> transpiler = mt.transpiler_class("C")
>>> transpiler.add_example("「Hello, world!」と表示する", \
... """#include <stdio.h>
... int main() { printf("Hello, world!"); }""")
>>> transpiler.transpile_code("「Hola!」と表示する")
'#include <stdio.h>\nint main() { printf("Hola!"); }'
>>>
```
