from typing import  Dict, List, Any
#import torch
#from transformers_supporter.models.embedded_rnn.modeling_embedded_rnn import EmbeddedRnnForSequenceClassification
#from transformers_supporter.models.embedded_rnn.feature_extraction_embedded_rnn import TorchtextFeatureExtractor
#from transformers import pipeline
#import transformers_supporter
#transformers_supporter.register()
from rest_api_supporter.utils.base64_decode_image import base64_decode_image
from rest_api_supporter.utils.base64_decode_audio import base64_decode_audio
from rest_api_supporter.utils.base64_decode_video import base64_decode_video
from rest_api_supporter.utils.base64_encode_image import base64_encode_image
from rest_api_supporter.utils.base64_encode_audio import base64_encode_audio
from rest_api_supporter.utils.base64_encode_video import base64_encode_video
from dotenv import load_dotenv
import os
import logging

load_dotenv()
#base_directory = os.path.dirname(__file__)
#load_dotenv(os.path.join(base_directory, '.env'))

#device = "cpu"
#if torch.cuda.is_available():
#    device = "cuda"
#elif torch.backends.mps.is_available():
#    device = "mps"

class EndpointHandler():
    def __init__(self, model_path="", use_base64=True):
        self.model_path = model_path
        self.use_base64 = use_base64
        #model = EmbeddedRnnForSequenceClassification.from_pretrained(model_path, use_auth_token=os.environ['HUGGINGFACE_API_KEY'])
        #feature_extractor = TorchtextFeatureExtractor.from_pretrained(model_path, use_auth_token=os.environ['HUGGINGFACE_API_KEY'])
        #self.pl = pipeline('text-classification', model=model, tokenizer=feature_extractor, device=device)
        
    def __call__(self, data: Any) -> List[List[Dict[str, float]]]:
        inputs = data.pop("inputs", data)
        parameters = data.pop("parameters", None)
        #logging.info(inputs) #
        if self.use_base64:
            pass

        if parameters is not None:
            #prediction = self.pl(inputs, **parameters)
            prediction = [{'label': 'pos', 'score': 0.8038843274116516}]
        else:
            #prediction = self.pl(inputs)
            prediction = [{'label': 'pos', 'score': 0.8038843274116516}]
        '''
        from PIL import Image
        image = Image.open('rock.jpg')
        #image = image.convert('RGB') #'L': greyscale, '1': 이진화, 'RGB' , 'RGBA', 'CMYK' #색상 모드 변경
        prediction[0]["outputs"] = image
        '''
        '''
        import datasets
        path = 'up.wav'
        dataset = datasets.Dataset.from_dict({"audio": [path]})
        dataset = dataset.cast_column("audio", datasets.Audio(sampling_rate=16_000)) #https://huggingface.co/blog/audio-datasets#1-resampling-the-audio-data
        array = dataset[0]["audio"]["array"] #numpy array
        #sampling_rate = dataset[0]["audio"]["sampling_rate"] #Wav2Vec2FeatureExtractor was trained using a sampling rate of 16000. Please make sure that the provided `raw_speech` input was sampled with 16000 and not 8000.
        sampling_rate = 16000
        prediction[0]["outputs"] = array 
        '''
        
        if self.use_base64:
            pass
        return prediction

if __name__ == "__main__":
    #model_path = '/Users/automatethem/models/naver-movie-review-text-classification-model-transformers-custom-supporter'
    model_path = 'automatethem-back-model/naver-movie-review-text-classification-model-transformers-custom-supporter'
    endpoint_handler = EndpointHandler(model_path, use_base64=False)
    inputs = {
        "inputs": "This is a good movie!"
    }
    prediction = endpoint_handler(inputs)
    print(prediction) #[{'label': 'pos', 'score': 0.8038843274116516}]
