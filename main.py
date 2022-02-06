import os, random, string
import pyAesCrypt as crypt
import simplejson as json


class PassGen:
    def __init__(self, cwd) -> None:
        self.cwd = cwd
        self.pass_file = f"{self.cwd}/passwords.json"
        self.check_file()

    def check_file(self):
        if not os.path.exists(self.pass_file):
            with open(self.pass_file, "w+") as file:
                data = {}
                json.dump(data, file)

    def create_password(self):
        spl_chars = "!#$%&()*+,-./:;?@[]^_`~"
        kwd = str(input("Enter a keyword for the password > ")).lower()+"@"
        password = "".join(random.choices(string.ascii_letters + string.digits + spl_chars, k=32))
        return kwd+password

    def write_to_file(self, app, password):
        with open(self.pass_file, "r+") as file:
            data = json.load(file)
            data[app] = password
            file.seek(0)
            json.dump(data, file)
        
    
def main():
    passgen = PassGen(
        cwd=os.getcwd()
    )
    app = str(input("Enter the app password is going to be used for > "))
    while True:
        password = passgen.create_password()
        print(f"Your password: {password}\nAre you satisfied with this password?")
        ans = str(input("y/n? > ")).lower()
        if ans == "y":
            passgen.write_to_file(app, password)
            print("Password has been saved.")
            break
        elif ans == "n":
            continue
        else:
            print("Invalid input")
            continue
    
if __name__ == "__main__":
    main()
