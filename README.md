# Tor Network Circuit Viewer

This Python script connects to the Tor network and retrieves information about active circuits. It checks if Tor is running, and if so, it displays the details of the active circuits, including the entry and exit nodes involved in each circuit.

## Features

- Checks if the Tor service is running and connects to the Tor Controller.
- Displays the entry and exit nodes of active circuits, showing their nicknames and IP addresses.
- Prints the status of each circuit (only showing those that are "built").

## Requirements

To run this script, you need to have the following dependencies installed:

- **Python 3.x**: The script is compatible with Python 3.
- **stem**: A Python library for interacting with the Tor network.
