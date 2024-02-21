from PIL import Image
import os
from pillow_heif import read_heif

def convert_heic_to_jpg(input_dir):
    successfully_converted = []

    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.endswith(".heic"):
                input_path = os.path.join(root, filename)
                output_filename = os.path.splitext(filename)[0] + ".jpg"
                output_path = os.path.join(root, output_filename)

                i = 1
                while os.path.exists(output_path):
                    base_name, ext = os.path.splitext(output_filename)
                    new_output_filename = f"{base_name}_{i}.jpg"
                    output_path = os.path.join(root, new_output_filename)
                    i += 1

                try:
                    heif_file = read_heif(input_path)
                    img = Image.frombytes(
                        heif_file.mode,
                        heif_file.size,
                        heif_file.data,
                        "raw",
                        heif_file.mode,
                        heif_file.stride,
                    )

                    img.save(output_path, "JPEG")
                    print(f"Converted {filename} to {output_path}")
                    successfully_converted.append(input_path)
                except Exception as e:
                    print(f"Error converting {filename}: {e}")

    return successfully_converted

def delete_files(file_paths):
    for file_path in file_paths:
        os.remove(file_path)
        print(f"Deleted {file_path}")

input_directory = "input//path"
