#!/usr/bin/env python3

import calculator

class TestCalculator:
    def test_infix_operator_precedence(self):
        v1 = calculator.evaluate_infix("1+2*3")
        v2 = calculator.evaluate_infix("2*3+1")
        assert(v1 == 7)
        assert(v1 == v2)

    def test_evaluate_rpn(self):
        e = [1, 2, 3, "*", "+"]
        assert(calculator.evaluate_rpn(e) == 7)
