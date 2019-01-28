# 함수화 처리
# 아이디, 비번을 인자로 입력 받아서, 재활용성을 높이고, 모듈화의 모양새를 갖춘다.
import pymysql as my

# 키워드를 이용하여 이름에 해당 키워드가 포함된 주식 목록을 리턴한다.
def selectProjectByKeyword(keyword):
    connection = None
    rows = None # 해당 정보들을 가져오는 변수
    try:
        connection = my.connect(host='localhost', # 디비 주소
                                user='root',      # 디비 접속 계정
                                password='2736', # 디비 접속 비번
                                db='tum_db',      # 데이터베이스 이름
                                #  port=3306,         # 포트
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # 커서타입지정
        # 퀴리 수행
        with connection.cursor() as cursor: 
            sql = '''
                select 
                    pname,purl,category
                from 
                    tumblbuck
                where noun like '%%%s%%';
            '''% keyword

            cursor.execute(sql)    
            # 여러개 데이터를 다 가져올때        
            rows = cursor.fetchall()
    except Exception as e:
        print('->',e)
        rows =None
    finally:
        if connection:
            connection.close()
    return rows
    
    