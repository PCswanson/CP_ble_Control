# CircuitPython Controller and NeoPixel Color Picker Example
# Based on code by Adafruit, modified by Mr. Swanson

import board
import neopixel
from time import sleep
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.color_packet import ColorPacket
from adafruit_bluefruit_connect.button_packet import ButtonPacket

# set up bluetooth instance
ble = BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)

# set up neopixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)

# Main loop
while True:
    # Advertise when not connected.
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass
    ble.stop_advertising()

    while ble.connected:
        packet = Packet.from_stream(uart_server)
        # Check if packet is for the colorpicker or controller
        if isinstance(packet, ColorPacket):
            print(packet.color)
            pixels.fill(packet.color)
        elif isinstance(packet, ButtonPacket):
            # Select action based on which button is pressed
            if packet.button == '1':
                print("Button 1")
            elif packet.button == '2':
                print("Button 2")
            elif packet.button == '3':
                print("Button 3")
            elif packet.button == '4':
                print("Button 4")
            elif packet.button == '5':
                print("UP")
            elif packet.button == '6':
                print("DOWN")
            elif packet.button == '7':
                print("LEFT")
            elif packet.button == '8':
                print("RIGHT")
        sleep(1)
