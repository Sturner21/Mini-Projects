list_of_gifts = ["twelve Drummers Drumming,", " eleven Ppipers Piping,", " ten Lords-a-leaping,", " nine Ladies dancing,", " eight Maids-a-milking,", " seven Swans a swiming,", " six Geese-a-laying,", " five Gold Rings,", " four Calling Birds,", " three French Hens,", " two Turtle Doves,", " a Partridge in a Pear Tree."]

days = {11:"twelth", 10:"eleventh", 9:"tenth", 8:"ninth", 7:"eighth", 6:"seventh", 5:"sixth", 4:"fifth", 3:"fourth", 2:"thrid", 1:"second", 0:"first"}

a = input("What day of Christmas is it?:")
a = int(a)
for i in range(0, a):
    if a == 1:
        song = "On the {} day of Christmas my true love gave to me:".format(days[i]) + ''.join(list_of_gifts[abs(a-12):12])
    else:
        song = "On the {} day of Christmas my true love gave to me:".format(days[i]) + ''.join(list_of_gifts[abs(a-12):11]) + " and" + ''.join(list_of_gifts[11])

print(song)