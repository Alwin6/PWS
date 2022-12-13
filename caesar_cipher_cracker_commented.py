# Creating a string with the aplhabet for getting the letter frequency of the cipher text and deciphering
alphabet = "abcdefghijklmnopqrstuvwxyz" * 2
# List of letter frequencies in the English language
eFreq = [.082, .015, .028, .043, .13, .022, .02, .061, .07, .0015, .0077, .04, .024, .067, .075, .019, .00095, .06, .063, .091, .028, .0098, .024, .0015, .02, .00074] * 2
while True:
    cipher = input("Caesar cipher encoded text: ").lower()
    cFreq = [0] * 26

    # Finding the letter frequencies of the input and storing them in a list
    for x in cipher:
        if alphabet.find(x) != -1:
            cFreq[alphabet.find(x)] += 1 / len(cipher)

    # Comparing the frequencies of the English language with the ones from the input
    # The shift that produces the closest result ( closer to 0 ) will be selected
    shift = i = 0
    low = 99
    for x in cFreq:
        i += 1
        match = n = 0
        for y in cFreq:
            match += abs(y - eFreq[n + i])
            n += 1
        if match < low:
            shift = i
            low = match

    # Decipher the input with the shift and display it
    print("\nShift was", 26 - shift)
    cracked = ""
    for x in cipher:
        if alphabet.find(x) != -1:
            cracked += alphabet[alphabet.find(x) + shift]
        else:
            cracked += x
    print(cracked)
