# ls = sorted([3, 5, 1, 2])
# print(ls)

# ls = sorted([9,3,5,1], reverse=True)
# print(ls)

# lst = [2, 7, 4, 6, 1]
# lst = ['h', 'sks', 'askdjfhajksdhf']
# sorted_lst = sorted(lst, key=len, reverse=True)
# print(sorted_lst)

# def lowercase(string):
#     return string.lower()

# animals = ["Cat", "dog", "ZEBRA", "monkey"]
# s_a = sorted(animals, key=lowercase)
# print(s_a)

# people = [("Jack", 30), ("John", 25), ("Betty", 25), ("Anna", 30)]

# def sort_people(person):
#     name, age = person
#     return (age, name)

# s_p = sorted(people, key=sort_people)
# print(s_p)

# lst = [10, 9, -6, 11, 7, -16, 50, 8]
# print(sorted(lst, key=str))
# print(sorted(lst, reverse=True, key=str))
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def year_sort(entry):
    return int(entry['published'])

books.sort(key=year_sort)
print(books)