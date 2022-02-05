import os, random, string
import pyAesCrypt as crypt
import simplejson as json


class PassGen:
    def __init__(self, cwd) -> None:
        self.cwd = cwd
        self.pass_file = f"{self.cwd}/passwords.json"

    def check_file(self):
        if not os.path.exists(self.pass_file):
            with open(self.pass_file, "w+") as file:
                data = {}
                json.dumps(file.write(data))

    def create_password(self):
        spl_chars = "!#$%&()*+,-./:;?@[]^_`~"
        kwd = str(input("Enter a keyword for the password > ")).lower()+"@"
        password = "".join(random.choice(string.ascii_letters + string.digits + spl_chars, k=32))
        return kwd+password
    

def main():
    passgen = PassGen(
        cwd = os.getcwd()
    )
    passgen.check_file()
    
if __name__ == "__main__":
    main()
