# VISIONARY - Visual Image Analyzer

A Python command-line tool that analyses an image and reports its brightness, contrast, saturation and composition, then gives an overall **Visual Score out of 100**.

> **Course:** Essentials of Python (VITyarthi), VIT Bhopal University
> **Author:** Anuj Singh (Reg. No. 26BAI10913)
> **Mentor:** Venkat Prasad Padhy

---

## Overview

Judging whether a photo is too dark, too flat or over-saturated is usually done by eye, which is subjective. **VISIONARY** makes this objective. You give it the path of an image; it loads the file with the Pillow library, calculates a set of measurable metrics, labels each one in plain words (for example *Dark / Balanced / Bright*) and prints a neatly formatted report. Invalid input (a missing file or a file that is not an image) is handled with a friendly error message instead of a crash.

## Features

- Accepts an image path, including paths pasted with surrounding quotes
- Validates that the file exists and is a real, readable image
- **Basic information:** width, height, orientation (Landscape / Portrait / Square) and aspect ratio
- **Brightness** as a percentage, labelled Dark / Balanced / Bright
- **Contrast** as a percentage, labelled Low / Moderate / High
- **Saturation** as a percentage, labelled Muted / Moderate / Vivid
- **Composition analysis:** mean brightness of the four quadrants and the brightest / darkest region
- **Visionary Score** (0-100) combining brightness, contrast and saturation
- Clean, sectioned console report

## Technologies / Tools Used

| Tool | Purpose |
|------|---------|
| Python 3 | Programming language |
| [Pillow (PIL)](https://pillow.readthedocs.io/) | Opening, converting and cropping images; `ImageStat` for statistics |
| `os` (standard library) | Checking that the file exists |
| `math` (standard library) | Imported for numeric support |
| Git / GitHub | Version control |

## Project Structure

```
vityarthi_project_visionary/
|-- visionary.py          # main program
|-- requirements.txt      # dependencies (Pillow)
|-- README.md
|-- sample_images/        # images for quick testing
|   |-- sunset.jpg
|   |-- gray_square.png
|   |-- dark_portrait.png
|-- screenshots/          # example outputs
```

## Installation and Running

**1. Prerequisites:** Python 3.8 or newer. Check with:

```bash
python --version
```

**2. Clone the repository:**

```bash
git clone https://github.com/anujMANDERNA07/vityarthi_project_visionary.git
cd vityarthi_project_visionary
```

**3. Install the dependency:**

```bash
pip install -r requirements.txt
```

(or simply `pip install pillow`)

**4. Run the program:**

```bash
python visionary.py
```

**5. Enter the path of an image when prompted**, for example:

```
Enter the path of your image: sample_images/sunset.jpg
```

Full paths work too, e.g. `C:\Users\you\Pictures\photo.jpg`. Quotes around the path are optional (they are removed automatically), so you can paste a path straight from File Explorer or Finder.

## How the Score Is Calculated

| Metric | Formula |
|--------|---------|
| Brightness | mean grayscale value / 255 x 100 |
| Contrast | grayscale standard deviation / 128 x 100 (capped at 100) |
| Saturation | average of (max(R,G,B) - min(R,G,B)) / max(R,G,B) over all pixels, x 100 |
| Brightness sub-score | 100 - abs(50 - brightness) x 2 (minimum 0) |
| Saturation sub-score | 100 - abs(50 - saturation) x 2 (minimum 0) |
| Contrast sub-score | equal to the contrast value |
| **Visionary Score** | (brightness + contrast + saturation sub-scores) / 3 |

| Metric | Level 1 | Level 2 | Level 3 |
|--------|---------|---------|---------|
| Brightness | Dark (< 30) | Balanced (30 - 64.99) | Bright (65+) |
| Contrast | Low (< 25) | Moderate (25 - 59.99) | High (60+) |
| Saturation | Muted (< 25) | Moderate (25 - 59.99) | Vivid (60+) |

## Instructions for Testing

Testing is manual: run the program with different inputs and compare the output with the expected result.

| # | Test | Input | Expected result |
|---|------|-------|-----------------|
| 1 | Landscape image | `sample_images/sunset.jpg` | Type = Landscape, aspect ratio 1.6, brightness about 42.66 % (Balanced), score about 73.54 |
| 2 | Square, uniform grey | `sample_images/gray_square.png` | Type = Square, contrast 0 %, saturation 0 %, score about 33.2 |
| 3 | Dark portrait | `sample_images/dark_portrait.png` | Type = Portrait, brightness about 6.99 % (Dark), score about 26.56 |
| 4 | Quoted path | `"sample_images/sunset.jpg"` (with quotes) | Quotes removed, image loads normally |
| 5 | Missing file | `missing.jpg` | `Error: The file does not exist.` |
| 6 | Not an image | Any text file, e.g. `README.md` | `Error: The selected file is not a valid image.` |
| 7 | Your own photo | Any JPG / PNG | Full report printed; score always between 0 and 100 |

**Quick way to run a test without typing the path** (Linux / macOS / Git Bash):

```bash
echo "sample_images/sunset.jpg" | python visionary.py
```

On Windows PowerShell:

```powershell
"sample_images/sunset.jpg" | python visionary.py
```

## Screenshots

**Landscape image (`sunset.jpg`)**

![Landscape result](screenshots/result_landscape.png)

**Uniform grey square**

![Grey square result](screenshots/result_grey_square.png)

**Dark portrait**

![Dark portrait result](screenshots/result_dark_portrait.png)

**Error handling: missing file and invalid image**

![Missing file](screenshots/error_missing_file.png)
![Invalid image](screenshots/error_invalid_image.png)

## Notes and Limitations

- The saturation calculation loops over every pixel, so very large images take a few seconds.
- In recent Pillow versions, `Image.getdata()` prints a deprecation warning. The program still works correctly.
- When all four quadrants have equal brightness, the same region is reported as both brightest and darkest.
- One image is analysed per run.

## Future Enhancements

- Graphical interface with a file picker and image preview
- Faster processing with NumPy
- Batch analysis of a folder with CSV export
- Histograms and rule-of-thirds / sharpness analysis

## References

- [Python documentation](https://docs.python.org/3/)
- [Pillow documentation](https://pillow.readthedocs.io/)
- [HSL and HSV (saturation)](https://en.wikipedia.org/wiki/HSL_and_HSV)
