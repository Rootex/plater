# A python interpreter
# Plaix Inc, Rootex Co.
# by Sotaya Yakubu

from src.python.paser import *


class Interpreter(object):
    def __init__(self, statement):
        """
        Input as a string e.g "4+3"
        :param statement:
        :return:
        """

        self.statement = statement
        self.position = 0
        self.current_token = None

    def error(self):
        raise Exception("Error parsing the input")

    def scanner(self):
        """
        Lexical analyzer, it decomposes the input into tokens
        one at a time.
        :return:
        """

        # if position is greeter than the length
        # of the statement, return EOF
        # Everything have been converted
        statement = self.statement
        if self.position > len(statement) - 1:
            return Token(EOF, None)

        current_unit = statement[self.position]

        # if the current unit is a digit, convert
        # and return its token object
        if current_unit.isdigit():
            token = Token(INTEGER, int(current_unit))
            self.position += 1
            return token

        # if the current unit is a +, convert
        # and return its token object
        if current_unit == '+':
            token = Token(PLUS, current_unit)
            self.position += 1
            return token

        # if the current unit is '-', convert
        # and return its token object
        if current_unit == '-':
            token = Token(MINUS, current_unit)
            self.position += 1
            return token

        self.error()

    def consume(self, token_type):
        """
        If previous and current token are of same type
        consume the current token and send point to next value.
        :return:
        """

        if self.current_token.type == token_type:
            self.current_token = self.scanner()
        else:
            self.error()

    def expression(self):
        """
        Our expression should have the form > INTEGER PLUS INTEGER
        :return:
        """

        self.current_token = self.scanner()

        # first the integer
        left = self.current_token
        self.consume(INTEGER)

        # then the operator plus
        op = None
        if self.current_token.value == '+':
            op = self.current_token
            self.consume(PLUS)

        if self.current_token.value == '-':
            op = self.current_token
            self.consume(MINUS)

        # then the last integer
        right = self.current_token

        self.consume(INTEGER)
        result = 0
        if op.value == '+':
            result = left.value + right.value
        elif op.value == '-':
            result = left.value - right.value
        return result


def main():
    while True:
        try:
            statement = input('pl> ')
            statement = statement.replace(" ", "")
            if statement == "exit":
                break
        except EOFError:
            break
        if not statement:
            continue
        interpreter = Interpreter(statement)
        result = interpreter.expression()
        print(result)

if __name__ == '__main__':
    main()


