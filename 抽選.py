import csv
import random
import sys

#選手配置の最大ループ回数
max_trial = 10

#配置対象となる枠のリスト。[「組番号」, 「枠名」]。
positions = [
    [1, 'A'], [1, 'B'], [1, 'C'], [1, 'D'], [1, 'E'], [1, 'F'], [1, 'G'], [1, 'H'], 
    [2, 'A'], [2, 'B'], [2, 'C'], [2, 'D'], [2, 'E'], [2, 'F'], [2, 'G'], [2, 'H'], 
    [3, 'A'], [3, 'B'], [3, 'C'], [3, 'D'], [3, 'E'], [3, 'F'], [3, 'G'], [3, 'H'], 
    [4, 'A'], [4, 'B'], [4, 'C'], [4, 'D'], [4, 'E'], [4, 'F'], [4, 'G'], [4, 'H'], 
    [5, 'A'], [5, 'B'], [5, 'C'], [5, 'D'], [5, 'E'], [5, 'F'], [5, 'G'], [5, 'H'], 
    [6, 'A'], [6, 'B'], [6, 'C'], [6, 'D'], [6, 'E'], [6, 'F'], [6, 'G'], [6, 'H'], 
    [7, 'A'], [7, 'B'], [7, 'C'], [7, 'D'], [7, 'E'], [7, 'F'], [7, 'G'], [7, 'H'], 
    [8, 'A'], [8, 'B'], [8, 'C'], [8, 'D'], [8, 'E'], [8, 'F'], [8, 'G'], [8, 'H'], 
    [9, 'A'], [9, 'B'], [9, 'C'], [9, 'D'], [9, 'E'], [9, 'F'], [9, 'G'], [9, 'H'], 
    [10, 'A'], [10, 'B'], [10, 'C'], [10, 'D'], [10, 'E'], [10, 'F'], [10, 'G'], [10, 'H'], 
    [11, 'A'], [11, 'B'], [11, 'C'], [11, 'D'], [11, 'E'], [11, 'F'], [11, 'G'], [11, 'H'], 
    [12, 'A'], [12, 'B'], [12, 'C'], [12, 'D'], [12, 'E'], [12, 'F'], [12, 'G'], [12, 'H'], 
    [13, 'A'], [13, 'B'], [13, 'C'], [13, 'D'], [13, 'E'], [13, 'F'], [13, 'G'], [13, 'H'], 
    [14, 'A'], [14, 'B'], [14, 'C'], [14, 'D'], [14, 'E'], [14, 'F'], [14, 'G'], [14, 'H'], 
    [15, 'A'], [15, 'B'], [15, 'C'], [15, 'D'], [15, 'E'], [15, 'F'], [15, 'G'], [15, 'H'], 
    [16, 'A'], [16, 'B'], [16, 'C'], [16, 'D'], [16, 'E'], [16, 'F'], [16, 'G'], [16, 'H'], 
]

#配置を固定する枠のリスト。CSVファイルから読み込む。
fixed_positions  = []

#選手のリスト。[「id」, 「氏名」, 「学校名」] 。CSVファイルから読み込む。
players = []

#選手リストのうち、配置を固定する選手のリスト。CSVファイル内で組番号と枠名が明記されている選手。
fixed_players = []

#CSVファイル名：固定する場合は以下に指定する。
#in_file = '抽選入力サンプル.csv'
#out_file = '抽選出力サンプル.csv'
args = sys.argv
if len(args)!=3:
    print(f'使い方：{args[0]} 「入力ファイル名」 「出力ファイル名」')
    exit()

in_file = args[1]
out_file = args[2]

########## 以下は基本的に編集不要 ##########
#選手情報の表示
def print_players(ps):
    print('------------------------------------')
    for p in ps:
        print_player(p)
    print('------------------------------------')
def print_player(p):
    print(', '.join(p))

#配置情報＋選手情報の表示
def print_positions_players(pss, pls):
    print('------------------------------------')
    for (ps, pl) in zip(pss, pls):
        print_position_player(ps, pl)
    print('------------------------------------')
def print_position_player(ps, pl):
    print(str(ps[0]) + '-' + ps[1]  + ': ' + ', '.join(pl))

#選手の読み込み
print(f'{in_file}から選手リストを読み込みます')
with open(in_file, 'r', encoding='cp932') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader: # id, 氏名, 学校名, （組番号、枠名）
        player = row[0:3] #選手情報（id, 氏名, 学校名）
        position = row[-2:] #固定枠情報（組番号, 枠名）
        players.append(player) #選手リストに追加
        if position != ['','']: #固定枠の指定がある。
            if not position[0].isdecimal(): #組番号が整数ではない
                print('------------------------------------')
                print("エラー：組番号は整数でなければなりません。")
                print('------------------------------------')
                print_player(row)
            else:
                position[0] = int(position[0])
                if position not in positions : #固定枠がリスト内に無い
                    print('------------------------------------')
                    print("エラー：配置指定が不正です。")
                    print('------------------------------------')
                    print_player(row)
                else: #正しい固定枠指定
                    fixed_players.append(player) 
                    fixed_positions.append(position)     
                    #print_position_player(position, player)

print(f'{len(players)}件のデータを読み込みました')

#数の確認
if(len(players) != len(positions)):
    print("エラー：枠の数と選手数が異なります")

#初期状態
print("初期状態です")
print('------------------------------------')
print("選手一覧")
print_players(players)
print("固定枠に配置する選手一覧")
print_positions_players(fixed_positions, fixed_players)

#ランダム抽選
print("手順1. ランダム抽選をします")
random.shuffle(players)
print_positions_players(positions, players)

#固定枠の処理
print("手順2. 固定枠の選手を指定位置に配置します")
for (i, f_player, f_position) in zip(range(len(fixed_players)), fixed_players, fixed_positions):
    print("固定枠選手：", end="")
    print_player(f_player)
    j1 = players.index(f_player) #固定枠選手の現在の配置場所
    j2 = positions.index(f_position) #固定枠選手が本来配置されるべき場所
    print("入替対象選手：", end="")
    print_player(players[j2])
    players[j1], players[j2] = players[j2], players[j1]
    print("両者を入れ替えました")
    print("------------------")
print_positions_players(positions, players)

#重複をさける。
print("手順3. 同じ学校の選手が同一組に属さないように調整をします")
changed = True
trial = 1
while changed and trial <= max_trial:
    schools = set() #同じリーグ内の学校名の集合
    league = 0 #リーグ番号
    print(f'{trial}回目の調整: ')
    changed = False
    for (i, player, position) in zip(range(len(players)), players, positions):
        school = player[2] #学校名
        if position[0] != league: #新しいグループなので問題ない。
            league = position[0]
            schools = set([school])
        else:
            if school in schools: #学校名が重複する場合。
                print(f'第{league}組に「{school}」の重複が出ました')
                if position in fixed_positions: #動かしてはいけないポジション
                    print("エラー：動かしてはいけないポジションに重複が出ました")
                else: #学校名が重複しないように移動する必要がある。
                    j = (i + 1) % len(players) #交換の候補
                    while True:
                        if j == i:
                            print("候補が見つかりませんでした！")
                            break
                         #j番は変更禁止, jのグループとiのグループが同じ→意味ない, #jの学校が既にグループ内に存在する
                        if (positions[j] in fixed_positions) \
                            or (positions[j][0] == league) \
                            or (players[j][2] in schools) : 
                            j = (j + 1) % len(players)
                            continue
                        else : #入替対象
                            print(f'割振番号{i}と{j}を入れ替えます')
                            players[i], players[j] = players[j], players[i]
                            schools.add(players[i][2])
                            print_position_player(positions[i], players[i])
                            print_position_player(positions[j], players[j])
                            print("--------------------")
                            changed = True
                            break
            else: #学校名が重複しない
                schools.add(players[i][2])
    print(f'{trial}回目の入替が終了しました。')
    print_positions_players(positions, players)
    trial += 1
if changed: #最終配置で移動があった→配置失敗
    print(f'{max_trial}回の試行をしましたが、配置に失敗しました。プログラムを再度起動し、新しいランダム配置で試行してください。')
else: #配置成功
    print(f'{trial-1}回目で条件を満たす選手配置に成功しました。{out_file}に出力します。')
    with open(out_file, 'w', encoding="utf_8_sig") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
        for (player, position) in zip(players, positions):
            spamwriter.writerow(player + position)
print('抽選を終了します')






                






    
