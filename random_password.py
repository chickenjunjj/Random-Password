import random
class RandomPassword:
    def __init__(self):
        self.start()

    def start(self):
        min_password_length = input("Minimum password length: ")
        max_password_length = input("Maximum password length: ")
        if int(min_password_length) >= int(max_password_length):
            print("")
            print("Invalid input \n")
            self.start()
        else:
            password_number = input("Minimum amount of numbers in password: ")
            if int(password_number) >= int(max_password_length):
                print("")
                print("Invalid input \n")
                self.start()
            elif int(password_number) < int(max_password_length):
                password_special_chars = input("Minimum amount of special characters: ")
                if int(password_special_chars) >= int(max_password_length):
                    print("")
                    print("Invalid input \n")
                    self.start()
                elif int(password_number) + int(password_special_chars) >= int(max_password_length):
                    print("")
                    print("Invalid input \n")
                    self.start()
                else:
                    self.make_password(min_password_length, max_password_length, password_number, password_special_chars)
            else:
                self.make_password(min_password_length, max_password_length, password_number, password_special_chars)
        


                

    def make_password(self, min_password_length, max_password_length, password_number, password_special_chars):
        password_letter_length = 0
        password_number_length = 0
        password_special_char_length = 0
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "u", "x", "y", "z"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        special_chars = ["!", "@", "$", "%", "^", "&", "*", "_", "-", "+", "=", "<", ">", "?", "#"]
        password = []
        amount_letters = random.randrange(int(min_password_length) - (int(password_number) + int(password_special_chars)), int(max_password_length) - (int(password_number) + int(password_special_chars)))
        self.password_loop(password_letter_length, password_number_length, password_special_char_length, amount_letters, letters, numbers, special_chars, password, password_number, password_special_chars)
        passw = password
        random.shuffle(passw)
        passwo = "".join(passw)
        print(passwo)

    def password_loop(self, password_letter_length, password_number_length, password_special_char_length, amount_letters, letters, numbers, special_chars, password, password_number, password_special_chars):
        while int(password_letter_length) <= int(amount_letters):
            random_letter = random.randrange(0, 26)
            letter = letters[random_letter]
            password.append(letter)
            password_letter_length += 1

        while int(password_number_length) < int(password_number):
            random_number = random.randrange(0, 10)
            number = numbers[random_number]
            password.append(number)
            password_number_length += 1
            
        while int(password_special_char_length) < int(password_special_chars):
            random_special_char = random.randrange(0, 15)
            special_char = special_chars[random_special_char]
            password.append(special_char)
            password_special_char_length += 1

random_password = RandomPassword()
