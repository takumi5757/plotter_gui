地図データを読んで制限速度が変化するポイントを抽出するスクリプト
抽出したポイントをkml,csvにして出力

python3.8.3
モジュールのインストール
pip install -r requirements.txt
実行方法
python main.py

選択パラメータ
main()内
state : どの州のデータを読むか state = VA だとVA/ushr_lane_center_points.csvを読む
chunksize : 何行ずつデータを読むか、csvを丸ごと読んで実行すると時間がかなりかかるため

生成ファイル
制限速度が切り替わった点のkmlファイル　kml_output/に格納される
制限速度が切り替わった点のcsvファイル　csv_output/に格納される

