import serial
import serial.tools.list_ports

def scan():
    """
    Scans for connected micro:bits.
    Returns a list of dictionaries containing: 'port', 'serial_number', 'description'
    """
    found_devices = []
    ports = serial.tools.list_ports.comports()
    
    for port in ports:
        # 1. Check for the specific micro:bit Vendor ID (3368)
        # 2. Keep the string check as a backup for other OSs/drivers
        p_str = (str(port.description) + str(port.hwid)).lower()
        
        # Check VID 3368 (Micro:bit common) or string match
        if port.vid == 3368 or "microbit" in p_str or "mbed" in p_str:
            device_info = {
                "port": port.device,
                "serial_number": port.serial_number,
                "description": port.description
            }
            found_devices.append(device_info)
            
    return found_devices

def find(interactive=True):
    """
    Finds a micro:bit and returns the port name (e.g., 'COM3') as a string.
    """
    devices = scan()
    
    selected = None
    
    if len(devices) == 0:
        return None
        
    elif len(devices) == 1:
        selected = devices[0]
        
    else:
        # Multiple found
        if not interactive:
            selected = devices[0]
        else:
            print(f"\n⚠️  Found {len(devices)} micro:bits:")
            for i, dev in enumerate(devices):
                print(f"   [{i}] Port: {dev['port']} | Serial: {dev['serial_number']}")
            
            while True:
                selection = input("\n   Select device number (0-9): ")
                try:
                    index = int(selection)
                    if 0 <= index < len(devices):
                        selected = devices[index]
                        break
                    print("   ❌ Number out of range.")
                except ValueError:
                    print("   ❌ Invalid input.")

    # Return just the port string (e.g., "COM3")
    return selected['port']

def connect(baudrate=115200, interactive=True, **kwargs):
    """
    Finds a micro:bit and returns a connected serial.Serial object.
    
    Args:
        baudrate (int): Defaults to 115200.
        interactive (bool): Ask user to select if multiple devices found.
        **kwargs: Extra arguments passed to serial.Serial (e.g., timeout=2).
        
    Returns:
        serial.Serial object if successful, None if not found or busy.
    """
    # 1. Find the port string
    port = find(interactive=interactive)
    
    if port is None:
        return None
        
    try:
        # 2. Create the connection
        # **kwargs passes 'timeout', 'parity', etc. directly to pyserial
        conn = serial.Serial(port, baudrate=baudrate, **kwargs)
        return conn
        
    except serial.SerialException as e:
        print(f"❌ Error: Could not connect to {port}.")
        print("   (The device might be busy or open in another app like MakeCode)")
        return None
