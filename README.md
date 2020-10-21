【アプリケーション名】
market_search

【アプリケーション概要】
会社の決算情報・財務分析をみることができる

【URL】
https://market-search29703.herokuapp.com/

【利用方法】
見たい会社の決算年度を選択することで、情報をみることができる

【目指した課題解決】
会社の財務分析により、株式投資の銘柄選択をしたい人が、

【洗い出した要件】
"優先順位
（高：3、中：2、低：1）"     
  機能	                目的	                                                                                詳細	                                                                                      ストーリー(ユースケース)	                                                   ¥
3	会社決算データを推移表示	会社の決算情報をみることができる	                                                           年度決算を横並びにすることにより、推移をみることができる	                                                 会社決算ページに画面遷移すると自動的に表示されている
3	会社決算データの推移分析  会社の決算情報を推移で見ることにより、会社が成長しているのかどうかがわかるため                          比率を出すことにより、どのように推移しているかわかりやすくなる	                                             会社決算ページに画面遷移すると自動的に表示されている
3	会社決算データのグラフ化   売上・売上総利益・営業利益を折れ線グラフ、総資産・固定負債・純資産を棒グラフで表示することにより、一眼でわかる	売上・売上総利益・営業利益を折れ線グラフ、総資産・固定負債・純資産を棒グラフで表示することにより、一眼でわかるようにする	会社決算ページに画面遷移すると自動的に表示されている
3	決算詳細表示	　　   　  単年の決算情報をみることができる	                                                          ある会社の当該年度の決算を表示する                                                               	決算詳細ページに画面遷移すると自動的に表示されている
3	財務指標の表示       	 会社の資産を効率的に運用しているか知ることができる	                                             ある会社の当該年度の財務指標を見ることができる	                                                      決算詳細ページに画面遷移すると自動的に表示されている	
3	決算詳細分析のグラフ化  	 資産、負債・純資産の内訳を円グラフで表示し、一眼でわかる	                                         資産、負債・純資産の内訳を円グラフで表示し、一眼でわかるようにする	                                         決算詳細ページに画面遷移すると自動的に表示されている	


【実装した機能】
・4年間の会社の決算情報の一覧表示
・決算データのグラフ表示
・決算を対売上比率で表示
・単年の決算を表示
・ROA、ROEなどの財務指標を表示


【実装予定の機能】
ユーザー管理機能
お気に入り機能
株価・株価チャート表示機能

【データベース設計】
Companyクラス　　　　　Statementクラス
  name------------- company（ForeignKey）
                    fiscal_year
                    bs_current_assets
                    bs_fixed_assets
                    bs_deferred_assets
                    bs_current_liabilities
                    bs_fixed_liabilities
                    bs_net_assets
                    pl_gross_sales
                    pl_gross_profit
                    pl_operating_profit
                    pl_ordinary_income
                    pl_income_before_tax
                    pl_net_income
                    cf_operating
                    cf_investment
                    cf_finance

【ローカルでの動作方法】
git clone後下記ライブラリをpip installする

asgiref==3.2.10
certifi==2020.6.20
chardet==3.0.4
dj-database-url==0.5.0
Django==3.1.2
django-filter==2.4.0
django-forms-bootstrap==3.1.0
djangorestframework==3.12.1
gunicorn==20.0.4
humanize==3.0.1
idna==2.10
Pillow==8.0.0
psycopg2-binary==2.8.6
pytz==2020.1
requests==2.24.0
sqlparse==0.4.1
urllib3==1.25.10
whitenoise==5.2.0
