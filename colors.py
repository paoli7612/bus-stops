class Colors:
    WHITE  = '\033[0m'
    RED  = '\033[31m'
    GREEN  = '\033[32m'
    ORANGE  = '\033[33m'
    BLUE  = '\033[34m'
    PURPLE  = '\033[35m'
    CYAN = '\033[36m'
    TAN  = '\033[93m'

    def show(text,color):
        print(color + text)
