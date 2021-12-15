from dateutil import parser
def get_value_with_default(data: dict, key: str, default=None):
    return data.get(key, default)

def get_timestamp(value: str):
    try:
        timestamp = parser.parse(value).strftime('%s')
        return timestamp
    except:
        return None