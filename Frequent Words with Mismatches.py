
def LastSymbol(Pattern):
    return Pattern[:-1]


def PatternToNumber(Pattern)
        if symbol not in Pattern:
            return 0
        symbol = LastSymbol(Pattern)
        Prefix = Prefix(Pattern)
        return 4 * PatternToNumber(Prefix) + SymbolToNumber(symbol)