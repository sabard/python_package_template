""" Example Class """


class HelloWorld:
    """ HelloWorld Class  """

    def __init__(self, name):
        """ Initialize HelloWorld. """

        self.name = name

    def message(self):
        """ Return greeting for name """

        return f"Hello {self.name}"
