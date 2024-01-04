import pyowm
import sys

from PyQt5 import QtWidgets

from myform import Ui_Dialog


app = QtWidgets.QApplication([])

Dialog = QtWidgets.QDialog()
application = Ui_Dialog()
application.setupUi(Dialog)
Dialog.show()


def get_weather_city():
    owm = pyowm.OWM('4cd8ee9fc362f21b6e68a92b15d09a26')
    city = application.lineEdit.text()

    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    status = w.detailed_status
    temperature = w.temperature('celsius')['temp']
    wind_speed = w.wind()['speed']
    wind_deg = w.wind()['deg']

    application.label.setText(f'Погода: {status}\nТемпература: {temperature}\nВетер: {wind_deg}, \nскоростью {wind_speed}')


application.pushButton.clicked.connect(get_weather_city)

sys.exit(app.exec())