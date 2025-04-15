import json

def get_file_path_list():
    json_file_path = 'config.json'  # JSONファイルのパスを指定
    target_key = 'folder_path'         # 取得したいパスリストのキー名を指定
    path_list = []                     # パスリストを初期化
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f) 
        path_list = data[target_key]
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")
    return path_list




