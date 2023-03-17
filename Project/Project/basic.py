
#######################################
# CONSTANTS
# --------------------------------------


DIGITS = '0123456789'

#######################################
# Errors class
# --------------------------------------


class Error:
    def __init__(self, name, details):
        self.error_name = name
        self.details = details

    def as_string(self):
        return f'{self.error_name} : {self.details}'


class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal charactar', details)


class InvalidSyntaxError(Error):
    def __init__(self, details):
        super().__init__('InvalidSyntax', details)


#######################################
# TOKENS
# --------------------------------------
'''
Numbers have a type and value
'''
tokens_map = {'+': 'PLUS',
              '-': 'MINUS',
              '*': 'MULTIPLICATION',
              '/': 'DIVITION',
              '(': 'LEFT_PAREN',
              ')': 'RIGHT_PAREN',
              'TT_INT': 'INT',
              'TT_FLOAT': 'FLOAT',
              'TT_PLUS': 'PLUS'}


TT_char = 'CHAR'     # this my touch

#####################################
# Token class
# -----------------------------------


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

#######################################
# LEXER
# --------------------------------------


class Lexer:
    def __init__(self, statment):
        self.statment = statment
        self.index = -1
        self.cur_chr = None
        self.move()

    def move(self):
        self.index += 1
        self.cur_chr = self.statment[self.index] if self.index < len(
            self.statment) else None

    def make_tokens(self):
        tokens = []

        while self.cur_chr != None:
            print("infinte")
            if self.cur_chr in ' \t':
                self.move()
            elif self.cur_chr in DIGITS:
                tokens.append(self.make_number())
            elif self.cur_chr in ['+', '-', '/', '*', '(', ')']:
                tokens.append(Token(tokens_map[str(self.cur_chr)]))
                self.move()
            else:
                print("here some error")
                char = self.cur_chr
                self.move()
                return [], IllegalCharError("'"+char+"'")
                pass
        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.cur_chr != None and self.cur_chr in DIGITS + '.':
            if self.cur_chr == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.cur_chr
            self.move()

        if dot_count == 0:
            return Token(tokens_map['TT_INT'], int(num_str))
        else:
            return Token(tokens_map['TT_FLOAT'], float(num_str))


#####################
# NOde
# -------------
class Node:
    def __init__(self, token) -> None:
        self.token = token

    def __repr__(self) -> str:
        return f'(self.token)'

#####################
# BinOPRANode
# -------------


class BinOPRANode:
    def __init__(self, left_node, op_tok, right_node) -> None:
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self) -> str:
        return f'({self.left_node},{self.op_tok},{self.right_node})'


#####################
# Parser
# -------------
class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.tok.idx = -1
        self.move()

    def move(self):
        self.tok.idx += 1
        if self.tok.idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok.idx]
        return self.current_tok

    def parse(self):
        res = self.current_tok
        return res

    def factor(self):
        temp_tok = self.current_tok

        if temp_tok.type in (tokens_map['TT_INT'], tokens_map['TT_FLOAT']):
            self.move()
            return Node(temp_tok)

    def make_term(self):
        return self.make_bin_op(self.factor, (tokens_map['*'], tokens_map['/']))

    def make_expretion(self):
        return self.make_bin_op(self.make_term, (tokens_map['+'], tokens_map['-']))

    def make_bin_op(self, func, oprators):
        left = func()
        while self.current_tok.type in oprators:
            op_tok = self.current_tok
            self.move()
            right = func()

             
            left = BinOPRANode(left, op_tok, right)
        return left


#####################
# RUN
# -------------
def run(text):
    # generate tokens
    l = Lexer(text)
    tokens, error = l.make_tokens()
    if error:
        return None, error

    # Generate AST
    parser = Parser(tokens =  tokens)
    return (tokens, error)


if __name__ == "__main__":
    tble = run("11111111 )))) 123.121 (aafg)")
    print(tble[1].as_string())
