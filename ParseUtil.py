class Parser:

    def __init__(self, parse_method):
        """
            A generic parser class that accepts a file parsing method to execute later on
                Args:
                    parse_method (method): a parsing method
            """
        self.read_file = parse_method

