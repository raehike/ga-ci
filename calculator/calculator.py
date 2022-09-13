#!/usr/bin/env python3
# adapted from
# https://github.com/noah1400/rpn-calculator/blob/main/python/rpn-calculator.py

def evaluate_infix(s: str):
    """
    Parse a string as an infix numeric expression and evaluate.
    """
    return evaluate_rpn(infix_to_rpn(s))

def infix_to_rpn(s: str):
    """
    Translate an expression in infix notation to reverse Polish notation (RPN).
    """
    precedence = {
        '(': 0,
        '-': 1,
        '+': 1,
        '*': 2,
        '/': 2,
        '%': 2,
    }

    i = 0
    fin = []
    ops = []

    while i < len(s):
        tok = s[i]
        if is_digit(tok):
            n, i = read_int(s, i)
            fin.append(n)
            continue
        if is_operator(tok):
            top = ops[-1] if ops else None
            if top is not None and precedence[top] >= precedence[tok]:
                fin.append(ops.pop())
            ops.append(tok)
            i += 1
            continue
        if tok == '(':
            ops.append(tok)
            i += 1
            continue
        if tok == ')':
            while True:
                operator = ops.pop()
                if operator == '(':
                    break
                fin.append(operator)
                if not ops:
                    break
            i += 1
            continue
        i += 1

    while ops:
        fin.append(ops.pop())

    return fin

##############

def is_operator(tok: str):
    return tok in ['+', '-', '*', '/', '%']

def is_digit(tok: str):
    return tok >= '0' and tok <= '9'

def evaluate_rpn(rpn: list):
    """
    Evaluate an expression in reverse Polish notation.
    """
    stack = []
    for tok in rpn:
        if is_operator(tok):
            r = stack.pop()
            l = stack.pop()
            if   tok == '+':
                stack.append(l + r)
            elif tok == '-':
                stack.append(l - r)
            elif tok == '*':
                stack.append(l * r)
            elif tok == '/':
                stack.append(l / r)
            elif tok == '%':
                stack.append(l % r)
        else:
            stack.append(tok)
    return stack[0]

##############

def read_int(s: str, i: int):
    i_end = i+1
    while i_end < len(s) and is_digit(s[i_end]):
        i_end += 1
    return int(s[i:i_end]), i_end
