import speech_recognition as sr
import os

global GLOBAL_TEMPLATE_STOP
GLOBAL_TEMPLATE_STOP = "\nreturn 0;\n}"


global GLOBAL_TEMPLATE_START
GLOBAL_TEMPLATE_START = "#include<bits/stdc++.h>\nusing namespace std\nint main()\n{\n"
outfile_start = open("v_output.txt",'a')
outfile_start.write(GLOBAL_TEMPLATE_START)
outfile_start.close()

while 1:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if text == "stop":
                break
            print("You said : {}".format(text))
            file = open("v_input.txt",'a')
            file.write(text)
            file.write("\n")
            file.close()
            os.startfile("logic_start.bat")   
        except:
            print("Sorry could not recognize what you said")
file1 = open("v_input.txt",'w')  
file1.close()
outfile_stop = open("v_output.txt",'a')
outfile_stop.write(GLOBAL_TEMPLATE_STOP)
outfile_stop.close()