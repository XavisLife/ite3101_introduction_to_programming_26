def check_bit4(input: int) -> str:
    mask = 0b1000
    if input & mask > 0:
        print