
class Calculator:
    def __init__(self):
        self.operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens):
        output = []
        op_stack = []

        for token in tokens:
            if token in self.operators:
                while op_stack and op_stack[-1] in self.operators and self.precedence[token] <= self.precedence[op_stack[-1]]:
                    output.append(op_stack.pop())
                op_stack.append(token)
            elif token.replace('.', '', 1).isdigit():
                output.append(token)
            else:
                raise ValueError('Invalid token: {}'.format(token))

        while op_stack:
            output.append(op_stack.pop())

        if not output:
            return None

        return self._evaluate_postfix(output)

    def _evaluate_postfix(self, tokens):
        stack = []
        for token in tokens:
            if token in self.operators:
                if len(stack) < 2:
                    raise ValueError('Not enough operands')
                op2 = float(stack.pop())
                op1 = float(stack.pop())
                result = self.operators[token](op1, op2)
                stack.append(result)
            else:
                stack.append(token)
        if len(stack) != 1:
            raise ValueError('Invalid expression')
        return float(stack[0])
