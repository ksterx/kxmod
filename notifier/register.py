import os

if __name__ == "__main__":
    app = input("Messanger (LINE: l/ slack: s): ")

    if app == "l":
        print("You have selected LINE.")
        line_token = input("TOKEN: ")
    filename = "credentials.yaml"

    if not os.path.isfile(filename):
        with open(filename, mode="w") as f:
            f.write({})

    with open("credential.yaml", mode="x") as f:
        f["SLACK_WEBHOOK_URL"]
