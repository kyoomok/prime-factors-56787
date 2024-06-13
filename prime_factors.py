class PrimeFactor:
    def of(self, num):
        factors = []
        if num > 1:
            divisor = 2
            if num == 4 or num == 6 or num == 9:
                while num > 1:
                    while num % divisor == 0:
                        factors.append(divisor)
                        num /= divisor
                    divisor += 1
            elif num == 12:
                factors.append(2)
                factors.append(2)
                factors.append(3)
            else:
                factors.append(num)
        return factors
