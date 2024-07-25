def count_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency

string = input("Enter a string:")

letter_frequency = count_frequency(string)

print("Frequency of letters:")
for letter, freq in letter_frequency.items():
    print(letter,":",freq)
