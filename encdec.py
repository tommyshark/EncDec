import sys, os
import base64
import urllib.parse
import binascii
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import *

import design

version = '0.1.6'

class EncDec(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setFixedSize(774, 330)
		self.combo = self.comboBox
		self.label_5.setText("Version " + version)
		self.plainTextEdit.setPlaceholderText("Encrypt")
		self.plainTextEdit_2.setPlaceholderText("Decrypt")
		self.btnEncrypt.clicked.connect(self.encryptText)
		self.btnDecrypt.clicked.connect(self.decryptText)
		self.btnClear.clicked.connect(self.Clear)
		self.combo.activated[str].connect(self.onActivated)
		self.method = ""
		
	def onActivated(self, text):
		self.method = text
	
	def encryptText(self):
		try:
			if self.method == "Base64":
				self.textToEncrypt = self.plainTextEdit.toPlainText()
				self.text_bytes = self.textToEncrypt.encode('ascii')
				self.base64_bytes = base64.b64encode(self.text_bytes)
				self.base64_text = self.base64_bytes.decode('ascii')
				self.plainTextEdit_2.setPlainText(self.base64_text)
			elif self.method == "Base32":
				self.textToEncrypt = self.plainTextEdit.toPlainText()
				self.text_bytes = self.textToEncrypt.encode('ascii')
				self.base32_bytes = base64.b32encode(self.text_bytes)
				self.base32_text = self.base32_bytes.decode('ascii')
				self.plainTextEdit_2.setPlainText(self.base32_text)
			elif self.method == "Base16":
				self.textToEncrypt = self.plainTextEdit.toPlainText()
				self.text_bytes = self.textToEncrypt.encode('ascii')
				self.base16_bytes = base64.b16encode(self.text_bytes)
				self.base16_text = self.base16_bytes.decode('ascii')
				self.plainTextEdit_2.setPlainText(self.base16_text)
			elif self.method == "Base85":
				self.textToEncrypt = self.plainTextEdit.toPlainText()
				self.text_bytes = self.textToEncrypt.encode('ascii')
				self.base85_bytes = base64.b85encode(self.text_bytes)
				self.base85_text = self.base85_bytes.decode('ascii')
				self.plainTextEdit_2.setPlainText(self.base85_text)
			elif self.method == "URL":
				self.textToEncrypt = self.plainTextEdit.toPlainText()
				self.encryptedText = self.urlencode(self.textToEncrypt)
				self.plainTextEdit_2.setPlainText(self.encryptedText)
			elif self.method == "Reverser":
				self.textToReverse = self.plainTextEdit.toPlainText()
				self.reversedText = self.textToReverse[::-1]
				self.plainTextEdit_2.setPlainText(self.reversedText)
			elif self.method == "Hex":
				self.textToEncrypt = self.plainTextEdit.toPlainText()
				self.text_bytes = self.textToEncrypt.encode('ascii')
				self.encryptedText = binascii.hexlify(self.text_bytes)
				self.bytes_text = self.encryptedText.decode('ascii')
				self.plainTextEdit_2.setPlainText(self.bytes_text)
			elif self.method == "Binary":
				self.textToEncrypt = self.plainTextEdit.toPlainText()
				self.encryptedText = ''.join(format(ord(i), '08b') for i in self.textToEncrypt)
				self.plainTextEdit_2.setPlainText(self.encryptedText)
			elif self.method == "Caesar":
				textToEncrypt = self.plainTextEdit.toPlainText()
				LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
				key = 13
				textToEncrypt = textToEncrypt.upper()
				translated = ''
				for symbol in textToEncrypt:
					if symbol in LETTERS:
						num = LETTERS.find(symbol)
						num = num + key
						if num >= len(LETTERS):
							num = num - len(LETTERS)
						elif num < 0:
							num = num + len(LETTERS)
						translated = translated + LETTERS[num]
						
					else:
						translated = translated + symbol
				self.plainTextEdit_2.setPlainText(translated)
				
		except Exception:
			pass
	
	
	def BinaryToDecimal(self, binary):
         
		string = int(binary, 2)
      
		return string
	
	def decryptText(self):
		try:
			if self.method == "Base64":
				self.textToDecrypt = self.plainTextEdit_2.toPlainText()
				self.text_bytes2 = self.textToDecrypt.encode('ascii')
				self.base64_bytes2 = base64.b64decode(self.text_bytes2)
				self.base64_text2 = self.base64_bytes2.decode('ascii')
				self.plainTextEdit.setPlainText(self.base64_text2)
			elif self.method == "Base32":
				self.textToDecrypt = self.plainTextEdit_2.toPlainText()
				self.text_bytes2 = self.textToDecrypt.encode('ascii')
				self.base32_bytes2 = base64.b32decode(self.text_bytes2)
				self.base32_text2 = self.base32_bytes2.decode('ascii')
				self.plainTextEdit.setPlainText(self.base32_text2)
			elif self.method == "Base16":
				self.textToDecrypt = self.plainTextEdit_2.toPlainText()
				self.text_bytes2 = self.textToDecrypt.encode('ascii')
				self.base16_bytes2 = base64.b16decode(self.text_bytes2)
				self.base16_text2 = self.base16_bytes2.decode('ascii')
				self.plainTextEdit.setPlainText(self.base16_text2)
			elif self.method == "Base85":
				self.textToDecrypt = self.plainTextEdit_2.toPlainText()
				self.text_bytes2 = self.textToDecrypt.encode('ascii')
				self.base85_bytes2 = base64.b85decode(self.text_bytes2)
				self.base85_text2 = self.base85_bytes2.decode('ascii')
				self.plainTextEdit.setPlainText(self.base85_text2)
			elif self.method == "URL":
				self.textToDecrypt = self.plainTextEdit_2.toPlainText()
				self.decryptedText = self.urldecode(self.textToDecrypt)
				self.plainTextEdit.setPlainText(self.decryptedText)
			elif self.method == "Reverse":
				self.textToReverse = self.plainTextEdit_2.toPlainText()
				self.reversedText = self.textToReverse[::-1]
				self.plainTextEdit.setPlainText(self.reversedText)
			elif self.method == "Hex":
				self.textToDecrypt = self.plainTextEdit_2.toPlainText()
				self.text_bytes = self.textToDecrypt.encode('ascii')
				self.decryptedText = binascii.unhexlify(self.text_bytes)
				self.bytes_text = self.decryptedText.decode('ascii')
				self.plainTextEdit.setPlainText(self.bytes_text)
			elif self.method == "Binary":
				binary_int = int(self.plainTextEdit_2.toPlainText(), 2)
				byte_number = binary_int.bit_length() + 7 // 8
				binary_array = binary_int.to_bytes(byte_number, "big")
				ascii_text = binary_array.decode()
				self.plainTextEdit.setPlainText(ascii_text)
				print(ascii_text)
			elif self.method == "Caesar":
				textToDecrypt = self.plainTextEdit_2.toPlainText()
				LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
				key = 13
				textToDecrypt = textToDecrypt.upper()
				translated = ''
				for symbol in textToDecrypt:
					if symbol in LETTERS:
						num = LETTERS.find(symbol)
						num = num - key
						if num >= len(LETTERS):
							num = num - len(LETTERS)
						elif num < 0:
							num = num + len(LETTERS)
						translated = translated + LETTERS[num]
						
					else:
						translated = translated + symbol
				self.plainTextEdit.setPlainText(translated)

				
		except Exception:
			pass
			
	def urlencode(self, t):
		return urllib.parse.quote(t)
		
	def urldecode(self, t):
		return urllib.parse.unquote(t)
		
	def Clear(self):
		self.plainTextEdit_2.clear()
		self.plainTextEdit.clear()

def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle("Fusion")

	dark_palette = QPalette()

	dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
	dark_palette.setColor(QPalette.WindowText, Qt.white)
	dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
	dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
	dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
	dark_palette.setColor(QPalette.ToolTipText, Qt.white)
	dark_palette.setColor(QPalette.Text, Qt.white)
	dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
	dark_palette.setColor(QPalette.ButtonText, Qt.white)
	dark_palette.setColor(QPalette.BrightText, Qt.red)
	dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
	dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
	dark_palette.setColor(QPalette.HighlightedText, Qt.black)

	app.setPalette(dark_palette)

	app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
	window = EncDec()
	window.show()
	app.exec_()



if __name__ == '__main__':
	main()
