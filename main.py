import time
import mouse

time_per_click = []


def sample():
    print("Begin clicking!")
    while len(time_per_click) < 10:
        if mouse.is_pressed(button='left') or mouse.is_pressed(button='right'):
            time_taken = time.time()
            time_per_click.append(time_taken)
        #print(time_per_click)
            time.sleep(0.1)
            if len(time_per_click) == 10:
                time1 = time_per_click[9] - time_per_click[8]
                time2 = time_per_click[7] - time_per_click[6]
                time3 = time_per_click[5] - time_per_click[4]
                time4 = time_per_click[3] - time_per_click[2]
                time5 = time_per_click[1] - time_per_click[0]
                average_clicks = (time1 + time2 + time3 + time4 + time5)/5
                #print(time1)
                mil_seconds = average_clicks*1000000
                hours = round((mil_seconds/60)/60)
                minutes = abs(round((((mil_seconds/60)/60)-hours)*60))
                seconds = abs(round((((((mil_seconds/60)/60)-hours)*60)-minutes)*60))
                print("It'll take you {} hours, {} minutes, and {} seconds to get 1 million clicks".format(hours,minutes,seconds))
if __name__ == "__main__":
    sample()
