import time
from naoqi import ALProxy

def intro(preg,answers):
    tts.say(archtest[preg])
    answers.append("-1")
    time.sleep(1)
    nextQuestion(preg,answers)

def askQuestion(preg,answers):

    tts.say(archtest[preg])

    asr.subscribe("ocean")
    time.sleep(5)
    asr.unsubscribe("ocean")
    data = memory.getData("WordRecognized")
    print(data)
    answers.append(data[0])
    nextQuestion(preg,answers)

def nextQuestion(preg,answers):
    preg+=1
    if preg<=5:
        askQuestion(preg,answers)
    else:
        tts.say("Gracias por responder a estas preguntas")
        calcOCEAN(answers)

def calcOCEAN(answers):
    Answers = []
    for i in answers:
        if i==-1:
            Answers.append(-1)
        elif i=="uno":
            Answers.append(1)
        elif i=="dos":
            Answers.append(2)
        elif i=="tres":
            Answers.append(3)
        elif i=="cuatro":
            Answers.append(4)
        else:
            Answers.append(5)
    oceanValue = calcOCEANValue(Answers)
    return oceanValue

def calcOCEANValue(Answer):
    E = 20+Answer[1]
    A = 14-Answer[2]

    C = 14+Answer[3]

    N = 38-Answer[4]

    O = 8+Answer[5]

    return E,A,C,N,O



def main():
    #Init variables globales
    preg = 0
    answers = []
    IP = "192.168.1.9"

    #Creacion proxies con Modulos NaoQi necesarios
    #ALTextToSpeech, ALSpeechRecognition, #ALMemory
    try:
        global tts
        tts = ALProxy("ALTextToSpeech",IP , 9559)
    except Exception, e:
        print "Error: x",e
    try:
        global asr
        asr = ALProxy("ALSpeechRecognition",IP,9559)
    except Exception, e:
        print "Error: ",e
    try:
        global memory
        memory = ALProxy("ALMemory",IP, 9559)
    except Exception, e:
        print "Error: ",e

    #Set idioma en que habla NAO
    tts.setLanguage("Spanish")
    tts.setVolume(0.3)
    #Vocabulario a reconocer
    vocabulary = ["uno","dos","tres","cuatro","cinco"]
    #Pausa del sistema de reconocimiento de voz para configuracion
    asr.pause(True)
    asr.setLanguage("Spanish")
    asr.setVocabulary(vocabulary,False)
    asr.pause(False)
    #Lectura fichero preguntas Test Ocean
    global archtest
    archtest = open("OceanEspanol.txt").read().split(".")
    intro(preg,answers)

    o = calcOCEAN(answers)
    return o
