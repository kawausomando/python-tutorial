import sys

try:
    f = open('myfile.txt')
    s = f.readline()
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("データが整数に変換できません。")
except:
    print("予期せぬエラー: ", sys.exc_info()[0])
    raise # 呼び出し元でキャッチできるように例外を再送出
else:
    print(s)
    f.close()