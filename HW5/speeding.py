# speeding.py
# Jason Moldan

def is_speeding(limit, speed):
    if speed < limit:
        return "legal"
    else:
        fine = float(50.0)
        fine = fine + round(((speed - limit) * 5),2)
        if speed > 90:
            fine = fine + 200
        return fine

def main():
    limit = float(input("enter speed limit:"))
    speed = float(input("enter speed:"))

    print(is_speeding(limit, speed))

main()
