import urllib.parse
import webbrowser

import pyperclip

text = pyperclip.paste()
alt_text_dict = {
    "-\r": "",
    "-\n": "",
    "- ": "",
    "\r": "",
    "\n": "",
}

for key in alt_text_dict.keys():
    text = text.replace(key, alt_text_dict[key])
pyperclip.copy(text)


encoded_text = (
    urllib.parse.quote(text, safe="|/")
    .replace("|", "%5C%7C")
    .replace("/", "%5C%2F")
    .replace("-%0D%0A", "")
    .replace(".%0D%0A", "DUMMY1")
    .replace("%0D%0A", "%20")
    .replace("DUMMY1", ".%0D%0A%0D%0A")
)

webbrowser.open("https://www.deepl.com/en/translator#en/ja/" + encoded_text)
