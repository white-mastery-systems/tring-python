"""
Tring TTS grpc client
"""

import grpc
try:
    from tts_stream_pb2 import TTSRequest
    from tts_stream_pb2_grpc import TTSServiceStub
except ImportError:
    from .tts_stream_pb2 import TTSRequest
    from .tts_stream_pb2_grpc import TTSServiceStub

from scipy.io import wavfile

import numpy

SAMPLE_RATE = 44100
QUALITY_MAP = {'PCM_16': ('h', numpy.int16), 'PCM_32': ('i', numpy.int32), 'PCM_float32': ('f', numpy.float32)}

def generate(text:str, speaker:str, speed:float=1.0, save_path:str='', format:str='PCM_16', pad_silence:int=0):
    """
    Generate TTS using tring tts grpc api

    Args:
        text (str): The text to be converted into speech.
        speaker (str): The speaker to use for TTS.
        speed (float, optional): The speed at which the text should be spoken. Default is 1.0.
        save_path (str, optional): The path to save the generated audio file. Default is an empty string, meaning no file is saved.
        format (str, optional): Bits per sample of the audio. Default is 'PCM_16'. Use PCM_float32 if you need professional qualoty audio.
        pad_silence (int, optional): The amount of silence (in milliseconds) to pad at the beginning and end of the audio. Default is 0.

    Returns:
        numpy.ndarray: The generated audio data as a numpy array.
    """
    with grpc.insecure_channel('127.0.0.1:5005') as channel:

        quality, dtype = QUALITY_MAP[format]

        stub = TTSServiceStub(channel)

        responses = stub.GenerateTTS(TTSRequest(
            text=text,
            speaker=speaker,
            speed=speed,
            quality=quality))

        audio = numpy.frombuffer(responses.speech_audio, dtype=dtype)

        if pad_silence:
            silence = numpy.zeros(int((pad_silence / 1000) * SAMPLE_RATE), dtype=dtype)
            audio = numpy.concatenate([silence, audio, silence])

        if save_path:
            wavfile.write(save_path, SAMPLE_RATE, audio)

        return audio

