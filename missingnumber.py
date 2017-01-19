def find_missing(firstList, secondList):
    """
    This function compares two lists and returns the extra number in the longer list
    """
    extraList = []
    lesserList = []
    if len(firstList) > len(secondList):
        extraList = firstList
        lesserList = secondList
    else:
        extraList = secondList
        lesserList = firstList
    extraNumber = [x for x in extraList if x not in lesserList]
    if len(extraNumber) == 0:
      return 0
    return extraNumber.pop()