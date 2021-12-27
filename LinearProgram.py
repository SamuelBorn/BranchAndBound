class LinearProgram:

    # Functions are stored as
    # min cTx
    # with respect to mx<=b where a = (m|b)
    def __init__(self, a, c, was_maximize):
        self.a = a
        self.c = c
        self.was_maximize = was_maximize  # max cTx is stored as -min -cTx. This stores the - at the front

    def convert_to_traditional_layout(self):
        pass
