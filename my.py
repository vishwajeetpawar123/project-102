
import wikipedia
import time

while True:
    print("you may be a simple human but internet treats everyone a king gives everyone information they want dont you think so?")
    time.sleep(2)
    search=input("time's over what information do you what from your internet--")
    print("searching needs time.....")
    time.sleep(1)
    result = wikipedia.page(search)
    print("here you go.")
    print("")
    print("")
    print("")
    print("")
    print(result.summary)