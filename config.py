from configparser import ConfigParser
import os


class Config:  # {
    """
    Store config
    """
    __conf = None

    @classmethod
    def config(cls, key='DEFAULT'):  # {
        if cls.__conf is None:  # {
            cls.__conf = ConfigParser()
            conf_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),  "config.ini")
            cls.__conf.read(conf_file)
        # }
        section_conf = cls.__conf.items(section=key)
        return {tup[0]: tup[1] for tup in section_conf}
    # }
# }


if __name__ == '__main__':
    import itertools

    # or, better:
    conf = Config.config()
    print(conf)
