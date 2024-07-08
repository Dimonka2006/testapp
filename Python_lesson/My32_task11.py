# Написать программу расчета частоты повторения каждого слова в заданном отрывке текста
# модифицировать программу так чтобы выводились только слова встречающиеся 5 и более раз
txt = """
The wheels on the bus go round and round round and round round and round
Twinkle twinkle little star how I wonder what you are
Peter Peter pumpkin eater had a wife and couldn't keep her
The rain had been falling falling falling for days A relentless monotonous drumming on the roof that seeped into every corner of the old house Sarah huddled deeper into her armchair the worn fabric a familiar comfort against the chilling chilling dampness that clung to the air
Outside the world had become a blurry watercolor painting The once vibrant green fields were now a muddy muddy expanse swallowing the distant trees in a veil of grey The wind a constant constant moan rattled the windows like skeletal fingers
Boredom gnawed at Sarah She had read every book on the shelf played every game of solitaire imaginable Time seemed to stretch stretch stretch into an eternity of dripping rain and howling wind
Suddenly a sharp sharp crack pierced the monotony Sarah lurched upright heart hammering in her chest Had a branch fallen? Or was it something more?
The silence that followed the crack was even more deafening deafening than the storm's roar Sarah strained to hear every muscle tensed Then a faint creaking creaking sound started from somewhere above
Fear cold and sharp flooded through her The creaking creaking grew louder closer  Was someone in the attic?  An intruder perhaps?  Her mind raced with possibilities each one more terrifying terrifying than the last
Taking a deep breath Sarah forced herself to move She grabbed a heavy iron poker from beside the fireplace its cold metal a grounding presence in her trembling hand Slowly cautiously she crept towards the stairs the creaking floorboards groaning under her weight
As she reached the landing the creaking stopped abruptly The silence was back thicker and heavier than ever Sarah stood frozen every nerve on edge waiting for the sound to resume
Then a soft soft thud From the attic  Her heart lurched  Taking another deep breath Sarah gripped the poker tighter and pushed open the attic door
The scene that greeted her was bathed in an eerie dusty dusty light filtering through a small window Cobwebs hung from the rafters like ghostly drapes and the air was thick with the smell of neglect and decay
There was no one there The silence was absolute  Sarah her body shaking with relief let out a shaky breath  Perhaps it had just been the wind after all
As she turned to leave a single single raven feather fluttered down from the rafters landing at her feet  Sarah stared at it a shiver crawling down her spine  The feather seemed to wink wink in the dim light a silent unsettling message from the shadows
With a newfound urgency Sarah hurried back downstairs the creaking floorboards seeming to echo her frantic heartbeat  The rain continued to fall fall fall but the sound no longer seemed monotonous  It now held a sinister undercurrent a relentless whisper of secrets hidden within the old house
"""

def words_frequrency(text: str):
    res = {}
    words = text.split()

    for w in words:
        word = w.lower()
        if word not in res:
            res[word] = 1
        else:
            res[word] += 1
    return res


def get_key(x: tuple):
    return x[1]


def top(words_dict: dict, count=5):
    dict_list = list(words_dict.items())
    return sorted(dict_list, key=lambda x: x[1], reverse=True)[:count]
    # return sorted(dict_list, key=get_key, reverse=True)[:count]


if __name__=="__main__":
    words_dict = words_frequrency(txt)
    res = top(words_dict=words_dict)
    print(res)
