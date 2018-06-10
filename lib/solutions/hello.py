

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    full_name = ' '.join([x.capitalize() for x in str(friend_name).split()])
    return "Hello, {}".format(full_name)


# Testing
if __name__ == '__main__':
    print hello("Mr. x jackson")