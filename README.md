# Cinar's Meeting Pad (Hack Club Blueprint)

This is a custom RP2040-based macropad designed to streamline meetings. 
It features 6 mechanical switches, a rotary encoder for volume control, and an OLED display.
The design is complete and ready for assembly once the parts are received.

## Hardware Specifications
- **Controller:** Seeed XIAO RP2040
- **Display:** 128x32 OLED (I2C)
- **Encoder:** 2-phase Rotary Encoder (No push button)
- **Switches:** 6x Mechanical Switches (Cherry MX style)

## Pinout
- **Buttons (SW1-6):** GP1, GP2, GP4, GP3, GP0, GP28
- **Encoder:** A: GP27, B: GP29
- **OLED:** SDA: GP6, SCL: GP7

## Firmware
The firmware is built using **KMK** on **CircuitPython**. 
The configuration is optimized for meeting shortcuts (Mute, Camera, Volume).

## 📂 Project Structure
- `/hardware`: KiCad PCB and Schematic files.
- `/firmware`: code.py (KMK Firmware configuration).
- `/case`: 3D design files for the enclosure.

# Notes on Hardware
In the schematic, a 128x64 OLED symbol was used because a 128x32 symbol was unavailable. However, the physical build will use a 128x32 OLED display. The pinout remains the same (I2C).

## Visuals
<img width="1385" height="754" alt="Macropad" src="https://github.com/user-attachments/assets/15301c08-44a4-4fc0-bedc-ea94af4f8d21" />
<img width="1385" height="754" alt="Macropad2" src="https://github.com/user-attachments/assets/e2404488-04b2-47e4-8373-c450ce2d5ce3" />
<img width="1004" height="688" alt="image" src="https://github.com/user-attachments/assets/d7c1492c-da9b-4d38-a5aa-eb0bbe37aefc" />
<img width="707" height="499" alt="image" src="https://github.com/user-attachments/assets/77f70d68-2dfe-4b8a-9ea9-262548f1f556" />
<img width="1398" height="513" alt="image" src="https://github.com/user-attachments/assets/ccaeacb4-e8e0-418a-9f01-5b0141e72313" />



