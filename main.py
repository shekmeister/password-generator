import os, random, string
import simplejson as json
from tabulate import tabulate


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
        spl_chars = "!#$%&*+-./:;?@^_~"
        kwd = str(input("Enter a keyword for the password > ")).lower()+"@"
        password = "".join(random.choices(string.ascii_letters + string.digits + spl_chars, k=16))
        return kwd+password

    def write_to_file(self, app, password):
        with open(self.pass_file, "r+") as file:
            data = json.load(file)
            data[app] = password
            file.seek(0)
            json.dump(data, file)

    def show_passwords(self):
        with open(self.pass_file, "r+") as file:
            data = json.load(file)
            kvp = data.items()
            print(tabulate(kvp, headers=["App", "Password"], showindex="always", tablefmt="rst"))
        
    def delete_password(self, app_name):
        with open(self.pass_file, "r+") as file:
            data = json.load(file)
            data.pop(app_name)
        
        with open(self.pass_file, "w+") as file:
            json.dump(data, file)

def main():
    passgen = PassGen(
        cwd=os.getcwd()
    )
    while True:
        print("""
\nChoose action:
1 - Generate new password.
2 - View passwords.
3 - Delete password.
4 - Exit.
""")
        ans1 = str(input("> "))
        if ans1 == "1":
            app = str(input("\nEnter the app password is going to be used for > "))
            while True:
                password = passgen.create_password()
                ans2 = str(input((f"\nYour password: {password}\nAre you satisfied with this password? (y/n) > "))).lower()
                if ans2 == "y":
                    passgen.write_to_file(app, password)
                    print("\nPassword has been saved.")
                    break
                elif ans2 == "n":
                    continue
                else:
                    print("\nInvalid input.")
                    break
            
        elif ans1 == "2":
            passgen.show_passwords()
            cont = str(input("\nDo you wish to continue? (y/n) > ")).lower()
            if cont == "y":
                continue
            elif cont == "n":
                print("\nOperation complete.\nTerminating Program...")
                break
            else:
                print("\nInvalid input.\nTerminating program...")
                break
        
        elif ans1 == "3":
            passgen.show_passwords()
            app_name = str(input("Enter the app name associated with the password you wish to delete > "))
            passgen.delete_password(app_name=app_name)
            cont = str(input("\nDo you wish to continue? (y/n) > ")).lower()
            if cont == "y":
                continue
            elif cont == "n":
                print("\nOperation complete.\nTerminating Program...")
                break
            else:
                print("\nInvalid input.\nTerminating program...")
                break

        elif ans1 == "3":
            print("Terminating process...")
            break
        else:
            print("Invalid input.")
            continue
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Terminating session.")
