# Kinova Robotic Arm Control with Unicorn Hybrid Black

## Overview
This project demonstrates the integration of the Kinova Kortex API with the Unicorn Hybrid Black EEG device to control a Kinova robotic arm using brain signals. The system captures EEG signals, processes them to detect specific commands, and then translates those commands into movements of the robotic arm.

## Prerequisites
Before running this project, ensure that the following are installed and properly configured:

- **Kinova Kortex SDK**: Required to control the Kinova robotic arm.
- **Unicorn Hybrid Black SDK**: Required to capture and process EEG signals.
- **Python 3.x**: Ensure Python is installed along with the necessary libraries.
- **Dependencies**: Install necessary Python packages using:
  ```bash
  pip install -r requirements.txt
