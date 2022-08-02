from itertools import zip_longest
from functools import reduce, partial


def _chunk_bindings(bindings):
    return list(zip_longest(*[iter(bindings)] * 2))


def _arg_val(state, arg):
    return state[arg] if arg in state.keys() else arg


def _binding_key(binding):
    return binding[0]


def _binding_form(binding):
    return binding[1]


def _form_symbol(form):
    return form[0]


def _callable_args(state, form):
    return map(partial(_arg_val, state), form[1:])


def _listy_args(state, form):
    return map(partial(_arg_val, state), form)


def _is_callable_form(form):
    return type(form) is tuple and callable(form[0])


def _is_listy_form(form):
    return type(form) in [list, tuple]


def _eval_binding(state, binding):
    if _is_callable_form(_binding_form(binding)):
        return state | {
            _binding_key(binding): _form_symbol(_binding_form(binding))(
                *_callable_args(state, _binding_form(binding))
            )
        }
    elif _is_listy_form(_binding_form(binding)):
        return state | {
            _binding_key(binding): list(_listy_args(state, _binding_form(binding)))
        }
    else:
        return state | {_binding_key(binding): _binding_form(binding)}


def _named_bindings(bindings):
    return reduce(_eval_binding, _chunk_bindings(bindings), {})


def _expr_symbol(expr):
    return expr[0]


def _expr_args(state, expr):
    return map(partial(_arg_val, state["bindings"]), expr[1:])


def _eval_expr(state, expr):
    return state | {
        "exprs": state["exprs"] + [_expr_symbol(expr)(*_expr_args(state, expr))]
    }


def let(bindings, *exprs):
    """Evaluates the exprs in a lexical context in which the symbols in
    the binding-forms are bound to their respective init-exprs or parts
    therein."""
    return reduce(
        _eval_expr,
        exprs,
        {"exprs": [], "bindings": _named_bindings(bindings)},
    )["exprs"][-1]
