from cgitb import reset
import pandas as pd
import numpy as np
import sys

def main(recommendTitle):
    result=[]
    cosine_sim = np.load("")
    indices = pd.read_pickle('')
    df = pd.read_csv('', low_memory=False, encoding='utf-8')

    travelList = []
    for i in range(1, len(recommendTitle)):
        travelList.append(int(recommendTitle[i]))
    
    recommendList = []
    cnt = 50//len(travelList)
    for travel in travelList:
        idx = indices[travel]
        sim_scores = cosine_sim[idx]
        sim_scores = list(enumerate(sim_scores))
        # 유사도에 따라 관광지 정렬
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        travel_indices = [i[0] for i in sim_scores[0:cnt]]
        for i in range(len(travel_indices)):
            recommendList.append(df['travel_id'].iloc[travel_indices[i]])

    print(recommendList)

if __name__ == "__main__":
    main(sys.argv)
    