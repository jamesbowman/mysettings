# debugtools

def hexdump(s):
    def toprint(c):
        if 32 <= ord(c) < 127:
            return c
        else:
            return "."
    def hexline(s):
        return (" ".join(["%02x" % ord(c) for c in s]).ljust(49) +
                "|" +
                "".join([toprint(c) for c in s]).ljust(16) +
                "|")
    return "\n".join([hexline(s[i:i+16]) for i in range(0, len(s), 16)])

def diff(actual, expect):
    assert len(actual) == len(expect), "Actual and expect must have same length"
    for i in range(len(actual)):
        if actual[i] != expect[i]:
            print "mismatch at %#x/%#x %#x/%#x" % (i, len(expect), ord(actual[i]), ord(expect[i]))
            print "expect @ %x: %s" % (i, hexdump(expect[i:i+16]))
            print "actual @ %x: %s" % (i, hexdump(actual[i:i+16]))
            assert 0

def bitunpack(sl, v):
    """ Unpack a bitfield from lsb up, using field sizes sl, cf struct.unpack() """
    assert sum(sl) <= 32
    r = []
    sl = list(sl)
    while sl:
        b = sl.pop()
        r.append(v & (2**b-1))
        v >>= b
    return tuple(r[::-1])

