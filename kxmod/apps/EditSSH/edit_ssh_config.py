from pathlib import Path

import PySimpleGUI as sg


def config_to_dict(config: str):
    conf_dict = {}
    conn = -1
    for line in config.splitlines():
        line = line.split(" ", maxsplit=1)
        if line == [""]:
            continue
        key, value = line[0], line[1]
        if key == "Host":
            conn += 1
        if line[0] and line[1]:
            conf_dict[conn] = {**conf_dict.get(conn, {}), **{key: value}}
    return conf_dict


def set_layout(conf_dict: dict):
    FONT = ("Arial", 14)
    layout = []

    for conn, kv in conf_dict.items():
        for key, value in kv.items():
            if key == "Host":
                layout.append(
                    [sg.Text(f"Connection #{conn:02d}", font=("Times New Roman", 20))]
                )
                layout.append([sg.Text("Host", font=FONT), sg.Input(value, font=FONT)])
                subkeys = []
                subvalues = []
            else:
                if value in ["yes", "no"]:
                    user_input = sg.Checkbox("", default=(value == "yes"), font=FONT)
                    subkeys.append([sg.Text(key, font=FONT)])
                    subvalues.append([user_input])
                elif not value:
                    continue
                else:
                    user_input = sg.Input(default_text=value, font=FONT)
                    subkeys.append([sg.Text(key, font=FONT)])
                    subvalues.append([user_input])
        layout.append([sg.Column(subkeys), sg.Column(subvalues)])

    return [
        [
            sg.Column(
                layout, scrollable=True, vertical_scroll_only=True, size=(600, 400)
            ),
            [sg.OK(font=FONT), sg.Cancel(font=FONT)],
        ]
    ]


def write_config(conf_dict: dict, values: dict, file_path: str):
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
            write_config(conf_dict, values, file_path)
            break


def flatten_dict_keys(d):
    """{a: {b: c, d: e}, f: {g: h}} -> [b, d, g]

    Args:
        d (dict): dict to flatten
    """
    flattened = []
    for kv in d.values():
        for k in kv.keys():
            flattened.append(k)
    return flattened


if __name__ == "__main__":
    main()
