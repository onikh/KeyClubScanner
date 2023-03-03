import keyboard
from pyzbar import pyzbar

barcode = ''

while True:
    event = keyboard.read_event()

    if event.event_type == 'down':
        if event.name == 'enter':
            # Barcode has been scanned
            barcodes = pyzbar.decode(barcode.encode('utf-8'))

            for barcode in barcodes:
                print(barcode.data.decode('utf-8') + "is the student's ID.")

            barcode = ''
        else:
            # Add character to barcode string
            barcode += event.name
