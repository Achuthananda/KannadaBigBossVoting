import requests,json

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Content-Type': 'application/json'
}

contestantData = {
    "Priyanka":"ab730a10-ab3d-11eb-9eb0-e55c4357c4c9",
    "Divya Suresh":"fc1aeb30-7b1e-11eb-a1af-d93c47ce2886",
    "Manju":"23db2860-7b1f-11eb-a1af-d93c47ce2886",
    "Nidhi": "32817680-7b1f-11eb-a1af-d93c47ce2886",
    "Prashanth":"53377c80-7b1f-11eb-a1af-d93c47ce2886",
    "Raghu":"656d32f0-7b1f-11eb-a1af-d93c47ce2886",
    "Chakravarthy":"338a6350-9b92-11eb-bfb1-f1b639fa1416"
}

data =  {"showId":"6b3d31e0-7b1e-11eb-a1af-d93c47ce2886",
        "showName":"BBK Voting",
        "contestantId":"ab730a10-ab3d-11eb-9eb0-e55c4357c4c9",
        "contestantName":"Priyanka",
        "loginProvider":"Google"
        }

for keys in contestantData.keys():
    print("Now Voting {}".format(keys))
    data['contestantName'] = keys
    data['contestantId'] = contestantData[keys]
    datajson = json.dumps(data)
    response = requests.post('https://voting-api.voot.com/v1/addvote', headers=headers, data=datajson)
    if response.ok:
        print("Voted {} Successfully".format(keys))
    print('*'*80)