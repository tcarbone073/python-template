import pathlib


class Path:
    base = pathlib.Path(__file__).parent

    @classmethod
    def base(cls, filename):
        return pathlib.Path.joinpath(cls.base, filename)
