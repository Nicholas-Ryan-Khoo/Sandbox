class ProgrammingLanguage:
    """Class for programming language."""
    def __init__(self, name, typing, reflection, year):
        """Values for programming language."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if language is dynamically typed"""
        if self.typing == "Dynamic":
            return True

    def __str__(self):
        """Returns in str"""
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name,
                                                                    self.typing, self.reflection, self.year)
