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

---

### Task 11: Active Participation  

I actively participated in the **GeeksforGeeks Bengaluru Workshop Series** under the Nation SkillUp initiative. The workshops topic MERN development.  During the sessions, I gained practical experience in designing and deploying applications. Alongside learning, I actively engaged in activities and won a **quiz competition**, earning a **GfG T-shirt** as a reward.  
I also received a **certificate of participation** for successfully attending the workshop.  
 Certificate: ![GFG Certificate](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/GFG%20cert%201.jpeg?raw=true)  
 T-shirt Reward: ![GFG T-shirt](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/GFG%20cert%202.jpeg?raw=true)  

---

### Task 12: 3D Printing  

For this task, I learned about the **working of a 3D printer** theory and its main components such as the extruder, filament, print bed, and controller board. I understood how the process works in three stages – **designing (STL file)**, **slicing (using software like Ultimaker Cura or Creality Slicer)**,  and **printing** where material is added layer by layer. I also studied the **different types of 3D printing technologies** like FDM, SLA, and SLS, along with the materials used in each. 
![3D Printing GIF](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/Task%201%203D%20prinitng%20GIF.gif?raw=true)  


---

### Task 13: Build Your Own Brain - Linear Regression from Scratch  

In this task, I implemented **Linear Regression manually** using Gradient Descent and compared it with the **Scikit-learn implementation**. The goal was to predict house values based on median income using the California Housing dataset.  
- **Manual Gradient Descent**: Started with random slope and intercept, updated them step by step to reduce error.  
- **Scikit-learn**: Used built-in LinearRegression which gives results instantly using matrix algebra.  
- **Comparison**: Both models gave similar best-fit lines, but sklearn was faster and more optimized.  
I plotted the real data, my manual regression line (red), and sklearn’s regression line (green dashed).  

![Linear Regression Plot](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/Task%206%20Linear%20Regression%20from%20scratch.png?raw=true)  

---

### Task 14: The Matrix Puzzle — Decode with NumPy & Reveal the Image  
In this task, I decoded a **scrambled matrix** to reveal a hidden image using **NumPy** and **Matplotlib**.  
- First reshaped the scrambled 1D array into a square matrix.  
- Then transposed and flipped it to fix the orientation.  
- Finally, visualized the corrected image with matplotlib.  
This helped me practice reshaping, slicing, transposing, and flipping arrays with NumPy.  
![Matrix Puzzle Result](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/Task%207%20Matrix%20Puzzle.png?raw=true)  

---

### Task 15: Speed Control of DC Motor  

In this task, I explored how to control the **speed of a DC motor** using an **Arduino UNO** and the **L298N Motor Driver (H-Bridge)**. The key idea was that the motor’s speed depends on the applied voltage, and by using **PWM (Pulse Width Modulation)** from Arduino, I could smoothly vary the average voltage and thus control the speed.  

I first simulated the setup in **Tinkercad** and then tested it on hardware with a **5V BO motor**. The L298N module was used to manage both **direction** (IN1/IN2 pins) and **speed** (ENA pin connected to Arduino’s PWM). A simple Arduino sketch was written to gradually increase and decrease the motor speed, demonstrating smooth acceleration and deceleration.  

This activity helped me understand the **working of PWM in speed control**, **motor driver interfacing**, and the importance of an external power supply for better torque.  

Project Image:  
![DC Motor Speed Control](https://github.com/dedlinux777/uvce-marvel-tasks/blob/main/assets/TASK%2010%20Speed%20Control%20of%20DC%20Motor.jpeg?raw=true)  


# Conclusion  

Completing Level 0 tasks gave me practical exposure to different domains, improved helped me become comfortable with tools of different domains.
