class A:
    pass
class D(A):
    pass
class B(A):
    pass
class C(B):
    pass

class E(D, A, C):
    pass


class F(D):
    pass

class G(E, C):
    pass

class H(E, B):
    pass

class O(F, G, H):
    pass

print(O.mro())