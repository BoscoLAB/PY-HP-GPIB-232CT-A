import serial
import time
import os

def load_hpgl_file(filepath):
    """
    Load an HPGL file and split commands by semicolon.
    """
    with open(filepath, 'r') as file:
        data = file.read()
    return [cmd + ';' for cmd in data.split(';') if cmd.strip()]

def process_commands(commands):
    """
    Process commands to split `PD` or `PU` commands into standalone `PA x,y;` commands.
    """
    processed_commands = []
    for command in commands:
        if command.startswith("PD") or command.startswith("PU") or command.startswith("PA"):
            # Extract coordinates from the command
            prefix = command[:2]
            processed_commands.append(prefix+";")
            coordinates = command[2:].strip(";").split(",")
            # Create individual PA commands for each coordinate pair
            for i in range(0, len(coordinates), 2):
                if i + 1 < len(coordinates):  # Ensure pairs exist
                    x, y = coordinates[i], coordinates[i + 1]
                    processed_commands.append(f"PA {x},{y};")
        else:
            processed_commands.append(command)
    return processed_commands

def send_command(ser, command, address, debug_file=None):
    """
    Send a command to the serial device or write to debug file.
    """
    def write_debug(data):
        if debug_file:
            debug_file.write(data)

    try:
        # Step 1: Send "wrt <address>" and CR
        wrt_command = f"wrt {address}\r"
        if ser:
            time.sleep(0.001)
            ser.write(wrt_command.encode())
        write_debug(wrt_command)
        print(wrt_command.encode())

        # Step 2: Send the actual command and CR
        actual_command = f"{command}\r"
        if ser:
            time.sleep(0.001)
            ser.write(actual_command.encode())
        print(actual_command.encode())
        write_debug(actual_command)

        # Step 3: Send "wrt <address>" and CR, then "OE" and CR
        wrt_oe_command = f"wrt {address}\r"
        oe_command = "OE;\r"
        if ser:
            time.sleep(0.001)
            ser.write(wrt_oe_command.encode())
            time.sleep(0.001)
            ser.write(oe_command.encode())
        write_debug(wrt_oe_command)
        print(wrt_oe_command.encode())
        write_debug(oe_command)
        print(oe_command.encode())
        # Step 4: Send "rd #1,<address>" and CR
        rd_command = f"rd #1,{address}\r"
        if ser:
            time.sleep(0.001)
            ser.write(rd_command.encode())
        write_debug(rd_command)
        print(rd_command.encode())

        # Step 5: Wait for a reply
        reply = ""
        if ser:
  #          while reply == "":
            reply = ser.readline()
            time.sleep(0.001)
        else:
            
            reply = "0"  # Simulated reply for debug
        
        print(reply)
        reply = reply.decode().strip()
        #print(f"Reply: {reply}")
        write_debug(f"Reply: {reply}\n")

        # Step 6: Check the first character of the reply
        if reply and reply[0].isdigit() and int(reply[0]) >= 1:
            print(f"Device reply indicates pause: {reply}")
            time.sleep(1)  # Pause before resuming
        else:
            print(f"Device reply indicates continue: {reply}")
    except Exception as e:
        print(f"Error during communication: {e}")

def main():
    # Load HPGL commands
    filepath = input("Enter the path to the HPGL file: ").replace('"', '')
    if filepath=="":
        default = True
        filepath='C:/Users/Bosco/Nextcloud/Projekte/BoscoFab_3/Plotter_Code HPIB/shuttle.hpgl'
    else:
        default = False
    if not os.path.exists(filepath):
        print("File not found!")
        return
    commands = load_hpgl_file(filepath)
    print(f"Loaded {len(commands)} commands from {filepath}.")

    # Process commands
    processed_commands = process_commands(commands)
    print(f"Processed into {len(processed_commands)} standalone commands.")

    if default:
        address = 5
    else:
        address = input("Enter the device address (e.g., 5): ")
    # Configure serial connection or debug mode
    debug_mode = input("Enable debug mode (write to file instead of serial)? (yes/no): ").strip().lower() == "yes"
    debug_file = None
    ser = None

    if debug_mode:
        if default:
            debug_filepath='C:/Users/Bosco/Nextcloud/Projekte/BoscoFab_3/Plotter_Code HPIB/debug.output'
        else:
            debug_filepath = input("Enter the debug file path: ").replace('"', '')
        debug_file = open(debug_filepath, 'w')
        print(f"Debug mode enabled. Writing to {debug_filepath}.")
    else:
        if default:
            com_port = "COM7"
        else:
            com_port = input("Enter the COM port (e.g., COM3): ")
        try:
            ser = serial.Serial(
                port=com_port,
                baudrate=38400,
                bytesize=serial.SEVENBITS,
                stopbits=serial.STOPBITS_ONE,
                parity=serial.PARITY_NONE,
                timeout=30,
                rtscts=True,
                dsrdtr=True,
            )
            print(f"Connected to {com_port}.")
            ser.write(f"wrt {address}\r".encode())
            ser.write("OE;\r".encode())
            ser.write(f"rd #1,{address}\r".encode())
        except serial.SerialException as e:
            print(f"Failed to open serial port: {e}")
            return

    # Send each command
    for command in processed_commands:
        send_command(ser if not debug_mode else None, command, address, debug_file)

    print("All commands sent.")

    # Cleanup
    if ser and ser.is_open:
        ser.close()
        print("Serial port closed.")
    if debug_file:
        debug_file.close()
        print("Debug file closed.")

if __name__ == "__main__":
    main()