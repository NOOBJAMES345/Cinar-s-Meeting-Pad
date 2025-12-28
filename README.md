# Cinar's Meeting Pad (Hack Club Blueprint)

This is a custom RP2040-based macropad designed to streamline meetings. 
It features 6 mechanical switches, a rotary encoder for volume control, and an OLED display.
The design is complete and ready for assembly once the parts are received.

## Hardware Specifications
- **Controller:** Seeed XIAO RP2040
- **Display:** 128x64 OLED (I2C)
- **Encoder:** 2-phase Rotary Encoder (No push button)
- **Switches:** 6x Mechanical Switches (Cherry MX style)

## Pinout
- **Buttons (SW1-6):** GP1, GP2, GP4, GP3, GP0, GP28
- **Encoder:** A: GP27, B: GP29
- **OLED:** SDA: GP6, SCL: GP7

## Firmware
The firmware is built using **KMK** on **CircuitPython**. 
The configuration is optimized for meeting shortcuts (Mute, Camera, Volume).

## Visuals
<img width="1385" height="754" alt="Macropad" src="https://github.com/user-attachments/assets/15301c08-44a4-4fc0-bedc-ea94af4f8d21" />
<img width="1385" height="754" alt="Macropad2" src="https://github.com/user-attachments/assets/e2404488-04b2-47e4-8373-c450ce2d5ce3" />
