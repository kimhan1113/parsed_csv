import pandas as pd

fileName = './csv_files/1.csv'

# byte 데이터 때문에 진짜 힘들게 구한값들..

def parsed_csv(csv_path):

    # 파일 불러오고 column name을 정해서 split 하기 편하게 한다.
    df = pd.read_csv(fileName, encoding ='utf-8', sep='delimiter', header=None, names=['name'])

    # column이 하나이고 ,로 구분되어 있기 때문에 다음 코드로 dataframe을 생성한다.
    df_ = df.name.str.split(',', expand=True)

    # dataframe에서 필요한 부분만 slicing 해서 만든다.
    df_ = df_.iloc[5:, :16]

    # 이유는 모르겠지만 개행이 되서 데이터마다 null값이 생성되있어서 없애지는 코드를 넣는다.
    df_.dropna(how='any', axis=0, inplace=True)

    # 저장할 dict을 생성한다.
    parsed = {}

    # for row in df_.iterrows(): 이것도 row를 하나씩 search해주지만 이걸 쓰면 byte변환이 안된다.

    for date, row in df_.T.iteritems():

        # byte 형식의 데이터를 제거해준다. 안해주면 값이 안담긴다.
        line = [str_.replace('\x00' ,'') for str_ in row]

        # 그래도 dict에다가 원하는 데이터셋을 담는다.
        arr_ind ,comp ,l ,w ,t = line[0] ,line[1] ,line[12] ,line[13] ,line[14]
        parsed['A{}'.format(arr_ind) + '_' +comp] = (float(l), float(w), float(t))

    return parsed

dict_list = parsed_csv(fileName)
print(dict_list.keys())