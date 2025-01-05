# Created by weardhat

from stem import Signal
from stem.control import Controller
from stem.control import CircStatus
import sys

def check_tor_running():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()  
        return True
    except Exception as e:
        print(f"Error: Could not connect to Tor. Is Tor running? ({e})")
        return False

def display_tor_nodes():
    if not check_tor_running():
        print("Tor is not running. Please start Tor and try again.")
        sys.exit(1) 

    with Controller.from_port(port=9051) as controller:
        controller.authenticate()  

        circuits = controller.get_circuits()

        if not circuits:
            print("No active circuits found.")
            return

        for circ in circuits:
            if circ.status == CircStatus.BUILT:  
                entry_node = circ.path[0]  
                exit_node = circ.path[-1]   

                entry_info = controller.get_network_status(entry_node[0])
                exit_info = controller.get_network_status(exit_node[0])

                print(f"Entry Node: {entry_info.nickname} ({entry_info.address})")
                print(f"Exit Node: {exit_info.nickname} ({exit_info.address})")
                print(f"Status: {circ.status}")
                print("-----")

if __name__ == "__main__":
    display_tor_nodes()
