import pyttsx3 as pyttsx


def time_to_text(time):
    hour, minute = map(int, time.split(":"))
    meridian = "am" if hour < 12 else "pm"
    teens = ["twelve ", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ",
             "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
    hour = teens[hour % 12]
    minute_text = ["twenty ", "thirty ", "fourty ", "fifty ", "sixty "][minute // 10 - 2] if minute > 19 else "oh " if 0 < minute < 10 else ""
    minute_text += teens[minute % 20 if 0 < minute < 20 else minute % 10] if minute % 10 > 0 else ""
    output = f"It's {hour}{minute_text}{meridian}"
    return output


def speak_time(time):
    text = time_to_text(time)
    s = pyttsx.init()
    s.say(text)
    s.runAndWait()
