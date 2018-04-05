import time
from naoqi import ALProxy

def intro(preg,answers):
    tts.say(archtest[preg])
    answers.append("-1")
    time.sleep(3)
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
    if preg<=50:
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
    E = 20+Answer[1]-Answer[6]+Answer[11]-Answer[16]+Answer[21]-Answer[26]+Answer[31]-Answer[36]+Answer[41]-Answer[46]

    A = 14-Answer[2]+Answer[7]-Answer[12]+Answer[17]-Answer[22]+Answer[27]-Answer[32]+Answer[37]+Answer[42]+Answer[47]

    C = 14+Answer[3]-Answer[8]+Answer[13]-Answer[18]+Answer[23]-Answer[28]+Answer[33]-Answer[38]+Answer[43]+Answer[48]

    N = 38-Answer[4]+Answer[9]-Answer[14]+Answer[19]-Answer[24]-Answer[29]-Answer[34]-Answer[39]-Answer[44]-Answer[49]

    O = 8+Answer[5]-Answer[10]+Answer[15]-Answer[20]+Answer[25]-Answer[30]+Answer[35]+Answer[40]+Answer[45]+Answer[50]

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
    tts.setVolume(0.5)
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
