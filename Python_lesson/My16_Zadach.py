# написать функции
# 1 возвращает список с диланми строк
# 2 созвращает словарь вида {"A":[...], "B": [...]} 
# где первая буква фразы является ключом, а значение список фраз
# начинающиеся с той же буквы
# 3 находит фразу максимальной длины и дополняет остальные символом _ до одинаковой длины
# так чтобы все строки имели на выходе одинаковый размер
rows = [
    "Share young official. One bill fire main clearly herself.",
    "Couple modern hope identify morning. Which visit executive.",
    "Both can politics bit. Me fight after next.",
    "Her some school. Carry well what kind east.",
    "During consumer particular. Begin near floor.",
    "Summer down start cost week.",
    "Stop decision beat trouble reveal.",
    "Strategy become nearly only identify evening chair.",
    "Business certainly none entire available.",
    "Threat sort ask might. Throughout popular man would.",
    "Role degree world remember chance.",
    "Resource contain official report bag along into soldier.",
    "Me sign Mr data market different address.",
    "On open along save room test difficult.",
    "Visit sign worker sense seat decide.",
    "Contain far page job environmental American away.",
    "Available enough radio popular sign. Crime story family TV.",
    "Nothing animal government skill no. Media high raise fall.",
    "Follow staff fly military federal about attorney.",
    "Movement point difficult act tend.",
    "Lay house course.",
    "Team little learn free go adult. Pick peace herself learn.",
    "Follow so nearly know adult simply debate east.",
    "Move quality range people. Also card again local industry.",
    "Campaign here traditional PM.",
    "Election marriage analysis none green between sea.",
    "Tonight but really which involve stop audience.",
    "Stock six reason share star action.",
    "Newspaper responsibility participant bad set.",
    "Remain enjoy close lead newspaper just.",
    "Involve instead individual side up beyond to.",
    "Light quickly compare sport hope.",
    "I worry too seem. Amount interest top measure.",
    "Parent dog case buy pick board point.",
    "Reason war future bed ahead arm. Nature until machine kid.",
    "American store civil order.",
    "Current team recent list.",
    "Just series than late.",
    "Eat Mrs future short radio always election.",
    "Us local camera peace back memory world today.",
    "Own opportunity your. Set author since view.",
    "News big either study.",
    "Simply know order important.",
    "Newspaper wrong sing. Statement during specific expert.",
    "Soon woman board ability camera process.",
    "Example maintain man floor station type again.",
    "Item school group around late check.",
    "Great know executive cover third under hold.",
    "Modern decision hand down identify military.",
    "Better side and finally can point worker.",
    "Miss none manage give close end difference.",
    "Guy support answer nothing modern involve its.",
    "Run good many pressure stuff letter.",
    "Hair seven test teach eye." 
    ]

def dlin_strok(m):
    result_spisok = []
    for i in m:
        result_spisok.append(len(i))
    return result_spisok

print(dlin_strok(rows))

def slovar_hitr(catty):
    result_slovar = {}
    for i in catty:
      #  print(i[0:1])
        key = i[0:1]
        if key in result_slovar:
            result_slovar[key].append(i)
        else :
            result_slovar[key] = []

    return result_slovar          
        
      
print(slovar_hitr(rows))    
    # 2 созвращает словарь вида {"A":[...], "B": [...]} 
# где первая буква фразы является ключом, а значение список фраз
# начинающиеся с той же буквы

