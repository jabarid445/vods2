from dataclasses import dataclass
from datetime import datetime

@dataclass
class Vod:
    url: str
    event_name: str
    p1_tag: str
    c1_icon_url: str
    p2_tag: str
    c2_icon_url: str
    round: str
    vod_date: datetime