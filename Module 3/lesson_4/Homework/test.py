class CatTailError(Exception):
    def __init__(self, message="У кішки відпав хвіст!"):
        self.message = message
        super().__init__(self.message)


def cat_tail_issue():
    try:
        raise CatTailError()
    except CatTailError as e:
        print("Помилка: ", e)


cat_tail_issue()
