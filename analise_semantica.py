import sys

def analise_semantica(node, variables):
    #print(node.type)
    if node.leaf is not None:
        ret_type = node.type
        if node.type == 'IDENTIFIER':
            ret_type = variables.get(node.leaf)
            if ret_type == '' or ret_type is None:
                sys.exit("ERRO variavel usada nao inicializada: " + node.leaf)
        return ret_type

    if node.type == '=':
        var_name = node.children[0].leaf
        L_type = variables.get(var_name)
        R_type = analise_semantica(node.children[1], variables)
        if L_type == '':
            variables[var_name] = R_type

    elif node.type == '+':
        L_type = analise_semantica(node.children[0], variables)
        R_type = analise_semantica(node.children[1], variables)
        if L_type != R_type:
            erro_binop("SOMA", L_type, R_type)
            return None        
        return L_type
    
    elif node.type == '-':
        L_type = analise_semantica(node.children[0], variables)
        R_type = analise_semantica(node.children[1], variables)
        if L_type != R_type:
            erro_binop("SUBTRACAO", L_type, R_type)
            return None        
        return L_type

    elif node.type == '*':
        L_type = analise_semantica(node.children[0], variables)
        R_type = analise_semantica(node.children[1], variables)
        if L_type != R_type:
            erro_binop("MULTIPLICACAO", L_type, R_type)
            return None        
        return L_type

    elif node.type == '/':
        L_type = analise_semantica(node.children[0], variables)
        R_type = analise_semantica(node.children[1], variables)
        if L_type != R_type:
            erro_binop("DIVISAO", L_type, R_type)
            return None        
        return L_type
    
    elif node.type == 'while':
        analise_semantica(node.children[0], variables) 
        analise_semantica(node.children[1], variables) 

    elif node.type == 'programa':
        for child in node.children:
            analise_semantica(child, variables)


def erro_binop(op, type1, type2):
    sys.exit("ERRO na operacao: " + op + "  tipo operandos: " + type1 + " e " + type2)