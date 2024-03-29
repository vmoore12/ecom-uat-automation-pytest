"""
Module for random utilities. Helpful functions go here.
Example:
    generating random email

"""
import random
import string
import logging as logger



def generate_random_email_and_password(domain='supersqa.com', email_prefix='testuser', elegnth= 15):
    """
    Generates a random email and password combination.
    :param domain:
    :param email_prefix:
    :return: dictionary. A dictionary with keys 'email' & 'password'
    """

    random_string = ''.join(random.choices(string.ascii_lowercase, k=int(elegnth)))
    # email = email_prefix + '_' + random_string + '@' + domain
    email = f'{email_prefix}_{random_string}@{domain}'

    password_length = 20
    password_string = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email': email, 'password': password_string}
    logger.debug(f"Randomly generated email and password: {random_info}")

    return random_info


def generate_random_string():
     random_string = ''.join(random.choices(string.ascii_lowercase, k=int(10)))

     return random_string

def generate_random_float():
    random_float = round(random.uniform(10.00, 24.99), 2)
    rand_num = str(random_float)
    return rand_num


if __name__ == '__main__':
    print(generate_random_email_and_password())