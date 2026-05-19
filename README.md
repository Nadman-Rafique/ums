# Edexcel UMS Converter

A terminal-based Python application designed to convert raw examination marks into UMS (Uniform Mark Scale) marks for Edexcel qualifications. 

This tool calculates precise UMS scores using mathematical interpolation between grade boundaries. It includes built-in standard grade boundaries for specific papers and allows users to input custom boundaries for flexible grading.

## Features
* **Multiple Subjects Supported:** Includes Pure Mathematics, Physics, Chemistry, Biology, and Further Pure Mathematics.
* **Unit Specific Tracking:** Calculates UMS based on the specific weighting and maximum marks of different paper units (e.g., P1, P2, M1, S1).
* **Standard UMS Scale:** Utilizes pre-configured reduction factors and standard grade boundaries for accurate conversion.
* **Custom Boundaries:** Allows users to manually input A*, A, B, C, and D lower boundaries to generate custom UMS conversions.
* **Input Validation:** Built-in error handling ensures the program does not crash if a user types invalid characters.

## Prerequisites
* Python 3.x installed on your system.
* No external libraries required (runs entirely on standard Python modules).
