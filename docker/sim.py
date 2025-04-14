import os
import sys
import libtmux
import time
from datetime import datetime
import subprocess

class Simulator:
    def __init__(self, sim_name = 'simulator'):
        self.session_name = sim_name
        self.server = libtmux.Server()
        self.session = self.server.new_session(self.session_name, attach=False)
        self.simulator = self.session.new_window(attach=True, window_name="ISAAC_SIM")
        self.dev_window = self.session.new_window(attach=True, window_name="DEV")
        self.paneDict = {}

    def run_simulator(self):
        pane = self.simulator.list_panes()[0]
        self.paneDict['simulator'] = pane
        pane.send_keys(cmd='/isaac-sim/isaac-sim.sh', enter=True)
        time.sleep(1)
        roslog = pane.capture_pane()
        print(roslog)
        pane.select()

    def run_dev_stack(self):
        self.b_init = True
        pane = self.dev_window.list_panes()[0]
        self.paneDict['dev_1'] = pane
        pane.send_keys(cmd='', enter=False)

if __name__ == '__main__':
    print(sys.argv)
    empty_tmux = False
    if 2 == len(sys.argv):
        empty_tmux = True if "1" == sys.argv[1] else False
    r = Simulator('simulator')
    if not empty_tmux:
        r.run_simulator()
    time.sleep(1)
    r.run_dev_stack()
