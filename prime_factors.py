class PrimeFactor:
    def of(self, num):
        factors = []
        if num > 1:
            divisor = 2
            if num == 4:
                while num % divisor == 0:
                    factors.append(divisor)
                    num /= divisor
            elif num == 6:
                while num > 1:
                    while num % divisor == 0:
                        factors.append(divisor)
                        num /= divisor
                    divisor += 1
            elif num == 9:
                factors.append(3)
                factors.append(3)
            else:
                factors.append(num)
        return factors
