x = input("Type phrase or word you would like to be translated to pig latin:")
x = x.strip()
x = x.lower()
y = x.split()
z = []
n = len(y)

for i in range(0, n):
    s = y.pop(0)
    def first_vowel(s):
        for index, char in enumerate(s):
            if char in 'aeiouy':
                return index
        raise ValueError('No vowel found')
    def convert(s):
        index = first_vowel(s)
        return s[index:] + s[:index] + 'ay'
    z.append(convert(s))

a = ' '.join(z)

print(a)