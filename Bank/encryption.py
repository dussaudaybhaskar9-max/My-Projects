from hashlib import shake_128
def encrypt(s):
    a = shake_128(str(s).encode()).hexdigest(length=64)
    return a