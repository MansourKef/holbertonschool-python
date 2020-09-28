#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    function taht returns
    true if all the boxes will be unlocked
    false if any box wont be unlocked
    """
    if boxes is None:
        raise TypeError("boxes can't be None")
    if not all(isinstance(el, list) for el in boxes):
        raise TypeError("boxes should only be a list of lists")
    if len(boxes) == 1:
        """
        By default the first box is unlocked
        if there is only one box then return true
        """
        return True
    else:
        """
        Add the 0 indexed Box by default to be unlocked
        """
        UnlockedBoxes = []
        if 0 not in UnlockedBoxes:
            UnlockedBoxes.append(0)
        """
        get the count of the unlocked boxes
        """
        UnlockedBoxesCount = len(UnlockedBoxes)
        """
        Iterate in the inlocked boxes
        """
        for i in UnlockedBoxes:
            if i in range(len(boxes)):
                for j in range(len(boxes[i])):
                    """
                    add only the new unlocked boxes in the list
                    """
                    if boxes[i][j] not in UnlockedBoxes \
                            and boxes[i][j] < len(boxes):
                        UnlockedBoxes.append(boxes[i][j])
        """
        return the result
        """
        return len(UnlockedBoxes) == len(boxes)
