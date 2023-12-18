from PyQt5.QtCore import QPoint, Qt, QTime, QTimer
from PyQt5.QtGui import QColor, QPainter, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget
class AnalogClock(QWidget):
    secondHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -95)
    ])
    hourHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -50)
    ])
    minuteHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -70)
    ])
    hourColor = QColor(127, 0, 127)
    minuteColor = QColor(0, 100, 250, 200)
    secondColor = QColor(195, 0, 0, 150)
    def __init__(self, parent=None):
        super(AnalogClock, self).__init__(parent)
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        self.setWindowTitle("Analog Clock")
        self.resize(600, 600)
    def paintEvent(self, event):
        side = min(self.width(), self.height())
        time = QTime.currentTime()
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200, side / 200)
        painter.setPen(Qt.NoPen)
        painter.setBrush(AnalogClock.hourColor)
        painter.save()
        painter.rotate(30.0 * (time.hour() + time.minute() / 60.0)) # 360/12.0 times per hour
        print(f'hour:{time.hour()}, minute:{time.minute()}, second:{time.second()}')
        painter.drawConvexPolygon(AnalogClock.hourHand)
        painter.restore()
        painter.setPen(AnalogClock.hourColor)
        for i in range(12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)
        painter.setPen(Qt.NoPen)
        painter.setBrush(AnalogClock.minuteColor)
        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))  # 6 times a minute
        painter.drawConvexPolygon(AnalogClock.minuteHand)
        painter.restore()
        painter.setPen(AnalogClock.minuteColor)
        for j in range(60):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)
        painter.setPen(Qt.NoPen)
        painter.setBrush(AnalogClock.secondColor)
        painter.save()
        painter.rotate(360 * (time.minute() + time.second() / 60.0))  # 360 times in a minute
        painter.drawConvexPolygon(AnalogClock.secondHand)
        painter.restore()
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    clock = AnalogClock()
    clock.show()
    sys.exit(app.exec_())