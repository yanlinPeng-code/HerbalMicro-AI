from dataclasses import dataclass

from injector import inject

from pkg import success_message
from pkg.response import success_json

@inject
@dataclass
class AppHandler:

     async def debug(self):
           return success_message("app" )