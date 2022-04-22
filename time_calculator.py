def add_time(start, duration, currentDay = ""):

  # list of days
  days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  
  time = start.split(" ")[0]
  meridiem = start.split(" ")[1]

  # 24h clock
  if meridiem == "PM" :
    hour = int(time.split(":")[0]) + 12
    time = str(hour) + ":" + time.split(":")[1]

  # current time
  hourStart = int( time.split(":")[0] )
  minuteStart = int( time.split(":")[1] )

  # duration
  hourDuration = int( duration.split(":")[0] )
  minuteDuration = int( duration.split(":")[1] )

  # future time
  fhour = hourStart + hourDuration
  fminute = minuteStart + minuteDuration

  # normalizing minutes
  if fminute > 60 :
    fminute = fminute % 60
    fhour += 1

  if fminute < 10 :
    fminute = "0" + str(fminute)
  fminute = str(fminute)

  
  # normalizing hourse
  dayCountdown = 0
  if fhour > 24 :
    dayCountdown = (fhour - (fhour % 24)) / 24
    fhour = fhour % 24
  fhour = str(fhour)

  
  # formating new time
  if int(fhour) == 0 :
    fhour = str(12)
    meridiem = "AM"
  elif int(fhour) < 12 :
    meridiem = "AM"
  elif int(fhour) == 12 :
    fhour = str(12)
    meridiem = "PM"
  else :
    meridiem = "PM"
    fhour = str( int(fhour) - 12 )


  # foramting the day cycle
  if currentDay != "" :
    try :
      index = days.index(currentDay.lower())
    except :
      return "That's not a day"

    currentDay = ", " + days[(index + int(dayCountdown))%7].capitalize()
    

  # formating the day
  if dayCountdown == 0 :
    dayCountdown = ""
  elif dayCountdown == 1 :
    dayCountdown = " (next day)"
  else :
    dayCountdown = " (" + str(int(dayCountdown)) + " days later)"
  

  # finishing
  new_time = fhour + ":" + fminute + " " + meridiem + currentDay + dayCountdown
  return new_time
