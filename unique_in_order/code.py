def unique_in_order(phrase):
    final = []
    past = None
    for number in phrase[0:]:
        if number != past:
            final.append(number)
            past = number
    return final
