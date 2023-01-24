from kxmod.service import SlackBot


class TestSlackBot:
    def test_say(self):
        bot = SlackBot()
        bot.say("test `say` method")

    def test_show(self):
        bot = SlackBot()
        bot.show("test `show` method", "tests/building.JPG")
