import csv
import os

current_directory = os.getcwd()
# major_files_path = os.path.join(current_directory, 'data/Actor_01/03-01-01-01-01-01-01.wav')

data_directory =  os.path.join(current_directory, 'data')

neutral_files_names = []
calm_files_names = []
happy_files_names = []
sad_files_names = []
angry_files_names = []
fearful_files_names = []
disgusted_files_names = []
surprised_files_names = []

counter = 0
for root, directories, files in os.walk(data_directory):
    for file in files:
        if '.wav' in file:
            # 3rd number in the file name equals to the encoding of the emotion, 
            emotion_code_number = file.split('-')[2]

            if emotion_code_number == '01':
                neutral_files_names.append(os.path.join(root, file))
            elif emotion_code_number == '02':
                calm_files_names.append(os.path.join(root, file))
            elif emotion_code_number == '03':
                happy_files_names.append(os.path.join(root, file))
            elif emotion_code_number == '04':
                sad_files_names.append(os.path.join(root, file))
            elif emotion_code_number == '05':
                angry_files_names.append(os.path.join(root, file))
            elif emotion_code_number == '06':
                fearful_files_names.append(os.path.join(root, file))
            elif emotion_code_number == '07':
                disgusted_files_names.append(os.path.join(root, file))
            elif emotion_code_number == '08':
                surprised_files_names.append(os.path.join(root, file))


file_headers = ['filename','emotion', 'target']

with open("dataset_metadata.csv", "w") as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(file_headers)

    for file_name in neutral_files_names:
        csv_writer.writerow([file_name, 'neutral', '00'])
    
    for file_name in calm_files_names:
        csv_writer.writerow([file_name, 'calm', '01'])
    
    for file_name in happy_files_names:
        csv_writer.writerow([file_name, 'happy', '02'])
    
    for file_name in sad_files_names:
        csv_writer.writerow([file_name, 'sad', '03'])
    
    for file_name in angry_files_names:
        csv_writer.writerow([file_name, 'angry', '04'])
    
    for file_name in fearful_files_names:
        csv_writer.writerow([file_name, 'fearful', '05'])
    
    for file_name in disgusted_files_names:
        csv_writer.writerow([file_name, 'disgust', '06'])
    
    for file_name in surprised_files_names:
        csv_writer.writerow([file_name, 'surprised', '07'])

file.close()

