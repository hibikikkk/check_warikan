from app import warikan


def check_warikan(amount, members, answer):
    result = warikan(amount, members) == answer

    if result:
        return "動作は順調~~"

    else:
        return "間違った動きしてるよ"


if __name__ == "__main__":

    input_warikan_check = [
        [1500, 3, "1人あたり: 500円, 端数: 0円"],
        [2000, 5, "1人あたり: 400円, 端数: 0円"],
        [1200, 12, "1人あたり: 100円, 端数: 0円"]
    ]

    for input in input_warikan_check:
        print(warikan(input[0], input[1]))
        print(check_warikan(input[0], input[1], input[2]))
