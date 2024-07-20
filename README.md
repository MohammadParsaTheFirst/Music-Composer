# Music-Composer

This project focuses on recognizing musical notes from given test images using Template Matching and other image processing techniques. The goal is to identify the notes and play the corresponding music.
An interesting point of this project is that the project is implemented in python and also matlab. The matlab implementation lies in the `..\Main` directory, while all other files and directories are python implementation of the project. 

## Project Description

In this project, we:
1. Identified musical notes using Template Matching.
2. Drawed rectangles around the identified notes in the images.
3. Generated audio outputs for each page of music.

## Requirements

- Python 
- OpenCV
- Jupyter Notebook
  or you can use the matlab file in `..\Main' diretory.
## Instructions
Firslty, we implemented Template Matching. Then, we identified notes for the songs: `Twinkle, Twinkle, Little Star` , `Ava Maria`, `Polyushka Polie`, and `jane-maryam`  and provide the corresponding outputs.
You can see the note' files in the images file: `..\images`. 
Afterwards we identified black, white, and whole notes  besides sharp and flat signs and confined them with red reactangles.
## Helper Functions

You can use the functions provided in `..\Helper\helper.ipynb` to assist with note recognition and drawing rectangles around identified notes.

## Tips

- Use the position of the notes relative to the staff lines for recognition.
- If you encounter difficulties in detecting the staff lines, you can use the `cv2.HoughLinesP` function to find their coordinates. 

## Output

At last for each song, we have submitted:
- Images with rectangles drawn around the identified notes.
- Audio outputs for each page of music.

![alt text](https://github.com/MohammadParsaTheFirst/Music-Composer/blob/main/images/Results/1.png?raw=true)
![alt text](https://github.com/MohammadParsaTheFirst/Music-Composer/blob/main/images/Results/2.png?raw=true)
![alt text](https://github.com/MohammadParsaTheFirst/Music-Composer/blob/main/images/Results/3.png?raw=true)
![alt text](https://github.com/MohammadParsaTheFirst/Music-Composer/blob/main/images/Results/4.png?raw=true)

Furthermore, You can see the output voices in `.wav` format in this folder: `..\Results`
![alt text](https://github.com/MohammadParsaTheFirst/Music-Composer/blob/main/Results/converted_to_mp4/avemaria.mp4)
![alt text](https://github.com/MohammadParsaTheFirst/Music-Composer/blob/main/Results/converted_to_mp4/maryam.mp4)
![alt text](https://github.com/MohammadParsaTheFirst/Music-Composer/blob/main/Results/converted_to_mp4/twinkle.mp4)
![alt text](https://github.com/MohammadParsaTheFirst/Music-Composer/blob/main/Results/converted_to_mp4/pole.mp4)

## Software Requirements

- Python 3.x
- OpenCV
- Jupyter Notebook

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/MohammadParsaTheFirst/Music-Composer.git
   ```
2. Navigate to the project directory:
   ```bash   
   cd music-note-recognition
   ```
3. Install the required packages:
    ```bash   
   pip install -r requirements.txt
   ```
4. Open the Jupyter Notebook and run the cells in `helper.ipynb` to perform note recognition and generate outputs.
   
## License
This project is licensed under the MIT License - see the LICENSE file for details.
