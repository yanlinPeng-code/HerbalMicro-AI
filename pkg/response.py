from dataclasses import field, dataclass

from pydantic import BaseModel, Field
from typing import Any
from .http_code import HttpCode
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class Response(BaseModel):
    """响应"""
    code: HttpCode
    message: str
    data: Any = Field(default_factory=dict)


def json(data: Response = None):
    if data is None:
        data = Response(code=HttpCode.SUCCESS, message="成功", data={}) # Default for empty data
    return JSONResponse(content=jsonable_encoder(data), status_code=200)


def success_json(data: Any = None):
    return json(Response(code=HttpCode.SUCCESS, message="成功", data=data))


def fail_json(data: Any = None):
    """失败数据响应"""
    return json(Response(code=HttpCode.FAIL, message="", data=data))


def message(code: HttpCode, msg: str = ""): # Ensure code is always provided
    """基础的消息响应，固定返回消息提示，数据固定为空字典"""
    return json(Response(code=code, message=msg, data={}))


def success_message(msg: str = ""):
    """成功的消息响应"""
    return message(code=HttpCode.SUCCESS, msg=msg)


def fail_message(msg: str = ""):
    """失败的消息响应"""
    return message(code=HttpCode.FAIL, msg=msg)


def not_found_message(msg: str = ""):
    """未找到消息响应"""
    return message(code=HttpCode.NOT_FOUND, msg=msg)


def unauthorized_message(msg: str = ""):
    """未授权消息响应"""
    return message(code=HttpCode.UNAUTHORIZED, msg=msg)


def forbidden_message(msg: str = ""):
    """无权限消息响应"""
    return message(code=HttpCode.FORBIDDEN, msg=msg)