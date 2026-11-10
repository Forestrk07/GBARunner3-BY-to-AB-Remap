# GBARunner3 — B/Y to A/B Button Remap 🎮

> **Unofficial, AI-assisted modification of GBARunner3.**  
> **Tested on a Nintendo DSi using DSpico / Pico Launcher.** Other models have not been tested.

## What does it change?

This modification changes the Nintendo DS button layout when playing Game Boy Advance games through GBARunner3:

| Nintendo DS button | Game Boy Advance input |
|---|---|
| **B** | **A** |
| **Y** | **B** |

The D-pad, L, R, Start and Select retain their original functions. The original physical A and X buttons are not assigned to the GBA A/B functions in this customized layout.

Important: If you download GBARunner3-buttons-changed.nds from this repository, rename it to GBARunner3.nds before installing it.

## Why did I make this?

I'm simply someone who wanted to play Game Boy Advance games on my Nintendo DSi. However, having the B and Y buttons mapped to GBA A and B was an absolute necessity for me, as I find that layout much more comfortable to use.

Since I couldn't find a way to configure this button layout in the original GBARunner3 project, and I have absolutely no programming experience, **I decided to use ChatGPT to make the modification for me.**

ChatGPT handled the technical side of the modification, including investigating the source code, preparing the changes, troubleshooting compilation errors, and providing build instructions. I simply followed those instructions, ran the GitHub Actions builds, and tested the resulting program on my own Nintendo DSi.

I am **not affiliated with the official GBARunner3 development team**. This is simply a personal modification made with AI assistance that I'd like to share because I believe I'm not the only one who prefers this button layout.

## Testing status

- **Hardware tested:** One Nintendo DSi
- **Launcher:** DSpico / Pico Launcher
- **Result:** The requested B → A and Y → B mapping worked during my testing
- **Not yet tested:** Original Nintendo DS, Nintendo DS Lite and other setups

This is a personal test result, **not** a guarantee that every game or console model will work.

## Credits

- **[Gericom](https://github.com/Gericom/GBARunner3)** — Creator and maintainer of the original GBARunner3 project.
- **[dhorlick](https://github.com/dhorlick/GBARunner3/releases/tag/y2b)** — Author of the experimental Y-to-B modification used as a starting point.

## Build your own `.nds`

If you'd rather build the modified emulator yourself instead of downloading a precompiled file, follow **[BUILD.md](BUILD.md)**. The GitHub Actions workflow uses the [dhorlick Y-to-B fork](https://github.com/dhorlick/GBARunner3) as a base, applies the B/Y-to-A/B modification and compiles the Nintendo DS executable.

## Installation on the tested setup

1. Back up the SD card and the existing `/_pico/emulators/GBARunner3.nds` file.
2. Copy the modified `GBARunner3.nds` to `/_pico/emulators/` on the DSpico SD card, replacing only that executable.
3. Launch a GBA game through Pico Launcher and test the buttons.
4. If it does not work as expected, restore the original `.nds`.

No commercial ROMs, save files or BIOS files are included in this project. The separate `gbarunner3.json` display settings are not changed by this button remap.
