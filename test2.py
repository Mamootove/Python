donation = {
    "mahan":20,
    "ali": 30,
    "fateme":252,
    'parsa':240,
    'paria': 50
}
def analyze(donat):
    number = len(donat)
    person = ''
    tot = 0
    richest = -1
    for people, money in donat.items():
        tot += money
        if money > richest:
            richest = money
            person = people

    avg =float(tot/ number)
    
    return number, avg, richest, person
number , avg, richest, person = analyze(donation)
print(f"numbers are {number}", f"avg is {avg}", f"most is {richest}",f"the most donaitor is {person}", sep='***')







