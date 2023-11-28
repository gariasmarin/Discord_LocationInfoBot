import pickle
import pandas as pd

from tokenizers import ByteLevelBPETokenizer
from transformers import BartConfig, BartTokenizerFast, AutoModelForMaskedLM
from transformers import LineByLineTextDataset, DataCollatorForLanguageModeling
from transformers import pipeline, Trainer, TrainingArguments

train = pd.read_pickle("Wikipedia-Abstracts/wikipedia_abstracts.pkl")

print(train.features)