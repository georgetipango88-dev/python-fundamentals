def calculate_numbers():
    not_divisible = []
    divisible_by_3 = []
    divisible_by_7 = []
    divisible_by_11 = []

    for number in range(1, 151):
      
      if number % 3 == 0:
            divisible_by_3.append(number)

      if number % 7 == 0:
            divisible_by_7.append(number)

      if number % 11 == 0:
            divisible_by_11.append(number)

      if number % 3 != 0 and number % 7 != 0 and number % 11 != 0:
            not_divisible.append(number)

    my_finding = {
        "divisible_by_3": divisible_by_3,
        "divisible_by_7": divisible_by_7,
        "divisible_by_11": divisible_by_11,
        "not_divisible_by_3_7_11": not_divisible
    }

    print(not_divisible)
    print(my_finding)


calculate_numbers()

