import os

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
import io
import azure.cognitiveservices.speech as speechsdk
from django.conf import settings
from django.templatetags.static import static
import os
from pydub import AudioSegment
from pydub.playback import play
import requests
from django.http import HttpResponse
import json
# Create your views here.
@csrf_exempt
def get_voice(request):
    return JsonResponse({"sdfsd":'dfgdfgdfg'})

def play_audio_from_bytes(audio_data,format='wave'):
    audio_Data_io = io.BytesIO(audio_data)
    audio_Segment = AudioSegment.from_file(audio_Data_io)
    play(audio_Segment)
@csrf_exempt
def my_api_view(request):
    if request.method == "POST":  # or 'GET'
        if request.method == "POST":  # or 'GET'
            subscription_key = "AsTBxRq7eULibLmiAAyfkZZyBuTLv2bZmnYK5QICODwsXdCWsCg0JQQJ99BBACHYHv6XJ3w3AAAYACOGrXnx"
            region = "eastus2"

            voice = "ka-GE-EkaNeural"
            data = json.loads(request.body)  # Parse incoming JSON data
            text = data.get('text', None)  # Get the text parameter

            headers = {
                "Ocp-Apim-Subscription-Key": subscription_key,
                "Content-Type": "application/ssml+xml",
                "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
            }

            # Create the SSML request with the correct language
            body = f"""
            <speak version='1.0' xml:lang='ka-GE'>
                <voice xml:lang='ka-GE' xml:gender='Female' name='{voice}'>
                    <prosody rate="+50%">
                        {text}
                    </prosody>
                </voice>
            </speak>"""

            # Send POST request to Azure TTS API
            url = f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"
            response = requests.post(url, headers=headers, data=body)

            # Check if request was successful
            if response.status_code == 200:
                # Send the audio data as a response for download
                audio_data = response.content
                response = HttpResponse(audio_data, content_type="audio/wav")
                response["Content-Disposition"] = 'attachment; filename="output1.wav"'
                return response
            else:
                # Print error details if the request fails
                print(f"Error: {response.status_code}, {response.text}")
                return HttpResponse("Failed to generate speech", status=500)


