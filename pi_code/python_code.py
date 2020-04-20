import requests
import threading
import asyncio
import RPi.GPIO as GPIO
import time


print("setting up the task executor ")


def sleep_until_next_interval(seconds):
    now = time.time()
    fall_asleep = seconds - now % seconds
    time.sleep(fall_asleep)


def request_to_server(url):
    response = requests.get(url)
    return response.json()


def gpio_setup(channel):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    print("setup up gpio for  --- :"+str(channel))


def power_on(pin):
    GPIO.output(pin, GPIO.HIGH)
    print("powering on ---:"+str(pin))


def power_off(pin):
    GPIO.output(pin, GPIO.LOW)
    print("powering off ---: "+str(pin))


URL = 'http://192.168.0.104:8000/tasks/queue/'  # will change the url later
while True:
    sleep_until_next_interval(3)
    tasks = request_to_server(URL)

    for task in tasks:
        print("completing task " + task["task_id"])
        channel = task["channel"]
        gpio_setup(channel)
        if task["task_todo"] == 'on':
            power_on(channel)
        elif task["task_todo"] == 'off':
            power_off(channel)

        # post the to the server that the task is done
        requests.get('http://192.168.0.104:8000/tasks/' + task["task_id"])

        # TODO
        GPIO.cleanup()



# def hello():
#     print("hello")

# set_interval(hello(),5)
