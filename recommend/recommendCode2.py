from cgitb import reset
import pandas as pd
import numpy as np
import sys

def main(recommendTitle):
    result=[]
    cosine_sim = np.load("")
    indices = pd.read_pickle('')
    df = pd.read_csv('', low_memory=False, encoding='utf-8')

    title = int(recommendTitle[1])
    idx = indices[title]
    sim_scores = cosine_sim[idx]
    sim_scores = list(enumerate(sim_scores))
    # 유사도에 따라 관광지 정렬
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    travel_indices = [i for i in sim_scores]
    for i in range(11):
        result.append([int(df['travel_id'].iloc[travel_indices[i][0]]), int(travel_indices[i][1]*100)])
    print(result)

if __name__ == "__main__":
    main(sys.argv)
    