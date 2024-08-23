# unicorn_interface.py

import unicornhybridblack
from Jay.kortex.kortex_control import move_arm_upwards, move_arm_downwards, move_arm_left, move_arm_right
from kortex_api.autogen.client_stubs import BaseClient

def detect_up_arrow_signal(unicorn_black):
    """
    Detects if the 'up arrow' signal is present in the EEG data.
    """
    try:
        eeg_data = unicorn_black.get_latest_data()
        if process_eeg_data_for_up_arrow(eeg_data):
            print("Up arrow signal detected!")
            return True
        return False
    except Exception as e:
        print(f"Error detecting up arrow signal: {e}")
        return False

def detect_down_arrow_signal(unicorn_black):
    """
    Detects if the 'down arrow' signal is present in the EEG data.
    """
    try:
        eeg_data = unicorn_black.get_latest_data()
        if process_eeg_data_for_down_arrow(eeg_data):
            print("Down arrow signal detected!")
            return True
        return False
    except Exception as e:
        print(f"Error detecting down arrow signal: {e}")
        return False

def detect_left_arrow_signal(unicorn_black):
    """
    Detects if the 'left arrow' signal is present in the EEG data.
    """
    try:
        eeg_data = unicorn_black.get_latest_data()
        if process_eeg_data_for_left_arrow(eeg_data):
            print("Left arrow signal detected!")
            return True
        return False
    except Exception as e:
        print(f"Error detecting left arrow signal: {e}")
        return False

def detect_right_arrow_signal(unicorn_black):
    """
    Detects if the 'right arrow' signal is present in the EEG data.
    """
    try:
        eeg_data = unicorn_black.get_latest_data()
        if process_eeg_data_for_right_arrow(eeg_data):
            print("Right arrow signal detected!")
            return True
        return False
    except Exception as e:
        print(f"Error detecting right arrow signal: {e}")
        return False

if __name__ == "__main__":
    unicorn_black = unicornhybridblack.UnicornBlackProcess()
    unicorn_black.connect(deviceID='', rollingspan=3.0, logfilename='default')

    router = ...  # Set up the Kortex router connection here
    base = BaseClient(router)

    try:
        while True:
            if detect_up_arrow_signal(unicorn_black):
                move_arm_upwards(base)
            elif detect_down_arrow_signal(unicorn_black):
                move_arm_downwards(base)
            elif detect_left_arrow_signal(unicorn_black):
                move_arm_left(base)
            elif detect_right_arrow_signal(unicorn_black):
                move_arm_right(base)
    finally:
        unicorn_black.disconnect()