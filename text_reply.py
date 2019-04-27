from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *



#---------------- self define module ----------------
import text_push as text_push


#---------------- end of define module ----------------

def text_reply_message(user_message):
    if('學歷' in user_message or '學校' in user_message):
        output_message = "我目前就讀於國立政治大學資訊管理學系三年級。"
    elif('工作' in user_message):
        output_message = "我目前正在潤得康資訊服務公司擔任實習生，負責軟體測試的工作。我也曾經在張赫數學擔任了一年的國中數學老師。"
    elif('專長' in user_message or '程式能力' in user_message):
        output_message = "我具備 Java, Python, HTML, SQL等程式能力，並且有相關實作經驗。\n這是我的Github網址:\n"+'https://github.com/nicolela5693'
    elif('名字' in user_message or '姓名' in user_message):
        output_message = "我是李雨津，你好!"
    elif('自我介紹' in user_message):
        output_message = "你好，我是李雨津，目前就讀於政治大學資管系三年級。我主要擅長的程式語言是JAVA, Python, SQL, 以及網頁前端的開發語言。"+ \
        "我目前在一家公司擔任軟體測試的實習生，學到了軟體測試的方法，並撰寫測試報告書。我的個性積極好學，樂於接觸學習新事物，也勇於接受挑戰!"
    elif('個性' in user_message):
        output_message = "1. 我的個性積極好學，喜歡接觸學習新事物，是個好奇寶寶。\n" + \
            "2. 我勇於嘗試，雖然有時還是會害怕，但我會鼓勵自己勇敢嘗試，不讓自己後悔!\n" + \
            "3. 我擅長將事情事先作規劃，讓自己更有目標去執行!\n" + \
            "4. 善於自省，分析自己的優缺並對缺點加以改善"
    elif('興趣' in user_message or '嗜好' in user_message or 'hobbies' in user_message):
        output_message = "我的休閒嗜好是看影集以及旅遊，旅遊可以幫助我拓展眼界，更加認識這個世界!"
    elif('你好' in user_message or '嗨' in user_message or '哈囉' in user_message):
        output_message = "你好，我是李雨津，很高興認識你!"
    elif('核心技能' in user_message):
        output_message = "我的核心技能如下 : \nJava \nJsp \nPython \nSQL \nHTML \nSoftware Testing"
    elif('競爭優勢' in user_message):
        output_message = "1. 具備 Java, Python, HTML, SQL等程式能力，且有相關實作經驗(詳見作品集) \n" + \
            "2. 擁有軟體測試之經驗，對於相關的實務工作能夠更加快速地掌握並執行 \n" + \
            "3. 商業分析能力，曾修習行銷管理、創業相關課程以及統計學，有商業模型分析相關經驗，且能運用統計相關知識進行分析 \n" + \
            "4. 個性積極，學習力強且具備好奇心，對於工作將會努力發揮所長，展現自身價值 \n" + \
            "5. 團隊協作能力，從多次課堂專案以及工作經驗中，了解一個團隊要如何去分工協調，達到最佳的結果"
    elif('職涯目標' in user_message):
        output_message = "我期望能夠透過自身的能力，讓人們能夠更加的便利，也期望能夠幫助企業甚至是社會有效率的解決問題!\n" + \
            "而我希望能夠透過這份實習，獲得更多實務上寶貴的經驗。我一直是LINE服務的愛用者，LINE帶給了我許多便利服務，我也很希望能夠成為其中的一員，一起努力!"
    elif('求學經歷' in user_message):
        output_message = "我目前就讀於國立政治大學資訊管理學系三年級，預計2020年畢業。\n" + \
            "曾修習相關課程: 程式設計、系統分析設計、資料庫管理、資料結構、演算法、網路概論"
    elif('社團' in user_message):
        output_message = "我曾經參加過證券研習社以及烹飪社，作為社員學習相關知識"
    elif('實習職缺爬蟲整合工具' in user_message):
        output_message = '介紹: 由於實習職缺散布於各人力銀行以及公司網站，因此製作此工具' + \
        '，透過Python結合Selenium針對各職缺網站進行爬蟲，並透過關鍵字排除重複職缺，再將各職缺進行分類存入資料庫，製成此工具'
    elif('狗狗主題搜尋引擎網站' in user_message):
        output_message = '介紹: 使用Java進行開發，透過從google搜尋資料將所有的網頁及子網頁文字資料進行蒐集，再把特定關鍵字加權，將網頁及標題根據權重重新排序，製成⼀個網頁，成為一個以狗為主題的搜尋引擎'
    elif('麵包店產銷系統' in user_message):
        output_message = '介紹: 將作業管理以及顧客關係管理知識融合，為麵包店的訂單及客戶制定資料庫及訂單排程，並製成一網站，可以直接在上面管理會員資料以及訂單資料，並預測未來訂單，產出物流排程，使用Java開發，並結合JSP及HTML架成一網站'
    elif('Email' in user_message):
        output_message = 'nicolela5693@gmail.com'
    else:  
        output_message = user_message

    return TextSendMessage(text=output_message)

