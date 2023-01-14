from transformers import pipeline
import torch

import torch
from transformers import pipeline

speech_recognizer = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")

print(classifier("I am going to smack you."))