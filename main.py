from deepgram import Deepgram
import asyncio, json

# Your Deepgram API Key
DEEPGRAM_API_KEY = '2838c28f86321af4889acaff0f5b950255feaed7'

# Name and extension of the file you downloaded (e.g., sample.wav)
PATH_TO_FILE = 'recording1.wav'

async def main():
  # Initialize the Deepgram SDK
  dg_client = Deepgram(DEEPGRAM_API_KEY)
  # Open the audio file
  with open(PATH_TO_FILE, 'rb') as audio:
    # Replace mimetype as appropriate
    source = {'buffer': audio, 'mimetype': 'audio/wav'}
    response = await dg_client.transcription.prerecorded(source, {'punctuate': True})
    print(json.dumps(response, indent=4))

asyncio.run(main())