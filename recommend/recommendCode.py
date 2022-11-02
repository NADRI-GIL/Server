from cgitb import reset
import pandas as pd
import numpy as np
import sys

def main(recommendTitle):
    result=[]
    cosine_sim = np.load("/home/ec2-user/Server/recommend/cosine_sim_id.npy")
    indices = pd.read_pickle('/home/ec2-user/Server/recommend/indices_id.pkl')
    df = pd.read_csv('/home/ec2-user/Server/recommend/travel.csv', low_memory=False, encoding='utf-8')

    title = int(recommendTitle[1])
    idx = indices[title]
    sim_scores = cosine_sim[idx]
    sim_scores = list(enumerate(sim_scores))
    # 유사도에 따라 관광지 정렬
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # print(sim_scores[:6])
    # print(sim_scores)
    travel_indices = [i[0] for i in sim_scores]
    # print(travel_indices)
    # print(df['name'].iloc[travel_indices])
    # print(df['info'].iloc[travel_indices])
    for i in range(6):
        result.append(int(df['travel_id'].iloc[sim_scores[i][0]]))
    print(result)

if __name__ == "__main__":
    main(sys.argv)