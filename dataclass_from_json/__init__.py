from dataclasses import make_dataclass, is_dataclass, fields
from typing import Optional, Any
from uuid import uuid4

from string_utils_py import to_snake_case, to_pascal_case


def dict_to_dataclass(obj, class_name: Optional[str] = None):
    if isinstance(obj, dict):
        return make_dataclass(
            cls_name=(class_name or str(uuid4()).split('-')[-1]).replace('-', ''),
            fields=[(to_snake_case(string=name), dict_to_dataclass(value, name)) for name, value in obj.items()]
        )
    elif isinstance(obj, (list, tuple)):
        type_set = set()
        for element in obj:
            res = dict_to_dataclass(element)
            type_set.add(
                tuple((field.name, field.type) for field in fields(res)) if is_dataclass(obj=res) else res
            )

        # if not type_set:
        return list
        # elif len(type_set) != 1:
        #     raise ValueError

        # return next(iter(type_set))

    elif isinstance(obj, (str, int, float)):
        return type(obj)
    elif obj is None:
        return Any
    else:
        raise ValueError


def dataclass_to_code(dataclass_class):
    """
    Produce a `dataclass` definition from a dataclass.

    :param dataclass_class: A `dataclass` class.
    :return: The code definition of the provided `dataclass` class.
    """

    return (
        '\n'.join(dataclass_to_code(field.type) for field in fields(dataclass_class) if is_dataclass(field.type)) + '\n\n\n' + (
            f'@dataclass\n'
            f'class {to_pascal_case(string=dataclass_class.__name__)}:\n    '
            + ('\n    '.join(
                f'{to_snake_case(string=field.name)}: {(to_pascal_case(string=field.type.__name__) if is_dataclass(field.type) else field.type.__name__) if isinstance(field.type, type) else field.type}'
                for field in fields(dataclass_class)
            ) or 'pass')
        )
    ).lstrip()
