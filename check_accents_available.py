import pyttsx3

if __name__ == '__main__':
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	for voice in voices:
		print(str(voice))
		