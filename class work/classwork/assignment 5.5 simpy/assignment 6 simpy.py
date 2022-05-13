import simpy

# process of car
def car(env):
    while True:
        print('Start parking at %d' % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration) 
        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)   

# start
env = simpy.Environment()   
env.process(car(env))   
env.run(until=15)   

from random import seed, randint
seed(23)

import simpy

class EV:
    def __init__(self, env):
        self.env = env
        self.drive_proc = env.process(self.drive(env))
        self.bat_ctrl_proc = env.process(self.bat_ctrl(env))
        self.bat_ctrl_reactivate = env.event()
        self.bat_ctrl_sleep = env.event()


    def drive(self, env):
        """Driving process"""
        while True:
            # driving 20-40
            print("Start driving time: ", env.now)
            yield env.timeout(randint(20, 40))
            print("Stop Driving Time: ", env.now)

            # parking 60-360
            print("Start parking time: ", env.now)
            self.bat_ctrl_reactivate.succeed() 
            self.bat_ctrl_reactivate = env.event()
            yield env.timeout(randint(60, 360)) & self.bat_ctrl_sleep
            print("Stop parking time:", env.now)

    def bat_ctrl(self, env):
        """Battery charging process"""
        while True:
            print("Charging program hibernation time:", env.now)
            yield self.bat_ctrl_reactivate 
            print("Charging program activation time:", env.now)
            yield env.timeout(randint(30, 90))
            print("End of charging procedure Time:", env.now)
            self.bat_ctrl_sleep.succeed()
            self.bat_ctrl_sleep = env.event()

def main():
    env = simpy.Environment()
    ev = EV(env)
    env.run(until=300)

if __name__ == '__main__':
    main()