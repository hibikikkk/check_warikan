def warikan(amount, number_of_people):
    quotient = amount / number_of_people
    remainder = amount % number_of_people

    return f"1人あたり: {quotient}円, 端数: {remainder}円"


# def check_result():
#     result = warikan(1500,3)

if __name__ == "__main__":
    check_result = warikan(1500, 3) == "1人あたり: 500円, 端数: 0円"

    print(warikan(1500, 3))
    print(check_result)
