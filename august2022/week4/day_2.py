class Dad:
    # Basketball=1
    special=47
    def __init__(self) -> None:
        # self.Basketball="I am  a player"
        self.special="I am a special"
        


class Son(Dad):
    kabaddi=1
    def __init__(self) -> None:
        self.kabaddi=456791
        self.special=67
        super().__init__()
        print(super().special)  

    # Basketball=3467890123468
    def players(self):
        return f"I love to play a kabaddi And My level is {self.kabaddi}"
class Grandson(Son):
    kabaddi=45
    def players(self):
        return f"I love to play a kabaddi And I am expert in playing that And my level is  {self.kabaddi} And I am pro"
class BaherwalaAdmi:
    pass


papa=Dad()
beta=Son()
chotabeta=Grandson()
# print(chotabeta.player())
# print(beta.player())
# print(chotabeta._Basketball)
# print(beta._Basketball)
# Bharwala=BaherwalaAdmi()
# print(Bharwala._)
print(beta.special)