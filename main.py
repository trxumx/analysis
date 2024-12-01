# Определение типов лексем
class LexTypes:
    LEX_NULL = 0
    LEX_INTEGER = 1
    LEX_REAL = 2
    LEX_BOOLEAN = 3
    LEX_BEGIN = 4
    LEX_END = 5
    LEX_IF = 6
    LEX_ELSE = 7
    LEX_FOR = 8
    LEX_TO = 9
    LEX_STEP = 10
    LEX_NEXT = 11
    LEX_WHILE = 12
    LEX_READLN = 13
    LEX_WRITELN = 14
    LEX_TRUE = 15
    LEX_FALSE = 16
    LEX_PROGRAM = 17
    LEX_VAR = 18
    LEX_SEMICOLON = 19
    LEX_COMMA = 20
    LEX_ASSIGN = 21
    LEX_EQ = 22  # Добавлено для '='
    LEX_NEQ = 23  # Добавлено для '<>'
    LEX_LSS = 24
    LEX_GTR = 25
    LEX_REQ = 26
    LEX_LEQ = 27
    LEX_PLUS = 28
    LEX_MINUS = 29
    LEX_OR = 30
    LEX_MULT = 31
    LEX_DIV = 32
    LEX_AND = 33
    LEX_NOT = 34
    LEX_START_COM = 35
    LEX_FINISH_COM = 36
    LEX_LPAREN = 37
    LEX_RPAREN = 38
    LEX_NUM = 39
    LEX_ID = 40
    LEX_LBRACKET = 41
    LEX_RBRACKET = 42
    LEX_THEN = 43
    LEX_DO = 44


# Словарь для текстового представления лексем
lex_dec = [
    "LEX_NULL",
    "LEX_INTEGER",
    "LEX_REAL",
    "LEX_BOOLEAN",
    "LEX_BEGIN",
    "LEX_END",
    "LEX_IF",
    "LEX_ELSE",
    "LEX_FOR",
    "LEX_TO",
    "LEX_STEP",
    "LEX_NEXT",
    "LEX_WHILE",
    "LEX_READLN",
    "LEX_WRITELN",
    "LEX_TRUE",
    "LEX_FALSE",
    "LEX_PROGRAM",
    "LEX_VAR",
    "LEX_SEMICOLON",
    "LEX_COMMA",
    "LEX_ASSIGN",
    "LEX_EQ",
    "LEX_NEQ",
    "LEX_LSS",
    "LEX_GTR",
    "LEX_REQ",
    "LEX_LEQ",
    "LEX_PLUS",
    "LEX_MINUS",
    "LEX_OR",
    "LEX_MULT",
    "LEX_DIV",
    "LEX_AND",
    "LEX_NOT",
    "LEX_START_COM",
    "LEX_FINISH_COM",
    "LEX_LPAREN",
    "LEX_RPAREN",
    "LEX_NUM",
    "LEX_ID",
    "LEX_LBRACKET",
    "LEX_RBRACKET",
    "LEX_THEN",
    "LEX_DO"
]

# Ключевые слова и их соответствующие типы
key_words_dict = {
    "integer": LexTypes.LEX_INTEGER,
    "real": LexTypes.LEX_REAL,
    "boolean": LexTypes.LEX_BOOLEAN,
    "begin": LexTypes.LEX_BEGIN,
    "end": LexTypes.LEX_END,
    "if": LexTypes.LEX_IF,
    "else": LexTypes.LEX_ELSE,
    "for": LexTypes.LEX_FOR,
    "to": LexTypes.LEX_TO,
    "step": LexTypes.LEX_STEP,
    "next": LexTypes.LEX_NEXT,
    "while": LexTypes.LEX_WHILE,
    "readln": LexTypes.LEX_READLN,
    "writeln": LexTypes.LEX_WRITELN,
    "true": LexTypes.LEX_TRUE,
    "false": LexTypes.LEX_FALSE,
    "program": LexTypes.LEX_PROGRAM,
    "var": LexTypes.LEX_VAR,
    "then": LexTypes.LEX_THEN,
    "do": LexTypes.LEX_DO
}

# Разделители и их соответствующие типы
sep_words_dict = {
    ";": LexTypes.LEX_SEMICOLON,
    ",": LexTypes.LEX_COMMA,
    "as": LexTypes.LEX_ASSIGN,
    "=": LexTypes.LEX_EQ,
    "<>": LexTypes.LEX_NEQ,
    ">": LexTypes.LEX_GTR,
    "<": LexTypes.LEX_LSS,
    ">=": LexTypes.LEX_REQ,
    "<=": LexTypes.LEX_LEQ,
    "+": LexTypes.LEX_PLUS,
    "-": LexTypes.LEX_MINUS,
    "or": LexTypes.LEX_OR,
    "*": LexTypes.LEX_MULT,
    "/": LexTypes.LEX_DIV,
    "and": LexTypes.LEX_AND,
    "not": LexTypes.LEX_NOT,
    "{": LexTypes.LEX_START_COM,
    "}": LexTypes.LEX_FINISH_COM,
    "(": LexTypes.LEX_LPAREN,
    ")": LexTypes.LEX_RPAREN,
    "[": LexTypes.LEX_LBRACKET,
    "]": LexTypes.LEX_RBRACKET
}


# Класс токена
class Token:
    def __init__(self, type_, value, x_coord=0, y_coord=0):
        self.type = type_
        self.value = value
        self.x_coord = x_coord
        self.y_coord = y_coord


# Состояния конечного автомата
class State:
    S = 0  # Начальное состояние конечного автомата
    ID = 1  # Обработка идентификаторов конечным автоматом
    NUM = 2  # Обработка чисел конечным автоматом
    COM = 3  # Обработка комментариев конечным автоматом
    EQ = 4  # Обработка операторов сравнивания и присвоения конечным автоматом
    NEQ = 5  # Обработка унарной операции или оператора неравенства конечным автоматом
    OP = 6  # Обработка бинарных операций конечным автоматом


# Лексический анализатор
class Lexer:
    def __init__(self, file_name):
        self.tokensVec = []
        self.x_coord = 1  # Начинаем с 1, так как первая позиция в строке
        self.y_coord = 1  # Начинаем с 1, так как первая строка имеет номер 1
        self.c = ''
        self.lexBuff = ''
        self.cState = State.S
        self.buffToken = None

        # Читаем весь файл целиком
        with open(file_name, 'r') as f:
            self.inputString = f.read()
        self.reading_mechanism(self.inputString)
        self.proc_tokens()

    def reading_mechanism(self, inputString):
        i = 0
        length = len(inputString)
        self.x_coord = 1
        self.y_coord = 1

        while i < length:
            c = inputString[i]
            self.c = c

            # Обработка символов переноса строки
            if c == '\n':
                self.y_coord += 1
                self.x_coord = 1
                i += 1
                continue
            elif c == '\r':
                i += 1
                if i < length and inputString[i] == '\n':
                    i += 1
                self.y_coord += 1
                self.x_coord = 1
                continue

            # Пропускаем пробелы и табуляции
            if c in ' \t':
                i += 1
                self.x_coord += 1
                continue

            # Обработка комментариев
            if c == '{':
                i += 1
                self.x_coord += 1
                while i < length:
                    c = inputString[i]
                    if c == '}':
                        i += 1
                        self.x_coord += 1
                        break
                    elif c == '\n':
                        self.y_coord += 1
                        self.x_coord = 1
                        i += 1
                    elif c == '\r':
                        i += 1
                        if i < length and inputString[i] == '\n':
                            i += 1
                        self.y_coord += 1
                        self.x_coord = 1
                    else:
                        i += 1
                        self.x_coord += 1
                else:
                    print(f"ERROR (unclosed comment) -> ({self.y_coord};{self.x_coord})")
                    exit(104)
                continue

            # Проверяем многосимвольные разделители и операторы
            multi_char_sep_found = False
            for sep in sorted(sep_words_dict.keys(), key=lambda x: -len(x)):
                if inputString.startswith(sep, i):
                    start_x_coord = self.x_coord
                    self.lexBuff = sep
                    self.buffToken = Token(sep_words_dict[sep], self.lexBuff, start_x_coord, self.y_coord)
                    self.tokensVec.append(self.buffToken)
                    i += len(sep)
                    self.x_coord += len(sep)
                    multi_char_sep_found = True
                    break
            if multi_char_sep_found:
                continue

            # Обработка идентификаторов и ключевых слов
            if c.isalpha():
                start_x_coord = self.x_coord
                self.lexBuff = ''
                while i < length and inputString[i].isalnum():
                    self.lexBuff += inputString[i]
                    i += 1
                    self.x_coord += 1
                self.buffToken = Token(None, self.lexBuff, start_x_coord, self.y_coord)
                if self.key_lex():
                    self.tokensVec.append(self.buffToken)
                else:
                    self.buffToken.type = LexTypes.LEX_ID
                    self.tokensVec.append(self.buffToken)
                continue

            # Обработка чисел
            elif c.isdigit() or c == '.':
                start_x_coord = self.x_coord
                self.lexBuff = ''
                while i < length and (inputString[i].isalnum() or inputString[i] in '.eE+-'):
                    self.lexBuff += inputString[i]
                    i += 1
                    self.x_coord += 1
                self.buffToken = Token(None, self.lexBuff, start_x_coord, self.y_coord)
                if self.num_lex():
                    self.tokensVec.append(self.buffToken)
                else:
                    print(
                        f"ERROR (incorrect number) -> {self.buffToken.value} ({self.buffToken.y_coord};{self.buffToken.x_coord})")
                    exit(102)
                continue


            # Обработка односимвольных разделителей
            elif c in sep_words_dict:
                start_x_coord = self.x_coord
                self.lexBuff = c
                self.buffToken = Token(sep_words_dict[c], self.lexBuff, start_x_coord, self.y_coord)
                self.tokensVec.append(self.buffToken)
                i += 1
                self.x_coord += 1
                continue

            # Неизвестный символ
            else:
                print(f"ERROR (incorrect symbol) -> {c} ({self.y_coord};{self.x_coord})")
                exit(101)

            # Увеличиваем координаты после обработки символа
            i += 1
            self.x_coord += 1

        # После обработки строки очищаем буфер
        self.clear_string()

    def add_to_string(self):
        self.lexBuff += self.c

    def clear_string(self):
        if self.lexBuff == '':
            return
        self.buffToken = Token(None, self.lexBuff, self.x_coord, self.y_coord)
        if self.key_lex() or self.sep_lex() or self.num_lex() or self.id_lex():
            self.tokensVec.append(self.buffToken)
        else:
            print(
                f"ERROR (incorrect identifier) -> {self.buffToken.value} ({self.buffToken.y_coord},{self.buffToken.x_coord})")
            exit(102)
        self.lexBuff = ''

    def key_lex(self):
        if self.buffToken.value in key_words_dict:
            self.buffToken.type = key_words_dict[self.buffToken.value]
            return True
        return False

    def sep_lex(self):
        if self.buffToken.value in sep_words_dict:
            self.buffToken.type = sep_words_dict[self.buffToken.value]
            return True
        return False

    def num_lex(self):
        buff = self.buffToken.value
        if len(buff) == 0:
            return False
        lastSymb = buff[-1].lower()
        if (buff[0].isdigit() and lastSymb in 'bodh') or self.check_e(buff):
            self.buffToken.type = LexTypes.LEX_NUM
            return True
        return False

    def id_lex(self):
        if self.buffToken.value[0].isalpha():
            self.buffToken.type = LexTypes.LEX_ID
            return True
        return False

    def check_e(self, buffStr):
        ePlace = -1
        dPlace = -1
        if buffStr[-1] in '+-':
            return False
        for i, ch in enumerate(buffStr):
            if ch.lower() == 'e':
                if ePlace == -1:
                    ePlace = i
                else:
                    return False  # Multiple 'e's not allowed
            elif ch == '.':
                if dPlace == -1:
                    dPlace = i
                else:
                    return False  # Multiple '.'s not allowed
            elif ch in '+-':
                if ePlace != -1 and i == ePlace + 1:
                    continue  # Sign after 'e' is allowed
                else:
                    return False
            elif not ch.isdigit():
                return False  # Any other character is invalid
        if ePlace != -1 and (ePlace == len(buffStr) - 1):
            return False  # 'e' cannot be the last character
        return True

    def print_all_tokens(self):
        for tok in self.tokensVec:
            print(f'({lex_dec[tok.type]}) -> {tok.value}')

    def proc_tokens(self):
        self.tokensVec = [tok for tok in self.tokensVec if tok.type != LexTypes.LEX_NULL]


# Структура для хранения переменных
class VarToken:
    def __init__(self, varType='', varName=''):
        self.varType = varType
        self.varName = varName


# Синтаксический и семантический анализатор
class Parser:
    def __init__(self, tokensVec):
        self.idx = 0
        self.tokensVec = tokensVec
        self.tokenCount = len(tokensVec)
        self.tokensVar = []
        self.singleTokenVar = VarToken()
        self.ifWhileCheck = 0
        self.ifWhileFlag = False

        if self.tokensVec[self.idx].type != LexTypes.LEX_PROGRAM:
            print(
                f"ERROR (there must be a keyword 'program') -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].x_coord};{self.tokensVec[self.idx].y_coord})")
            exit(201)
        self.idx += 1

    def start_prog(self):
        if self.idx < self.tokenCount and self.tokensVec[self.idx].type == LexTypes.LEX_VAR:
            self.idx += 1
            if self.idx < self.tokenCount and self.tokensVec[self.idx].type in (
                    LexTypes.LEX_INTEGER, LexTypes.LEX_REAL, LexTypes.LEX_BOOLEAN):
                while self.idx < self.tokenCount and self.tokensVec[self.idx].type in (
                        LexTypes.LEX_INTEGER, LexTypes.LEX_REAL, LexTypes.LEX_BOOLEAN):
                    self.start_vars()
            else:
                print(
                    f"ERROR (there must be a type of variable) -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
                exit(203)
        if self.idx < self.tokenCount and self.tokensVec[self.idx].type == LexTypes.LEX_BEGIN:
            self.idx += 1
            self.start_begin()
        else:
            print(
                f"ERROR (the program structure is broken) -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
            exit(202)

    def start_vars(self):
        # Process the type of variable
        if self.tokensVec[self.idx].type == LexTypes.LEX_INTEGER:
            self.singleTokenVar.varType = "INTEGER"
            self.idx += 1
        elif self.tokensVec[self.idx].type == LexTypes.LEX_REAL:
            self.singleTokenVar.varType = "REAL"
            self.idx += 1
        elif self.tokensVec[self.idx].type == LexTypes.LEX_BOOLEAN:
            self.singleTokenVar.varType = "BOOLEAN"
            self.idx += 1
        else:
            print(
                f"ERROR (there must be a type of variable) -> {self.tokensVec[self.idx].value} "
                f"({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
            exit(203)

        # Process the first identifier
        self.start_id()
        # Check for redeclaration before adding to the list
        for var in self.tokensVar:
            if var.varName == self.singleTokenVar.varName:
                print(
                    f"ERROR (re-declaring a variable) -> {self.singleTokenVar.varName} "
                    f"({self.tokensVec[self.idx - 1].y_coord};{self.tokensVec[self.idx - 1].x_coord})")
                exit(222)
        self.tokensVar.append(VarToken(self.singleTokenVar.varType, self.singleTokenVar.varName))

        # Process additional identifiers after commas
        while self.idx < self.tokenCount and self.tokensVec[self.idx].type == LexTypes.LEX_COMMA:
            self.idx += 1
            self.start_id()
            # Check for redeclaration before adding to the list
            for var in self.tokensVar:
                if var.varName == self.singleTokenVar.varName:
                    print(
                        f"ERROR (re-declaring a variable) -> {self.singleTokenVar.varName} "
                        f"({self.tokensVec[self.idx - 1].y_coord};{self.tokensVec[self.idx - 1].x_coord})")
                    exit(222)
            self.tokensVar.append(VarToken(self.singleTokenVar.varType, self.singleTokenVar.varName))

    def start_id(self, flagToken=True):
        if self.tokensVec[self.idx].type == LexTypes.LEX_ID:
            if flagToken:
                self.singleTokenVar.varName = self.tokensVec[self.idx].value
            else:
                self.id_check()
            self.idx += 1
        else:
            print(
                f"ERROR (there must be an id) -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].x_coord};{self.tokensVec[self.idx].y_coord})")
            exit(204)

    def start_begin(self):
        if self.idx >= self.tokenCount:
            return
        if self.tokensVec[self.idx].type == LexTypes.LEX_ID:
            self.id_check()
            self.idx += 1
            if self.tokensVec[self.idx].type == LexTypes.LEX_ASSIGN:
                self.idx += 1
                self.start_V()
            else:
                print(
                    f"ERROR (there must be an assignment sign) -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
                exit(205)
        elif self.tokensVec[self.idx].type == LexTypes.LEX_FOR:
            self.idx += 1
            if self.tokensVec[self.idx].type == LexTypes.LEX_ID:
                self.id_check()
                self.idx += 1
                if self.tokensVec[self.idx].type == LexTypes.LEX_ASSIGN:
                    self.idx += 1
                    self.start_V()
                    if self.tokensVec[self.idx].type == LexTypes.LEX_TO:
                        self.idx += 1
                        self.start_V()
                        # Check for 'do' keyword here
                        if self.tokensVec[self.idx].type == LexTypes.LEX_DO:
                            self.idx += 1
                            # Optional: Check for 'step' keyword if your language supports it
                            if self.tokensVec[self.idx].type == LexTypes.LEX_STEP:
                                self.idx += 1
                                self.start_V()
                            self.start_begin()
                            if self.tokensVec[self.idx].type == LexTypes.LEX_NEXT:
                                self.idx += 1
                                self.start_begin()
                            else:
                                print(
                                    f"ERROR (there must be a keyword 'next') -> {self.tokensVec[self.idx].value} "
                                    f"({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
                                exit(206)
                        else:
                            print(
                                f"ERROR (there must be a keyword 'do') -> {self.tokensVec[self.idx].value} "
                                f"({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
                            exit(225)  # Use an appropriate error code
                    else:
                        print(
                            f"ERROR (there must be a keyword 'to') -> {self.tokensVec[self.idx].value} "
                            f"({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
                        exit(207)
                else:
                    print(
                        f"ERROR (there must be an assignment sign) -> {self.tokensVec[self.idx].value} "
                        f"({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
                    exit(208)
            else:
                print(
                    f"ERROR (there must be an ID) -> {self.tokensVec[self.idx].value} "
                    f"({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
                exit(209)

        elif self.tokensVec[self.idx].type == LexTypes.LEX_IF:
            self.idx += 1
            if self.tokensVec[self.idx].type == LexTypes.LEX_LPAREN:
                self.ifWhileCheck = self.idx - 1
                self.idx += 1
                self.ifWhileFlag = False
                self.start_V()
                if not self.ifWhileFlag:
                    print(
                        f"ERROR ('if' statement accepts only logical expressions) -> {self.tokensVec[self.ifWhileCheck].value} "
                        f"({self.tokensVec[self.ifWhileCheck].y_coord};{self.tokensVec[self.ifWhileCheck].x_coord})")
                    exit(220)
                if self.tokensVec[self.idx].type == LexTypes.LEX_RPAREN:
                    self.idx += 1
                    # Check for 'then' keyword
                    if self.tokensVec[self.idx].type == LexTypes.LEX_THEN:
                        self.idx += 1
                        self.start_begin()
                        if self.idx < self.tokenCount and self.tokensVec[self.idx].type == LexTypes.LEX_ELSE:
                            self.idx += 1
                            self.start_begin()
                    else:
                        print(
                            f"ERROR (there must be a keyword 'then') -> {self.tokensVec[self.idx].value} "
                            f"({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
                        exit(224)  # Use an appropriate error code
                else:
                    print(
                        f"ERROR (there must be an ')') -> {self.tokensVec[self.idx].value} "
                        f"({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
                    exit(210)
            else:
                print(
                    f"ERROR (there must be an '(') -> {self.tokensVec[self.idx].value} "
                    f"({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
                exit(211)

        elif self.tokensVec[self.idx].type == LexTypes.LEX_WHILE:
            self.idx += 1
            if self.tokensVec[self.idx].type == LexTypes.LEX_LPAREN:
                self.ifWhileCheck = self.idx - 1
                self.idx += 1
                self.ifWhileFlag = False
                self.start_V()
                if not self.ifWhileFlag:
                    print(
                        f"ERROR ('while' statement accepts only logical expressions) -> {self.tokensVec[self.ifWhileCheck].value} ({self.tokensVec[self.ifWhileCheck].x_coord};{self.tokensVec[self.ifWhileCheck].y_coord})")
                    exit(221)
                if self.tokensVec[self.idx].type == LexTypes.LEX_RPAREN:
                    self.idx += 1
                    self.start_begin()
                else:
                    print(
                        f"ERROR (there must be an ')') -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].x_coord};{self.tokensVec[self.idx].y_coord})")
                    exit(212)
            else:
                print(
                    f"ERROR (there must be an '(') -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].x_coord};{self.tokensVec[self.idx].y_coord})")
                exit(213)
        elif self.tokensVec[self.idx].type == LexTypes.LEX_BEGIN:
            self.idx += 1
            self.start_begin()
            while self.tokensVec[self.idx].type == LexTypes.LEX_SEMICOLON:
                self.idx += 1
                self.start_begin()
            if self.tokensVec[self.idx].type == LexTypes.LEX_END:
                self.idx += 1
            else:
                print(
                    f"ERROR (incorrect input) -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].x_coord};{self.tokensVec[self.idx].y_coord})")
                exit(214)
        elif self.tokensVec[self.idx].type == LexTypes.LEX_READLN:
            self.idx += 1
            self.start_id(False)
            while self.tokensVec[self.idx].type == LexTypes.LEX_COMMA:
                self.idx += 1
                self.start_id(False)
        elif self.tokensVec[self.idx].type == LexTypes.LEX_WRITELN:
            self.idx += 1
            self.start_V()
            while self.tokensVec[self.idx].type == LexTypes.LEX_COMMA:
                self.idx += 1
                self.start_V()
        elif self.tokensVec[self.idx].type == LexTypes.LEX_END:
            if self.idx == self.tokenCount - 1:
                pass
            else:
                print(
                    f"ERROR (incorrect input) -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].x_coord};{self.tokensVec[self.idx].y_coord})")
                exit(215)
        else:
            print(
                f"ERROR (incorrect input) -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].x_coord};{self.tokensVec[self.idx].y_coord})")
            exit(216)

    def start_V(self):
        self.start_O()
        while self.tokensVec[self.idx].type in [LexTypes.LEX_EQ, LexTypes.LEX_NEQ, LexTypes.LEX_LSS, LexTypes.LEX_GTR,
                                                LexTypes.LEX_REQ, LexTypes.LEX_LEQ]:
            self.ifWhileFlag = True
            self.idx += 1
            self.start_O()

    def start_O(self):
        self.start_S()
        while self.tokensVec[self.idx].type in [LexTypes.LEX_PLUS, LexTypes.LEX_MINUS, LexTypes.LEX_OR]:
            self.idx += 1
            self.start_S()

    def start_S(self):
        self.start_M()
        while self.tokensVec[self.idx].type in [LexTypes.LEX_MULT, LexTypes.LEX_DIV, LexTypes.LEX_AND]:
            self.idx += 1
            self.start_M()

    def start_M(self):
        if self.tokensVec[self.idx].type == LexTypes.LEX_ID:
            self.id_check()
            self.idx += 1
        elif self.tokensVec[self.idx].type in [LexTypes.LEX_TRUE, LexTypes.LEX_FALSE]:
            self.ifWhileFlag = True
            self.idx += 1
        elif self.tokensVec[self.idx].type == LexTypes.LEX_NUM:
            self.num_check()
            self.idx += 1
        elif self.tokensVec[self.idx].type == LexTypes.LEX_NOT:
            self.idx += 1
            self.start_M()
        elif self.tokensVec[self.idx].type == LexTypes.LEX_LPAREN:
            self.idx += 1
            self.start_V()
            if self.tokensVec[self.idx].type == LexTypes.LEX_RPAREN:
                self.idx += 1
            else:
                print(
                    f"ERROR (there must be a closing parenthesis) -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].x_coord};{self.tokensVec[self.idx].y_coord})")
                exit(217)
        else:
            print(
                f"ERROR (there must be a variable or number) -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
            exit(217)

    def num_check(self):
        str_num = self.tokensVec[self.idx].value
        maxS = max(str_num[:-1], default='')
        maxS = max(maxS) if maxS else ''
        fE = max(str_num.find('E'), str_num.find('e'))
        if ((str_num[-1].lower() == 'b' and maxS > '1') or
                (str_num[-1].lower() == 'o' and maxS > '7') or
                (str_num[-1].lower() == 'd' and maxS > '9') or
                (fE != -1 and not ('0' <= maxS <= '9'))):
            print(
                f"ERROR (incorrect number) -> {self.tokensVec[self.idx].value} ({self.tokensVec[self.idx].x_coord};{self.tokensVec[self.idx].y_coord})")
            exit(218)

    def id_check(self):
        for var in self.tokensVar:
            if var.varName == self.tokensVec[self.idx].value:
                return
        print(
            f"ERROR (undeclared or incorrect variable) -> {self.tokensVec[self.idx].value} "
            f"({self.tokensVec[self.idx].y_coord};{self.tokensVec[self.idx].x_coord})")
        exit(219)


# Главная часть программы
if __name__ == '__main__':
    input_file_name = 'advanced_input.txt'  # Имя входного файла
    lexAnalys = Lexer(input_file_name)
    # lexAnalys.print_all_tokens() # Вывод всех лексем

    syntAnalys = Parser(lexAnalys.tokensVec)
    syntAnalys.start_prog()

    print("CORRECT")
