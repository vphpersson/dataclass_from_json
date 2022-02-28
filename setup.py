from setuptools import setup, find_packages

setup(
    name='dataclass_from_json',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'typed_argument_parser @ git+https://github.com/vphpersson/typed_argument_parser.git#egg=typed_argument_parser',
        'string_utils_py @ git+https://github.com/vphpersson/string_utils_py.git#egg=string_utils_py'
    ]
)
