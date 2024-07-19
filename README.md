# Music-Composer

This project focuses on recognizing musical notes from given test images using Template Matching and other image processing techniques. The goal is to identify the notes and play the corresponding music.

## Project Description

In this project, you will:
1. Identify musical notes using Template Matching.
2. Draw rectangles around the identified notes in the images.
3. Generate audio outputs for each page of music.

## Requirements

- Python
- OpenCV
- Jupyter Notebook

## Instructions

### 1. Template Matching (10 points)
Complete the exercise provided in the introduction to Template Matching.

### 2. Note Recognition (40 points)
Identify notes B3 to B5 for the song "Twinkle, Twinkle, Little Star" and provide the corresponding outputs.

### 3. Note Type Recognition (30 points)
Identify black, white, and whole notes for the song "Ave Maria" and provide the corresponding outputs.

### 4. Sharp and Flat Signs Recognition (20 points)
Identify sharp and flat signs for the song "Polyushka-polye" and provide the corresponding outputs.

## Helper Functions

Use the functions provided in `helper.ipynb` to assist with note recognition and drawing rectangles around identified notes.

## Tips

- Use the position of the notes relative to the staff lines for recognition.
- If you encounter difficulties in detecting the staff lines, you can use the `cv2.HoughLinesP` function to find their coordinates. Note that using this function will result in a 25-point deduction.

## Output

For each song, submit:
- Images with rectangles drawn around the identified notes.
- Audio outputs for each page of music.

## Software Requirements

- Python 3.x
- OpenCV
- Jupyter Notebook

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/music-note-recognition.git
