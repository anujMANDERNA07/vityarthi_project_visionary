from PIL import Image, ImageStat
import os
import math


# ============================================================
# VISIONARY
# Visual Image Analyzer
# Python Essentials Project
# ============================================================


def print_header():
    """Display the Visionary title."""
    print("=" * 60)
    print("                     VISIONARY")
    print("              VISUAL IMAGE ANALYZER")
    print("=" * 60)


def get_image_path():
    """Ask the user for the image path."""
    path = input("\nEnter the path of your image: ").strip()

    # Remove quotation marks if the user pasted a quoted path
    path = path.strip('"').strip("'")

    return path


def load_image(path):
    """Load the image and handle errors."""
    if not os.path.exists(path):
        print("\nError: The file does not exist.")
        return None

    try:
        image = Image.open(path)
        image.load()
        return image

    except Exception:
        print("\nError: The selected file is not a valid image.")
        return None


def get_basic_information(image):
    """Get basic information about the image."""

    width, height = image.size

    if width > height:
        image_type = "Landscape"
    elif height > width:
        image_type = "Portrait"
    else:
        image_type = "Square"

    aspect_ratio = width / height

    return {
        "width": width,
        "height": height,
        "type": image_type,
        "aspect_ratio": aspect_ratio
    }


def calculate_brightness(image):
    """Calculate average brightness of the image."""

    grayscale = image.convert("L")
    statistics = ImageStat.Stat(grayscale)

    brightness = statistics.mean[0]

    # Convert 0-255 into percentage
    percentage = (brightness / 255) * 100

    return percentage


def calculate_contrast(image):
    """Calculate approximate image contrast."""

    grayscale = image.convert("L")
    statistics = ImageStat.Stat(grayscale)

    standard_deviation = statistics.stddev[0]

    # Convert standard deviation into a simple percentage
    contrast = (standard_deviation / 128) * 100

    if contrast > 100:
        contrast = 100

    return contrast


def calculate_saturation(image):
    """Calculate approximate average saturation."""

    rgb_image = image.convert("RGB")

    pixels = list(rgb_image.getdata())

    total_saturation = 0

    for pixel in pixels:

        red = pixel[0] / 255
        green = pixel[1] / 255
        blue = pixel[2] / 255

        maximum = max(red, green, blue)
        minimum = min(red, green, blue)

        if maximum == 0:
            saturation = 0
        else:
            saturation = (maximum - minimum) / maximum

        total_saturation += saturation

    average_saturation = total_saturation / len(pixels)

    return average_saturation * 100


def determine_brightness_level(brightness):
    """Convert brightness percentage into a description."""

    if brightness < 30:
        return "Dark"
    elif brightness < 65:
        return "Balanced"
    else:
        return "Bright"


def determine_contrast_level(contrast):
    """Convert contrast percentage into a description."""

    if contrast < 25:
        return "Low"
    elif contrast < 60:
        return "Moderate"
    else:
        return "High"


def determine_saturation_level(saturation):
    """Convert saturation percentage into a description."""

    if saturation < 25:
        return "Muted"
    elif saturation < 60:
        return "Moderate"
    else:
        return "Vivid"


def analyze_composition(image):
    """
    Perform a basic composition analysis.

    The image is divided into four regions.
    We compare their average brightness.
    """

    image = image.convert("L")

    width, height = image.size

    middle_x = width // 2
    middle_y = height // 2

    top_left = image.crop(
        (0, 0, middle_x, middle_y)
    )

    top_right = image.crop(
        (middle_x, 0, width, middle_y)
    )

    bottom_left = image.crop(
        (0, middle_y, middle_x, height)
    )

    bottom_right = image.crop(
        (middle_x, middle_y, width, height)
    )

    regions = {
        "Top Left": ImageStat.Stat(top_left).mean[0],
        "Top Right": ImageStat.Stat(top_right).mean[0],
        "Bottom Left": ImageStat.Stat(bottom_left).mean[0],
        "Bottom Right": ImageStat.Stat(bottom_right).mean[0]
    }

    brightest_region = max(regions, key=regions.get)
    darkest_region = min(regions, key=regions.get)

    return regions, brightest_region, darkest_region


def calculate_image_score(brightness, contrast, saturation):
    """
    Create a simple numerical visual score.

    This is NOT an artistic judgment.
    It is only a mathematical score based on
    the image measurements.
    """

    brightness_score = 100 - abs(50 - brightness) * 2

    if brightness_score < 0:
        brightness_score = 0

    contrast_score = contrast

    saturation_score = 100 - abs(50 - saturation) * 2

    if saturation_score < 0:
        saturation_score = 0

    final_score = (
        brightness_score +
        contrast_score +
        saturation_score
    ) / 3

    return final_score


def display_report(
    basic_info,
    brightness,
    contrast,
    saturation,
    composition,
    score
):
    """Display the final Visionary report."""

    regions, brightest_region, darkest_region = composition

    print("\n")
    print("=" * 60)
    print("                  VISIONARY REPORT")
    print("=" * 60)

    print("\n[ IMAGE INFORMATION ]")
    print("-" * 60)

    print("Image Type       :", basic_info["type"])
    print("Width            :", basic_info["width"], "px")
    print("Height           :", basic_info["height"], "px")
    print("Aspect Ratio     :", round(basic_info["aspect_ratio"], 2))

    print("\n[ VISUAL ANALYSIS ]")
    print("-" * 60)

    print(
        "Brightness       :",
        round(brightness, 2),
        "%",
        "(" + determine_brightness_level(brightness) + ")"
    )

    print(
        "Contrast         :",
        round(contrast, 2),
        "%",
        "(" + determine_contrast_level(contrast) + ")"
    )

    print(
        "Saturation       :",
        round(saturation, 2),
        "%",
        "(" + determine_saturation_level(saturation) + ")"
    )

    print("\n[ COMPOSITION ANALYSIS ]")
    print("-" * 60)

    print("Brightest Region :", brightest_region)
    print("Darkest Region   :", darkest_region)

    print("\nRegional Brightness:")

    for region, value in regions.items():
        print(
            "  ",
            region,
            ":",
            round(value, 2)
        )

    print("\n[ VISIONARY SCORE ]")
    print("-" * 60)

    print("Visual Score     :", round(score, 2), "/ 100")

    print("\n" + "=" * 60)
    print("              ANALYSIS COMPLETE")
    print("=" * 60)


def main():
    """Main Visionary program."""

    print_header()

    path = get_image_path()

    image = load_image(path)

    if image is None:
        return

    print("\nImage loaded successfully!")
    print("Analyzing image...")

    basic_info = get_basic_information(image)

    brightness = calculate_brightness(image)

    contrast = calculate_contrast(image)

    saturation = calculate_saturation(image)

    composition = analyze_composition(image)

    score = calculate_image_score(
        brightness,
        contrast,
        saturation
    )

    display_report(
        basic_info,
        brightness,
        contrast,
        saturation,
        composition,
        score
    )


# Start the program
if __name__ == "__main__":
    main()