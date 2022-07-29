from math import factorial
import clinpy

def add(x, y): return x + y

def test_let():
    assert \
        clinpy.let(
            ("let:a", sum([1,2,3]),
            "let:b", (pow, "let:a", 2),
            "let:c", (add, "let:a", "let:b")),
            (factorial, "let:c")
        ) == 1
