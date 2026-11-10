# Build GBARunner3 — B/Y to A/B

This repository contains the customized button input file and an automated GitHub Actions build workflow. It **does not require you to download the prebuilt `.nds`**.

## Requirements

- A GitHub account and a repository containing these files
- GitHub Actions enabled for that repository
- No local compiler installation is needed when using GitHub Actions

## Build with GitHub Actions

1. Open the repository in GitHub.
2. Select **Actions** at the top.
3. Select **Build GBARunner3 B/Y to A/B for DSpico** on the left.
4. Select **Run workflow**, leave `main` selected and confirm **Run workflow**.
5. Open the new run after it finishes. A **green check** means the build completed; a red X means there was an error.
6. On the run summary page, scroll to **Artifacts** and download **GBARunner3-BY-to-AB-DSi**. Note: the number next to "Artifacts" is a count, not the download link.
7. Extract the downloaded ZIP. The compiled executable is `/_pico/emulators/GBARunner3.nds` inside it.
8. Back up the existing `.nds` on your SD card before replacing anything.

## What the workflow does

- Checks out the [dhorlick/GBARunner3](https://github.com/dhorlick/GBARunner3) `develop` branch and its submodules.
- Replaces `code/core/arm9/source/Peripherals/Input.s` with the optimized `patches/Input.s.modificado` input handler from this repository.
- Builds the emulator with `devkitpro/devkitarm:20241104` using `make -C emulator/code`.
- Produces a downloadable ZIP containing `/_pico/emulators/GBARunner3.nds`.

## Button layout

| Physical Nintendo DS button | GBA input |
| --- | --- |
| B | A |
| Y | B |
| D-pad, L, R, Start, Select | Unchanged |

## Important notes

- This was tested by the repository owner on **one Nintendo DSi using DSpico/Pico Launcher**. Other devices have not been verified.
- The upstream `develop` branch can change. A newly built executable may therefore not be bit-for-bit identical to the previously tested build.
- The workflow may fail if the upstream build or toolchain changes in the future. Check the first red step in the GitHub Actions run if that happens.
- Do not replace your BIOS, ROMs, saved games or `gbarunner3.json` when installing the remapped executable.
- This is an unofficial, AI-assisted modification; it is not part of the official GBARunner3 development team.
