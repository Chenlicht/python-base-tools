file_link = "http://xxxxxx.aliyuncs.com/Development/分析上传文件/frmgham2.xls
import wget
if len(EXCELURL.strip()) != 0:   # 文件地址字符串是否为空或全是空格
    # 获取文件名，生成保存本地地址
    file_path = f"data/{EXCELURL.split('/')[-1]}"
    try:
        wget.download(EXCELURL, file_path)
        # 加载本地文件
        # file_path = os.path.join(LOCAL_PATH, 'res/20230802100648-frmgham2.xls')
    except Exception as e:
        print('文件下载失败')
