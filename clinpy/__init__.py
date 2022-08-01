from itertools import zip_longest
from functools import reduce, partial

def _chunk_bindings(bindings):
    return list(
        zip_longest(*[iter(bindings)] * 2)
    )

def _arg_val(state, arg):
    return state[arg] if arg in state.keys() else arg

def _eval_binding(state, binding):
    key = binding[0]
    form = binding[1]
    if isinstance(form, tuple):
        symbol = form[0]
        args = map(partial(_arg_val, state), form[1:])
        state[key] = symbol(*args)
    else:
        state[key] = form
    return state

def let(bindings, *exprs):
    """Evaluates the exprs in a lexical context in which the symbols in
    the binding-forms are bound to their respective init-exprs or parts
    therein."""
    return reduce(lambda acc, binding: _eval_binding(acc, binding), _chunk_bindings(bindings), {})
