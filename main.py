from ogame_controller import OgameController

print("Loading ogame bot")
ogame_controller = OgameController("C:\\bin\\chromedriver.exe")
print("Logging in")
ogame_controller.login("admin", "1234")
