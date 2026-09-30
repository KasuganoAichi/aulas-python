def tem_numero(senha):
    return True if any(c.isdigit() for c in senha) else False