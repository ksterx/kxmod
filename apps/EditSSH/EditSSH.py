from pathlib import Path

import PySimpleGUI as sg


def config_to_dict(config: str):
    conf_dict = {}
    conn = -1
    for line in config.splitlines():
        line = line.split(" ")
        if line == [""]:
            continue
        key, value = line[0], line[1]
        if key == "Host":
            conn += 1
        conf_dict[conn] = {**conf_dict.get(conn, {}), **{key: value}}
    return conf_dict


def set_layout(conf_dict: dict):
    font = ("Arial", 14)
    layout = []

    for conn, kv in conf_dict.items():
        for key, value in kv.items():
            if key == "Host":
                layout.append([sg.Text(f"Connection #{conn:02d}", font=("Times New Roman", 16))])
                layout.append([sg.Text("Host", font=font), sg.Input(value, font=font)])
                subkeys = []
                subvalues = []
            else:
                if value in ["yes", "no"]:
                    user_input = sg.Checkbox("", default=(value == "yes"), font=font)
                    subkeys.append([sg.Text(key, font=font)])
                    subvalues.append([user_input])
                else:
                    user_input = sg.Input(default_text=value, font=font)
                    subkeys.append([sg.Text(key, font=font)])
                    subvalues.append([user_input])
        layout.append([sg.Column(subkeys), sg.Column(subvalues)])
    layout.append([sg.OK(font=font), sg.Cancel(font=font)])
    return layout


def main():
    file_path = Path.home() / ".ssh/config"
    with open(file_path, "r") as f:
        config = f.read()

    sg.theme("NeutralBlue")

    conf_dict = config_to_dict(config)
    layout = set_layout(conf_dict)
    window = sg.Window("SSH Config", layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        elif event == "OK":
            config = ""
            conn_count = 0
            for key, value in zip(flatten_dict_keys(conf_dict), values.values()):
                if key == "Host":
                    if conn_count > 0:
                        config += "\n"
                    conn_count += 1
                if value is True:
                    value = "yes"
                elif value is False:
                    value = "no"
                config += f"{key} {value}\n"
            with open(file_path, "w") as f:
                f.write(config)
            break


def flatten_dict_keys(d):
    """{a: {b: c, d: e}, f: {g: h}} -> [b, d, g]

    Args:
        d (dict): dict to flatten
    """
    flattened = []
    for v in d.values():
        for k in v.keys():
            flattened.append(k)
    return flattened


if __name__ == "__main__":
    main()
