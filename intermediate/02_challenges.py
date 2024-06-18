# Challenges

# FIIZ - BUZZ

def fizz_buzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("Fizzbuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print(index)


fizz_buzz()

print("\n ---------------- \n")

# Es un anagrama?


def is_anagram(word_one: str, word_two: str):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("Amor", "Roma"))


print("\n ---------------- \n")

# Fibonacci


def fibonacci():
    prev = 0
    next = 1
    for index in range(0, 50):
        print(prev)
        fibo = prev + next
        prev = next
        next = fibo


fibonacci()

print("\n ---------------- \n")

#  Numero primo


def is_prime():
    for number in range(1, 101):

        if number >= 2:
            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)


is_prime()

print("\n ---------------- \n")


def reverse(text: str):
    text_len = len(text)
    reversed_text: str = ""
    for letter in range(0, len(text)):
        reversed_text += text[text_len - letter - 1]
    return reversed_text


print(reverse("Hola mundo"))
