from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt

from operator import itemgetter
import numpy as np
from datetime import datetime, timedelta


# (2) Load news data--approach 2
def load_df_data_v1():
    
    global df # global variable
    #df = pd.read_csv('app_news_rcmd_bert/dataset/cna_news_200_preprocessed.csv',sep='|')
    df = pd.read_csv('api/dataset/technews_post_preprocessed.csv', sep='|')
    global news_sim_martrix
    news_sim_martrix = np.load('api/dataset/news_sim_martrix.npy')
    global postID2idx
    postID2idx={}

    for id, i in df.postID.items():
        postID2idx[i] = id

# call load data function when starting server
load_df_data_v1()

#-- API: input category
@csrf_exempt
def api_query_keyword_cate_news(request):
    cate = request.POST['category']
    user_keywords = request.POST['input_keywords']
    user_keywords = user_keywords.split()
    response = get_userkeyword_cate_latest_news(cate, user_keywords)
    return JsonResponse({"latest_news": response})

#-- API: input news_id, and then get news information
@csrf_exempt
def api_news_content(request):
    postID = request.POST['postID']
    content = get_news_content(postID)
    related = get_topk_similar_articles(postID)
    # print(related)
    return JsonResponse({"news_content": content, "related_news": related})


#-- Given a category, get the latest news
def get_userkeyword_cate_latest_news(cate, user_keywords):
    # get the last news (the latest news)
    # df_cate = df_cate.tail(10)  # Only 10 pieces
    # only return 10 news
    # proceed filtering: news category
    # and or 條件

    # end date: the date of the latest record of news
    end_date = df.date.max()    
    # start date 昨天新聞過濾
    days = 1     
    start_date_delta = (datetime.strptime(end_date, '%Y-%m-%d %H:%M').date() - timedelta(days=days)).strftime('%Y-%m-%d %H:%M')
    start_date_min = df.date.min()
    # set start_date as the larger one from the start_date_delta and start_date_min 開始時間選資料最早時間與周數:兩者較晚者
    start_date = max(start_date_delta,   start_date_min)

    # (1) proceed filtering: a duration of a period of time
    # 期間條件
    condition = (df.date >= start_date) & (df.date <= end_date) 
    
    # (2) proceed filtering: news category
    # 新聞類別條件
    # category condition
    condition = (df.category == cate) 
    
    # (3) query keywords condition使用者輸入關鍵字條件and
    # 若未輸入關鍵字，結果是true，因為"" in text 不管text字串內容為何，運算結果為True
    condition = condition & df.content.apply(lambda text: all(
            (qk in text) for qk in user_keywords))  # 寫法:all()
    
    
    # condiction is a list of True or False boolean value
    df_query = df[condition]

    # 隨機挑選五篇
    if len(df_query) >= 4:
        df_query = df_query.sample(4) # Sample only 4 pieces 若文章數不足會報錯!
    else:
        df_query = df_query.tail(4) # Only latest 4 pieces
    
    items = []
    for i in range( len(df_query)):
        postID = df_query.iloc[i].postID    
        title = df_query.iloc[i].title
        content = df_query.iloc[i].content
        category = df_query.iloc[i].category
        link = df_query.iloc[i].link
        image = df_query.iloc[i].image
        # if image value is NaN, replace it with empty string 
        if pd.isna(image):
            image=""

        news_info = {
            "postID": postID, 
            "category": category, 
            "title": title,
            "content": content, 
            "link": link,
            "image": image
        }

        items.append(news_info)
    return items

# -- Given a postID, get document information
def get_news_content(postID):
    df_item = df[df.postID == postID]
    title = df_item.iloc[0].title   
    content = df_item.iloc[0].content
    category = df_item.iloc[0].category
    link = df_item.iloc[0].link
    date = df_item.iloc[0].date
    image = df_item.iloc[0].image
    # if image value is NaN, replace it with empty string 
    if pd.isna(image):
        image=''

    news_info = {
        "postID": postID,
        "category": category,
        "title": title,
        "content": content,
        "link": link,
        "date": date,
        "image": image
    }

    return news_info

#-- Given postID, get three similar article information
def get_topk_similar_articles(postID):

    ## Find topk similar articles
    topk=2
    sim_dict = {}
    idx = postID2idx[postID]
    for i, value in enumerate(news_sim_martrix[idx]):
        sim_dict[i]=value
    similar_items = sorted(sim_dict.items(), key= itemgetter(1), reverse=True)[1:topk+1] # topk+1 多取一筆 有包含本身這一筆

    ## Get article information to display
    items = []
    for idx, score in similar_items:
        item = df.iloc[idx]
        postID = item.postID
        title = item.title
        content = item.content
        category = item.category
        link = item.link
        image = item.image
        # if image value is NaN, replace it with empty string 
        if pd.isna(image):
            image=''

        score = round(float(score), 2)
        news_info = {
            "category": category, 
            "title": title, 
            "link": link,
            "id": postID, 
            'score': score, 
            "image": image
            }
        items.append(news_info)

    return items

print("app Bert based news recommendation was loaded!")
