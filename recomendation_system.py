import pandas as pd

recommendations = pd.read_csv('data/recommendations.csv', index_col=0)


def get_customer_recommendation_top_10(product):
    recommendation = recommendations[product].sort_values(ascending=False).iloc[:10]
    return recommendation

if __name__ == '__main__':
    print(get_customer_recommendation_top_10('WHITE METAL LANTERN'))