from rembg import remove
from PIL import Image

# Load input image
input_path = 'Tan_HalfBody.jpg'
output_path = 'Tan_HalfBodyRemoved.jpg'  # Use .jpg since it's now on white

input_image = Image.open(input_path)

# Remove background
output_image = remove(input_image)

# Replace transparent background with white
white_bg = Image.new("RGB", output_image.size, (255, 255, 255))  # White background
white_bg.paste(output_image, mask=output_image.split()[3])  # Use alpha channel as mask

# Save the final image
white_bg.save(output_path, "JPEG")