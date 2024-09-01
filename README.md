# MagooshHelper

A simple application based on words published by Magoosh Vocabulary Flash Cards.
A tool for students who needed to improve their Vocabulary, for Competitive exams.

Users can run check_accents_available.py to check some of the voices/accents available on their platforms.

For example, users using Windows will have different accents available than users at OS X and Ubuntu.

Same applies for any combination. This is because of the driver support for pyttsx library use in this tool is different at this platforms.
Windows have different speech synthesiser driver, OS X have different and Ubuntu have different.

For Windows it is sapi5, for Ubuntu it is espeak and for OS X it is NSSS.

Kindly download the respective drivers for your platforms.

Then you can check the available accents.
Based on your preference, you can change the line voice = get_voice_property() inside speech_utilities.py
