import serial.tools.list_ports

def scan():
    """
    Scans for connected micro:bits.
    Returns a list of dictionaries containing: 'port', 'serial_number', 'description'
    """
    found_devices = []
    ports = serial.tools.list_ports.comports()
    
    for port in ports:
        # Normalize descriptions for easier matching
        p_str = (str(port.description) + str(port.hwid)).lower()
        
        # Check for standard micro:bit signatures
        if "microbit" in p_str or "mbed" in p_str:
            device_info = {
                "port": port.device,
                "serial_number": port.serial_number,
                "description": port.description
            }
            found_devices.append(device_info)
            
    return found_devices

def find(interactive=True):
    """
    Smart Selector:
    1. If 0 devices found -> Returns None
    2. If 1 device found  -> Returns that device dict automatically
    3. If >1 devices found -> 
       - If interactive=True: Asks user to type a number to select.
       - If interactive=False: Returns the first one found.
    """
    devices = scan()
    
    if len(devices) == 0:
        return None
    
    if len(devices) == 1:
        # Auto-select the only one
        return devices[0]
    
    # --- Multiple Devices Logic ---
    if not interactive:
        return devices[0]

    print(f"\n⚠️  Found {len(devices)} micro:bits:")
    for i, dev in enumerate(devices):
        print(f"   [{i}] Port: {dev['port']} | Serial: {dev['serial_number']}")
    
    while True:
        selection = input("\n   Select device number (0-9): ")
        try:
            index = int(selection)
            if 0 <= index < len(devices):
                return devices[index]
            else:
                print("   ❌ Number out of range.")
        except ValueError:
            print("   ❌ Invalid input. Please enter a number.")
