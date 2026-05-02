import sys
import os
from PIL import Image, ImageOps


def main():
    shirt_image_path = "shirt.png"
    input_image_path, output_image_path = check_conditions()
    new_image_generator(
        shirt_image_path=shirt_image_path,
        input_image_path=input_image_path,
        output_image_path=output_image_path,
    )


def check_conditions():
    arguments = sys.argv
    if len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    elif len(arguments) > 3:
        sys.exit("Too many command-line arguments")

    input_name = arguments[1].strip()
    output_name = arguments[2].strip()

    input_extension = os.path.splitext(input_name)[1].lower()
    output_extension = os.path.splitext(output_name)[1].lower()

    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")

    if input_extension not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")

    try:
        with Image.open(input_name) as im:
            pass
    except FileNotFoundError:
        sys.exit("Input does not exist")

    return (input_name, output_name)


def new_image_generator(
    shirt_image_path: str, input_image_path: str, output_image_path: str
) -> None:
    try:
        with Image.open(shirt_image_path) as shirt_image, Image.open(
            input_image_path
        ) as input_image:
            shirt_size = shirt_image.size
            resized_image = ImageOps.fit(input_image, shirt_size)
            resized_image.paste(shirt_image, (0, 0), shirt_image)
            resized_image.save(output_image_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    except Exception:
        sys.exit("Something went wrong!")


if __name__ == "__main__":
    main()
