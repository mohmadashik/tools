from PIL import Image, ImageDraw, ImageFont

# Load the generated forest scene image
image_path = "/home/amohmad/Pictures/ashik/editing/SnakeAndLion.webp"
img = Image.open(image_path)

# Define the quote and position settings
quote_text = (
    "You can tell a lion that you are a lion of strength and power, "
    "but you can't tell a snake that it is a creature of poison and toxicity. "
    "Lions and snakes live within us all. If a person cannot accept who they truly are, "
    "they become the snake. Their poison may be intentional or unintentional, "
    "but your duty is to protect yourself—not to save the snake."
)

# Font settings - note: this system may not have custom fonts, using default size and type.
try:
    # Try to use a common system font if available
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 32)
except IOError:
    # Default to a basic font if custom fonts are unavailable
    font = ImageFont.load_default()

# Define text position and colors
draw = ImageDraw.Draw(img)
image_width, image_height = img.size
text_width, text_height = draw.textsize(quote_text, font=font)
text_x = (image_width - text_width) // 2
text_y = image_height - text_height - 100  # Place the text above the bottom

# Text color and outline
text_color = (255, 255, 255)  # White for readability
outline_color = (0, 0, 0)     # Black outline for contrast

# Draw text with outline for readability
def draw_text_with_outline(draw, x, y, text, font, text_color, outline_color):
    # Outline
    for offset in [-1, 1]:
        draw.text((x + offset, y), text, font=font, fill=outline_color)
        draw.text((x, y + offset), text, font=font, fill=outline_color)
    # Text
    draw.text((x, y), text, font=font, fill=text_color)

# Split text into multiple lines to fit within image width
import textwrap
wrapped_text = textwrap.fill(quote_text, width=60)
draw_text_with_outline(draw, text_x, text_y, wrapped_text, font, text_color, outline_color)

# Save the edited image
output_path = "/home/amohmad/Pictures/ashik/editing/Forest_Lion_Snake_Quote_Image.png"
img.save(output_path)
output_path
