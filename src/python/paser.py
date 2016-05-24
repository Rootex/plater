# A python paser that processe each input and determines its type
# Plaix Inc, Rootex Co.
# by Sotaya Yakubu

INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


class Token(object):
    def __init__(self, type, value):
        """
        token types INTEGER, PLUS, EOF initialization.
        :param type:
        :param value:
        :return:
        """
        self.type = type
        self.value = value

    def __str__(self):
        """
        String formatting and representation of the class instance
        Example:
        Token(INTEGER, 5)
        :return:
        """
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()