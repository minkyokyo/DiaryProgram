# DiaryProgram

just for fun~

# 설치 (2022-01-15)

`pip install pyqt5` 로 pyqt5를 설치  
`pip install pyqt5-tools` 으로 설치

# VSCode Extension

- Python
- Python for VSCode
- Python Extension Pack
- PYQT Integration
  extension setting에서 Qtdesigner: Path에 아래 주소 경로 입력
  python설치경로\Lib\site-packages\qt5_applications\Qt\bin\designer.exe

# .ui -> .py 파일로 변환

- python -m PyQt5.uic.pyuic -x untitled.ui -o untitled.py
