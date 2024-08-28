# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/28 下午1:46
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : docstring.py
@Software: PyCharm
"""
from typing import Optional

from pydantic import BaseModel, Field

from liteyuki_autodoc.i18n import get_text


class Attr(BaseModel):
    name: str
    type: str = ""
    desc: str = ""


class Args(BaseModel):
    name: str
    type: str = ""
    desc: str = ""


class Return(BaseModel):
    desc: str = ""


class Exception_(BaseModel):
    name: str
    desc: str = ""


class Raise(BaseModel):
    exceptions: list[Exception_] = []


class Example(BaseModel):
    desc: str = ""
    input: str = ""
    output: str = ""


class Docstring(BaseModel):
    desc: str = ""
    args: list[Args] = []
    attrs: list[Attr] = []
    return_: Optional[Return] = None
    raise_: list[Exception_] = []
    example: list[Example] = []

    def add_desc(self, desc: str):
        if self.desc == "":
            self.desc = desc
        else:
            self.desc += "\n" + desc

    def add_arg(self, name: str, type_: str = "", desc: str = ""):
        self.args.append(Args(name=name, type=type_, desc=desc))

    def add_attrs(self, name: str, type_: str = "", desc: str = ""):
        self.attrs.append(Attr(name=name, type=type_, desc=desc))

    def add_return(self, desc: str = ""):
        self.return_ = Return(desc=desc)

    def add_raise(self, name: str, desc: str = ""):
        self.raise_.append(Exception_(name=name, desc=desc))

    def add_example(self, desc: str = "", input_: str = "", output: str = ""):
        self.example.append(Example(desc=desc, input=input_, output=output))

    def reduction(self) -> str:
        """
        通过解析结果还原docstring
        Args:

        Returns:

        """
        ret = ""
        ret += self.desc + "\n"
        if self.args:
            ret += "Args:\n"
            for arg in self.args:
                ret += f"    {arg.name}: {arg.type}\n        {arg.desc}\n"
        if self.attrs:
            ret += "Attributes:\n"
            for attr in self.attrs:
                ret += f"    {attr.name}: {attr.type}\n        {attr.desc}\n"
        if self.return_:
            ret += "Returns:\n"
            ret += f"    {self.return_.desc}\n"

        if self.raise_:
            ret += "Raises:\n"
            for exception in self.raise_:
                ret += f"    {exception.name}\n        {exception.desc}\n"

        if self.example:
            ret += "Examples:\n"
            for example in self.example:
                ret += f"    {example.desc}\n        Input: {example.input}\n        Output: {example.output}\n"

        return ret

    def markdown(self, lang: str, indent: int = 4, is_classmethod: bool = False) -> str:
        """
        生成markdown文档
        Args:
            is_classmethod:
            lang:
            indent:

        Returns:

        """
        PREFIX = "" * indent
        if is_classmethod:
            PREFIX = "  -"
        ret = ""
        ret += self.desc + "\n\n"
        if self.args:
            ret += PREFIX + f"{get_text(lang, 'docstring.args')}:\n\n"
            for arg in self.args:
                ret += PREFIX + f"{arg.name}: {arg.type}  {arg.desc}\n\n"
        if self.attrs:
            ret += PREFIX + f"{get_text(lang, 'docstring.attrs')}:\n\n"
            for attr in self.attrs:
                ret += PREFIX + f"{attr.name}: {attr.type}  {attr.desc}\n\n"
        if self.return_:
            ret += PREFIX + f"{get_text(lang, 'docstring.return')}:\n\n"
            ret += PREFIX + f"{self.return_.desc}\n\n"
        if self.raise_:
            ret += PREFIX + f"{get_text(lang, 'docstring.raises')}:\n\n"
            for exception in self.raise_:
                ret += PREFIX + f"{exception.name}  {exception.desc}\n\n"
        if self.example:
            ret += PREFIX + f"{get_text(lang, 'docstring.example')}:\n\n"
            for example in self.example:
                ret += PREFIX + f"{example.desc}\n        Input: {example.input}\n        Output: {example.output}\n\n"
        return ret

    def __str__(self):
        return self.desc