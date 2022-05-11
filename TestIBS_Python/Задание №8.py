with open('C:/Users/User/PycharmProjects/selenium_autotest_1/ibs.txt', 'r', encoding='utf-8') as f:
    str = f.read()
    print(str)
with open('C:/Users/User/PycharmProjects/selenium_autotest_1/newibs.txt', 'w', encoding='utf-8') as newf:
    newf.writelines(str[::-1])
with open('C:/Users/User/PycharmProjects/selenium_autotest_1/newibs.txt', 'r', encoding='utf-8') as newf:
    print(newf.read())