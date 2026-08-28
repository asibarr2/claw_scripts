# RaspClaw Scripts

Example scripts for controlling a RaspClaw hexapod robot's basic movements — leaning left, leaning right, and standing up — built on top of the Adeept RaspClaw servo control library.

## Overview

This repo contains simple shell scripts that trigger corresponding Python movement routines for the RaspClaw robot. A modified `move.py` is also included, which fixes an issue where all servos activating simultaneously can overload the Raspberry Pi and cause the robot to shut off.

## Requirements

- A RaspClaw robot with the [Adeept_RaspClaw](https://github.com/adeept/Adeept_RaspClaw) package already installed and working on the robot's Raspberry Pi
- Python 3

## Setup

1. Copy this package onto your RaspClaw's Raspberry Pi.
2. Replace the `move.py` in `Adeept_RaspClaw/server/` with the one provided in `backup_code/` here — this prevents the robot from cutting out when many servos move at once.

## Usage

From this package's directory on the robot:

```bash
./lean_left.sh
./lean_right.sh
./standup.sh
```

Each script is a thin wrapper that runs the corresponding Python movement routine in `backup_code/`.

## Customizing

To modify the movement logic itself, edit the Python scripts inside `backup_code/`. These are meant as a starting point — a working example of how to move the robot's legs — not a finished behavior. Extending them into something like obstacle avoidance or object tracking is the intended next step.

## Notes

- `lean_left.sh` currently references `backup_code/lean_lef.py` — check that this matches the actual filename in `backup_code/` (looks like it may be a typo for `lean_left.py`) if the script fails to run.

## Academic use

This was built as instructional material for a robotics course. You're welcome to use and modify this code freely, but if you're a student using it for a course assignment or final presentation, make sure any changes reflect genuine understanding and effort — submitting it unmodified as original work will be recognizable as such.

Questions welcome — reach out at asibarra98@gmail.com.
