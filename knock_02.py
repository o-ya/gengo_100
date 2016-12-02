"""
    「パトカー」＋「タクシー」＝「パタトクカシーー」
"""

if __name__ == "__main__":
    PATO = "パトカー"
    TAKU = "タクシー"
    msg = ""
    for (a, b) in zip(PATO, TAKU):
        msg += a+b
    print(msg)
