import random
def verse():
    comfort_verses = ["Do not falter or grieve, for you will have the upper hand, if you are ˹true˺ believers.♡ (3:139)",
                      "...Do not worry; Allah is certainly with us. ...♡ (9:40)",
                      "Perhaps you dislike something which is good for you and like something which is bad for you. Allah knows and you do not know.🤍 (2:216)",
                      "O believers! Seek comfort in patience and prayer. Allah is truly with those who are patient.🤍 (2:153)",
                      "Verily, with hardship, there is ease🩵 (94:6)",
                      "Your Lord ˹O Prophet˺ has not abandoned you, nor has He become hateful ˹of you˺.🤍 (93:3)"
                      ]

    hope_verses = [
        "Why should we not put our trust in Allah, when He has truly guided us to the very best of ways? Indeed, we will patiently endure whatever harm you may cause us. And in Allah let the faithful put their trust.🩵 (14:12)",
        "And proclaim the blessings of your Lord.🤍 (93:11)"
    ]

    reassuring_verses = ["Allah reassured ˹them˺, “Have no fear! I am with you, hearing and seeing.🩵 (20:46)",
                         "Your Lord has proclaimed, “Call upon Me, I will respond to you...🩷(40:60)",
                         "Surely in the remembrance of Allah do hearts find comfort.🩷 (13:28)"
                         ]

    comfort_verse = random.choice(comfort_verses)
    hope_verse = random.choice(hope_verses)
    reassuring_verse = random.choice(reassuring_verses)

    return (comfort_verse, hope_verse, reassuring_verse)
