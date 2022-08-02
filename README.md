# ClInPy
## Clojure Inspired Python

### `let`
Inspired by :: https://clojuredocs.org/clojure.core/let

`let` provides a way to create lexical bindings of data structures to named strings. The binding, and therefore the ability to resolve the binding, is available only within the lexical context of the `let`.

`let` uses pairs in a tuple for each binding you'd like to make and the returned value of the `let` is the value of the last expression to be evaluated.

```python
from operator import add
from clinpy import let

let(
    (
        "let:aa", add(1, 1),                # 2
        "let:aaa", [1, "let:aa", 3],        # [1, 2, 3]
        "let:a", (sum, "let:aaa"),          # 6
        "let:b", (pow, "let:a", 2),         # 36
        "let:c", (add, "let:a", "let:b"),   # 42
    ),
    (print, "let:c"),                       # None
    (add, "let:c", 10),                     # 52
) # 52
```
