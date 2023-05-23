class C:
    pass
class A:
    pass
class B:
    pass
class D:
    pass
class E:
    pass

class K1(C, A, B):
    pass

class K2(B, D, E):
    pass

class K3(A, D):
    pass

class Z(K1, K2, K3):
    pass

print(Z.mro())