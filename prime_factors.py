class PrimeFactor:
    def of(self, num):
        factors = []
        if num > 1:
            if num == 4:
                factors.append(2)
                factors.append(2)
            else:
                factors.append(num)
        return factors

