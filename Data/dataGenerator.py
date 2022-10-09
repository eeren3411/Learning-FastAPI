import json
import datetime
import random
from pathlib import Path

class meetingModel:
    def __init__(
        self, 
        startDate: datetime.datetime, 
        endDate: datetime.datetime, 
        participants: list[str],
        isOnline: bool,
        organizer: str
    ):
        self.startDate = startDate
        self.endDate = endDate
        self.participants = participants
        self.isOnline = isOnline
        self.organizer = organizer
    
    def __dict__(self):
        return {
            "startDate": self.startDate.strftime("%d-%m-%Y %H:%M:%S"),
            "endDate": self.endDate.strftime("%d-%m-%Y %H:%M:%S"),
            "participants": self.participants,
            "isOnline": self.isOnline,
            "organizer": self.organizer
        }


def toJson(meetings: list[meetingModel]):
    return json.dumps(
        meetings, 
        default=lambda o: o.__dict__(), 
        indent=4
    )

USERS = [
    "Eeren",
    "Hu Tao",
    "Yelan",
    "Zhongli",
    "Instructor Albedo",
    "Ayaka",
    "Shenhe",
    "Mona",
    "Venti",
    "Keqing",
    "Xingqiu",
    "Xiangling",
    "Bennett"
]

RANDOM_DATETIME_START_STRING = "01-09-2022 00:00:00"
RANDOM_DATETIME_END_STRING = "01-10-2022 23:59:59"
RANDOM_MIN_MEETING_TIME_SECONDS = 300
RANDOM_MAX_MEETING_TIME_SECONDS = 3600 
DATA_COUNT = 100

RANDOM_DATETIME_START = int(datetime.datetime.strptime(RANDOM_DATETIME_START_STRING, "%d-%m-%Y %H:%M:%S").timestamp())
RANDOM_DATETIME_END = int(datetime.datetime.strptime(RANDOM_DATETIME_END_STRING, "%d-%m-%Y %H:%M:%S").timestamp())


def randomMeeting() -> meetingModel:
    startDate = datetime.datetime.fromtimestamp(random.randrange(RANDOM_DATETIME_START, RANDOM_DATETIME_END))

    length = random.randrange(RANDOM_MIN_MEETING_TIME_SECONDS, RANDOM_MAX_MEETING_TIME_SECONDS)
    endDate = startDate + datetime.timedelta(seconds=length)

    participantCount = random.randrange(1, len(USERS))
    participants = random.sample(USERS, participantCount)

    isOnline = random.choice([True, False])

    organizer = random.choice(participants)

    return meetingModel(
        startDate=startDate,
        endDate=endDate,
        participants=participants,
        isOnline=isOnline,
        organizer=organizer
    )


def main():
    randomData = [randomMeeting() for a in range(DATA_COUNT)]
    path = Path(__file__).with_name("data.json")
    with path.open("w+") as outputFile:
        outputFile.write(toJson(randomData))

if __name__ == "__main__":
    main()