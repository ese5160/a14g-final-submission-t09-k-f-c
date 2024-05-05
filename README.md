[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/kzkUPShx)
# a14g-final-submission

    * Team Number: 09
    * Team Name: K.F.C.
    * Team Members: Chen Chen, Kexin Shu
    * Github Repository URL: https://github.com/ese5160/a14g-final-submission-t09-k-f-c
    * Description of test hardware: (development boards, sensors, actuators, laptop + OS, etc) 

## 1. Video Presentation

## 2. Project Summary

### 2.1 Device Description

The core vision of our FRIDGIT software is to "simplify and streamline fridge management." The primary functionality of this system revolves around tracking food quantities, logging purchase dates, and issuing expiration reminders. Our system's software is bifurcated into two main components: the Server Software (SS) and the Device Software (DS). Both are equipped with intuitive user interfaces (UIs) designed for ease of use.

This innovative solution employs a QR Code Reader to scan and record the quantity and expiration date of each food item, all of which are uniquely identified with QR codes. The information is then elegantly displayed on an LCD screen, offering users a clear and real-time overview of their remaining food inventory. To enhance user experience and energy efficiency, an Ambient Light Sensor intelligently controls the LCD screen's brightness. Additionally, a 3-Channel Touch Interface, featuring buttons and sliders, allows users to navigate menus and customize settings with ease.

Furthermore, when scanning a QR code, a buzzer will sound to indicate successful scanning. Additionally, when buttons are pressed or QR codes are scanned, a red LED will illuminate. During normal operation, a green LED will be lit, indicating that the device is functioning. In sleep mode, the green LED will be turned off to conserve energy.

The FRIDGIT system is designed for individuals who find it challenging to keep an accurate mental inventory of their refrigerator's contents. This issue becomes particularly pronounced in households where the fridge is consistently well-stocked, leading to items being forgotten and, regrettably, spoiling. Such neglect not only results in wastage but also poses potential health risks and can negatively affect the quality of other items stored nearby.

Additionally, our system's multi-user capability proves invaluable for those sharing living spaces, such as roommates. FRIDGIT adeptly manages the collective inventory, providing each user with a clear and organized view of their specific food items. This is achieved despite the shared physical storage, ensuring that each user can easily identify and track their groceries.

### 2.2 Inspiration

The idea of our project FRIDGIT born out of the necessity for organized living in shared spaces. In our communal living scenario, where the refrigerator tends to accumulate diverse food items over time, the system is designed to combat forgetfulness and prevent food wastage.

### 2.3 Device Functionality
- Hardware: The device is centered around the SAMW25 microcontroller and integrates key hardware components including the ambient light sensor, a LCD, 3-channel touch sensor, and the QR Code reader.

- Software: SS features a cloud-based UI, enabling users to remotely monitor their food inventory. In contrast, DS boasts a device-resident UI, which facilitates the addition and removal of food items from the system, thereby providing a local inventory checklist. These interfaces are tailored to empower users with seamless management of their fridge contents, whether they are adding new purchases or tracking existing items. Furthermore, the software architecture is crafted to accommodate multiple users, ensuring a collaborative and shared management experience. This is particularly beneficial for households or shared living spaces where fridge contents are communal.
- Challenges

- Prototype Learnings

- Next Steps

- Takeaways from ESE5160

- Project Links
  - URL to your Node-RED
  - A12G code repository
  - final PCBA on Altium 365
## 3. Hardware & Software Requirements

### 3.1 Hardware Requirements Specification (HRS)

- **HRS 01** - Project shall be based on SAMW25 microcontroller

- **HRS 02** - VEML6030 Ambient Light Sensor shall be used for adjusting screen brightness. When the light intensity increases, the screen brightness increases; when the light intensity decreases, the screen brightness decreases.

- **HRS 03** - 1.8" diagonal LCD TFT display shall be used for user interface. LCD can display user and menu interface

- **HRS 04** - button

- **HRS 05** - 5744 QR Code reader to I2C shall be used to scan and read QR codes on items in the refrigerator. Each item may be identified by a unique QR code, and the system can identify the item and update inventory information through a QR code reader. 

- **HRS 06** - Buzzer shall beep when QR code reader scans to make inventory-in.

### 3.2 Software Requirements Specification (SRS)

- **SRS 01** - The Server Software (SS) and Device Software (DS) shall establish connectivity via Wi-Fi, enabling seamless data transmission and reception between them.

- **SRS 02** - SS shall be operational on personal computers, while DS shall be operational on the designated hardware device.

- **SRS 03-1**

   \- DS shall feature a mode selection interface, presenting users with options including:

  - (a) User Selection: This mode allows a user to select their profile from a list of users.
  - (b) Food Log-In: In this mode, DS is ready to register new food items and update their quantities.
  - (c) Food Log-Out: This mode enables DS to decrement the food quantities, reflecting items removed from the fridge.

- **SRS 03-2**

   \- The mode selection interface of DS should offer:

  - (a) Expiration Alarm Setting: Users can configure the advance notice period for food expiration alerts.

- **SRS 04** - DS shall incorporate a "database" to systematically store user, food, and settings information. This database will employ a specific data structure, such as linked lists, for other efficient data organization.

- **SRS 05** - DS shall be tasked with calculating expiration dates and persistently displaying reminder banners. To ensure .'s exhibition effect, the DS should verify expiration status at a minimum frequency of once per second and synchronize these reminders with SS upon request.

- **SRS 06** - DS shall maintain a dynamic dictionary to encode each food item within the fridge. Each food type shall be assigned a unique identifier within this dictionary, which is then stored in the DS database.

- **SRS 07-1**

   \- SS shall provide a user interface (UI) capable of:

  - (a) Identifying and displaying the current user.
  - (b) Showcasing comprehensive details of the food items registered in the DS database.

- **SRS 07-2**

   \- The UI of SS should facilitate:

  - (a) The registration of new users and the de-registration of existing users.

- **SRS 08** - SS should possess the capability to retrieve on-line recipes via an API, curate recommended recipes, and dispatch these to DS.

- **SRS 09** - SS should ensure mobile device compatibility and accessibility.


## 4. Project Photos & Screenshots
- Final Project:
- The standalone PCBA, top
- The standalone PCBA, bottom
- Thermal camera images
- The Altium Board design in 2D view
- The Altium Board design in 3D view
- Node-RED dashboard
  ![Node-RED_dashboard](img\Node-RED_dashboard.png)
- Node-RED backend
  ![Node-RED_test](img\Node-RED_test.png)
  ![Node-RED_MQTT](img\Node-RED_MQTT.png)
- Web frontend (additional)
  ![NiceGUI_User](img\NiceGUI_User.png)
  ![NiceGUI_Stock](img\NiceGUI_Stock.png)
- Block diagram