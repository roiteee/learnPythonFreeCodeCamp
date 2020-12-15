from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_chicken()

myChineseChef = ChineseChef()
myChineseChef.make_chicken() #myChinese chef inherits make_chicken() from Chef class
myChineseChef.make_special_dish() #overrides method from Chef

