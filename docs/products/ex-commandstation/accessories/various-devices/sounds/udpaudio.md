# UDP Audio Driver for DCC-EX

UDPAudio is a HAL driver that enables UDP network audio control for Waveshare ESP32-S3 audio nodes (or any compatible UDP audio device). It allows **DCC-EX** to control multiple audio nodes simultaneously over WiFi, supporting play, stop, pause, resume, volume, and folder selection commands with full WAITFOR feedback.

## Features

| Feature | Status | Description |
| --------- | -------- | ------------- |
| UDP broadcast control | ✅ | Send commands to all nodes simultaneously |
| WAITFOR support | ✅ | Blocks **EXRAIL** until audio completes |
| Folder selection | ✅ | Switch between `/trains/`, `/music/`, `/soundfx/`, `/other/` |
| Volume control | ✅ | 0-30 DCC-EX scale (mapped to 0-100 on node) |
| Pause/Resume | ✅ | Pause and resume playback |
| Stop | ✅ | Stop playback immediately |
| Lazy UDP init | ✅ | No network overhead until first command |
| Multi-node support | ✅ | Up to 6 nodes (scalable) |
| RESET blocking | ✅ | Prevents Waveshare SD card bug |

## Installation

The UDPAudio is connected to a number of separate WaveShare tracks by defining VPINs in myAutomation.h

You can create a consecutive range of VPINS with a single HAL statement and also have multiple HAL statements for other pins or ranges.
The vpin numbers will be broadcast to waveshare devices which are responsible for recognizing their own vpin.

```cpp
// Node 1: Station (VPIN 11000)
HAL(UDPAudio, 11000)

// Node 2: Yard (VPINs 12000-1203)
HAL(UDPAudio, 12000, 4)
```

As for any other VPINs you may create aliases

```cpp
ALIAS(STATION_SPEAKER, 11000)
ALIAS(YARD_BACKGROUND, 12000)
ALIAS(YARD_WELDING, 12001)
ALIAS(YARD_HAMMERING, 12002)
ALIAS(YARD_WORKERS_CHOIR_REHERSAL, 12003)
```

## Playing sounds

Refer to the  [Sounds page](sounds.md)

## WaveShare implementation details

### Track numbers

| Parameter | Range | Description |
| ----------- | ------- | ------------- |
| track | 1-999 | MP3 file number (001.mp3, 002.mp3, etc.) |
| volume | 0-30 | DCC-EX scale (mapped to 0-100 on node) |

### Folders

```cpp
PLAY_FOLDER(STATION_SPEAKER, folder)
```

| Parameter | Value | Folder Path |
| ----------- | ------- | ------------- |
| folder | 1 | `/trains/` |
| folder | 2 | `/soundfx/` |
| folder | 3 | `/music/` |
| folder | 4 | `/other/` |

## Internal Imnplementation Details UDP Protocol

### Outbound (DCC-EX → Node)

Format:`<A vpin track volume opcode folder>`

| Parameter | Range | Description |
| ----------- | ------- | ------------- |
| vpin | 11000-16000 | Virtual pin identifier |
| track | 0-999 | Track number (0 for non-play commands) |
| volume | 0-30 | DCC-EX volume scale |
| opcode | 6,13,14,15,22,23 | Command type |
| filder | 0-4 | Folder number (0 \= current) |

### Opcode Mapping

| OPCODE | **EXRAIL** Command | Notes |
| -------- | ---------------- | ------- |
| 15 | `PLAY_TRACK` | Plays specified track |
| 14 | `PLAY_PAUSE` | Pauses playback |
| 13 | `PLAY_RESUME` | Resumes playback |
| 22 | `PLAY_STOP` | Stops playback |
| 6 | `PLAY_VOLUME` | Sets volume |
| 23 | `PLAY_FOLDER` | Changes folder |
| 12 | `RESET` | Not transmitted – hardware bug |

### Inbound (Node → DCC-EX)

`<z vpin >` (busy) or `<z -vpin>` (idle)

This feedback enables WAITFOR and IF statements in **EXRAIL**.

## VPIN Allocation

| Node | VPIN Base | IP Address | Scenescape | Example |
| ------ | ----------- | ------------ | ------------ | --------- |
| 1 | 11000 | 192.168.1.111 | Station | `PLAY_TRACK(11000, 1, 20)` |
| 2 | 12000 | 192.168.1.112 | Yard | `PLAY_TRACK(12000, 1, 20)` |
| 3 | 13000 | 192.168.1.113 | Platform | `PLAY_TRACK(13000, 1, 20)` |
| 4 | 14000 | 192.168.1.114 | Maintenance | `PLAY_TRACK(14000, 1, 20)` |
| 5 | 15000 | 192.168.1.115 | Carriage Shed | `PLAY_TRACK(15000, 1, 20)` |
| 6 | 16000 | 192.168.1.116 | Engine Shed | `PLAY_TRACK(16000, 1, 20)` |

## Network Requirements

| Setting | Value |
| --------- | ------- |
| Protocol | UDP |
| Port | 5000 |
| Destination | Broadcast or specific IP |
| Node IPs | Static recommended (192.168.1.111-116) |
| DCC-EX IP | Static (must match node config) |

## Troubleshooting

### Issue: No audio plays

Check:

- Waveshare node has power and SD card
- DCC-EX is connected to WiFi
- UDP port 5000 is not blocked
- Node IP is correct in driver (broadcast works)

### Issue: Folder changes don't work

Check:

- Using v1.04 or later (folder fix in param1)
- Waveshare has folders: `/trains/`, `/music/`, `/soundfx/`, `/other/`
- Folder command sent before play command
