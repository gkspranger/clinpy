from math import factorial
from clinpy import let
from operator import add


def test_let():
    assert (
        let(
            (
                "let:aa", 2,                        # 2
                "let:aaa", [1, "let:aa", 3],        # [1, 2, 3]
                "let:a", (sum, "let:aaa"),          # 6
                "let:b", (pow, "let:a", 2),         # 36
                "let:c", (add, "let:a", "let:b"),   # 42
            ),
            (print, "let:c"),
            (add, "let:c", 10),                     # 52
        )
        == 52
    )
