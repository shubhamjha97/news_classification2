from nltk.tokenize import word_tokenize
from os import listdir
import os
import database_ops
from file_loader import load_files
from tqdm import tqdm

loc="/home/shubham/PycharmProjects/news_classifier/training_set/"
loc_bow="/home/shubham/PycharmProjects/news_classifier/bag_of_words/"
cat_str=['sport', 'business', 'tech', 'entertainment', 'politics']

load_files(loc, cat_str)
