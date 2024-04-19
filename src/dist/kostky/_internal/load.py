def rules(dices):
    """

     Gets a list and computes the score if possible, else returns none.

    :param dices: list of the values of the dices.
    :type dices: list
    :return: if the list is a valid combination it returns the value of the combination, else returns False.
    :rtype: int
    :example: rules(6,6,6), return 600
    """

    NumberOfDices = len(dices)
    dices.sort()
    if NumberOfDices == 1:
        # jednička
        if dices[0] == 1:
            return 100
        # pětka
        elif dices[0] == 5:
            return 50
    elif NumberOfDices == 2:
        if dices[0] == dices[1]:
            if dices[0] == 1:
                return 200
            elif dices[0] == 5:
                return 100
        elif dices[0] == 1 and dices[1] == 5:
            return 150
    elif NumberOfDices == 3:
        # trojice
        if dices[0] == dices[1] == dices[2]:
            if dices[0] == 1:
                return 1000
            else:
                return dices[0] * 100
        elif dices[0] == dices[1] == 1 and dices[2] == 5:
            return 250
        elif dices[2] == dices[1] == 5 and dices[0] == 1:
            return 200
    elif NumberOfDices == 4:
        # čtveřice
        if dices[0] == dices[1] == dices[2] == dices[3]:
            if dices[0] == 1:
                return 2000
            else:
                return dices[1] * 200
        # trojice + 5
        elif dices[0] == dices[1] == dices[2]:
            # trojice 1 + 5
            if dices[0] == 1 and dices[3] == 5:
                return 1050
            # trojice + 5
            elif dices[3] == 5:
                return dices[0] * 100 + 50
        # trojice + 1/5
        elif dices[1] == dices[2] == dices[3]:
            # trojice 1 + 5
            if dices[1] == 1 and dices[0] == 5:
                return 1050
            # trojice + 1
            elif dices[0] == 1:
                return dices[1] * 100 + 100
            # trojice + 5
            elif dices[0] == 5:
                return dices[1] * 100 + 50
        # dvojce 1 a 5
        elif dices[0] == dices[1] == 1 and dices[2] == dices[3] == 5:
            return 300
    elif NumberOfDices == 5:
        # pětice
        if dices[0] == dices[1] == dices[2] == dices[3] == dices[4]:
            # pětice 1
            if dices[0] == 1:
                return 4000
            # pětice
            else:
                return dices[0] * 400
        # čtveřice + 5
        elif dices[0] == dices[1] == dices[2] == dices[3] and dices[4] == 5:
            # čtveřice 1 + 5
            if dices[0] == 1:
                return 2050
            else:
                # čtveřice + 5
                return dices[0] * 200 + 50
        # čtveřice + 1
        elif dices[4] == dices[1] == dices[2] == dices[3] and dices[0] == 1:
            return dices[4] * 200 + 100
            # čtveřice + 5
        elif dices[4] == dices[1] == dices[2] == dices[3] and dices[0] == 5:
            return dices[4] * 200 + 50
        # trojice + dvojice 5
        elif dices[0] == dices[1] == dices[2] and dices[3] == dices[4]:
            # trojice 1 + dvojice 5
            if dices[0] == 1:
                return 1100
            # trojice + dvojice 5
            elif dices[3] == 5:
                return dices[0] * 100 + 100
        # trojice + dvojice 1/5
        elif dices[2] == dices[3] == dices[4] and dices[0] == dices[1]:
            # trojice + dvojice 1
            if dices[0] == 1:
                return dices[2] * 100 + 200
            # trojice + dvojice 5
            elif dices[0] == 5:
                return dices[0] * 100 + 100
        # trojice + 1 + 5
        elif (
            dices[3] == dices[4] == dices[2]
            and dices[0] == 1
            and dices[1] == 5
            or dices[3] == dices[1] == dices[2]
            and dices[0] == 1
            and dices[4] == 5
        ):
            return dices[3] * 100 + 150
    elif NumberOfDices == 6:
        # šestice
        if (
            dices[0]
            == dices[1]
            == dices[2]
            == dices[3]
            == dices[4]
            == dices[5]
        ):
            if dices[0] == 1:
                return 8000
            else:
                return dices[1] * 800
        # dvojice
        elif (
            dices[0] == dices[1]
            and dices[2] == dices[3]
            and dices[4] == dices[5]
            and dices[0] != dices[2]
            and dices[2] != dices[4]
        ):
            return 1000
        # postupka
        elif (
            dices[0]
            == dices[1] - 1
            == dices[2] - 2
            == dices[3] - 3
            == dices[4] - 4
            == dices[5] - 5
        ):
            return 1500
        # dvě trojice
        elif (
            dices[0] == dices[1] == dices[2]
            and dices[3] == dices[4] == dices[5]
        ):
            # trojice 1 a trojice
            if dices[0] == 1:
                return 1000 + (dices[3] * 100)
            # dvě trojce
            else:
                return dices[0] * 100 + dices[3] * 100
        # pětice + 5
        elif (
            dices[0] == dices[1] == dices[2] == dices[3] == dices[4]
            and dices[5] == 5
            or dices[5] == dices[1] == dices[2] == dices[3] == dices[4]
            and dices[0] == 5
        ):
            # pětice 1 + 5
            if dices[0] == 1:
                return 4050
            # pětice + 5
            else:
                return dices[1] * 400 + 50
        # pětice + 1
        elif (
            dices[5] == dices[1] == dices[2] == dices[3] == dices[4]
            and dices[0] == 1
        ):
            return dices[1] * 400 + 50
        # čtveřice + dvojice 5
        elif (
            dices[0] == dices[1] == dices[2] == dices[3]
            and dices[4] == dices[5]
        ):
            if dices[0] == 1:
                return 2100
        # čtveřice + dvojice 1/5
        elif (
            dices[4] == dices[5] == dices[2] == dices[3]
            and dices[0] == dices[1]
        ):
            # čtveřice + dvojice 1
            if dices[0] == 1:
                return dices[2] * 200 + 200
            # čtveřice + dvojice 5
            elif dices[0] == 5:
                return dices[2] * 200 + 100
        # čtveřice + 1 + 5
        elif (
            dices[4] == dices[5] == dices[2] == dices[3]
            and dices[0] == 1
            and dices[1] == 5
            or dices[4] == dices[1] == dices[2] == dices[3]
            and dices[0] == 1
            and dices[5] == 5
        ):
            return dices[2] * 200 + 150
        # trojce + dvojice 1 + 5
        elif (
            dices[0] == dices[1] == 1
            and dices[2] == 5
            and dices[3] == dices[4] == dices[5]
            or dices[0] == dices[1] == 1
            and dices[5] == 5
            and dices[3] == dices[4] == dices[2]
        ):
            return dices[3] * 100 + 250
        # trojce + dvojice 5 + 1
        elif (
            dices[0] == 1
            and dices[1] == dices[2] == 5
            and dices[3] == dices[4] == dices[5]
            or dices[0] == 1
            and dices[1] == dices[2] == dices[3]
            and dices[4] == dices[5] == 5
        ):
            return dices[3] * 100 + 200
