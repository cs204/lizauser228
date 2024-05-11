import sm

class PureFunction(sm.SM):

    def __init__(self, f):
        self.lambda_function = f
    def getNextValues(self, state, inp):
        return('', self.lambda_function(inp))


if __name__ == "__main__":
    funcL = lambda x: 2 * x
    pf = PureFunction(funcL)
    print(pf.transduce([2, 3, 4, 5]))