# Report on MQ-135 Gas Sensor

## Introduction
The **MQ-135 Gas Sensor** is an electronic device designed to detect and measure concentrations of various harmful gases in the air. It is widely used in air quality monitoring systems, environmental safety devices, and IoT-based solutions. The sensor utilizes a gas-sensitive resistive material, typically tin dioxide (SnO₂), whose electrical resistance changes in response to the presence of specific gases. This change in resistance is the basis for detecting and quantifying gases such as ammonia, nitrogen oxides, benzene, smoke, and carbon dioxide. The MQ-135 is valued for its affordability, ease of integration with microcontrollers, and its ability to provide both analog and digital outputs for flexible application in different environments.

---

## Features
- **Wide Detection Range:** The MQ-135 can sense a variety of gases, including ammonia (NH₃), nitrogen oxides (NOₓ), benzene (C₆H₆), smoke, and carbon dioxide (CO₂). This makes it suitable for comprehensive air quality monitoring, as it can detect multiple pollutants simultaneously.
- **Analog and Digital Output:** The sensor provides an analog output that varies proportionally with the concentration of detected gases, allowing for precise measurement. It also offers a digital output that switches between HIGH and LOW states based on a user-defined threshold, enabling simple detection scenarios.
- **Low Cost and Easy to Interface:** The MQ-135 is designed for cost-effective deployment and can be easily connected to popular microcontrollers like Arduino and Raspberry Pi. Its straightforward pin configuration and compatibility with standard voltage levels simplify integration into electronic projects.
- **High Sensitivity and Fast Response:** The sensor exhibits rapid changes in resistance when exposed to target gases, resulting in quick detection and response times. This is crucial for real-time monitoring and timely alerts in safety-critical applications.

---

## Working
The MQ-135 operates using a sensing element made of tin dioxide (SnO₂), which is mounted on a small heater inside the sensor. In clean air, the SnO₂ material has low electrical conductivity due to the absence of reactive gas molecules. When the sensor is exposed to target gases, these molecules interact with the surface of the SnO₂, altering its conductivity. Specifically, the presence of reducing gases decreases the resistance of the sensing element. This change in resistance is detected by the sensor's circuitry and converted into an electrical signal. The analog output can be interpreted as the concentration of gases in parts per million (PPM), providing quantitative data for air quality assessment.

---

## Pin Configuration
The MQ-135 sensor module typically features four pins, each serving a specific function:
1. **VCC:** Connects to a 5V power supply, providing the necessary voltage for sensor operation.
2. **GND:** Ground pin, completing the electrical circuit.
3. **DO (Digital Output):** Outputs a digital signal (HIGH or LOW) based on whether the detected gas concentration exceeds a preset threshold. This is useful for simple alarm systems.
4. **AO (Analog Output):** Provides a variable voltage that corresponds to the concentration of detected gases, enabling precise measurement and monitoring.

---

## Calibrations for Different Gases
Accurate measurement with the MQ-135 requires calibration to relate the sensor's resistance to the concentration of specific gases. Calibration involves determining the ratio of sensor resistance in the presence of a target gas (**Rs**) to its resistance in clean air (**Ro**). This ratio (**Rs/Ro**) is mapped against known gas concentrations, typically using data provided in the sensor's datasheet. Calibration curves are established for each gas, allowing users to convert the analog output voltage into meaningful PPM values. For example, the sensor may be calibrated to detect ammonia in the range of 10–300 ppm, benzene from 10–1000 ppm, carbon dioxide from 350–10000 ppm, and smoke from 10–1000 ppm. Proper calibration ensures reliable and accurate gas concentration readings.

---

## Freundlich Adsorption Isotherm
The sensor's response to gas concentration can be described using the **Freundlich Adsorption Isotherm**, a mathematical model that explains how gas molecules adsorb onto the surface of the sensing material. The relationship is given by:

\[
\frac{Rs}{Ro} = K \cdot (C)^{-n}
\]

Where:
- \( Rs \) is the sensor resistance at a given gas concentration,
- \( Ro \) is the sensor resistance in clean air,
- \( C \) is the gas concentration in ppm,
- \( K \) and \( n \) are experimentally determined constants.

This equation shows that as the concentration of gas increases, the Rs/Ro ratio decreases, indicating higher conductivity of the sensing element. Graphically, plotting Rs/Ro against gas concentration (on a logarithmic scale) yields a downward-sloping curve, which is essential for interpreting sensor output and calibrating measurements.

---

## Applications
The MQ-135 sensor is used in a variety of applications where air quality monitoring is essential:
- **Indoor Air Quality Monitoring:** Detects harmful gases in homes, offices, and public spaces to ensure safe breathing environments.
- **Pollution Control Equipment:** Monitors air pollutants in industrial and urban settings to help manage and reduce emissions.
- **Smoke Detection:** Identifies the presence of smoke, contributing to fire safety systems.
- **Industrial Gas Leak Detection:** Alerts operators to dangerous gas leaks in factories and chemical plants.
- **IoT-Based Smart Environment Monitoring:** Integrates with IoT platforms for real-time, remote monitoring and data analysis of air quality.

---

## Advantages
- **Low Cost and Simple Operation:** The MQ-135 is affordable and easy to use, making it accessible for educational, hobbyist, and commercial projects.
- **Detection of Multiple Harmful Gases:** Its broad sensitivity range allows for simultaneous monitoring of several pollutants.
- **Real-Time Monitoring Capability:** Fast response times enable continuous and immediate air quality assessment.

---

## Limitations
- **Calibration Requirement:** Accurate readings depend on thorough calibration for each target gas, which can be time-consuming.
- **Cross-Sensitivity:** The sensor may respond to multiple gases at once, making it challenging to isolate specific pollutants without additional sensors or data processing.
- **Environmental Sensitivity:** Factors such as temperature and humidity can affect sensor performance, potentially leading to measurement errors if not properly compensated.

---

## Conclusion
The MQ-135 gas sensor is a versatile and cost-effective solution for air quality monitoring. Its ability to detect a wide range of harmful gases, combined with straightforward integration and operation, makes it suitable for both academic research and practical IoT deployments. While it requires careful calibration and consideration of environmental factors, the MQ-135 provides reliable estimates of gas concentrations, contributing to safer and healthier environments in various applications.

---
