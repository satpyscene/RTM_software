import sys
import math
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QLineEdit, QGraphicsView, QGraphicsScene
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor,QBrush

class RadiationViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口基本属性
        self.setWindowTitle('大气辐射位置示意图')
        self.setGeometry(100, 100, 800, 600)

        # 中心小部件和布局
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 滑块区域
        slider_layout = QHBoxLayout()
        layout.addLayout(slider_layout)

        # 探测器高度
        self.detector_slider = QSlider(Qt.Horizontal)
        self.detector_slider.setMinimum(40)
        self.detector_slider.setMaximum(900)
        self.detector_slider.setValue(900)
        self.detector_slider.valueChanged.connect(self.update_scene_from_slider)
        self.detector_input = QLineEdit("900")
        self.detector_input.textChanged.connect(self.update_scene_from_input)
        slider_layout.addWidget(QLabel('探测器高度'))
        slider_layout.addWidget(self.detector_slider)
        slider_layout.addWidget(self.detector_input)

        # 目标物高度
        self.target_slider = QSlider(Qt.Horizontal)
        self.target_slider.setMinimum(40)
        self.target_slider.setMaximum(900)
        self.target_slider.setValue(40)
        self.target_slider.valueChanged.connect(self.update_scene_from_slider)
        self.target_input = QLineEdit("40")
        self.target_input.textChanged.connect(self.update_scene_from_input)
        slider_layout.addWidget(QLabel('目标物高度'))
        slider_layout.addWidget(self.target_slider)
        slider_layout.addWidget(self.target_input)

        # 天顶角
        self.angle_slider = QSlider(Qt.Horizontal)
        self.angle_slider.setMinimum(0)
        self.angle_slider.setMaximum(180)
        self.angle_slider.setValue(45)
        self.angle_slider.valueChanged.connect(self.update_scene_from_slider)
        self.geo_lineEdit_angel = QLineEdit("45")
        self.geo_lineEdit_angel.textChanged.connect(self.update_scene_from_input)
        slider_layout.addWidget(QLabel('天顶角'))
        slider_layout.addWidget(self.angle_slider)
        slider_layout.addWidget(self.geo_lineEdit_angel)

        # 图形视图和场景
        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        layout.addWidget(self.view)
        
        self.update_scene()

    def update_scene_from_slider(self):
        self.detector_input.setText(str(self.detector_slider.value()))
        self.target_input.setText(str(self.target_slider.value()))
        self.geo_lineEdit_angel.setText(str(self.angle_slider.value()))
        self.update_scene()

    def update_scene_from_input(self):
        try:
            self.detector_slider.setValue(int(self.detector_input.text()))
            self.target_slider.setValue(int(self.target_input.text()))
            self.angle_slider.setValue(int(self.geo_lineEdit_angel.text()))
            self.update_scene()
        except ValueError:
            pass  # 如果输入不是有效的整数，忽略更新

    def update_scene(self):
        
        detector_height = self.detector_slider.value()
        target_height = self.target_slider.value()
        angle = self.angle_slider.value()

        # 清除现有图形
        self.scene.clear()

        # 计算目标物的位置
        radian = math.radians(angle)
        x = (detector_height -target_height) * math.tan(radian)
        y = target_height - 40
        # 绘制天空
        self.scene.addRect(-500, -900, 1000, 10, QPen(QColor(135, 206, 235)),QBrush(QColor(135, 206, 235)))
        # 绘制地面
        self.scene.addRect(-500, -40, 1000, 10, QPen(QColor(139, 69, 19)),QBrush(QColor(139, 69, 19)))


        # 绘制连接线
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(5)
        self.scene.addLine(0, -detector_height+10, x, -target_height+5, pen)
        # 绘制探测器和目标物
        self.scene.addEllipse(-10, -detector_height, 20, 20, QPen(QColor(255, 0, 0)),QBrush(QColor(255, 0, 0)))
        self.scene.addEllipse(x - 10, -target_height, 20, 20, QPen(QColor(0, 0, 255)),QBrush(QColor(0, 0, 255)))

        # 绘制法线
        self.scene.addLine(x, -40, x, -900, QPen(QColor(0, 0, 0), 1, Qt.DashLine))

        # 更新视图
        self.scene.setSceneRect(-500, -1000, 1000, 1000)
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RadiationViewer()
    ex.show()
    sys.exit(app.exec())
