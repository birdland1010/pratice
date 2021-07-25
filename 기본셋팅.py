import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.preprocessing import StandardScaler,MinMaxScaler



pd.get_dummies(fruit, columns = ['name'])



movie = {'naver': [2, 4, 6, 8, 10],
         'netflix': [1, 2, 3, 4, 5]
         }
movie=pd.DataFrame(movie)
movie_norm=pd.DataFrame()

movie_norm['naver']=movie['naver']/(movie['naver'].max()-movie['naver'].min())
movie_norm['netflix']=movie['netflix']/(movie['netflix'].max()-movie['netflix'].min())


movie_std=pd.DataFrame()
movie_std['naver']=movie['naver'] / movie['naver'].std()
movie_std['netflix']=movie['netflix'] / movie['netflix'].std()
