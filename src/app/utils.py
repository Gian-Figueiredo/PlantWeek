def type_check(*variables, expected_type):
    for var in variables:
        if not isinstance(var, expected_type):
            raise TypeError(f"Tipo esperado: {expected_type}, tipo recebido: {type(var)}")