def let(bindings: list, *exprs):
    """Evaluates the exprs in a lexical context in which the symbols in
    the binding-forms are bound to their respective init-exprs or parts
    therein."""
    is_callable_list = lambda x: isinstance(x, list | tuple) and callable(x[0])

    for pair in zip(*([iter(bindings)] * 2)):
        print(pair)
    return 1
