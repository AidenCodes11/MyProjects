import os, sys, datetime
import time


def relaunch_in_wt():
    script_path = os.path.abspath(sys.argv[0])
    os.system(f'start "" wt powershell -NoExit -Command "python \'{script_path}\' wtspawned"')

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "wtspawned":
        relaunch_in_wt()
        sys.exit()

    os.system("cmd /c cls")
    while True:
        now = datetime.datetime.now()
        hour = now.hour if now.hour <= 12 else now.hour - 12
        hour = 12 if hour == 0 else hour
        print(f"╔═════════════╗")
        print(f"║ {hour}:{now.minute:02}:{now.second:02} {now.strftime("%p")} ║")
        print(f"╚═════════════╝")
        time.sleep(1)
        os.system("cmd /c cls")