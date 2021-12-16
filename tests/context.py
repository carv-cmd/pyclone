from sys import path as sys_path
from os import path as os_path


_dirname = os_path.dirname(__file__)

_join_path = os_path.join(_dirname, '..')

sys_path.insert(0, _join_path)


# import <pyclone>

