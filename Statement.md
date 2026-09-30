# Visionary — Project Statement

## 1. Problem Statement

Images contain measurable visual properties such as brightness, contrast, color saturation, dimensions, and regional brightness. However, these properties are not always easy to evaluate manually in a consistent way.

The **Visionary** project addresses this problem by creating a Python-based image analyzer that accepts an image from the user and calculates measurable visual properties. The program then presents the results in a clear report.

The project focuses on mathematical and rule-based image analysis rather than subjective artistic judgment.

## 2. Scope of the Project

The current scope of Visionary includes:

- Loading an image from a user-provided file path.
- Checking whether the file exists.
- Validating that the file can be opened as an image.
- Determining whether the image is landscape, portrait, or square.
- Finding the image width, height, and aspect ratio.
- Calculating average brightness.
- Calculating approximate contrast.
- Calculating average saturation.
- Classifying brightness, contrast, and saturation into descriptive levels.
- Dividing the image into four regions.
- Comparing the average brightness of the four regions.
- Identifying the brightest and darkest regions.
- Producing a mathematical visual score out of 100.
- Displaying all results in a formatted console report.

The current project does **not** attempt to identify objects, understand the semantic meaning of an image, or make a subjective judgment about artistic quality.

## 3. Target Users

The project is intended for:

- Students learning Python and basic image processing.
- Beginners who want to understand how Python can process image data.
- Users who want a simple numerical and descriptive analysis of basic image properties.
- Students demonstrating Python programming concepts through a practical project.

## 4. High-Level Features

### Image Input
The user provides the path of an image file.

### Image Validation
The program checks whether the path exists and whether the file can be opened as an image.

### Basic Image Information
The program identifies:

- Image type
- Width
- Height
- Aspect ratio

### Visual Analysis
The program calculates:

- Brightness
- Contrast
- Saturation

### Visual Classification
The calculated values are converted into simple categories such as Dark/Balanced/Bright, Low/Moderate/High, and Muted/Moderate/Vivid.

### Composition Analysis
The image is divided into four regions and their average brightness values are compared.

### Visual Score
A numerical score out of 100 is calculated from brightness, contrast, and saturation measurements.

### Report Generation
The final results are displayed as a structured console report.

## 5. Expected Outcome

After running the program and providing a valid image path, the user receives a complete report containing the image information, visual measurements, regional brightness analysis, and the calculated visual score.

The output is intended to demonstrate practical use of Python programming concepts such as functions, conditional statements, dictionaries, loops, input handling, file validation, and calculations.
