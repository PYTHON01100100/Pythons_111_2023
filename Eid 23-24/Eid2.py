import datetime

# Get tomorrow's date
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

# Check if tomorrow is Eid al-Fitr
if tomorrow.month == 4 and tomorrow.day == 21:
  print("Eid Mubarak!")
  print("Eid Mubarak! May this Eid bring peace, happiness, and prosperity to you and your family.")
  print("Wishing you and your loved ones a blessed Eid.")

else:
    print("it's still Ramadan")