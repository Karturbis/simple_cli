class Cli:


    @classmethod
    def cli(cls, commands: dict = None):
        seperators: dict = {}
        commands["help"] = cls._help

    @classmethod
    def _help(cls, commands):
        print(commands)
