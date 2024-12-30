from deepgram import DeepgramClient, PrerecordedOptions
import os
import json
from dotenv import load_dotenv, find_dotenv
load_dotenv()

DEEPGRAM_API_KEY = os.environ["DEP_KEY"] = os.getenv('DEP_KEY')


# Replace with your file path
PATH_TO_FILE = 'testing_english1.M4A'

def main():
    deepgram = DeepgramClient(DEEPGRAM_API_KEY)

    with open(PATH_TO_FILE, 'rb') as buffer_data:
        payload = { 'buffer': buffer_data }

        options = PrerecordedOptions(
            smart_format=True, model="nova-2", language="en-US", diarize=True
        )

        response = deepgram.listen.prerecorded.v('1').transcribe_file(payload, options)
        #print(response['results']['channels'][0]['alternatives'][0]['transcript'])
        print(response.to_json(indent=4))
     

    # with open("output.txt", "w") as file:
    #     json.dump(response.to_json(indent=4), file)

if __name__ == '__main__':
    main()