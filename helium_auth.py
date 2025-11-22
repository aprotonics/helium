from helium import *


EMAIL = "aprotonics@yandex.ru"
PASSWORD = "eHD2gxJrQYuTshme"

# Auth

driver = start_chrome('gmail.com')
write(EMAIL, into="Email or phone")
wait_until(Button('Next').exists,timeout_secs = 100)
click(Button('Next'))
wait_until(TextField('Enter your password').exists,timeout_secs = 100)
write(PASSWORD, into="Enter your password")
wait_until(Button('Compose').exists,timeout_secs = 100)
click(Button('Compose'))

kill_browser()
