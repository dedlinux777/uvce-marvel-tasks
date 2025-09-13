# Marvel Tasks Report  
*Level 0*  
*Date: 12/09/2025*  

The following tasks were assigned under Marvel Level 1. These tasks helped me explore multiple technical domains and gain hands on experience. My learnings and implementations are explained below.  

---

## Task 1: Working with GitHub  

In this task, I worked with GitHub to understand how **Issues, Pull Requests, and GitHub Actions** work together in a project. The goal was to fix an error in the main branch of the given repository and submit a Pull Request with the correction.  

Through this task, I learned: 
How to fork a repository and create my own copy, cloning the repository to my local system and made changes in the new branch, identified the bug in the code and I resolved it, next commit and push the changes to Github by creating a **Pull Request** that I've fixed the bug in the code.

**Screenshots**:
![Comparing changes](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/TASK%203%20Working%20with%20Github%202.png?raw=true) ![Pull request](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/TASK%203%20Working%20with%20Github%203.png?raw=true)

---

## Task 2: Get Familiar with the Command Line on Ubuntu  

In this task, I explored the basic usage of the **command line in Ubuntu**,
I practiced different commands such as mkdir, cd, touch, ls, echo, cat etc...
### Steps I Performed  
- Created a folder named **test** and moved inside it.  
- Created a blank file using `touch`.  
- Listed the contents of the folder using `ls`.  
- Created 2600 folders with unique names using the `mkdir` command.  
- Made two text files (`file1.txt` and `file2.txt`) with random text and concatenated them into a new file `concat.txt`.  
- Displayed the combined result on the terminal.  
### Screenshots :
1. ![Ubuntu Commands 1](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/TASK%204%20Ubuntu%201.png?raw=true)  
2. ![Ubuntu Commands 2](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/TASK%204%20Ubuntu%202.png?raw=true)  

---

## Task 3: Karnaugh Maps and Deriving the Logic Circuit  

In this task, I learned how to use **Karnaugh Maps (K-Maps)** to simplify Boolean expressions and design a simple burglar alarm circuit.  
The burglar alarm should work based on the whether the **door is locked or open**, whether the **key is pressed or not pressed**.  By using these conditions on a **4-variable K-Map**, I identified the simplified Boolean expression for the output. This logic was then used to design a circuit using **logic gates**. 

### Image:
![K-Map Solution](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/Task%2014%20Kmap.png?raw=true)  

---

## Task 4: Tinkercad  

In this task, I learned how to use Tinkercad to simulate Arduino circuits virtually. I created a simple circuit with **Arduino UNO** where an **Ultrasonic Sensor** was connected along with **I2C LCD Display**. The purpose of the circuit was to measure the distance between the sensor and an obstacle, and then display the result on the LCD screen. The working principle was simple: the ultrasonic sensor sends a trigger pulse, and the time taken for the echo to return is measured. Using the formula  
**Distance (cm) = (Time × Speed of Sound) / 2**,  
the distance is calculated is displayed on the LCD, and I have used a code by referring sites .  

### Screenshot :
![Tinkercad Simulation](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/Task%209%20Tinkercad.png?raw=true)  

---

## Task 5: Sad Servers – Command Line Murders  

In this task, I worked on a **Linux troubleshooting challenge** called *Sad Servers*. The scenario was a “Command Line Murder Mystery,” where I had to investigate a crime using only Linux commands. I changing given directories and files, then searched for the first clues using the `grep` command. The crimescene file revealed initial hints that guided to murderer. By checking the **people**, **streets**, and **interviews** files, I located witness named Annabel, then revealed**vehicles** file using filters to filter cars that matched the description of a “Blue Honda” with a specific license plate. Once I found the matching car, I looked for its owner. The final step was to confirm the suspect through multiple membership files, which pointed to the criminal named **Jeremy Bowers**, which solved the case challenge.

### Screenshots:
![Intial Clue](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/Task%2018%20Sad%20Servers%200.png?raw=true) 
![Important Clue](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/Task%2018%20Sad%20Servers%201.png?raw=true) 
![Found murderer](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/Task%2018%20Sad%20Servers%204.png?raw=true) 

---


---

## Task 6: Writing Resource Article using Markdown  

In this task, I explored **Markdown** as a simple way to format technical articles. I wrote an article on the topic *“Process vs. Thread: OS Concepts Simplified”*, where I explained the differences between processes and threads with examples, a comparison table, and short Python demos.  Markdown made it easy to add headings, tables, code blocks, and images without using HTML. This helped me understand how Markdown can be used for technical documentation and publishing resources online.  

You can read the full article here:  
[Process vs. Thread: OS Concepts Simplified](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/Level%200/process-mutlithreading.md)  

---

### Task 7: Portfolio Webpage Report  

For this task, I built a **responsive portfolio website** using **React** and **Bootstrap**.  The site showcases my profile, interests, projects, and social links with a clean design.  A dynamic gradient background changes with user interaction.

Portfolio Link: [harsha-portfolio-taupe.vercel.app](https://harsha-portfolio-taupe.vercel.app/)  

---

### Task 8: API Report  

For this task, I built a simple web app called **Scanalyze** using the **VirusTotal API**.  
The app can scan both **URLs** and **files** to check if they contain any malicious content. 
App Link: [Scanalyze](https://scanlyze-roan.vercel.app/)  
Referred site for VirusTotal Python API Docs: [vt-py Quickstart](https://virustotal.github.io/vt-py/quickstart.html#get-information-about-a-file)  

---

### Task 9: LED Toggle Using ESP32  

For this task, I worked with the **ESP32 microcontroller** and learned how to create a web server to control an LED through its GPIO pins. I Installed and configured **Arduino IDE** with ESP32 board support. Connected the ESP32 board and verified communication with the IDE. Wrote and uploaded a program that created a simple web server. Served an HTML page with **ON/OFF buttons**. Accessed the ESP32’s **IP address** via a browser. Controlled an LED connected to ESP32 GPIO pins based on user input.  

![ESP32 toggling LED's](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/ESP%2032%20GIF.gif?raw=true)

---

### Task 10: Datasheets Report Writing  

For this task, I studied the **MQ-135 Gas Sensor** and prepared a detailed report covering its working principle, pin configuration, gas calibrations, and the Freundlich Adsorption Isotherm graph. The report also explains its applications, advantages, and limitations in air quality monitoring and IoT-based systems.  

Full Report: [MQ-135 Gas Sensor Task Report](http://github.com/dedlinux777/uvce-marvel-tasks/blob/main/Level%200/MQ135%20Gas%20sensor%20task%20report.md)  




# Conclusion  
Completing Level 1 tasks gave me practical exposure to different domains, improved my problem-solving skills, and helped me become comfortable with tools like [list tools/technologies you used]. I look forward to advancing to the next levels and exploring more.  
