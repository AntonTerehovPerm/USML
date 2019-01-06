import random
import string
import os


class RandomMessageGenerator:
    def __init__(self):
        self.__init_generators()

    def random_message(self):
        key = random.choice(list(self.__generators.keys()))
        queue_name = key
        message = self.__generators[key]()
        return queue_name, message

    def __init_generators(self):
        self.__generators = {
            'queue_one': self.__queue_one_generator,
            'queue_two': self.__generate_random_string,
            'queue_three': self.__generate_words_list,
            'queue_mail': self.__generate_mail,
            'queue_sms': self.__generate_sms,
            'queue_tlgrm': self.__generate_telegram_message,
            'queue_Tgm_1': self.__generate_telegram_message
        }

    @staticmethod
    def __queue_one_generator():
        return "Generated number:" + str(random.randint(0, 100))

    @staticmethod
    def __generate_random_string():
        n = random.randint(5, 65)
        return ''.join(random.choice(
            string.ascii_uppercase
            + ' ' * 12
            + string.digits
            + string.ascii_lowercase
        ) for _ in range(n))

    @staticmethod
    def __generate_words_list():
        n = random.randint(1, 12)
        return RandomMessageGenerator.__get_random_strings_from_file("generator_3_data.txt", n)

    @staticmethod
    def __generate_sms():
        phone_number = RandomMessageGenerator.__get_random_strings_from_file("phone_numbers.txt", 1)[0]
        text = RandomMessageGenerator.__get_random_strings_from_file("one_line_texts.txt", 1)[0]
        return {'phone_number': phone_number, 'text': text}

    @staticmethod
    def __generate_mail():
        subject = random.choice(['Проблема на сайте', 'Приглашение на концерт', 'Ежедневная рассылка скидок'])
        to = RandomMessageGenerator.__get_random_strings_from_file("emails.txt", 1)[0]
        message = RandomMessageGenerator.__get_random_strings_from_file("one_line_texts.txt", 1)[0]
        return {
            'subject': subject,
            'to': to,
            'message': message
        }

    @staticmethod
    def __generate_telegram_message():
        channel = random.choice(['zdravokost', 'all_sales'])
        message = RandomMessageGenerator.__get_random_strings_from_file("one_line_texts.txt", 1)[0]
        return {
            'channel': channel,
            'message': message
        }

    @staticmethod
    def __get_full_filepath(filename):
        current_script_dir = os.path.dirname(__file__)
        return os.path.join(current_script_dir, filename)

    @staticmethod
    def __get_random_strings_from_file(filename, count):
        filepath = RandomMessageGenerator.__get_full_filepath(filename)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = list(map(lambda s: s.strip(), f.readlines()))
            result = [random.choice(lines) for _ in range(count)]
            return result
