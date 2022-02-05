import os, random
import pyAesCrypt as crypt
import simplejson as json


class PassGen:
    def __init__(self, cwd) -> None:
        self.cwd = cwd

    def check_file(self):
        pass_file = f"{self.cwd}/passwords.json"
        if not os.path.exists(f"{self.cwd}/passwords.json"):
            with open(pass_file, "w+") as file:
                data = {}
                json.dumps(file.write(data))
    