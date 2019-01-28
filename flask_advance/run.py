from flask import Flask, render_template, url_for, request, redirect, session, jsonify
from db.sql import *
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/analysis/reco')
def reco():
    return render_template('reco.html')

@app.route('/analysis/findProject')
def findProject():
    return render_template('findproject.html')

@app.route('/analysis/data')
def data():
    return render_template('data.html')


# 검색
@app.route('/analysis/search', methods=['POST'])
def search():
    # 검색어 획득
    keyword = request.form['keyword']

    # 검색 쿼리 수행
    rows = selectProjectByKeyword( keyword );
    if rows:
        # 성공 : 검색 결과를 json 형식으로 응답
        return jsonify(rows)
    else:
        # 실패 : 검색 결과가 없으면 json의 다른 형태로 응답
        return jsonify([])  

if __name__=='__main__':
    app.run(debug=True)