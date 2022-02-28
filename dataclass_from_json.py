#!/usr/bin/env python

from typing import Type
from json import load as json_load
from sys import stderr

from dataclass_from_json.cli import MakeDataclassArgumentParser
from dataclass_from_json import dataclass_to_code, dict_to_dataclass


def main():
    args: Type[MakeDataclassArgumentParser.Namespace] = MakeDataclassArgumentParser().parse_args()

    json_data = json_load(fp=args.input_file)

    if isinstance(json_data, list):

        if not json_data:
            print('The input data is an empty list.', file=stderr)
            exit(1)

        print('The input data is a list; using the first element.', file=stderr)

        json_data = json_data[0]

    if not isinstance(json_data, dict):
        print(f'The input data is not a JSON object, but {type(json_data)}', file=stderr)
        exit(1)

    print(
        dataclass_to_code(
            dataclass_class=dict_to_dataclass(
                obj=json_data,
                class_name=args.class_name
            )
        )
    )


if __name__ == '__main__':
    main()
