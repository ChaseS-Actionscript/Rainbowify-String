import random, math
def randomRainbowify(word: str) -> str:
    """
    Colors every character of a string by randomly selecting an ansi color code.

    Parameters
    ----------
    word : str
        String to turn to a random assortment of colors.

    Returns
    -------
    str
        The result of randomly coloring the characters of the string.
    """
    colors = {

        "Pink":"\u001b[38;5;206m",
        "Orange":"\u001b[38;5;214m",
        "Red":"\u001b[38;5;196m",
        "Yellow":"\u001b[38;5;226m",
        "Green":"\u001b[38;5;28m",
        "Blue":"\u001b[38;5;21m",
        "Purple":"\u001b[38;5;99m",
        "Cyan":"\u001b[38;5;45m",
        }
    data = [random.choice(list(colors.values())) + i +"\033[;0;0m" for i in word]
    return "".join(data)
def rainbowify(word: str) -> str:
    """
    Splits a string into the 8 parts of a rainbow and then colors each individual part in the order a rainbow is in by using ansi color codes.

    Parameters
    ----------
    word : str
        String to turn to a rainbow assortment of colors.

    Returns
    -------
    str
        The result of coloring the characters of the string.
    """
    rainbow_colors = {
    "Red": "\u001b[38;5;196m",
    "Orange": "\u001b[38;5;202m",
    "Yellow": "\u001b[33m",
    "Yellow Green": "\u001b[38;5;118m",
    "Green": "\u001b[32m",
    "Cyan": "\u001b[96m",
    "Blue": "\u001b[34m",
    "Violet": "\u001b[35m",
    "Pink":"\u001b[38;5;201m",
    "Pink Red":"\u001b[38;5;198m",
    "Pink Red Again": "\u001b[38;5;197m"
    }
    numColors = len(list(rainbow_colors.values()))
    if numColors >= len(word): #This ensures if the number of colors is greater than the length, the chunks comprehension doesn't go out of bounds
        numColors = len(word)
    data = list(word)
    chunks = [data[x:x+int(len(data)/numColors)] for x in range(0, len(data), int(math.ceil(len(data))/numColors))]
    #Separates the word by chunks of x(the current iterator) to x + length of the word / number of colors
    #The step is the same as the sum of the slice end index (length of data / number of colors)
    coloredChunks = [list(rainbow_colors.values())[int((position))] + "".join(x) + "\033[;0;0m" if position < numColors else list(rainbow_colors.values())[int((position-(numColors)))] + "".join(x) + "\033[;0;0m" for position, x in enumerate(chunks)]
    #The if else in this comprehension is there so if the 
    return "".join(coloredChunks)
