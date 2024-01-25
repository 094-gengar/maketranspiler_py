# maketranspiler_py

- WSL2 Ubuntu 22.04 + Python 3.10.12 + openai 1.8.0 で動作確認済み
- 手元で使うときは、`secret_information.py`というファイルを`maketranspiler.py`と同じディレクトリに作成し、API-keyを`SECRET_API_KEY`という変数名で定義してください

### Usage / Example

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
