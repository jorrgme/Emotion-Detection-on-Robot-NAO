########### Python 2.7 #############
import httplib, urllib, base64, ast, time, json

headers = {
    # Usage of octet-stream to allow the image to come from a file and not a URL
    'Content-type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '721d2ad21d4a4106bd80185d091f982a ',
}

params = urllib.urlencode({
})


def detEmotion(image):
    f = open(image, "rb")
    body = f.read()

    try:
        i = time.time()
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse("")
        data = response.read()

        conn.close()

        response = json.loads(data)
        scores = response[0]['scores']
        anger = scores['anger']
        contempt = scores['contempt']
        disgust = scores['disgust']
        fear = scores['fear']
        happiness = scores['happiness']
        neutral = scores['neutral']
        sadness = scores['sadness']
        surprise = scores['surprise']

        emotion_names = ["Anger", "Contempt", "Disgust", "Fear", "Happiness", "Neutral", "Sadness", "Surprise"]
        emotion_scores = [anger, contempt, disgust, fear, happiness, neutral, sadness, surprise]

        f = time.time()

        print(f-i)

        return emotion_names, emotion_scores

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    ####################################
