---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

# FRIDGIT - a GIT of your FRIDGE

    * Team Number: 09
    * Team Name: K.F.C.
    * Team Members: Chen Chen(cccc@seas.upenn.edu), Kexin Shu(kexins@seas.upenn.edu)
    * Github Repository URL: https://github.com/ese5160/a14g-final-submission-t09-k-f-c

## Project Demo

<iframe width="560" height="315" src="https://www.youtube.com/embed/FC_td5RAi3Q?si=UgLtsfkp-B2EjYaO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Project Overview

The FRIDGIT software aims to simplify fridge management by tracking food quantities, logging purchase dates, and providing expiration reminders.  It consists of two main components: the Server Software (SS) and the Device Software (DS), each featuring intuitive user interfaces for easy operation.  The system uses a QR Code Reader to scan food items, each tagged with a QR code, displaying details like quantity and expiration on an LCD screen.  An Ambient Light Sensor adjusts the screen brightness for energy efficiency, while two buttons allow for easy navigation and settings adjustment.

Designed for those struggling to maintain a mental inventory of their fridge contents, FRIDGIT is particularly useful in well-stocked households where food spoilage is common.  The system also supports multi-user environments, making it ideal for roommates to manage and track their groceries collectively, ensuring easy identification and minimal waste.

## Inspiration

The idea of our project FRIDGIT born out of the necessity for organized living in shared spaces. In our communal living scenario, where the refrigerator tends to accumulate diverse food items over time, the system is designed to combat forgetfulness and prevent food wastage.

## Device Functionality
- Hardware: The device is centered around the SAMW25 microcontroller and integrates key hardware components including the ambient light sensor, and the QR Code reader and LCD.

- Software: SS features a cloud-based UI, enabling users to remotely monitor their food inventory. In contrast, DS boasts a device-resident UI, which facilitates the addition and removal of food items from the system, thereby providing a local inventory checklist. These interfaces are tailored to empower users with seamless management of their fridge contents, whether they are adding new purchases or tracking existing items. Furthermore, the software architecture is crafted to accommodate multiple users, ensuring a collaborative and shared management experience. This is particularly beneficial for households or shared living spaces where fridge contents are communal.

## Challenges

- It is kind of tricky to design the layout of PCB due to the appearance of prototype, components' position on board, especially on a relative compact board.
- We did not consider much about the availability when designing the schematics, for each pin on MCU, to be configured as specific function (such as I2C buses). So when we were working on the board, we found us unavailable to achieve the target without doing hardware modification (such as flying wire).
- The development of I2C devices was a big challenge. We spent a lot of time studying and debugging the mechanism of different I2C devices. And we had one component (CAP1203 Touch Slider Module) that we cannot figure out the issue and we had to looking for other solutions.
- Both of our Azure virtual machines was banned by Microsoft. We had to implement it on our local service at last.
- The first version of our 3D-printed container box was short in depth, so it turned out that we cannot fit the battery into it. So we did the second version and made it in time.
- Too many to be listed...

## Prototype Learnings

- Be sure leaving "redundant functions" in PCB layout (such as extra pins).
- Add more testpoints to PCB, especially through-hole testpoints in the first design.
- In a real demo, if you can use a simpler to realize a function, do not use the complexer one.
- Get to the place in more advance at demo day to have more time to check the device.

## Next Steps

- Continuously debug the system, figure out the reason of fails and make it more robust.
- Add more features, such as cuisine recommendation.
- Reroute the PCB and fix the issues in the first version design.
- ... more to be considered ...

## Takeaways from ESE5160

- The ability to design schematics depending on datasheet.
- Drawing PCB layout using Altium Designer.
- Using debugger and serial terminal on debugging.
- Basic usage of FreeRTOS.
- Learning to make migration on different projects.
- Learning to use software frameworks; applying code by reading official documents and examples.
- Lesson-learns:
  - Read datasheet carefully before developing it!
  - Utilize logic analyzer and be careful about connection of hardware.
  - Ask others for help when trapped (especially the teacher).

## Related Links

- URL to your Node-RED: We are running node-red on local service due to the forbidden in our Azure VM. The source code of node-red and additional python web service, please see [A12G/web/](https://github.com/ese5160/a12g-firmware-drivers-t09-k-f-c/tree/main/web)
- A12G code repository: https://github.com/ese5160/a12g-firmware-drivers-t09-k-f-c
- final PCBA on Altium 365: https://upenn-eselabs.365.altium.com/designs/folder-5853D6FB-9421-4C9F-A2A8-B61DBEEFAA1B
## Hardware & Software Requirements

### Hardware Requirements Specification (HRS)

- **HRS 01** - Project shall be based on SAMW25 microcontroller

- **HRS 02** - VEML6030 Ambient Light Sensor shall be used for adjusting screen brightness. When the light intensity increases, the screen brightness increases; when the light intensity decreases, the screen brightness decreases.

- **HRS 03** - 1.8" diagonal LCD TFT display shall be used for user interface. LCD can display user and menu interface

- **HRS 04** - Two different buttons shall be used to switch the menu and to confirm the selected menu in LCD.

- **HRS 05** - 5744 QR Code reader to I2C shall be used to scan and read QR codes on items in the refrigerator. Each item may be identified by a unique QR code, and the system can identify the item and update inventory information through a QR code reader. 

- **HRS 06** - Buzzer shall beep when QR code reader scans to make inventory-in and inventory-out.

### Software Requirements Specification (SRS)

- **SRS 01** - The Server Software (SS) and Device Software (DS) shall establish connectivity via Wi-Fi, enabling seamless data transmission and reception between them.

- **SRS 02** - SS shall be operational on personal computers, while DS shall be operational on the designated hardware device.

- **SRS 03**

   \- DS shall feature a mode selection interface, presenting users with options including:

  - (a) User Selection: This mode allows a user to select their profile from a list of users.
  - (b) Food Log-In: In this mode, DS is ready to register new food items and update their quantities.
  - (c) Food Log-Out: This mode enables DS to decrement the food quantities, reflecting items removed from the fridge.

- **SRS 04** - DS shall incorporate a "database" to systematically store user, food, and settings information. This database will employ a specific data structure, such as linked lists, for other efficient data organization.

- **SRS 06** - DS shall maintain a dynamic dictionary to encode each food item within the fridge. Each food type shall be assigned a unique identifier within this dictionary, which is then stored in the DS database.

- **SRS 07-1**

   \- SS shall provide a user interface (UI) capable of:

  - (a) Identifying and displaying the current user.
  - (b) Showcasing comprehensive details of the food items registered in the DS database.

- **SRS 07-2**

   \- The UI of SS should facilitate:

  - (a) The registration of new users and the de-registration of existing users.


## Project Photos & Screenshots
- Final Project: ![alt text](<img/final project.jpg>)
- The standalone PCBA, top:![alt text](img/PCBA-1.jpg) ![alt text](img/PCBA-2.jpg)
- The standalone PCBA, bottom:![alt text](img/PCBA-3.jpg)
- Thermal camera images:![alt text](img/thermal.jpg)
- The Altium Board design in 2D view: ![alt text](img/2D.png)
- The Altium Board design in 3D view:![alt text](img/3D.png)
- Node-RED dashboard
  ![Node-RED_dashboard](img/Node-RED_dashboard.png)
- Node-RED backend
  ![Node-RED_test](img/Node-RED_test.png)
  ![Node-RED_MQTT](img/Node-RED_MQTT.png)
- Web frontend (additional)
  ![NiceGUI_User](img/NiceGUI_User.png)
  ![NiceGUI_Stock](img/NiceGUI_Stock.png)
- Block diagram:![alt text](img/detailed_block.png)